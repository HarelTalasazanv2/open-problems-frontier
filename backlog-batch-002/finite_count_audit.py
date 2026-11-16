"""Exact, nonblind re-audit of four literal double planes; standard library only.

Run with -B -OO. require() is intentional: verification must survive -OO.
The producer uses quadratic factors and root multiplicities. The consumer
uses norms of six linear factors and a prime-field Legendre character.
"""
from pathlib import Path
from collections import Counter
from itertools import combinations
from hashlib import sha256
import argparse
import copy
import json

CASES = [(17, 1, 0, 313), (23, 1, 0, 547),
         (17, 2, 3, 83881), (23, 2, 5, 280729)]
MODEL = 'W^2=(-y^2+8yz-8z^2)(7x^2+40xz+56z^2)(2x^2+3xy+y^2)'

def require(ok, reason):
    if not ok:
        raise ValueError(reason)

class Field:
    def __init__(self, p, e, d):
        require(type(p) is int and p > 2 and all(p % n for n in range(2, p)), 'odd prime')
        require((e == 1 and d == 0) or (e == 2 and 0 < d < p), 'field contract')
        require(e == 1 or d not in {a*a % p for a in range(p)}, 'irreducible modulus')
        self.p, self.e, self.d, self.q = p, e, d, p**e

    def add(self, x, y):
        p = self.p
        return (x % p + y % p) % p + p*((x//p + y//p) % p)

    def neg(self, x):
        return (-x % self.p) % self.p + self.p*((-(x//self.p)) % self.p)

    def mul(self, x, y):
        p, d = self.p, self.d
        a, b, c, f = x % p, x//p, y % p, y//p
        return (a*c+d*b*f) % p + p*((a*f+b*c) % p)

    def scale(self, c, x):
        return self.mul(c % self.p, x)

    def power(self, x, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, x)
            x = self.mul(x, x)
            n //= 2
        return out

def model(f, x, y, z):
    xx, yy, zz = f.mul(x,x), f.mul(y,y), f.mul(z,z)
    q1 = f.add(f.add(f.neg(yy), f.scale(8, f.mul(y,z))), f.scale(-8,zz))
    q2 = f.add(f.add(f.scale(7,xx), f.scale(40,f.mul(x,z))), f.scale(56,zz))
    q3 = f.add(f.add(f.scale(2,xx), f.scale(3,f.mul(x,y))), yy)
    return f.mul(f.mul(q1,q2),q3)

def points(q):
    for y in range(q):
        for z in range(q):
            yield 0, (1,y,z)
    for z in range(q):
        yield 1, (0,1,z)
    yield 2, (0,0,1)

def geometry(p):
    r = [t for t in range(p) if (-t*t+8*t-8) % p == 0]
    s = [t for t in range(p) if (7*t*t+40*t+56) % p == 0]
    require(len(r) == len(s) == 2, 'six split lines')
    require((sum(r)-8) % p == 0 and (r[0]*r[1]-8) % p == 0, 'q1 Vieta')
    require((7*sum(s)+40) % p == 0 and (7*s[0]*s[1]-56) % p == 0, 'q2 Vieta')
    lines = [(0,1,(-t) % p) for t in r]+[(1,0,(-t) % p) for t in s]+[(1,1,0),(2,1,0)]
    def norm(v):
        i = next((i for i in range(3) if v[i] % p), None)
        require(i is not None, 'distinct lines')
        inv = pow(v[i] % p,p-2,p)
        return tuple(x*inv % p for x in v)
    require(len({norm(l) for l in lines}) == 6, 'distinct six lines')
    nodes = []
    for i,j in combinations(range(6),2):
        a,b = lines[i],lines[j]
        v = norm((a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]))
        incident = [k for k,l in enumerate(lines) if sum(u*w for u,w in zip(l,v)) % p == 0]
        require(incident == [i,j], 'transverse exactly-two-line node')
        nodes.append({'pair':[i,j], 'point':list(v)})
    require(len({tuple(n['point']) for n in nodes}) == 15, '15 distinct nodes')
    return {'lines':lines, 'nodes':nodes, 'factor_scalar':-7}

def norm_fibre(p, e, d, lines, v):
    # Does not call Field.add, Field.mul, model or the producer square table.
    coordinates = [(t % p,t//p) for t in v]
    n = (-7) % p if e == 1 else 49 % p
    for line in lines:
        a = sum(c*t[0] for c,t in zip(line,coordinates)) % p
        b = sum(c*t[1] for c,t in zip(line,coordinates)) % p
        n = n*(a if e == 1 else (a*a-d*b*b)) % p
    if n == 0:
        return 1
    character = pow(n,(p-1)//2,p)
    require(character in (1,p-1), 'prime character')
    return 2 if character == 1 else 0

def produce(case):
    p,e,d,target = case
    f = Field(p,e,d)
    roots = [0]*f.q
    for w in range(f.q):
        roots[f.mul(w,w)] += 1
    require(Counter(roots) == Counter({0:(f.q-1)//2,1:1,2:(f.q-1)//2}), 'root table distribution')
    payload = bytes(roots[model(f,*v)] for _,v in points(f.q))
    meta = {'p':p,'e':e,'d':d,'q':f.q,'model':MODEL,'chart_sizes':[f.q*f.q,f.q,1],
            'fibres_sha256':sha256(payload).hexdigest(),'singular_count':sum(payload),
            'fibre_counts':{str(k):payload.count(k) for k in range(3)},
            'resolved_count':sum(payload)+15*f.q}
    return meta,payload

def consume(case, meta, payload):
    p,e,d,target = case
    q = p**e
    Field(p,e,d)  # separately admit exactly the frozen field
    require({k:meta.get(k) for k in ['p','e','d','q','model','chart_sizes']} ==
            {'p':p,'e':e,'d':d,'q':q,'model':MODEL,'chart_sizes':[q*q,q,1]}, 'case/model/chart contract')
    require(len(payload) == q*q+q+1, 'full projective membership length')
    require(set(payload) <= {0,1,2}, 'root multiplicity domain')
    require(sha256(payload).hexdigest() == meta['fibres_sha256'], 'payload custody')
    lines = geometry(p)['lines']
    chart_sums, chart_sizes = [0,0,0], [0,0,0]
    # Index membership is exact: the three disjoint canonical charts map to
    # indices y*q+z; q^2+z; q^2+q, respectively.
    visited = bytearray(len(payload))
    for i,(chart,v) in enumerate(points(q)):
        expected_index = v[1]*q+v[2] if chart == 0 else q*q+(v[2] if chart == 1 else q)
        require(i == expected_index and not visited[i], 'canonical membership')
        visited[i] = 1
        expected = norm_fibre(p,e,d,lines,v)
        require(payload[i] == expected, 'semantic fibre mismatch')
        chart_sizes[chart] += 1
        chart_sums[chart] += expected
    require(all(visited) and chart_sizes == [q*q,q,1], 'complete chart membership')
    require(sum(chart_sums) == meta['singular_count'] == target, 'exact count')
    require({str(k):payload.count(k) for k in range(3)} == meta['fibre_counts'], 'distribution')
    require(payload.count(1) == 6*q-9, 'branch union inclusion-exclusion')
    require(meta['resolved_count'] == target+15*q, 'resolution correction')
    return {'chart_sizes':chart_sizes,'chart_sums':chart_sums,'points_checked':len(payload),
            'geometry':geometry(p),'singular_count':target,'resolved_count':target+15*q}

def control_suite(case,meta,payload):
    rejected = []
    def reject(name,m,b):
        try:
            consume(case,m,b)
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError('invalid certificate accepted: '+name)
    m = copy.deepcopy(meta);m['model'] = 'wrong sign';reject('wrong model',m,payload)
    m = copy.deepcopy(meta);m['d'] += 1;reject('wrong field',m,payload)
    m = copy.deepcopy(meta);m['chart_sizes'][1] -= 1;reject('missing infinity metadata',m,payload)
    reject('short payload',meta,payload[:-1]);reject('long payload',meta,payload+b'\x00')
    b = bytearray(payload);b[0] = 3;m = copy.deepcopy(meta);m['fibres_sha256']=sha256(b).hexdigest();reject('invalid root byte with new hash',m,bytes(b))
    a,z = payload.index(0),payload.index(2)
    b = bytearray(payload);b[a],b[z] = b[z],b[a]
    m = copy.deepcopy(meta);m['fibres_sha256']=sha256(b).hexdigest()
    reject('same-total fibre swap with new hash',m,bytes(b))
    m = copy.deepcopy(meta);m['resolved_count'] += 15;reject('q+1 instead of q correction',m,payload)
    f = Field(*case[:3]);roots = Counter(f.mul(w,w) for w in range(f.q))
    nonsquare = next(a for a in range(1,f.q) if roots[a] == 0)
    positive = {'zero':f.q*f.q+f.q+1, 'square_z6':2*f.q*f.q+f.q+1, 'nonsquare_z6':f.q+1}
    totals = dict.fromkeys(positive,0)
    for _,v in points(f.q):
        v6 = f.power(v[2],6)
        totals['zero'] += roots[0]
        totals['square_z6'] += roots[v6]
        totals['nonsquare_z6'] += roots[f.mul(nonsquare,v6)]
    require(totals == positive, 'complete known-good fixtures')
    try:
        Field(case[0],2,1)
    except ValueError:
        rejected.append('reducible extension modulus')
    else:
        raise ValueError('reducible modulus accepted')
    return {'negative_controls_detected':rejected,'negative_controls_scored':9,
            'positive_fixture_totals':totals,'nonsquare_element_id':nonsquare}

def check_historical(root,case,meta):
    p,e,d,target = case
    if e == 1:
        path = root/'artifacts/m05_ej14_source_cycle174/basefield_certificate.json'
        old = next(row for row in json.loads(path.read_text())['results'] if row['p'] == p)
    else:
        folder = 'm05_f17sq_count_cycle175' if p == 17 else 'm05_f23sq_count_cycle176'
        path = root/'artifacts'/folder/'count_certificate.json'
        old = json.loads(path.read_text())
        source = (path.parent/'point_fibres.bin').read_bytes()
        f = Field(p,e,d);seen = bytearray(len(source))
        roots = Counter(f.mul(w,w) for w in range(f.q))
        for _,(x,y,z) in points(f.q):
            if z:
                inv = f.power(z,f.q-2)
                a,b = f.mul(x,inv),f.mul(y,inv)
                index = a*f.q+b
                expected = roots[model(f,a,b,1)]
            elif y:
                a = f.mul(x,f.power(y,f.q-2));index = f.q*f.q+a
                expected = roots[model(f,a,1,0)]
            else:
                index = f.q*f.q+f.q;expected=roots[model(f,1,0,0)]
            require(index < len(source) and not seen[index], 'historical membership')
            seen[index] = 1
            require(source[index] == expected, 'historical fibre mismatch')
        require(all(seen), 'historical full membership')
        require(sha256(source).hexdigest() == old['payload_sha256'], 'historical payload pin')
    require(old['singular_count'] == meta['singular_count'] and old['resolved_count'] == meta['resolved_count'], 'historical verdict mismatch')
    return {'path':str(path.relative_to(root)),'sha256':sha256(path.read_bytes()).hexdigest(),
            'verdict_match':True,'historical_per_fibre_check':e == 2}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--historical-root',type=Path)
    parser.add_argument('--verify',action='store_true')
    args = parser.parse_args()
    if not args.verify:
        args.output.mkdir(parents=True,exist_ok=False)
    results=[]
    for case in CASES:
        tag = 'F'+str(case[0]**case[1])
        if args.verify:
            meta=json.loads((args.output/(tag+'.json')).read_text())
            payload=bytes.fromhex((args.output/(tag+'.hex')).read_text())
        else:
            meta,payload=produce(case)
            (args.output/(tag+'.json')).write_text(json.dumps(meta,indent=2)+'\n')
            (args.output/(tag+'.hex')).write_text(payload.hex()+'\n')
        checked=consume(case,meta,payload)
        controls=control_suite(case,meta,payload)
        historical=check_historical(args.historical_root,case,meta) if args.historical_root else None
        results.append({'field':tag,'certificate':meta,'verification':checked,'controls':controls,'historical_comparison':historical})
    result={'status':'PASS_RESTRICTED','outcome':'CERTIFIED_RANGE','records':['C174','C175','C176'],
            'results':results,'total_projective_points':sum(r['verification']['points_checked'] for r in results),
            'negative_controls_detected':sum(len(r['controls']['negative_controls_detected']) for r in results),
            'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'claim_ceiling':'Four literal singular double-plane counts and explicit15-node resolution correction only; not a rank/RM/Frobenius/Hodge proof.',
            'independence':'Fresh algorithms, same exposed actor/model/Python integers; nonblind, no external human or formal verification.'}
    if not args.verify:
        (args.output/'AUDIT_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    else:
        previous=json.loads((args.output/'AUDIT_CERTIFICATE.json').read_text())
        require(previous['code_sha256'] == result['code_sha256'], 'code pin')
        require([r['certificate'] for r in previous['results']] == [r['certificate'] for r in results], 'saved certificate agreement')
    print(json.dumps({'status':result['status'],'fields':[(r['field'],r['certificate']['singular_count'],r['certificate']['resolved_count']) for r in results], 'points_checked':result['total_projective_points'],'negative_controls_detected':result['negative_controls_detected']}))

if __name__ == '__main__':
    main()
