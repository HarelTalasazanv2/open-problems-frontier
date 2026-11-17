"""Independent exact certificate consumer. Does not import discovery code."""
import json,sys
from math import isqrt,gcd
from fractions import Fraction as F

A=F(-7,3);B=F(107,108)
P=(F(1,3),F(1,2));Q=(F(4,3),F(1,2))
class Reject(Exception):pass
def need(ok,stage):
    if not ok:raise Reject(stage)
def intype(x):return type(x) is int
def add(p,q,a=A):
    if p is None:return q
    if q is None:return p
    u,v=p;x,y=q
    if u==x:
      if v+y==0:return None
      need(v==y,'invalid_addition')
      lam=(3*u*u+a)/(2*v)
    else:lam=(v-y)/(u-x)
    xx=lam*lam-u-x
    return xx,lam*(u-xx)-v
def scale(n,p):
    if n<0:return scale(-n,(p[0],-p[1])) if p is not None else None
    out=None
    while n:
      if n&1:out=add(out,p)
      p=add(p,p);n//=2
    return out
def original(p):return None if p is None else (p[0]-F(1,3),p[1]-F(1,2))
def lift(p):return None if p is None else (p[0]+F(1,3),p[1]+F(1,2))
def pack(p):return None if p is None else [p[0].numerator,p[0].denominator,p[1].numerator,p[1].denominator]
def readpoint(raw):
    need(type(raw) is list and len(raw)==4 and all(map(intype,raw)),'point_schema')
    a,b,c,d=raw
    need(b>0 and d>0 and gcd(a,b)==gcd(c,d)==1,'canonical_fraction')
    p=F(a,b),F(c,d);x,y=p
    need(y*y+y==x**3+x*x-2*x,'curve_equation')
    U,V=lift(p);need(V*V==U**3+A*U+B,'transformed_curve')
    return p
def universe():
    points=set();pairs=set();raw=0
    for v in range(1,2049):
      c=isqrt(v)
      if c*c!=v:continue
      for a in range(-2048,2049):
        raw+=1
        if gcd(a,v)!=1:continue
        pairs.add((a,c))
        # A rational square iff numerator/denominator of this reduced Fraction are squares.
        disc=4*F(a,v)**3+4*F(a,v)**2-8*F(a,v)+1
        if disc<0:continue
        n=isqrt(disc.numerator);d=isqrt(disc.denominator)
        if n*n!=disc.numerator or d*d!=disc.denominator:continue
        for t in {F(n,d),-F(n,d)}:
          p=F(a,v),(t-1)/2
          points.add(p)
    expected={(a,c) for c in range(1,46) for a in range(-2048,2049) if gcd(a,c)==1}
    need(pairs==expected and raw==184365 and len(pairs)==113201,'domain_membership')
    return points,raw,len(pairs)
def canaries():
    need(original(add(P,Q))==(F(-2),F(-1)),'canary_PplusQ')
    need(original(scale(2,P))==(F(3),F(5)),'canary_2P')
    need(original(scale(2,Q))==(F(6),F(-16)),'canary_2Q')
    need(add(P,(P[0],-P[1])) is None and add(None,Q)==Q,'canary_inverse_identity')
    # Valid 2-torsion boundary on a separate declared short curve y²=x³-x.
    T=(F(0),F(0));need(T[1]**2==T[0]**3-T[0] and add(T,T,F(-1)) is None,'canary_2torsion')
def bounds(data):
    need(data.get('height_normalization')=='lim4^-n*h(2^nP)','height_normalization')
    N=112**3;need(N==1404928 and N<2**21,'height_invariants')
    # Exact rational margins; analytic justifications for the logarithm inequalities are in the proof.
    need(1+F(7,10)+F(7,10)**2/2+F(7,10)**3/6>2,'log2_upper_canary')
    U=21*F(7,10)/6+F(7,10)+F(107,50)
    C=21*F(7,10)/4+F(7,10)+F(961,500)
    need(U<F(53,10) and C<F(63,10),'height_difference_margins')
    need((22*F(7,10)+F(53,10))/16==F(207,160)<F(13,10),'height_doubling_factor')
    need(F(13,10)+F(63,10)==F(38,5)<11*F(56,81),'finite_height_cutoff')
    need(45**2<=2048<46**2,'denominator_endpoint')
    fourths={k:pack(original(scale(4,p))) for k,p in [('P',P),('Q',Q),('R',add(P,Q))]}
    need(data.get('fourths')==fourths,'fourths')
    for raw in fourths.values():
      p=readpoint(raw);need(max(abs(p[0].numerator),p[0].denominator)<2**22,'fourth_height')
    return {'U_rational_upper':str(U),'C_rational_upper':str(C),'coset_height_upper':'207/160 < 13/10','naive_height_upper':'38/5 < 11*56/81 < 11log2','fourths':fourths}
def check(data):
    need(data.get('model')==[0,1,1,-2,0],'model')
    need(data.get('M')==2048,'domain_bound')
    canaries();bd=bounds(data)
    need(data.get('infinity')=={'point':None,'m':0,'n':0},'infinity')
    rows=data.get('rows');need(type(rows) is list,'rows_schema')
    supplied=[readpoint(row.get('point')) for row in rows]
    need(len(set(supplied))==len(supplied),'duplicate')
    expected,raw,coprime=universe();need(set(supplied)==expected,'complete_membership')
    need(data.get('point_count')==len(expected) and data.get('raw_pairs')==raw and data.get('coprime_pairs')==coprime,'declared_counts')
    maxcoeff=0
    for point,row in zip(supplied,rows):
      m,n=row.get('m'),row.get('n')
      need(intype(m) and intype(n) and abs(m)<=16 and abs(n)<=16,'coefficients')
      need(original(add(scale(m,P),scale(n,Q)))==point,'membership_witness')
      maxcoeff=max(maxcoeff,abs(m),abs(n))
    need(data.get('unknown')==[],'unknown_members')
    return {'status':'ACCEPT','affine_points':len(expected),'infinity':1,'raw_pairs':raw,'coprime_pairs':coprime,'max_witness_coefficient':maxcoeff,'bounds':bd,
      'finite_claim':'Complete affine point set of naiveheight<=log2048 has exact positiveLmembership witnesses.',
      'basis_claim':'Under named canonicalheight/difference theorems, provedheightball generation lemma and086/089quotient facts, E(Q)=ZP+ZQ;086independence makes aZbasis andtorsiontrivial. NoShaorder/fullBSD/regulator.'}
if __name__=='__main__':
    try:
      with open(sys.argv[1]) as f:data=json.load(f)
      result=check(data);code=0
    except Reject as e:result={'status':'REJECT','stage':str(e)};code=2
    except Exception as e:result={'status':'INVALID','error':type(e).__name__,'detail':str(e)};code=3
    print(json.dumps(result,sort_keys=True));sys.exit(code)
