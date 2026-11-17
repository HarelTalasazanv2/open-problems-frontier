"""Exposed finite replays for the fixed curve; imported theorems remain explicit."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D
from hashlib import sha256
import argparse
import copy
import json
import central_check as central
import rank_check as rank
import basis_check as basis
import height_check as height
import period_check as period
import derivative_replay as derivative

HERE=Path(__file__).resolve().parent

def need(ok,message):
    if not ok: raise ValueError(message)

def read(name): return json.loads((HERE/name).read_text())

def reject(name,fn):
    try: fn()
    except (ValueError,central.ValueError if hasattr(central,'ValueError') else ValueError,
            rank.Reject,basis.Reject,height.Rejected,period.Reject): return name
    raise ValueError('Undetected selected fault: '+name)

def exp_bounds(x,k=200):
    if x<0:
        a,b=exp_bounds(-x,k);return 1/b,1/a
    need(x<k+2,'Taylor geometric tail domain')
    s=t=F(1)
    for j in range(1,k+1): t=t*x/j;s+=t
    nxt=t*x/(k+1)
    return s,s+nxt/(1-x/F(k+2))

def log_bounds(x,k=150):
    need(x>=1,'atanh log domain')
    z=(x-1)/(x+1)
    s=2*sum((z**(2*j+1)/F(2*j+1) for j in range(k)),F(0))
    return s,s+2*z**(2*k+1)/(F(2*k+1)*(1-z*z))

def encloses(given,exact):
    a,b=map(F,given);lo,hi=exact
    need(a<=lo<=hi<=b,'outward enclosure')

def derivative_contract(c,fresh):
    ignored={'seconds','python'}
    need(set(c)==set(fresh),'complete derivative fields')
    # All7900 cells are recomputed, not trusted from submitted finite_integral.
    # JSON normalization changes integer dictionary keys into strings only.
    need({k:v for k,v in c.items() if k not in ignored}==
         {k:v for k,v in json.loads(json.dumps(fresh)).items() if k not in ignored},
         'full derivative recomputation')
    need(F(c['raw_Lsecond'][0])>0,'strict nonzero second derivative')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--certificate',type=Path,required=True)
    ap.add_argument('--verify',action='store_true')
    args=ap.parse_args();controls=[]
    c389=read('central_389.json');c11=read('central_11.json')
    central_results=[central.verify(c389,389),central.verify(c11,11)]
    for name,change in [
        ('central omitted relation',lambda q:q['relations'].pop()),
        ('central zero witness',lambda q:q.update(w=[])),
        ('central wrong eigenvalue',lambda q:q.update(a2=2)),
        ('central zero target',lambda q:q.update(target=[]))]:
        q=copy.deepcopy(c389);change(q);controls.append(reject(name,lambda:central.verify(q,389)))
    q=copy.deepcopy(c11);q['dual']=[]
    controls.append(reject('central zero nonimage dual',lambda:central.verify(q,11)))
    rank_data=read('rank.json');rank_result=rank.check(rank_data)
    for name,change in [
        ('quartic omitted member with adjusted count',lambda q:(q['rows'].pop(),q.update(count=q['count']-1))),
        ('quartic duplicate membership',lambda q:q['rows'].append(copy.deepcopy(q['rows'][0]))),
        ('quartic forged equivalence root',lambda q:q['rows'][0]['certificate'].update(root=q['rows'][0]['certificate']['root']+1)),
        ('quartic boolean root',lambda q:q['rows'][0]['certificate'].update(root=True))]:
        q=copy.deepcopy(rank_data);change(q);controls.append(reject(name,lambda:rank.check(q)))
    basis_data=read('basis.json');basis_result=basis.check(basis_data)
    for name,change in [
        ('basis omitted point with adjusted count',lambda q:(q['rows'].pop(),q.update(point_count=q['point_count']-1))),
        ('basis false positive membership',lambda q:q['rows'][0].update(m=0,n=0)),
        ('basis missing infinity',lambda q:q.pop('infinity')),
        ('basis wrong height normalization',lambda q:q.update(height_normalization='half-height'))]:
        q=copy.deepcopy(basis_data);change(q);controls.append(reject(name,lambda:basis.check(q)))
    height.selftest();height_data=read('height.json');height_result=height.check(height_data)
    for name,change in [
        ('height missing point',lambda q:q['points'].pop()),
        ('height missing infinite-limit bound',lambda q:q.update(lower_height_difference='0')),
        ('height half convention',lambda q:q.update(height='half-height')),
        ('height inward determinant',lambda q:q.update(determinant_interval=['1','2']))]:
        q=copy.deepcopy(height_data);change(q);controls.append(reject(name,lambda:height.check(q)))
    period.selftest();period_data=read('period.json');period_result=period.check(period_data)
    for name,change in [
        ('period missing root',lambda q:q['roots'].pop()),
        ('period omitted real component',lambda q:q.update(real_components=1)),
        ('period half value',lambda q:q.update(period_interval=[str(F(x)/2) for x in q['period_interval']])),
        ('period inward interval',lambda q:q.update(period_interval=['5','6']))]:
        q=copy.deepcopy(period_data);change(q);controls.append(reject(name,lambda:period.check(q)))
    derivative_data=read('derivative.json');fresh=derivative.recompute()
    derivative_contract(derivative_data,fresh)
    for name,change in [
        ('derivative omitted cell',lambda q:q['grid'].update(count=7899,last=7898)),
        ('derivative missing coefficient',lambda q:q['coefficients'].pop()),
        ('derivative omitted coefficient tail',lambda q:q.update(coefficient_tail_included=False)),
        ('derivative omitted integration tail',lambda q:q.update(integration_tail_included=False)),
        ('derivative wrong factorial',lambda q:q.update(normalization='divided by two')),
        ('derivative inward endpoint',lambda q:q.update(raw_Lsecond=['2','3']))]:
        q=copy.deepcopy(derivative_data);change(q);controls.append(reject(name,lambda:derivative_contract(q,fresh)))
    canaries=[]
    for x in [F(0),F(3,10),F(-1),F(2),F(-24)]:
        encloses(derivative.fracI(x).exp().pair(),exp_bounds(x));canaries.append('exp '+str(x))
    for x in [F(1),F(5,4),F(2)]:
        encloses(derivative.fracI(x).ln().pair(),log_bounds(x));canaries.append('ln '+str(x))
    x=D('0.0000232019100737547389346735167208')
    need(F((-derivative.I(x)).a)==-F(x),'repaired exact negation')
    need(F(-x)>-F(x),'historical ambient negation fault reproduced')
    canaries.append('ambient negation fault and repaired path')
    controls.append(reject('derivative division across zero',lambda:derivative.I(1)/derivative.I(-1,1)))
    controls.append(reject('derivative invalid log',lambda:derivative.I(0).ln()))
    # The complete halving obstruction is independent of an assumed database rank.
    h1=lambda u:u**4-4*u**3+6*u+2
    hr=lambda u:u**4+8*u**3+12*u*u-18*u+5
    tors=lambda u:u**3+4*u*u-32*u+16
    need([h1(u)%3 for u in range(3)]==[2,2,1] and [hr(u)%3 for u in range(3)]==[2,2,1],'complete nonzero halving residues')
    need([tors(u)%5 for u in range(5)]==[1,4,1,3,1],'complete two-torsion obstruction')
    # h0=u^4+(2u-1/2)^2+11/4 and the duplication identity are analytic.
    polynomial_results={'halving_parity_classes':3,'mod3_residues':3,'two_torsion_mod5_residues':5,'known_true_half':basis.original(basis.scale(2,basis.P))==(F(3),F(5))}
    need(polynomial_results['known_true_half'],'known true half')
    result={'status':'PASS_FIXED_389A1_FINITE_REPLAYS','central':central_results,'quartics':rank_result,'basis':basis_result,'height':height_result,'period':period_result,'derivative_raw_range':derivative_data['raw_Lsecond'],'derivative_cells_reintegrated':7900,'derivative_coefficient_indices':100,'derivative_arithmetic_canaries':canaries,'halving':polynomial_results,'negative_controls':controls,'negative_controls_detected':len(controls),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'claim_ceiling':'Only the stated fixed curve, exact finite identities and enclosures. Mathematical modularity, descent completeness/equivalence, height theory, period identity and Kummer exactness are named imported theorems, not machine-proved here. No general BSD, full Sha, novelty or external expert/formal review.'}
    if args.verify: need(read_certificate(args.certificate)==result,'complete serialized finite-replay certificate')
    else:
        with args.certificate.open('x') as f: json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':result['status'],'records':8,'negative_controls_detected':len(controls),'derivative_cells_reintegrated':7900,'quartics':rank_result['quartics'],'affine_points':basis_result['affine_points']}))

def read_certificate(path): return json.loads(path.read_text())

if __name__=='__main__': main()
