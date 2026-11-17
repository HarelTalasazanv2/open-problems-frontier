"""Rational outward enclosures for three historical M07 local claims."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import argparse
import json


def need(ok, message):
    if not ok:
        raise ValueError(message)


def scalar(x):
    need(type(x) in {int, F}, 'exact rational input required')
    return F(x), F(x)


def add(x, y): return x[0]+y[0], x[1]+y[1]
def neg(x): return -x[1], -x[0]
def sub(x, y): return add(x, neg(y))
def mul(x, y):
    products=[a*b for a in x for b in y]
    return min(products), max(products)
def div(x, y):
    need(not y[0] <= 0 <= y[1], 'zero-containing divisor')
    return mul(x, (1/y[1], 1/y[0]))


def log_point(x, terms=80):
    need(type(x) in {int,F} and x > 0, 'positive rational logarithm')
    x=F(x)
    if x < 1: return neg(log_point(1/x,terms))
    z=(x-1)/(x+1)
    lower=sum((2*z**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    tail=2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return lower,lower+tail


def log_interval(x):
    need(0 < x[0] <= x[1], 'positive interval logarithm')
    return log_point(x[0])[0],log_point(x[1])[1]


P=scalar(F(1,10));Q=scalar(F(9,10));ONE=scalar(1)


def values(r):
    need(1 < r[0] <= r[1], 'r strictly above equilibrium')
    a=add(mul(P,r),Q);lr=log_interval(r);la=log_interval(a)
    d=sub(mul(mul(P,r),lr),mul(a,la))
    need(d[0] > 0, 'positive entropy denominator')
    i=mul(mul(P,Q),mul(sub(r,ONE),lr))
    ip=mul(mul(P,Q),sub(add(lr,ONE),div(ONE,r)))
    dp=mul(P,sub(lr,la))
    stationary=sub(mul(ip,d),mul(i,dp))
    ell=div(la,sub(a,ONE))
    I2=div(mul(mul(P,Q),add(r,scalar(3))),scalar(2))
    D2=sub(Q,mul(mul(Q,Q),ell))
    c=div(sub(mul(I2,d),mul(i,D2)),mul(scalar(2),mul(d,d)))
    h=sub(mul(add(r,ONE),d),mul(div(r,a),i))
    beta=div(sub(mul(mul(P,Q),add(r,scalar(3))),
                     mul(mul(scalar(2),div(i,d)),D2)),mul(scalar(2),d))
    return {'d':d,'stationary':stationary,'offdiagonal_C':c,'rotation_H':h,'mixed_beta':beta}


def controls():
    need(log_point(2,1)==(F(2,3),F(25,36)), 'independent one-term log2 canary')
    need(sub((F(-2),F(3)),(F(5),F(7)))==(F(-9),F(-2)), 'signed subtraction')
    need(mul((F(-2),F(3)),(F(-5),F(7)))==(F(-15),F(21)), 'signed product')
    need(div((F(-2),F(3)),(F(2),F(4)))==(F(-1),F(3,2)), 'positive division')
    need(log_point(F(1,2))==neg(log_point(2)), 'reciprocal log sign')
    need(values(scalar(4))['offdiagonal_C'][1]<0, 'known negative nonoptimizer curvature')
    rejected=[]
    for name,fn in [('zero divisor',lambda:div(ONE,(F(-1),F(1)))),
                    ('equilibrium',lambda:values(scalar(1))),
                    ('float input',lambda:scalar(0.1)),
                    ('boolean input',lambda:scalar(True)),
                    ('zero logarithm',lambda:log_point(0))]:
        try:fn()
        except ValueError:rejected.append(name)
        else:raise ValueError('Invalid control accepted: '+name)
    return {'known_good_canaries':6,'invalid_inputs_detected':rejected}


def encode_fraction(x):
    return {'numerator_base16': hex(x.numerator), 'denominator_base16': hex(x.denominator)}


def decode_fraction(x):
    n=int(x['numerator_base16'],16);d=int(x['denominator_base16'],16)
    need(d>0,'positive serialized denominator')
    return F(n,d)


def calculate():
    bracket=(F(68809,8192),F(1100945,131072))
    v=values(bracket)
    need(F(4685,10**6)<v['offdiagonal_C'][0]<=v['offdiagonal_C'][1]<F(4690,10**6),'C017 strict enclosure')
    need(F(9,10)<v['rotation_H'][0]<=v['rotation_H'][1]<F(91,100),'C018 strict enclosure')
    lo,hi=F(8),F(9)
    need(values(scalar(lo))['stationary'][1]<0 and values(scalar(hi))['stationary'][0]>0,'root endpoint signs')
    steps=[]
    for _ in range(18):
        mid=(lo+hi)/2;s=values(scalar(mid))['stationary']
        if s[1]<0:steps.append({'midpoint':str(mid),'sign':-1});lo=mid
        elif s[0]>0:steps.append({'midpoint':str(mid),'sign':1});hi=mid
        else:raise ValueError('Inconclusive root sign; no bisection promotion')
    beta=values((lo,hi))['mixed_beta']
    need(F(23,2500)<beta[0]<=beta[1]<F(6,625),'C036 strict beta enclosure')
    root=values((lo,hi))
    rr=(lo,hi);aa=add(mul(P,rr),Q);cc=div(mul(mul(P,Q),mul(sub(rr,ONE),log_interval(rr))),root['d'])
    h1=sub(div(mul(mul(P,Q),add(rr,ONE)),mul(rr,rr)),mul(cc,div(mul(P,Q),mul(rr,aa))))
    h2=mul(mul(P,Q),sub(scalar(2),cc))
    h3=mul(mul(scalar(2),root['d']),beta)
    need(all(x[0]>F(1,1000) for x in [h1,h2,h3]) and root['d'][1]<1,'C040normal margins')
    need(decode_fraction(encode_fraction(F(-3,7)))==F(-3,7),'signed hexadecimal rational roundtrip')
    encoded={k:[encode_fraction(a),encode_fraction(b)] for k,(a,b) in v.items()}
    return {'status':'PASS_EXACT_LOCAL_ENCLOSURES','historical_bracket':[str(x) for x in bracket],
            'bracket_intervals':encoded,'root_bracket':[str(lo),str(hi)],'bisections':steps,
            'mixed_beta':[encode_fraction(x) for x in beta], 'normal_coefficients':[[encode_fraction(y) for y in x] for x in [h1,h2,h3]], 'normal_margin_gt_1_over_1000':True,'controls':controls(),
            'arithmetic':'Exact Fraction intervals; positive atanh series and geometric outward tail; no float decision.',
            'claim_ceiling':'Six restricted local coefficient enclosures. Scalar uniqueness and Hessian/local-neighbourhood arguments are separately analytic; no global theorem or new optimum.',
            'rational_encoding':'Exact signed hexadecimal numerator / positive hexadecimal denominator',
            'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}


def main():
    p=argparse.ArgumentParser();p.add_argument('--certificate',type=Path,required=True);p.add_argument('--verify',action='store_true');a=p.parse_args()
    result=calculate()
    if a.verify:need(json.loads(a.certificate.read_text())==result,'complete serialized result')
    else:
        with a.certificate.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'status':result['status'],'local_coefficients':6,'root_sign_decisions':20,'arithmetic_canaries':7,'invalid_inputs_detected':5}))


if __name__=='__main__':main()
