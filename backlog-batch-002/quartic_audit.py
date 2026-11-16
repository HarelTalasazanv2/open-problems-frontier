"""Literal quartic algebra, exact integers/Fraction; no cohomology inference."""
from pathlib import Path
from fractions import Fraction
from itertools import product
from hashlib import sha256
import copy
import json
import argparse

INSTANCES = [(17,[83521,8092,646,28,1]),(23,[279841,27508,1702,52,1])]

def require(ok,msg):
    if not ok:
        raise ValueError(msg)

def rem(f,g,p=3):
    f=[c % p for c in f]
    while f and f[-1] == 0:
        f.pop()
    while len(f) >= len(g):
        c=f[-1]*pow(g[-1],p-2,p) % p
        k=len(f)-len(g)
        for j,a in enumerate(g):
            f[j+k]=(f[j+k]-c*a) % p
        while f and f[-1] == 0:
            f.pop()
    return f

def divisors():
    return [list(v)+[1] for degree in [1,2] for v in product(range(3),repeat=degree)]

def produce():
    rows=[]
    for p,f in INSTANCES:
        rows.append({'p':p,'coefficients_ascending':f,
                     'mod3_remainders':[{'divisor':g,'remainder':rem(f,g)} for g in divisors()],
                     'normalized_coefficients':[[a.numerator,a.denominator] for a in [Fraction(c,p**(4-i)) for i,c in enumerate(f)]]})
    return {'schema':'OPF_GITHUB_BATCH002_QUARTIC_V1','rows':rows}

def consume(payload):
    require(payload['schema']=='OPF_GITHUB_BATCH002_QUARTIC_V1','schema')
    require([r['p'] for r in payload['rows']]==[17,23],'complete exact prime identities')
    for row,(p,f) in zip(payload['rows'],INSTANCES):
        require(row['coefficients_ascending']==f,'literal coefficients')
        require([a % 3 for a in f]==[1,1,1,1,1],'Phi5 reduction')
        require([r['divisor'] for r in row['mod3_remainders']]==divisors(),'all12 divisors, exact membership')
        for r in row['mod3_remainders']:
            actual=rem(f,r['divisor'])
            require(r['remainder']==actual and actual,'nonzero exact remainder')
        normalized=[[a.numerator,a.denominator] for a in [Fraction(c,p**(4-i)) for i,c in enumerate(f)]]
        require(row['normalized_coefficients']==normalized,'exact p^-4 f(pX) normalization')
        require(normalized[3][1] > 1,'nonintegral cubic coefficient')
    return True

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);parser.add_argument('--verify',action='store_true');args=parser.parse_args()
    payload=json.loads(args.output.read_text()) if args.verify else produce()
    consume(payload)
    detected=[]
    def reject(name,mutant):
        try:
            consume(mutant)
        except ValueError:
            detected.append(name)
        else:
            raise ValueError('accepted '+name)
    bad=copy.deepcopy(payload);bad['rows'].pop();reject('missing instance',bad)
    bad=copy.deepcopy(payload);bad['rows'][1]=copy.deepcopy(bad['rows'][0]);reject('duplicate instance',bad)
    bad=copy.deepcopy(payload);bad['rows'][0]['coefficients_ascending'][1]+=1;reject('wrong coefficient',bad)
    bad=copy.deepcopy(payload);bad['rows'][0]['mod3_remainders'].pop();reject('missing divisor',bad)
    bad=copy.deepcopy(payload);bad['rows'][0]['mod3_remainders'][1]=copy.deepcopy(bad['rows'][0]['mod3_remainders'][0]);reject('duplicate divisor',bad)
    bad=copy.deepcopy(payload);bad['rows'][0]['mod3_remainders'][0]['remainder']=[2];reject('wrong nonzero remainder',bad)
    bad=copy.deepcopy(payload);bad['rows'][0]['normalized_coefficients'][3]=[28,1];reject('wrong scaling',bad)
    reducible=[1,0,2,0,1]  # (X^2+1)^2: no F3 roots, but reducible
    require(all(sum(c*pow(a,i,3) for i,c in enumerate(reducible)) % 3 for a in range(3)), 'root-only canary')
    require(rem(reducible,[1,0,1])==[], 'quadratic factor must be found')
    h=[16,-12,-2,-3,1]  # (T^2+2T+4)(T^2-5T+4)
    require(Fraction(h[3],2)==Fraction(-3,2),'nonintegral shortcut canary')
    # h(2X) is divisible by X^2+X+1, hence has2-times roots of unity.
    scaled=[c*2**i for i,c in enumerate(h)]
    quotient=[16,-40,16]
    product_coeff=[sum(quotient[j] for j in range(3) if 0 <= i-j < 3) for i in range(5)]
    require(scaled==product_coeff,'exact reducible shortcut counterexample')
    result={'status':'PASS_RESTRICTED','outcome':'PROVED','record':'M05-QUARTICS-NONCYCLOTOMIC-C178','polynomial_cases':2,'divisor_cases':24,
            'negative_controls_detected':detected,'analytic_control':'Reducible nonintegral normalized polynomial retains2-times cube roots of unity; irreducibility hypothesis is essential.',
            'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'claim_ceiling':'Literal polynomial irreducibility and all-orders p-times-root-of-unity exclusion only. No actual Frobenius-factor identification or rank/RM consequence.'}
    if not args.verify:
        with args.output.open('x') as f: json.dump(payload,f,indent=2);f.write('\n')
        with args.output.with_name('QUARTIC_AUDIT.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result))

if __name__=='__main__':
    main()
