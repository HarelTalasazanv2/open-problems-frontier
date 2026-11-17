"""Literal CNF membership and exact Boolean controls; no graph search."""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
from hashlib import sha256
import argparse,json

def need(ok,message):
    if not ok: raise ValueError(message)

def clause(parts):
    if True in [x for x in parts if type(x) is bool]: return None
    q={x for x in parts if type(x) is not bool}
    need(all(type(x) is int and x for x in q),'nonzero integer literal')
    if any(-x in q for x in q): return None
    return tuple(sorted(q,key=lambda x:(abs(x),x)))

def negate(x): return not x if type(x) is bool else -x

def counter(kind,x,k,start):
    m=len(x);need(kind in ['functional','sequential'] and 0<=k<m and len(set(x))==m,'counter domain')
    need(all(type(a) is int and 0<a<start for a in x),'input/auxiliary disjointness')
    rows=[]
    def emit(*p):
        c=clause(p)
        if c is not None: rows.append(c)
    if kind=='functional':
        def z(i,j): return True if j==0 else False if i==0 else start+(i-1)*(k+1)+j-1
        for i in range(1,m+1):
            for j in range(1,k+2):
                o,a,b,c=z(i,j),z(i-1,j),x[i-1],z(i-1,j-1)
                emit(-o,a,b);emit(-o,a,c);emit(o,negate(a));emit(o,negate(b),negate(c))
        emit(-z(m,k+1));aux=m*(k+1)
    elif k==0:
        for a in x: emit(-a)
        aux=0
    else:
        def s(i,j): return start+(i-1)*k+j-1
        emit(-x[0],s(1,1))
        for j in range(2,k+1): emit(-s(1,j))
        for i in range(2,m):
            emit(-x[i-1],s(i,1));emit(-s(i-1,1),s(i,1))
            for j in range(2,k+1):
                emit(-x[i-1],-s(i-1,j-1),s(i,j));emit(-s(i-1,j),s(i,j))
            emit(-x[i-1],-s(i-1,k))
        emit(-x[-1],-s(m-1,k));aux=(m-1)*k
    return rows,aux

def evaluate(rows,values): return all(any(values[abs(l)]==(l>0) for l in row) for row in rows)

def parse(raw):
    lines=raw.decode('ascii').splitlines();head=lines[0].split()
    need(len(head)==4 and head[:2]==['p','cnf'],'DIMACS header')
    nv,nc=map(int,head[2:]);rows=[]
    for line in lines[1:]:
        tokens=list(map(int,line.split()));need(tokens and tokens[-1]==0,'clause terminator')
        q=tokens[:-1];need(q and all(0<abs(x)<=nv for x in q),'literal range')
        need(len(set(q))==len(q) and not any(-x in q for x in q),'literal membership')
        rows.append(tuple(sorted(q,key=lambda x:(abs(x),x))))
    need(nv>0 and len(rows)==nc,'complete declared clause count')
    return nv,rows

def target(kind):
    edges={e:i+1 for i,e in enumerate(combinations(range(17),2))};base=[]
    for vertices in combinations(range(17),5): base.append(tuple(-edges[e] for e in combinations(vertices,2)))
    for vertices in combinations(range(17),4): base.append(tuple(edges[e] for e in combinations(vertices,2)))
    need(len(base)==8568,'base clause membership')
    rows=base.copy();auxcount=128 if kind=='functional' else 105
    for v in range(17):
        ids=[edges[tuple(sorted((u,v)))] for u in range(17) if u!=v]
        local,aux=counter(kind,ids,7,137+v*auxcount)
        need(aux==auxcount,'auxiliary block size');rows.extend(local)
    return 136+17*auxcount,rows

def match(nv,rows,expected):
    need(nv==expected[0] and Counter(rows)==Counter(expected[1]),'complete literal clause multiset')

def rejected(name,fn):
    try: fn()
    except ValueError: return name
    raise ValueError('Accepted bad control: '+name)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--certificate',type=Path,required=True);ap.add_argument('--verify',action='store_true');args=ap.parse_args()
    here=Path(__file__).resolve().parent;outputs=[];bad=[];states=0;cohorts=0
    # Independently check all16gate truth assignments, including false outputs.
    gate=[(-1,2,3),(-1,2,4),(1,-2),(1,-3,-4)]
    for o,a,b,c in product([False,True],repeat=4):
        need(evaluate(gate,{1:o,2:a,3:b,4:c})==(o==(a or (b and c))),'gate truth table')
    for kind in ['functional','sequential']:
        raw=(here/(kind+'17.cnf')).read_bytes();nv,rows=parse(raw);expected=target(kind);match(nv,rows,expected)
        need(rows[:8568]==expected[1][:8568],'unchanged exact base prefix')
        outputs.append({'kind':kind,'variables':nv,'clauses':len(rows),'literal_occurrences':sum(map(len,rows)),'bytes':len(raw),'sha256':sha256(raw).hexdigest()})
        bad.append(rejected(kind+' omitted clause',lambda:match(nv,rows[:-1],expected)))
        bad.append(rejected(kind+' duplicate clause',lambda:match(nv,rows+[rows[-1]],expected)))
        altered=rows.copy();altered[-1]=tuple(137 if abs(x)==nv else x for x in altered[-1])
        bad.append(rejected(kind+' auxiliary alias',lambda:match(nv,altered,expected)))
        allowed=0
        local,aux=counter(kind,list(range(1,17)),7,17)
        for bits in range(1<<16):
            x={j+1:bool(bits&(1<<j)) for j in range(16)}
            width=8 if kind=='functional' else 7
            for i in range(1,17 if kind=='functional' else 16):
                prefix=(bits&((1<<i)-1)).bit_count()
                for j in range(1,width+1):x[17+(i-1)*width+j-1]=prefix>=j
            ok=evaluate(local,x);need(ok==(bits.bit_count()<=7),'all sixteen-input canonical predicates')
            allowed+=ok
        need(allowed==26333,'complete sixteen-input population')
        outputs[-1]['sixteen_bit_inputs']=65536;outputs[-1]['accepted_inputs']=allowed
        for m in range(1,4):
            for k in range(m):
                local,aux=counter(kind,list(range(1,m+1)),k,m+1);counts=[0]*(1<<m)
                for vals in product([False,True],repeat=m+aux):
                    assignment={j+1:v for j,v in enumerate(vals)}
                    if evaluate(local,assignment):
                        index=sum(1<<j for j in range(m) if vals[j]);counts[index]+=1
                    states+=1
                for bits,count in enumerate(counts):
                    need((count>0)==(bits.bit_count()<=k),'small full existential projection')
                    if kind=='functional':need(count==int(bits.bit_count()<=k),'functional uniqueness')
                if kind=='sequential' and (m,k)==(3,1):need(counts[0]>1,'sequential nonunique positive control')
                cohorts+=1
    # Removing the final overflow actually admits the first forbidden last input.
    local,_=counter('sequential',[1,2],1,3)
    need(not evaluate(local,{1:True,2:True,3:True}) and evaluate(local[:-1],{1:True,2:True,3:True}),'overflow fault witness')
    bad.append('missing final overflow exposes explicit forbidden input')
    local,_=counter('functional',[1,2],1,3)
    need(not evaluate(local,{1:True,2:True,3:True,4:False,5:True,6:True}) and evaluate(local[:-1],{1:True,2:True,3:True,4:False,5:True,6:True}),'functional cap fault witness')
    bad.append('missing functional cap exposes explicit forbidden input')
    bad.append(rejected('zero literal',lambda:parse(b'p cnf 1 1\n0 0\n')))
    bad.append(rejected('malformed dimension',lambda:parse(b'p cnf 1 1\n2 0\n')))
    result={'status':'PASS_LITERAL_DEGREE_PROJECTION_CHECKS','formulas':outputs,'gate_truth_assignments':16,'small_joint_states':states,'small_cohorts':cohorts,'full_sixteen_input_checks':131072,'negative_controls':bad,'negative_controls_detected':len(bad),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact two saved CNFs and finite controls. Analytic induction proves existential projection for all graph inputs; no SAT decision or graph nonexistence certificate.'}
    if args.verify:need(json.loads(args.certificate.read_text())==result,'complete serialized degree certificate')
    else:
        with args.certificate.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':result['status'],'formulas':2,'small_cohorts':cohorts,'full_sixteen_input_checks':131072,'negative_controls_detected':len(bad)}))

if __name__=='__main__':main()
