"""Exact input bindings and Gram algebra for the separately proved C181 geometry."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from hashlib import sha256
import argparse,copy,importlib.util,json

def need(ok,msg):
    if not ok: raise ValueError(msg)

def normalized(v,p):
    need(len(v)==3 and all(type(x) is int for x in v),'projective vector')
    j=next((i for i,x in enumerate(v) if x%p),None)
    need(j is not None,'nonzero projective vector')
    a=pow(v[j]%p,p-2,p)
    return tuple(x*a%p for x in v)

def check(data):
    path=Path(__file__).resolve().parents[2]/'backlog-batch-002/finite_count_audit.py'
    spec=importlib.util.spec_from_file_location('owned_geometry_base',path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    need([r['p'] for r in data['instances']]==[17,23],'complete ordered field membership')
    outputs=[]
    for instance in data['instances']:
        p=instance['p'];reference=m.geometry(p)
        lines=instance['lines'];nodes=instance['nodes']
        need(len(lines)==6 and [normalized(v,p) for v in lines]==[normalized(v,p) for v in reference['lines']],'exact six line bindings')
        pairs=list(combinations(range(6),2))
        need([tuple(row['pair']) for row in nodes]==pairs,'exact fifteen node-pair identities')
        for row,ref in zip(nodes,reference['nodes']):
            v=row['point']
            need(normalized(v,p)==normalized(ref['point'],p),'actual node binding')
            incidence=[i for i,l in enumerate(lines) if sum(a*b for a,b in zip(l,v))%p==0]
            need(incidence==row['incident_lines']==row['pair'],'complete exactly-two-line incidence')
        # Vieta gives the full polynomial factor identity with scalar -7;
        # no finite point sample is substituted for that algebraic identity.
        need(reference['factor_scalar']==-7,'literal sextic normalization')
        diag=[2]+[-2]*15;G=[[F(diag[i] if i==j else 0) for j in range(16)] for i in range(16)]
        det=F(1);rank=0
        for j in range(16):
            pivot=next((i for i in range(rank,16) if G[i][j]),None)
            if pivot is None:continue
            if pivot!=rank:G[pivot],G[rank]=G[rank],G[pivot];det=-det
            d=G[rank][j];det*=d;G[rank]=[x/d for x in G[rank]]
            for i in range(rank+1,16):
                a=G[i][j];G[i]=[x-a*y for x,y in zip(G[i],G[rank])]
            rank+=1
        need(rank==16 and det==-65536,'exact nondegenerate rational Gram')
        outputs.append({'p':p,'lines':6,'nodes':15,'divisor_classes':16,'pairings':256,'rank':rank,'determinant':str(det),'untwisted_action_if_standard_imports':str(p)+'I16','twisted_action_if_standard_imports':'I16'})
    return outputs

def reject(name,fn):
    try:fn()
    except ValueError:return name
    raise ValueError('Undetected geometry defect: '+name)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--certificate',type=Path,required=True);ap.add_argument('--verify',action='store_true');args=ap.parse_args()
    here=Path(__file__).resolve().parent;data=json.loads((here/'geometry_inputs.json').read_text());results=check(data);controls=[]
    for name,change in [('missing field',lambda q:q['instances'].pop()),('duplicate field',lambda q:q['instances'].__setitem__(1,copy.deepcopy(q['instances'][0]))),('missing node',lambda q:q['instances'][0]['nodes'].pop()),('duplicate node',lambda q:q['instances'][0]['nodes'].__setitem__(-1,copy.deepcopy(q['instances'][0]['nodes'][0]))),('changed point',lambda q:q['instances'][0]['nodes'][0].update(point=[0,0,1])),('wrong incidence',lambda q:q['instances'][0]['nodes'][0].update(incident_lines=[0,2]))]:
        q=copy.deepcopy(data);change(q);controls.append(reject(name,lambda:check(q)))
    # A permutation among equally negative exceptional classes preserves the
    # pairing but is not pointwise scalar Frobenius. Reject that inference.
    d=[2]+[-2]*15;perm=list(range(16));perm[1],perm[2]=perm[2],perm[1]
    need(all(d[perm[i]]==d[i] for i in range(16)) and perm!=list(range(16)),'pairing-preserving nonscalar action canary')
    controls.append('similitude alone does not imply scalar action')
    out={'status':'PASS_C181_GEOMETRY_INPUTS','instances':results,'negative_controls':controls,'negative_controls_detected':len(controls),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact input and rational matrix facts. Smooth minimal resolution and16-dimensional cohomological subspace are the separately reviewed analytic deductions under named standard imports. No observed full Frobenius operator or Hodge/RM theorem.'}
    if args.verify:need(json.loads(args.certificate.read_text())==out,'complete serialized geometry certificate')
    else:
        with args.certificate.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({'status':out['status'],'fields':2,'nodes':30,'negative_controls_detected':len(controls)}))

if __name__=='__main__':main()
