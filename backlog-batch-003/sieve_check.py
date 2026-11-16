"""Exact finite noncovering criterion and the fixed U877rational vector."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import isqrt,lcm,gcd
from hashlib import sha256
import argparse,copy,json

def need(ok,msg):
    if not ok:raise ValueError(msg)

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def factors(n):
    result={};p=2
    while p*p<=n:
        while n%p==0:result[p]=result.get(p,0)+1;n//=p
        p+=1
    if n>1:result[n]=result.get(n,0)+1
    return result

def rational(s):
    need(type(s) is str,'rational must be exact text')
    try:v=Q(s)
    except (ValueError,ZeroDivisionError):raise ValueError('invalid rational')
    need(str(v)==s,'canonical rational')
    return v

def evaluate(U,delta,diagonal_only=False,exponent_weight=False):
    need(len(U)==len(set(U)) and all(type(d) is int and d>1 for d in U),'distinct moduli')
    prime_keys=sorted({p for d in U for p in factors(d)})
    need(set(delta)==set(prime_keys) and all(Q(0)<=d<=Q(1,2) for d in delta.values()),'complete delta domain')
    groups={p:[] for p in prime_keys}
    for d in U:
        p=max(factors(d));power=1
        while d%(power*p)==0:power*=p
        groups[p].append((d,d//power,power))
    def nu(m):
        out=Q(1)
        for p,e in factors(m).items():out/=(1-delta[p])**(e if exponent_weight else 1)
        return out
    rows=[];beta=Q();pairs=0
    for p in prime_keys:
        group=groups[p];F=sum((nu(c)/d for d,c,power in group),Q());G=Q()
        for i,(d,c,power) in enumerate(group):
            for j,(e,b,power2) in enumerate(group):
                if diagonal_only and i!=j:continue
                pairs+=1;co=lcm(c,b);G+=nu(co)/(power*power2*co)
        alt=Q()
        for i,(d,c,_) in enumerate(group):
            for j in range(i,len(group)):
                e,b,_=group[j]
                alt+=(1 if i==j else 2)*Q(gcd(c,b),d*e)*nu(lcm(c,b))
        if not diagonal_only:need(G==alt,'ordered/unordered moment identity')
        contribution=F if delta[p]==0 else min(F,G/(4*delta[p]*(1-delta[p])))
        beta+=contribution
        rows.append({'prime':p,'moduli':sorted(d for d,_,_ in group),'F':str(F),'G':str(G),'contribution':str(contribution),'ordered_pairs':len(group)**2})
    return {'beta':str(beta),'margin':str(1-beta),'rows':rows,'ordered_pairs':pairs}

def accept_noncover(value):
    need(type(value) is Q,'exact threshold arithmetic')
    return value<1

def consume_candidate(data):
    need(data['schema']=='OPF_M09_RATIONAL_DELTA_V1' and data['P']==877,'fixed pool scope')
    U=[p-1 for p in range(5,878) if prime(p)]
    flags=bytearray(b'\x01')*878;flags[:2]=b'\x00\x00'
    for p in range(2,isqrt(877)+1):
        if flags[p]:flags[p*p:878:p]=bytes((877-p*p)//p+1)
    need(U==[p-1 for p in range(5,878) if flags[p]],'two complete prime oracles')
    need(data['moduli']==U and len(U)==149,'complete unique U877membership')
    entries=data['deltas'];keys=[row['prime'] for row in entries]
    need(len(keys)==len(set(keys))==47 and set(keys)=={p for d in U for p in factors(d)},'complete unique47keys')
    delta={row['prime']:rational(row['value']) for row in entries}
    out=evaluate(U,delta)
    beta=Q(out['beta']);need(accept_noncover(beta) and beta<Q(199983,200000),'strict fixed certificate bound')
    need(out['ordered_pairs']==1187,'complete ordered pairs')
    return out

def kernel(h,k,delta):
    alpha=Q(k,h)
    if alpha<=delta:
        return [Q()]*k+[1/(h*(1-alpha))]*(h-k)
    return [(alpha-delta)/(h*alpha*(1-delta))]*k+[1/(h*(1-delta))]*(h-k)

def kernel_tests():
    cells=prior_vectors=0
    def check(values,h,k,delta,prior):
        alpha=Q(k,h);need(len(values)==h and all(v>=0 for v in values),'kernel dimension/sign')
        need(sum(values,Q())==1,'kernel mass conservation')
        need(all(v<=1/(h*(1-delta)) for v in values),'kernel pointwise distortion')
        mass=prior*sum(values[:k],Q())
        need(mass<=prior*alpha,'first moment bound')
        if delta:need(mass<=prior*alpha*alpha/(4*delta*(1-delta)),'second moment bound')
    for h in range(1,10):
        for k in range(h+1):
            for d in [Q(),Q(1,8),Q(1,4),Q(1,2)]:
                values=kernel(h,k,d);cells+=1
                for prior in [Q(),Q(1,3),Q(1)]:check(values,h,k,d,prior);prior_vectors+=1
    broken=kernel(4,3,Q(1,2));broken[0]+=Q(1,4)
    try:check(broken,4,3,Q(1,2),Q(1))
    except ValueError:pass
    else:raise ValueError('bad actual kernel accepted')
    return {'cells':cells,'prior_vectors':prior_vectors,'zero_prior_and_alpha0_1_delta0_half':True,'actual_kernel_fault_detected':True}

def controls(data):
    detected=[]
    def reject(name,change):
        x=copy.deepcopy(data);change(x)
        try:consume_candidate(x)
        except ValueError:detected.append(name)
        else:raise ValueError('accepted bad candidate:'+name)
    reject('missing modulus',lambda x:x['moduli'].pop())
    reject('duplicate modulus same count',lambda x:x['moduli'].__setitem__(1,x['moduli'][0]))
    reject('wrong pool member',lambda x:x['moduli'].__setitem__(0,8))
    reject('missing prime key',lambda x:x['deltas'].pop())
    reject('duplicate prime key',lambda x:x['deltas'].__setitem__(1,copy.deepcopy(x['deltas'][0])))
    reject('float delta',lambda x:x['deltas'][0].update(value=0.0))
    reject('inadmissible delta',lambda x:x['deltas'][0].update(value='3/4'))
    reject('zero denominator',lambda x:x['deltas'][0].update(value='1/0'))
    reject('noncanonical rational',lambda x:x['deltas'][0].update(value='0/2'))
    correct=evaluate([4,8],{2:Q(1,2)})
    need(Q(correct['beta'])==Q(9,64),'hand first pool')
    wrong=evaluate([4,8],{2:Q(1,2)},diagonal_only=True)
    need(Q(wrong['rows'][0]['G'])==Q(5,64)!=Q(correct['rows'][0]['G']),'actual omitted-cross-term canary');detected.append('actual omitted ordered cross pairs')
    correct=evaluate([12],{2:Q(1,2),3:Q(1,2)})
    wrong=evaluate([12],{2:Q(1,2),3:Q(1,2)},exponent_weight=True)
    need(correct['rows'][-1]['F']=='1/6' and wrong['rows'][-1]['F']=='1/3','actual distinct-prime weight canary');detected.append('actual exponent instead of distinct-prime weight')
    need(Q(evaluate([6,12],{2:Q(1,2),3:Q(1,2)})['beta'])==Q(5,18),'hand cofactor pool')
    equal=Q(evaluate([2,3,6],{2:Q(),3:Q()})['beta']);need(equal==1 and not accept_noncover(equal),'actual strict beta boundary');detected.append('beta equality must not certify')
    classes=[(0,2),(0,3),(1,4),(1,6),(11,12)]
    need(all(any(n%m==a for a,m in classes) for n in range(12)),'known actual cover')
    value=Q(evaluate([m for a,m in classes],{2:Q(1,2),3:Q(1,2)})['beta'])
    need(value==Q(185,144) and not accept_noncover(value),'actual cover not falsely excluded')
    return detected

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--candidate',type=Path,required=True);parser.add_argument('--certificate',type=Path,required=True);parser.add_argument('--verify',action='store_true');args=parser.parse_args()
    data=json.loads(args.candidate.read_text());result=consume_candidate(data);detected=controls(data);kt=kernel_tests()
    report={'status':'PASS_RESTRICTED','records':['C146','C147'],'result':result,'kernel_controls':kt,'negative_controls_detected':detected,'negative_controls_scored':len(detected),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'candidate_sha256':sha256(args.candidate.read_bytes()).hexdigest(),'claim_ceiling':'Every subset of the fixed U877pool fails to cover Z, using the full finite criterion proof. No larger pool, density theorem, optimality or unrestricted global result.','independence':'Fresh code/formulation with exposed inputs/answers and shared actor/Python Fraction backend; nonblind, not external or formal.'}
    if args.verify:need(json.loads(args.certificate.read_text())==report,'saved exact certificate')
    else:
        with args.certificate.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
    print(json.dumps({'status':report['status'],'moduli':149,'prime_keys':47,'ordered_pairs':result['ordered_pairs'],'strict_beta_lt_199983_over_200000':True,'kernel_cells':kt['cells'],'prior_vectors':kt['prior_vectors'],'negative_controls':len(detected)}))

if __name__=='__main__':main()
