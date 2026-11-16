"""Exact coefficient proof of eight fixed unit-fraction families."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
import argparse,copy,json

FAMILIES=[('even',2,0,[[0,1],[0,2],[0,2]]),('div3',3,0,[[0,1],[0,6],[0,6]]),
('mod3_2',3,2,[[1,1],[2,5,3],[2,3]]),('mod4_3',4,3,[[1,1],[6,14,8],[6,14,8]]),
('mod8_5',8,5,[[2,2],[5,13,8],[10,26,16]]),('div5',5,0,[[0,2],[0,4],[0,20]]),
('mod40_33',40,33,[[10,10],[165,365,200],[66,146,80]]),('mod20_17',20,17,[[5,5],[34,74,40],[170,370,200]])]

def need(ok,msg):
    if not ok:raise ValueError(msg)

def add(a,b):
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b):out[i+j]+=c*d
    return out

def value(a,t):
    out=0
    for c in reversed(a):out=out*t+c
    return out

def consume(data):
    need(data['schema']=='OPF_C158_UNIT_FRACTION_COVER_V1' and data['numerator']==4 and data['min_n']==2 and data['period']==120,'fixed domain')
    need(data['identity_degree_bound']==6 and data['identity_check_sites']==list(range(7)),'finite-to-infinite contract')
    rows=data['families'];need(len(rows)==8 and len({r['id'] for r in rows})==8,'complete family identities')
    byid={r['id']:r for r in rows};proofs=[]
    for name,m,r,denoms in FAMILIES:
        need(name in byid,'missing fixed family');row=byid[name]
        need(row['modulus']==m and row['residue']==r and row['denominators']==denoms,'fixed literal polynomial family')
        minimum=max(0,-((r-2)//m))
        need(row['min_t']==minimum,'minimum admissible parameter')
        for poly in denoms:
            need(1<=len(poly)<=3 and all(type(c) is int and c>=0 for c in poly),'integer nonnegative degree<=2')
            need(value(poly,minimum)>0,'positive denominators on full admitted domain')
        x,y,z=denoms
        lhs=[4*c for c in mul(mul(x,y),z)]
        rhs=mul([r,m],add(add(mul(x,y),mul(x,z)),mul(y,z)))
        residual=add(lhs,[-c for c in rhs]);need(all(c==0 for c in residual),'exact zero polynomial coefficients')
        # Independent rational evaluation challenges coefficient arithmetic at
        # the first three actual admissible n values; it is not the proof.
        for t in range(minimum,minimum+3):
            n=m*t+r;xs=[value(p,t) for p in denoms]
            need(n>=2 and sum((Q(1,a) for a in xs),Q())==Q(4,n),'rational identity boundary controls')
        proofs.append({'id':name,'min_t':minimum,'residual_coefficients':residual,'denominator_degrees':[len(p)-1 for p in denoms]})
    coverage=data['coverage'];need(len(coverage)==120 and len({r['residue'] for r in coverage})==120,'complete residue membership')
    rows_by_r={r['residue']:r for r in coverage};need(set(rows_by_r)==set(range(120)),'all exact residue identities')
    uncovered=[]
    for r in range(120):
        expected=sorted(name for name,m,a,ds in FAMILIES if r%m==a)
        actual=rows_by_r[r]['families'];need(len(actual)==len(set(actual)) and sorted(actual)==expected,'exact applicable family set')
        if not expected:uncovered.append(r)
    need(uncovered==data['uncovered']==[1,49],'exact method complement')
    witness=data['solved_uncovered_example'];need(witness['n']==49 and len(witness['denominators'])==3 and all(type(a) is int and a>0 for a in witness['denominators']),'admissible49witness')
    need(sum((Q(1,a) for a in witness['denominators']),Q())==Q(4,49),'49is solved despite family gap')
    need(data['global_conjecture_resolved'] is False and data['uncovered_are_counterexamples'] is False,'no global promotion')
    return {'families':proofs,'residue_classes':120,'covered_residue_classes':118,'uncovered_by_fixed_family':[1,49],'49_witness':[14,196,196]}

def controls(data):
    detected=[]
    def reject(name,change):
        x=copy.deepcopy(data);change(x)
        try:consume(x)
        except ValueError:detected.append(name)
        else:raise ValueError('accepted '+name)
    reject('missing family',lambda x:x['families'].pop())
    reject('duplicate family same count',lambda x:x['families'].__setitem__(1,copy.deepcopy(x['families'][0])))
    reject('wrong polynomial',lambda x:x['families'][0]['denominators'][0].__setitem__(0,1))
    reject('negative coefficient',lambda x:x['families'][0]['denominators'][0].__setitem__(0,-1))
    reject('wrong min parameter',lambda x:x['families'][0].update(min_t=0))
    reject('missing residue',lambda x:x['coverage'].pop())
    reject('duplicate residue same count',lambda x:x['coverage'].__setitem__(1,copy.deepcopy(x['coverage'][0])))
    reject('wrong applicable family',lambda x:x['coverage'][1]['families'].append('even'))
    reject('global numerator changed',lambda x:x.update(numerator=3))
    reject('domain includes1',lambda x:x.update(min_n=1))
    reject('fake complement',lambda x:x.update(uncovered=[1]))
    reject('global solution promotion',lambda x:x.update(global_conjecture_resolved=True))
    reject('gap promoted to counterexample',lambda x:x.update(uncovered_are_counterexamples=True))
    reject('zero witness denominator',lambda x:x['solved_uncovered_example']['denominators'].__setitem__(0,0))
    reject('missing root site',lambda x:x['identity_check_sites'].pop())
    reject('higher denominator degree',lambda x:x['families'][0]['denominators'][0].extend([0,1]))
    reordered=copy.deepcopy(data);reordered['families'].reverse();reordered['coverage'].reverse()
    for row in reordered['coverage']:row['families'].reverse()
    consume(reordered)
    return detected

def main():
    p=argparse.ArgumentParser();p.add_argument('--candidate',type=Path,required=True);p.add_argument('--certificate',type=Path,required=True);p.add_argument('--verify',action='store_true');args=p.parse_args()
    data=json.loads(args.candidate.read_text());result=consume(data);detected=controls(data)
    report={'status':'PASS_RESTRICTED','record':'M11-MOD120-C158','outcome':'PROVED','result':result,'negative_controls_detected':detected,'negative_controls_scored':len(detected),'equivalent_permutation_accepted':True,'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'candidate_sha256':sha256(args.candidate.read_bytes()).hexdigest(),'claim_ceiling':'For every n>=2outside1and49mod120the eight fixed families give positive integer unit-fraction solutions. Neither complement is a counterexample family; no global or current-status result.','independence':'Fresh exact coefficient convolution and boundary rational checks; same exposed actor/model/Python backend. Nonblind, no external/formal review.'}
    if args.verify:need(json.loads(args.certificate.read_text())==report,'saved unit-fraction audit')
    else:
        with args.certificate.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
    print(json.dumps({'status':report['status'],'identities':8,'residue_classes':120,'covered':118,'negative_controls':len(detected),'global_solution':False}))

if __name__=='__main__':main()
