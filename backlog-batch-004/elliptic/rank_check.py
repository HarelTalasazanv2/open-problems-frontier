"""Independent exact certificate consumer: no import of discover.py."""
import json, sys
from math import isqrt

I,J=112,-1712
TARGETS={'T':[1,0,-20,44,-24], 'P':[1,0,-2,4,9],
         'Q':[1,0,-8,4,4], 'R':[1,0,10,-4,1]}
class Reject(Exception):pass
def require(condition,stage):
    if not condition:raise Reject(stage)
def integer(x):return type(x) is int
def inv(g):
    a,b,c,d,e=g
    return c*c+12*a*e-3*b*d,9*b*c*d+72*a*c*e-2*c**3-27*(a*d*d+e*b*b)
def val(g,x):
    a,b,c,d,e=g
    return a*x**4+b*x**3+c*x*x+d*x+e
def universe():
    """Eliminate e from I,J, solve the resulting quadratic in d exactly."""
    found=set();triples=set()
    for a in range(-1,9):
      if a==0:continue
      for b in range(-2*abs(a),2*abs(a)+1):
       for c in range(-32,33):
        triples.add((a,b,c))
        A=108*a*a;B=27*b**3-108*a*b*c
        C=4*a*J-24*a*c*I+32*a*c**3+9*b*b*I-9*b*b*c*c
        D=B*B-4*A*C
        if D<0:continue
        s=isqrt(D)
        if s*s!=D:continue
        for n in {-B+s,-B-s}:
          if n%(2*A):continue
          d=n//(2*A);num=I+3*b*d-c*c
          if num%(12*a):continue
          e=num//(12*a);g=(a,b,c,d,e)
          require(inv(g)==(I,J),'enumerator_invariant')
          found.add(g)
    expected_triples={(a,b,c) for a in (-1,1,2,3,4,5,6,7,8)
      for b in range(-2*abs(a),2*abs(a)+1) for c in range(-32,33)}
    require(triples==expected_triples and len(triples)==10205,'domain_membership')
    return found,triples
def equivalence_root(g,h,u):
    a,b,c,d,e=g;A,B,C,D,E=h
    p=3*b*b-8*a*c;q=3*B*B-8*A*C
    r=b**3+8*a*a*d-4*a*b*c;s=B**3+8*A*A*D-4*A*B*C
    # Evaluate27 times the monic polynomial; avoid rounded divisions.
    return (27*u**4-18*(32*a*A*I+p*q)*u*u-216*r*s*u
      +64*I*(a*a*q*q+A*A*p*p+a*A*p*q)
      -256*a*A*J*(a*q+A*p)-p*p*q*q)==0
def check(data):
    require(data.get('I')==I and data.get('J')==J,'invariant_pair')
    require(data.get('targets')==TARGETS,'targets')
    for g in TARGETS.values():require(inv(g)==(I,J) and g[0]==1,'target_solubility')
    require(val(TARGETS['T'],2)==0,'trivial_target')
    # Elliptic invariants and rational model map, checked coefficientwise.
    b2,b4,b6,b8=4,-4,1,-3
    c4=b2*b2-24*b4;c6=-b2**3+36*b2*b4-216*b6
    delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    require((c4,2*c6,delta)==(I,J,389),'elliptic_model')
    # 46656*(x^3+x^2-2x)+11664 equals(36x+12)^3-3024(36x+12)+46224.
    require((36**3,3*36*36*12,3*36*12*12-3024*36,12**3-3024*12+46224)
      ==(46656,46656,-93312,11664),'model_isomorphism')
    rows=data.get('rows');require(type(rows) is list,'schema')
    supplied=[];counts={}
    for row in rows:
      g=row.get('coefficients')
      require(type(g) is list and len(g)==5 and all(map(integer,g)),'schema')
      require(inv(g)==(I,J),'row_invariant')
      supplied.append(tuple(g))
    require(len(set(supplied))==len(supplied),'duplicate')
    expected,triples=universe()
    require(set(supplied)==expected,'complete_membership')
    require(data.get('count')==len(expected) and data.get('triples')==len(triples),'declared_counts')
    for row in rows:
      cert=row.get('certificate');require(type(cert) is dict,'certificate_schema')
      require(cert.get('kind')=='equivalent' and cert.get('target') in TARGETS,'certificate_kind')
      u=cert.get('root');require(integer(u),'root_type')
      require(equivalence_root(row['coefficients'],TARGETS[cert['target']],u),'equivalence_root')
      counts[cert['target']]=counts.get(cert['target'],0)+1
    return {'status':'ACCEPT','triples':len(triples),'quartics':len(expected),'target_counts':counts,
      'finite_claim':'Every integral quartic with invariants112,-1712 in the conservative box is equivalent to at least one of T,P,Q,R by source Proposition3.6.3.',
      'rank_claim':'Under the explicitly sourced complete descent/reduction theorems and086 lower-bound proof, fixed E has rank2. No fullBSD/saturation/Sha claim.'}
if __name__=='__main__':
    try:
      with open(sys.argv[1]) as f:data=json.load(f)
      result=check(data);code=0
    except Reject as e:result={'status':'REJECT','stage':str(e)};code=2
    except Exception as e:result={'status':'INVALID','error':type(e).__name__,'detail':str(e)};code=3
    print(json.dumps(result,sort_keys=True));sys.exit(code)
