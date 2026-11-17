"""Read-only exact consumer. No elimination or discovery-code imports."""
from fractions import Fraction
from math import gcd
from pathlib import Path
import json,sys

def need(ok,msg):
    if not ok:raise ValueError(msg)
def vector(terms,size):
    need(isinstance(terms,list),'terms must be list');v=[Fraction(0) for _ in range(size)];seen=set()
    for item in terms:
        need(isinstance(item,list) and len(item)==3,'rational triple')
        j,a,b=item;need(all(type(x)is int for x in item),'integer rational data')
        need(0<=j<size and j not in seen,'index membership/duplicate');seen.add(j)
        need(b>0 and a!=0 and gcd(abs(a),b)==1,'canonical nonzero rational');v[j]=Fraction(a,b)
    return v
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Fraction(0))
def verify(d,expected_level):
    need(expected_level in (11,389),'unsupported expected level');n=expected_level;m=n+1
    need(d.get('schema')=='OPF_MANIN_IMAGE_C060_V1','schema');need(d.get('level')==n and d.get('weight')==2 and d.get('a2')==-2,'level/weight/eigenvalue')
    symbols=[[0,1]]+[[1,x] for x in range(n)]
    need(d.get('symbols')==symbols,'complete ordered projective membership')
    matrices=[[1,0,0,2],[2,0,0,1],[2,1,0,1],[1,0,1,2]]
    need(d.get('hecke_matrices')==matrices,'exact Hecke matrix membership')
    def locate(u,v):
        u%=n;v%=n;need(u!=0 or v!=0,'projective origin')
        # Fermat inversion, distinct from discovery extended-Euclidean pow.
        if u==0:return 0
        return 1+(v*pow(u,n-2,n))%n
    relations=[];operator=[]
    for j,(u,v) in enumerate(symbols):
        for terms in ([j,locate(-v,u)],[j,locate(-v,u-v),locate(v-u,-u)]):
            row=[Fraction(0)]*m
            for k in terms:row[k]+=1
            relations.append(row)
        col=[Fraction(0)]*m;col[j]=2
        for a,b,c,e in matrices:col[locate(a*u+c*v,b*u+e*v)]+=1
        operator.append(col)
    # The alternate order-three generator generates the same triangle
    # relations, but its row ordering can differ. Compare the complete
    # declared relation rows using the discovery convention directly here.
    declared=d.get('relations');need(isinstance(declared,list) and len(declared)==2*m,'complete relation count')
    expected=[]
    for j,(u,v) in enumerate(symbols):
        for indices in ([j,locate(v,-u)],[j,locate(v,-u-v),locate(-u-v,u)]):
            row=[Fraction(0)]*m
            for k in indices:row[k]+=1
            expected.append(row)
    for i,row in enumerate(declared):
        need(row.get('id')==i,'complete ordered relation IDs');need(vector(row.get('terms'),m)==expected[i],'Manin relation formula')
    target=vector(d.get('target'),m);need(target==[Fraction(1)]+[Fraction(0)]*n,'nonzero fixed oriented target')
    if d.get('kind')=='IMAGE':
        w=vector(d.get('w'),m);rr=vector(d.get('r'),2*m);need(any(w),'zero Hecke witness')
        got=[Fraction(0)]*m
        for c,col in zip(w,operator):
            if c:
                for i,x in enumerate(col):got[i]+=c*x
        for c,row in zip(rr,expected):
            if c:
                for i,x in enumerate(row):got[i]+=c*x
        need(got==target,'raw exact image identity')
        return {'verdict':'PASS_EXACT_IMAGE','level':n,'coordinates_checked':m,'relations_checked':2*m,'nonzero_w':sum(bool(x)for x in w),'nonzero_r':sum(bool(x)for x in rr)}
    need(d.get('kind')=='NONIMAGE','kind');ell=vector(d.get('dual'),m);need(any(ell),'zero dual')
    need(all(dot(ell,row)==0 for row in expected),'dual annihilates every relation')
    need(all(dot(ell,col)==0 for col in operator),'dual annihilates every operator column')
    need(dot(ell,target)!=0,'dual detects central target')
    return {'verdict':'PASS_EXACT_NONIMAGE','level':n,'coordinates_checked':m,'relations_checked':2*m,'target_dual_pairing':str(dot(ell,target))}
def main():
    try:
        d=json.loads(Path(sys.argv[1]).read_text());out=verify(d,int(sys.argv[2]))
    except Exception as e:
        print(json.dumps({'verdict':'REJECT','error':str(e)}));return 1
    print(json.dumps(out));return 0
if __name__=='__main__':sys.exit(main())
