"""Project-authored graph proof checker. An exact external seed is required.
No curator graph6, adjacency or original CNF data is redistributed or downloaded.
"""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
from math import comb
from hashlib import sha256
import argparse,copy,json
SEED_PIN='7fda67be9b2d99b376c0f4e8188edf004599e64d5541331fbdd2d599246a067d'
CNF_PIN='5934d7346d6365809788730caa203e1655542f5c4a051a6c5019facaa77ee17e'

def require(ok,msg):
    if not ok:
        raise ValueError(msg)

def decode(raw):
    if raw.endswith(b'\n'):
        raw=raw[:-1]
    require(bool(raw) and all(63<=c<=126 for c in raw),'graph6 ASCII')
    n=raw[0]-63
    require(0<=n<=62,'short graph6 order')
    bits=n*(n-1)//2
    require(len(raw)==1+(bits+5)//6,'graph6 length')
    values=[c-63 for c in raw[1:]]
    pad=(-bits)%6
    require(not pad or values[-1] % (1<<pad)==0,'zero right padding')
    edges=set();offset=0
    for j in range(1,n):
        for i in range(j):
            if (values[offset//6]>>(5-offset%6))&1:
                edges.add((i,j))
            offset+=1
    require(offset==bits,'complete edge-bit membership')
    return n,edges

def adjacency(n,edges):
    return [set(j if i==v else i for i,j in edges if i==v or j==v) for v in range(n)]

def count_edges(edges,vertices):
    return sum(pair in edges for pair in combinations(vertices,2))

def encoding(n,edges):
    clauses=[];types=Counter()
    for subset in combinations(range(n),4):
        e=count_edges(edges,subset)
        if e==6:
            clauses.append(tuple(-v-1 for v in subset));types['cliques']+=1
        elif e==0:
            clauses.append(tuple(v+1 for v in subset));types['independent']+=1
        else:
            types['mixed']+=1
    require(sum(types.values())==comb(n,4),'complete four-set membership')
    require(len(set(clauses))==len(clauses),'distinct encoding clauses')
    return clauses,dict(types)

def parse_cnf(raw):
    lines=[s.strip() for s in raw.decode('ascii').splitlines() if s.strip() and not s.lstrip().startswith('c')]
    require(bool(lines),'empty CNF text')
    h=lines[0].split();require(len(h)==4 and h[:2]==['p','cnf'],'DIMACS header')
    n,m=map(int,h[2:]);require(n>=0 and m>=0,'DIMACS dimensions')
    clauses=[]
    for line in lines[1:]:
        row=list(map(int,line.split()))
        require(bool(row) and row[-1]==0,'DIMACS terminator')
        row=row[:-1]
        require(all(0<abs(a)<=n for a in row) and len(row)==len(set(row)),'literal membership')
        clauses.append(tuple(row))
    require(len(clauses)==m,'complete declared clauses')
    return n,clauses

def validate_encoding(raw,expected,n):
    declared,clauses=parse_cnf(raw)
    require(declared==n and clauses==expected,'exact complete signed encoding membership')
    return clauses

def resolution(raw,proof):
    n,rows=parse_cnf(raw);clauses=[set(c) for c in rows]
    require(set(proof)=={'schema','input_sha256','input_clauses','nvars','steps','final'},'resolution schema')
    require(proof['schema']=='OPF_RESOLUTION_V1' and proof['input_sha256']==sha256(raw).hexdigest(),'resolution input binding')
    require(proof['nvars']==n and proof['input_clauses']==len(rows),'resolution dimensions')
    require(type(proof['steps']) is list and len(proof['steps'])<=100000,'bounded steps')
    for step in proof['steps']:
        require(set(step)=={'left','right','pivot','clause'},'step schema')
        l,r,p=step['left'],step['right'],step['pivot']
        require(all(type(x) is int for x in (l,r,p)) and 1<=l<=len(clauses) and 1<=r<=len(clauses) and 1<=p<=n,'earlier parents and pivot')
        require(p in clauses[l-1] and -p in clauses[r-1],'opposite signed pivots')
        derived={a for a in clauses[l-1] if a!=p}|{a for a in clauses[r-1] if a!=-p}
        row=step['clause']
        require(type(row) is list and all(type(a) is int and 0<abs(a)<=n for a in row) and len(row)==len(set(row)),'derived literal membership')
        require(derived==set(row),'exact resolvent, no lost literal')
        clauses.append(derived)
    require(type(proof['final']) is int and proof['final']==len(clauses) and not clauses[-1],'last derived empty clause')
    return {'steps':len(proof['steps']),'final_empty_clause':len(clauses),'outcome':'UNSAT'}

def graph_controls(raw,expected,proof):
    rejected=[]
    def reject(name,fn):
        try:
            fn()
        except (ValueError,UnicodeError):
            rejected.append(name)
        else:
            raise ValueError('invalid input accepted:'+name)
    fixtures=[(b'B?',set()),(b'B_',{(0,1)}),(b'Bg',{(0,1),(1,2)}),(b'Bw',{(0,1),(0,2),(1,2)}),(b'Cs',{(0,1),(0,2),(0,3)})]
    for data,edges in fixtures:
        require(decode(data)[1]==edges,'labeled decoder canary')
    for name,data in [('empty',b''),('illegal byte',b'B!'),('short',b'Dh'),('long',b'B??'),('padding',b'Dhd'),('extended header',b'~???')]:
        reject(name,lambda data=data:decode(data))
    for name,mut in [('missing clause',expected[:-1]),('duplicate clause',[expected[0]]+expected),('wrong sign',[tuple(-a for a in expected[0])]+expected[1:])]:
        body=('p cnf 42 '+str(len(mut))+'\n'+''.join(' '.join(map(str,c))+' 0\n' for c in mut)).encode()
        reject(name,lambda body=body:validate_encoding(body,expected,42))
    for name,change in [
        ('wrong pivot',lambda p:p['steps'][0].update(pivot=42)),
        ('future parent',lambda p:p['steps'][0].update(left=999999)),
        ('lost nonpivot literal',lambda p:p['steps'][0]['clause'].pop()),
        ('duplicate derived literal',lambda p:p['steps'][0]['clause'].append(p['steps'][0]['clause'][0])),
        ('missing final step',lambda p:p['steps'].pop()),
        ('false final pointer',lambda p:p.update(final=1)),
        ('wrong input hash',lambda p:p.update(input_sha256='0'*64)),
        ('empty asserted final clause',lambda p:p['steps'][-2].update(clause=[]))]:
        mutant=copy.deepcopy(proof);change(mutant)
        reject(name,lambda mutant=mutant:resolution(raw,mutant))
    # A manually sound UNSAT proof and a SAT formula challenge reject-all and
    # false-empty consumers without depending on the actual42-variable seed.
    hand=b'p cnf 1 2\n1 0\n-1 0\n'
    hp={'schema':'OPF_RESOLUTION_V1','input_sha256':sha256(hand).hexdigest(),'input_clauses':2,'nvars':1,'steps':[{'left':1,'right':2,'pivot':1,'clause':[]}],'final':3}
    resolution(hand,hp)
    sat=b'p cnf 1 2\n1 0\n1 0\n';hp['input_sha256']=sha256(sat).hexdigest()
    require(any(all(any((bool(a>>(abs(x)-1)&1))==(x>0) for x in c) for c in parse_cnf(sat)[1]) for a in range(2)),'SAT truth-table canary')
    reject('SAT formula false refutation with updated hash',lambda:resolution(sat,hp))
    return {'negative_controls_detected':rejected,'negative_controls_scored':18,'hand_labeled_graphs':len(fixtures),'healthy_manual_unsat_proof':True,'SAT_truth_table_checked':True}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--seed',type=Path,required=True,help='Externally supplied first42vertex graph6record; not included in this release')
    p.add_argument('--resolution',type=Path,required=True)
    p.add_argument('--certificate',type=Path,required=True)
    p.add_argument('--verify',action='store_true')
    args=p.parse_args()
    record=args.seed.read_bytes();clean=record[:-1] if record.endswith(b'\n') else record
    require(sha256(clean).hexdigest()==SEED_PIN,'exact external seed required')
    n,edges=decode(record);require(n==42 and len(edges)==425,'fixed source seed')
    hist=[0]*11;seen=0
    for subset in combinations(range(n),5):hist[count_edges(edges,subset)]+=1;seen+=1
    require(seen==comb(n,5)==850668 and hist[0]==hist[10]==0,'complete noK5/noI5')
    clauses,types=encoding(n,edges)
    # Regenerated from the supplied mathematical graph, not shipped input data.
    raw=('p cnf 42 '+str(len(clauses))+'\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses)).encode('ascii')
    require(sha256(raw).hexdigest()==CNF_PIN,'regenerated exact CNF binding')
    validate_encoding(raw,clauses,42)
    proof=json.loads(args.resolution.read_text());decision=resolution(raw,proof)
    adj=adjacency(n,edges);centres=[v for v in range(n) if len(adj[v])==22]
    local=[{'vertex':v,'degree':22,'edges':count_edges(edges,sorted(adj[v])),'pairs_checked':231} for v in centres]
    require(centres==[39,40,41] and [r['edges'] for r in local]==[108,107,107],'complete degree22family')
    controls=graph_controls(raw,clauses,proof)
    result={'status':'PASS_RESTRICTED','records':['C168','C169','C171'],'publication_profile':'PROJECT_OUTPUTS_ONLY_EXTERNAL_SEED_REQUIRED','source_record_sha256_without_LF':SEED_PIN,'source_record_bytes_without_LF':145,'five_subsets':seen,'five_subset_histogram':hist,'four_subsets':sum(types.values()),'four_subset_types':types,'regenerated_CNF_sha256':CNF_PIN,'resolution':decision,'degree22_results':local,'controls':controls,'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'resolution_sha256':sha256(args.resolution.read_bytes()).hexdigest(),'source_data_license':'Unresolved; no curator graph6, adjacency list or original CNF file is redistributed.','claim_ceiling':'One exact externally supplied42vertex seed and its fixed one-vertex extension/three-centre claims only. No complete seed catalogue or global Ramsey result.','independence':'Adapted same-actor batch002consumer; interface reproduction, no new algorithmic-independence credit.'}
    if args.verify:
        require(json.loads(args.certificate.read_text())==result,'entire saved output certificate')
    else:
        with args.certificate.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':'PASS_RESTRICTED','external_seed_exact':True,'five_subsets':seen,'four_subsets':sum(types.values()),'resolution_steps':decision['steps'],'negative_controls':len(controls['negative_controls_detected']),'curator_data_redistributed':False}))

if __name__=='__main__':main()
