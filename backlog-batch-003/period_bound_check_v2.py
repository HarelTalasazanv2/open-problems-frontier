"""Exact complete density/parity/CRT certificate; no solver or source-code imports."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import isqrt,gcd,lcm,prod
from hashlib import sha256
import argparse,copy,json

BOUND=393120
WITNESS=[(0,2),(1,4),(1,6),(7,10),(11,12),(9,18),(21,30),(15,36),(3,40),(15,60),(39,72),(39,180)]

def need(ok,msg):
    if not ok:raise ValueError(msg)

def prime_flags(n):
    flags=bytearray(b'\x01')*(n+1);flags[0:2]=b'\x00\x00'
    for a in range(2,isqrt(n)+1):
        if flags[a]:flags[a*a:n+1:a]=bytes((n-a*a)//a+1)
    return flags

def spf_table(n):
    # Linear least-prime-factor sieve, independent of the strided flag sieve.
    table=[0]*(n+1);primes=[]
    for a in range(2,n+1):
        if not table[a]:table[a]=a;primes.append(a)
        for p in primes:
            if p>table[a] or p*a>n:break
            table[p*a]=p
    return table

def divisors(n,spf):
    out=[1];remaining=n
    while remaining>1:
        p=spf[remaining];power=1;old=list(out)
        while remaining%p==0:
            remaining//=p;power*=p;out.extend(d*power for d in old)
    return out

def pool(n,flags,spf):
    return sorted(d for d in divisors(n,spf) if d>=4 and flags[d+1])

def verify_cover(rows,cutoff):
    mods=[m for a,m in rows]
    need(len(mods)==len(set(mods)) and bool(mods),'distinct nonempty moduli')
    P=lcm(*mods);need(P<=1000000,'cover resource cap')
    flags=prime_flags(max(mods)+1)
    need(all(type(a) is int and type(m) is int and 0<=a<m and m+1>=cutoff and flags[m+1] for a,m in rows),'canonical shifted primes')
    multiplicities=[sum(x%m==a for a,m in rows) for x in range(P)]
    need(all(multiplicities),'actual full-period cover')
    return P,min(multiplicities),max(multiplicities)

def compute():
    flags=prime_flags(BOUND);spf=spf_table(BOUND)
    need(all(bool(flags[a])==(spf[a]==a) for a in range(2,BOUND+1)),'complete prime agreement')
    capacity=[0]*BOUND
    for m in range(4,BOUND):
        if flags[m+1]:
            k=1
            for L in range(m,BOUND,m):capacity[L]+=k;k+=1
    survivors=[]
    # Check every capacity by the different complete-divisor route.
    for L in range(1,BOUND):
        ds=pool(L,flags,spf)
        direct=sum(L//m for m in ds)
        need(direct==capacity[L],'full-domain divisor capacity')
        if direct>=L:survivors.append((L,ds,direct))
    need(len(survivors)==28 and survivors[0][0]==55440,'exposed finite scope')
    p3=verify_cover(WITNESS,3)
    d360=pool(360,flags,spf);slots=sum(360//m for m in d360)
    need(p3==(360,1,3) and slots==280 and sum((Q(1,m) for m in d360),Q())==Q(7,9),'360 boundary')
    rows=[];cases_total=0
    for L,ds,T in survivors:
        forced=[m for m in ds if L//m>T-L]
        need(4 in forced and 6 in forced and 12*(T-L)<L,'opposite-parity prerequisites')
        parity=sum(max((12 if m%4==0 else 6)*(L//m),(12 if m%6==0 else 8)*(L//m)) for m in ds if m not in (4,6))
        row={'L':L,'pool':ds,'capacity':T,'forced':forced,'parity_capacity_scaled':parity,'parity_target_scaled':7*L}
        if parity<7*L:
            row['method']='parity'
        else:
            row['method']='CRT';q=lcm(*forced);axes=[m for m in forced if m!=4]
            groups={}
            for m in ds:
                if m not in forced:
                    g=gcd(q,m);groups[g]=groups.get(g,0)+L//lcm(q,m)
            records=[];maximum=None
            for residues in product(*(range(m) for m in axes)):
                holes=[u for u in range(q) if u%4 and all(u%m!=a for m,a in zip(axes,residues))]
                H=len(holes);cap=0
                for g,c in groups.items():
                    hist=[0]*g
                    for u in holes:hist[u%g]+=1
                    cap+=c*max(hist)
                margin=cap-H*(L//q)
                need(H>0 and margin<0,'strict all-configuration CRT exclusion')
                records.append({'residues':list(residues),'holes':H,'capacity':cap,'margin':margin})
                maximum=margin if maximum is None else max(maximum,margin)
            need(len(records)==prod(axes),'complete Cartesian configuration domain')
            row.update(Q=q,axes=axes,configurations=records,largest_margin=maximum)
            cases_total+=len(records)
        rows.append(row)
    maxima={str(r['L']):r['largest_margin'] for r in rows if r['method']=='CRT'}
    need(maxima=={'110880':-5474,'166320':-5943,'221760':-7116,'277200':-8793,'332640':-6477} and cases_total==14400,'CRT scope and outcomes')
    return {'schema':'OPF_BATCH003_PERIOD_BOUND_V1','minimum_prime':5,'exclusive_bound':BOUND,'positive_periods_checked':BOUND-1,'complete_prime_candidates_checked':BOUND-1,'density_survivors':28,'first_density_survivor':55440,'rows':rows,'CRT_configurations':cases_total,'boundary':{'p3_witness':[list(row) for row in WITNESS],'period':360,'coverage_min_max':[1,3],'p5_divisor_pool':d360,'available_slots':280,'guaranteed_uncovered_at_least':80},'claim_ceiling':'Any finite distinct p-1 (prime p>=5) covering must have exact LCM>=393120. No existence, optimality, current-best or global nonexistence claim.'}

def consume(actual,expected):
    need(actual['schema']==expected['schema'] and actual['minimum_prime']==5 and actual['exclusive_bound']==BOUND,'scope')
    need(actual['positive_periods_checked']==BOUND-1 and actual['density_survivors']==28,'complete density scope')
    rows=actual['rows'];need(len(rows)==len(expected['rows']),'period count')
    byL={r['L']:r for r in rows};need(len(byL)==len(rows) and set(byL)=={r['L'] for r in expected['rows']},'exact period identities')
    for e in expected['rows']:
        a=byL[e['L']]
        for k in ['pool','capacity','forced','parity_capacity_scaled','parity_target_scaled','method']:need(a[k]==e[k],'mathematical period field:'+k)
        if e['method']=='CRT':
            need(a['Q']==e['Q'] and a['axes']==e['axes'] and a['largest_margin']==e['largest_margin'],'CRT normalization/max')
            aa=a['configurations'];em={tuple(r['residues']):r for r in e['configurations']};am={tuple(r['residues']):r for r in aa}
            need(len(am)==len(aa)==len(em) and set(am)==set(em),'complete unique Cartesian identities')
            for key in em:need(am[key]==em[key],'semantic CRT holes/capacity/margin')
    for k in ['boundary','first_density_survivor','CRT_configurations','claim_ceiling']:need(actual[k]==expected[k],'summary:'+k)

def controls(expected):
    detected=[]
    def reject(name,change):
        x=copy.deepcopy(expected);change(x)
        try:consume(x,expected)
        except ValueError:detected.append(name)
        else:raise ValueError('accepted bad certificate:'+name)
    reject('missing period',lambda x:x['rows'].pop())
    reject('duplicate period same count',lambda x:x['rows'].__setitem__(1,copy.deepcopy(x['rows'][0])))
    reject('wrong capacity',lambda x:x['rows'][0].update(capacity=x['rows'][0]['capacity']+1))
    reject('omitted pool modulus',lambda x:x['rows'][0]['pool'].pop())
    reject('wrong forced set',lambda x:x['rows'][0]['forced'].pop())
    index=next(i for i,r in enumerate(expected['rows']) if r['method']=='CRT')
    reject('wrong CRT period',lambda x:x['rows'][index].update(Q=120))
    reject('omitted configuration',lambda x:x['rows'][index]['configurations'].pop())
    reject('duplicate configuration same count',lambda x:x['rows'][index]['configurations'].__setitem__(1,copy.deepcopy(x['rows'][index]['configurations'][0])))
    reject('forged zero margin',lambda x:x['rows'][index]['configurations'][0].update(margin=0))
    reject('forged maximum',lambda x:x['rows'][index].update(largest_margin=0))
    reject('wrong prime cutoff',lambda x:x.update(minimum_prime=3))
    # Actual cover consumer must reject using the p3 witness as a p5 witness.
    try:verify_cover(WITNESS,5)
    except ValueError:detected.append('p3 cover promoted to p5')
    else:raise ValueError('wrong cutoff accepted')
    changed=list(WITNESS);changed[-1]=(0,180)
    try:verify_cover(changed,3)
    except ValueError:detected.append('damaged boundary residue')
    else:raise ValueError('damaged boundary cover accepted')
    # Exact equality is retained in the density screen and not used as a
    # forced-modulus or negative-margin proof.
    need(sum(Q(1,m) for m in [2,4,6,12])==1,'density equality canary')
    need(not(Q(1,4)>Q(1,4)) and not(0<0),'strict forced/margin boundaries')
    return detected

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--certificate',type=Path,required=True);parser.add_argument('--verify',action='store_true');args=parser.parse_args()
    expected=compute();actual=json.loads(args.certificate.read_text()) if args.verify else expected
    consume(actual,expected);detected=controls(expected)
    if not args.verify:
        with args.certificate.open('x') as f:json.dump(expected,f,separators=(',',':'));f.write('\n')
        consume(json.loads(args.certificate.read_text()),expected)
        with args.certificate.with_name('PERIOD_AUDIT_V2.json').open('x') as f:json.dump({'status':'PASS_RESTRICTED','records':['C063','C064','C065'],'negative_controls_detected':detected,'negative_controls_scored':len(detected),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'prime_and_divisor_algorithms':'Strided Eratosthenes plus linear least-prime-factor sieve; every capacity checked by complete divisors.','independence':'Fresh implementation, same exposed actor/model/expected values/Python integers; notblind, external or formal.'},f,indent=2);f.write('\n')
    print(json.dumps({'status':'PASS_RESTRICTED','periods':BOUND-1,'density_survivors':28,'parity_exclusions':23,'CRT_configurations':14400,'negative_controls_detected':len(detected),'bound':BOUND}))

if __name__=='__main__':main()
