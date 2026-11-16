"""Portable convention controls; universal claims rest on the analytic proofs."""
from pathlib import Path
from itertools import combinations
from math import comb
from hashlib import sha256
import json, argparse

def require(ok,msg):
    if not ok:
        raise ValueError(msg)

def adjacency(n,edges):
    return [set(j if i==v else i for i,j in edges if i==v or j==v) for v in range(n)]

def count_edges(edges,vertices):
    return sum(pair in edges for pair in combinations(vertices,2))

def excess_checks():
    membership=0;centre_faults=0
    def dual_membership(n,v,neighbors,B):
        require(set(B)==set(range(n))-neighbors-{v} and len(B)==n-1-len(neighbors),'dual exact membership')
    for n in range(5):
        pairs=list(combinations(range(n),2))
        for bits in range(1<<len(pairs)):
            e={p for i,p in enumerate(pairs) if bits>>i&1};adj=adjacency(n,e);lhs=rhs=0
            for v in range(n):
                N=sorted(adj[v]);B=sorted(set(range(n))-adj[v]-{v});d=len(N)
                dual_membership(n,v,adj[v],B)
                lhs+=2*(count_edges(e,B)-count_edges(e,N));rhs+=d*(n-2*d)
                require(count_edges(e,sorted(set(B)|{v}))==count_edges(e,B),'centre-edge insensitivity')
            require(lhs==rhs,'excess identity control')
            membership+=1
            if n:
                wrong=sorted((set(range(n))-adj[0]-{0})|{0})
                try:
                    dual_membership(n,0,adj[0],wrong)
                except ValueError:
                    centre_faults+=1
                else:
                    raise ValueError('centre membership fault survived')
    require(membership==76 and centre_faults==75,'complete small graph domain')
    t={21:107,22:113,23:119,24:127}
    def margin_table(strict_improvement):
        return {str(d):comb(45-d,2)-t[45-d]-t[d]+2*strict_improvement-d*(46-2*d)//2 for d in t}
    margins=margin_table(1)
    require(margins=={'21':2,'22':1,'23':1,'24':2},'exact threshold margins')
    # On K3 the correct doubled identity has lhs=rhs=-6. These three
    # wrong coefficient/sign/order conventions have nonzero residuals.
    triangle={(0,1),(0,2),(1,2)};adj=adjacency(3,triangle)
    A=sum(count_edges(triangle,sorted(set(range(3))-adj[v]-{v})) for v in range(3))
    C=sum(count_edges(triangle,sorted(adj[v])) for v in range(3))
    correct=sum(len(a)*(3-2*len(a)) for a in adj)
    wrong_n=sum(len(a)*(2-2*len(a)) for a in adj)
    require([A-C-correct,2*(C-A)-correct,2*(A-C)-wrong_n]==[3,12,6],'known-bad identity variants')
    # Losing the integer strict-boundary improvements destroys the proof
    # margin, so it cannot be accepted as the same four-case argument.
    require(list(margin_table(0).values())==[0,-1,-1,0],'strict threshold control')
    return {'complete_graph_orders':[0,1,2,3,4],'graphs_checked':76,'centre_membership_faults_detectable':75,'centre_empty_equivalent':1,'threshold_cases':4,'exact_margins':margins,'analytic_proof_required_for_all_n':True}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--certificate',type=Path,required=True);args=parser.parse_args()
    result=excess_checks()
    saved=json.loads(args.certificate.read_text())
    require(saved['controls']==result,'saved convention-control certificate')
    require(saved['code_sha256']==sha256(Path(__file__).read_bytes()).hexdigest(),'portable checker code pin')
    print(json.dumps({'status':'PASS_RESTRICTED','controls':result,'universal_proof':'See EXCESS_IDENTITY_PROOF.md and TYPED_COVERING_PROOF.md; finite checks do not establish their universal quantifiers.'}))

if __name__=='__main__':main()
