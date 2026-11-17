"""Confirmation: short-model group law; separately written enclosure consumer."""
import json
import sys
from fractions import Fraction as F
from pathlib import Path

class Rejected(Exception):
    pass

def require(ok, stage):
    if not ok:
        raise Rejected(stage)

def unit_log(r, terms=26):
    require(1 <= r <= 2, 'LOG_DOMAIN')
    z = (r-1)/(r+1)
    power = z
    s = F(0)
    for i in range(terms):
        s += 2*power/(2*i+1)
        power *= z*z
    tail = 2*power/((2*terms+1)*(1-z*z))
    return s, s+tail

def int_log(m):
    require(type(m) is int and m >= 1, 'LOG_DOMAIN')
    k = m.bit_length()-1
    bits = 64
    if k > bits:
        a = m >> (k-bits)
        u,v = F(a,2**bits),F(a+1,2**bits)
    else:
        u=v=F(m,2**k)
    z = unit_log(F(2))
    return unit_log(u)[0]+k*z[0], unit_log(v)[1]+k*z[1]

def sq(iv):
    a,b = iv
    require(a <= b, 'INTERVAL_ORDER')
    low = 0 if a <= 0 <= b else min(a*a,b*b)
    return F(low),max(a*a,b*b)

def det(p,q,r):
    xy = [a*b for a in p for b in q]
    cross = ((r[0]-p[1]-q[1])/2, (r[1]-p[0]-q[0])/2)
    v = sq(cross)
    return min(xy)-v[1],max(xy)-v[0]

A = F(-7,3)
B = F(107,108)

def oncurve(t):
    return t is None or t[1]**2 == t[0]**3+A*t[0]+B

def add(s,t):
    require(oncurve(s) and oncurve(t), 'POINT_DOMAIN')
    if s is None:
        return t
    if t is None:
        return s
    x,y=s; u,v=t
    if x == u and y == -v:
        return None
    m=(3*x*x+A)/(2*y) if s == t else (v-y)/(u-x)
    w=m*m-x-u
    z=m*(x-w)-y
    out=(w,z)
    require(oncurve(out), 'GROUP_LAW')
    return out

def lift(x,y):
    return F(x)+F(1,3),F(y)+F(1,2)

def selftest():
    p,q=lift(0,0),lift(1,0)
    require(add(p,q)==lift(-2,-1), 'SELFTEST_GROUP_SUM')
    require(add(p,p)==lift(3,5), 'SELFTEST_GROUP_DOUBLE')
    require(add(q,q)==lift(6,-16), 'SELFTEST_GROUP_DOUBLE')
    require(add(p,(p[0],-p[1])) is None and add(None,p)==p, 'SELFTEST_IDENTITY')
    require(int_log(1)==(0,0), 'SELFTEST_LOG_ONE')
    # The exact positive two-term series proves log(2)>56/81.
    require(unit_log(F(2),1)[1] > F(56,81), 'SELFTEST_LOG_TAIL')
    require(unit_log(F(2))[0] > F(56,81) and unit_log(F(2))[1] < F(7,10), 'SELFTEST_LOG_TWO')
    require(sq((F(-2),F(3)))==(0,9) and sq((F(-3),F(-2)))==(4,9), 'SELFTEST_SQUARE')
    require(det((F(2),F(2)),(F(3),F(3)),(F(7),F(7)))==(5,5), 'SELFTEST_PAIRING')

def parse_interval(v):
    require(type(v) is list and len(v)==2, 'INTERVAL_SHAPE')
    iv=tuple(map(F,v))
    require(iv[0] <= iv[1], 'INTERVAL_ORDER')
    return iv

def check(c):
    require(c.get('schema')=='OPF_M02_HEIGHT_DETERMINANT_C152_V1','SCHEMA')
    require(c.get('curve')==[0,1,1,-2,0],'MODEL')
    require(c.get('height')=='H=lim4^-n*h_x(2^nT)' and c.get('pairing')=='(H(P+Q)-H(P)-H(Q))/2','NORMALIZATION')
    require(c.get('doublings')==8,'EXPONENT')
    require(c.get('lower_height_difference')=='-63/10' and c.get('upper_height_difference')=='53/10','SOURCE_BOUND')
    require(c.get('log_method')=={'terms':24,'retained_bits':60,'tail':'positive_geometric'},'LOG_SPEC')
    rows=c.get('points')
    require(type(rows) is list and len(rows)==3 and {r.get('id') for r in rows}=={'P','Q','R'},'MEMBERSHIP')
    byid={r['id']:r for r in rows}; heights={}
    for name,xy in [('P',[0,0]),('Q',[1,0]),('R',[-2,-1])]:
        row=byid[name]
        require(row.get('point')==xy,'POINT_DOMAIN')
        t=lift(*xy)
        for _ in range(8):
            t=add(t,t)
            require(t is not None,'SINGULAR_OR_TORSION')
        x=t[0]-F(1,3)
        require(row.get('x_after_doublings')==[hex(x.numerator),hex(x.denominator)],'EXACT_COORDINATE')
        h=int_log(max(abs(x.numerator),x.denominator))
        actual=((h[0]-F(63,10))/65536,(h[1]+F(53,10))/65536)
        given=parse_interval(row['height_interval'])
        require(given[0] <= actual[0] and actual[1] <= given[1], 'HEIGHT_ENCLOSURE')
        heights[name]=given
    actual=det(heights['P'],heights['Q'],heights['R'])
    claimed=parse_interval(c['determinant_interval'])
    require(claimed[0] <= actual[0] and actual[1] <= claimed[1], 'DETERMINANT_ENCLOSURE')
    require(claimed[0]>0 and claimed[1]-claimed[0] < F(1,1000),'TARGET')
    return {'outcome':'CERTIFIED_RANGE','determinant_interval':list(map(str,claimed)),
            'width':str(claimed[1]-claimed[0]),'doublings':8,'source_theorem':'imported Cremona Proposition3.5.1',
            'basis':'not needed for named-point determinant; regulator interpretation inherits Cycle090 full basis'}

if __name__=='__main__':
    try:
        selftest()
        answer=check(json.loads(Path(sys.argv[1]).read_text()))
        print(json.dumps(answer)); sys.exit(0)
    except Rejected as e:
        print(json.dumps({'outcome':'REJECTED','stage':str(e)})); sys.exit(2)
