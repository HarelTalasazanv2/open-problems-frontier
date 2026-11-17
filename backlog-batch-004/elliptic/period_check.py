"""Independent complete-integral binomial-series consumer; imports no producer."""
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path
import json
import sys

class Reject(Exception):
    pass

def need(ok,stage):
    if not ok:
        raise Reject(stage)

def g(x):
    return ((4*x+4)*x-8)*x+1

def interval(v):
    need(type(v) is list and len(v)==2,'INTERVAL_SHAPE')
    a,b=map(F,v)
    need(a<=b,'INTERVAL_ORDER')
    return a,b

def sqrt_iv(x,scale=10**18):
    need(x>=0,'SQRT_DOMAIN')
    n=isqrt(x.numerator*scale**2//x.denominator)
    lo=F(n,scale)
    hi=lo if lo**2==x else F(n+1,scale)
    return lo,hi

def atan_iv(x,n=60):
    power=x; total=F(0)
    for j in range(n):
        total+=power/(2*j+1)
        power*=-x*x
    tail=abs(power)/(2*n+1)
    return total-tail,total+tail

def pi_iv():
    # tan(atan(1/2)+atan(1/3))=1, with sum in the first quadrant.
    a=atan_iv(F(1,2)); b=atan_iv(F(1,3))
    return 4*(a[0]+b[0]),4*(a[1]+b[1])

def series(m,n=120):
    need(0<=m<1,'SERIES_DOMAIN')
    s=sum((F(comb(2*j,j)**2,16**j)*m**j for j in range(n)),F(0))
    tail=m**n/(1-m)
    return s,s+tail

def full_from_mean(pi,mean):
    need(mean[0]>0,'MEAN_DOMAIN')
    return 2*pi[0]/mean[1],2*pi[1]/mean[0]

def selftest():
    lo,hi=sqrt_iv(F(2),10)
    need(lo*lo<=2<=hi*hi and (lo,hi)==(F(7,5),F(3,2)),'SELFTEST_SQRT_OUTWARD')
    need(sqrt_iv(F(4))==(2,2),'SELFTEST_PERFECT_SQUARE')
    x=F(1,5); upper3=x-x**3/3+x**5/5
    need(atan_iv(x,1)[0]<upper3,'SELFTEST_ATAN_TAIL')
    need(series(F(0),1)==(1,1),'SELFTEST_SERIES_ZERO')
    # c1^2=1/4 gives a strict positive omitted term at m=1/2.
    need(series(F(1,2),1)[1]>F(9,8),'SELFTEST_SERIES_TAIL')
    need(full_from_mean((F(3),F(3)),(F(4),F(4)))==(F(3,2),F(3,2)),'SELFTEST_COMPONENT_FACTOR')

def check(c):
    need(c.get('schema')=='OPF_M02_REAL_PERIOD_C153_V1','SCHEMA')
    need(c.get('curve')==[0,1,1,-2,0] and c.get('cubic')==[4,4,-8,1],'MODEL')
    need(c.get('differential')=='dx/(2y+1)' and c.get('period')=='integral_all_E(R)_abs(omega)','NORMALIZATION')
    need(c.get('real_components')==2,'COMPONENT_COVERAGE')
    need(c.get('root_bisections')==40 and c.get('agm_steps')==4 and c.get('sqrt_scale')==10**18,'PARAMETERS')
    need(c.get('formula')=='Omega=2*pi/AGM(sqrt(e1-e3),sqrt(e1-e2))','FORMULA')
    rows=c.get('roots')
    need(type(rows) is list and len(rows)==3 and {r.get('id') for r in rows}=={'e1','e2','e3'},'ROOT_MEMBERSHIP')
    roots={r['id']:interval(r['interval']) for r in rows}
    need(all(g(v[0])*g(v[1])<0 for v in roots.values()),'ROOT_SIGN')
    e1,e2,e3=roots['e1'],roots['e2'],roots['e3']
    need(e3[1]<e2[0] and e2[1]<e1[0],'ROOT_ORDER')
    # Three disjoint sign-changing intervals account for every root of a cubic.
    A=e1[0]-e3[1],e1[1]-e3[0]
    B=e1[0]-e2[1],e1[1]-e2[0]
    C=e2[0]-e3[1],e2[1]-e3[0]
    need(A[0]>0 and B[0]>0 and C[0]>0,'ROOT_DOMAIN')
    p=pi_iv(); given_pi=interval(c['pi_interval'])
    need(given_pi[0]<=p[0] and p[1]<=given_pi[1],'PI_ENCLOSURE')
    # Independently check the finite AGM trace, as well as the different series.
    aa=(sqrt_iv(A[0])[0],sqrt_iv(A[1])[1])
    bb=(sqrt_iv(B[0])[0],sqrt_iv(B[1])[1])
    trace=[]
    for _ in range(4):
        newa=((aa[0]+bb[0])/2,(aa[1]+bb[1])/2)
        newb=(sqrt_iv(aa[0]*bb[0])[0],sqrt_iv(aa[1]*bb[1])[1])
        aa,bb=newa,newb
        trace.append({'a':list(map(str,aa)),'b':list(map(str,bb))})
    need(c.get('agm_trace')==trace,'AGM_TRACE')
    mean=interval(c['agm_interval'])
    need(mean==(bb[0],aa[1]),'AGM_ENCLOSURE')
    agm_period=full_from_mean(given_pi,mean)
    mlo,mhi=C[0]/A[1],C[1]/A[0]
    need(0<mlo<=mhi<1,'SERIES_DOMAIN')
    lower=series(mlo)[0]; upper=series(mhi)[1]
    sqrtA=sqrt_iv(A[0])[0],sqrt_iv(A[1])[1]
    secondary=2*p[0]*lower/sqrtA[1],2*p[1]*upper/sqrtA[0]
    claimed=interval(c['period_interval'])
    need(claimed[0]<=agm_period[0] and agm_period[1]<=claimed[1],'AGM_PERIOD_ENCLOSURE')
    need(claimed[0]<=secondary[0] and secondary[1]<=claimed[1],'SERIES_PERIOD_ENCLOSURE')
    one=interval(c['one_component_interval'])
    need(one[0]<=agm_period[0]/2 and agm_period[1]/2<=one[1],'ONE_COMPONENT_ENCLOSURE')
    need(claimed[0]>0 and claimed[1]-claimed[0]<F(1,10000),'TARGET')
    return {'outcome':'CERTIFIED_RANGE','period_interval':list(map(str,claimed)),
            'one_component_interval':list(map(str,one)),
            'width':str(claimed[1]-claimed[0]),'complete_real_components':2,
            'series_terms':120,'secondary_method':'positive binomial integral series with explicit tail',
            'arithmetic':'exact integer/Fraction','general_BSD_or_Sha_order_proved':False}

if __name__=='__main__':
    try:
        selftest()
        print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())))); sys.exit(0)
    except Reject as e:
        print(json.dumps({'outcome':'REJECTED','stage':str(e)})); sys.exit(2)
