"""Exact specified source-seed relationships. Downloaded code remains inert data."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
import argparse
import gzip
import json
import re
import shlex
from matrix_check import parse as parse_matrix, gram, require

HEADERS=[('+++',664),('+++',712),('++-',892),('++-',1132),('++-',1244),('+--',1368),('-++',1408),('+++',1672),('+++',1768),('+-+',1904),('++-',1948),('++-',1964)]
EXTRAS={'+-+':(336,48,48,48,48),'+--':(880,120,120,120,120),'-++':(1680,896,896,896,896)}
CASES=[(3,1132,'g'),(4,1244,'g'),(1,716,'h'),(5,1388,'v'),(9,1916,'w'),(6,1436,'u'),(7,1676,'h'),(8,1772,'h'),(10,1948,'g'),(11,1964,'g')]
GS=[[(0,1,0),(1,1,1),(2,1,1),(3,1,1)],[(1,-1,1),(0,1,0),(3,1,2),(2,-1,2)],[(2,-1,1),(3,-1,2),(0,1,0),(1,1,2)],[(3,-1,1),(2,1,2),(1,-1,2),(0,1,0)]]
TBL=[[(0,1,False),(1,1,True),(2,1,True),(3,1,True)],[(1,-1,True),(0,1,False),(3,1,False),(2,-1,False)],[(2,-1,True),(3,-1,False),(0,1,False),(1,1,False)],[(3,-1,True),(2,1,False),(1,-1,False),(0,1,False)]]
CORNER=['-++-','+-+-','++--','----']
TOP=['---+','--+-','-+--','+---']
LEFT=['+++-','--+-','-+--','+---']

class Heading(HTMLParser):
    def __init__(self):
        super().__init__();self.depth=0;self.count=0;self.parts=[]
    def handle_starttag(self,tag,attrs):
        if tag=='h1': self.depth+=1;self.count+=1
    def handle_endtag(self,tag):
        if tag=='h1': self.depth-=1
    def handle_data(self,s):
        if self.depth: self.parts.append(s)

def heading(raw):
    p=Heading();p.feed(raw.decode())
    s=''.join(p.parts)
    require(p.count==1 and p.depth==0 and s.startswith('levent on X: "') and s.endswith('"'),'heading contract')
    return s[len('levent on X: "'):-1]

def inert_derivative(raw):
    text=heading(raw); first,rest=text.split('\n',1)
    delimiter="<<'_'"; suffix='\n_\nsh /tmp/r $*'
    require(delimiter in first and rest.endswith(suffix),'inert wrapper contract')
    args=shlex.split(first.split(delimiter,1)[0]);prefix='s/M/\\\\/g;s/I/\\//g;y/'
    require(len(args)==2 and args[0]=='sed' and args[1].startswith(prefix) and args[1].endswith('/'),'inert alphabet contract')
    source,target=args[1][len(prefix):-1].split('/')
    require(len(source)==len(target) and len(set(source))==len(source),'one-to-one literal alphabet')
    return (rest[:-len(suffix)]+'\n').replace('M','\\').replace('I','/').translate(str.maketrans(source,target))

def records(payload,source):
    require(len(payload)==23828 and set(payload)==set('+-'),'payload grammar/membership')
    match=re.findall(r'e=\$\(echo ([a-p]+)\|sed',source)
    require(len(match)==1 and len(match[0])==48,'one complete header')
    bits=''.join(format(ord(c)-97,'04b') for c in match[0]);pos=0;out=[]
    for i,expected in enumerate(HEADERS):
        word=bits[16*i:16*(i+1)]
        code=word[:3].translate(str.maketrans('01','+-'))
        n=int(word[3:].translate(str.maketrans('01','10')),2)
        require((code,n)==expected,'ordered exact headers')
        lengths=(n,)+EXTRAS.get(code,());parts=[];start=pos
        for size in lengths:
            part=payload[pos:pos+size];require(len(part)==size,'complete source segment')
            parts.append(part);pos+=size
        out.append({'index':i,'code':code,'n':n,'start':start,'stop':pos,'parts':parts})
    require(pos==len(payload) and len(out)==12,'source exhaustion')
    return out

def sign(x): return 1 if x=='+' else -1

def source_rows(record,order,kind,fault=None):
    parts=record['parts']; main=parts[0]
    if kind in ('g','h'):
        m=len(main)//4; require(len(main)==4*m,'four full words')
        words=[main[j*m:(j+1)*m] for j in range(4)]
        require(order==4*m+(4 if kind=='h' else 0),'bordered dimension')
        if kind=='h':
            require([sum(map(sign,w)) for w in words]==[2,0,0,0],'bordered seed sums')
            for i in range(4): yield CORNER[i]+''.join(c*m for c in TOP[i])
        for g in range(4):
            for k in range(m):
                row=(TOP[g] if fault=='frames' else LEFT[g]) if kind=='h' else ''
                for j in range(4):
                    group,sgn,mode=GS[g][j]
                    indexes=[(t-k)%m if mode==0 else (m-1-t-k)%m if mode==1 else (k+t+(0 if fault=='offset' else 1))%m for t in range(m)]
                    block=''.join(words[group][a] for a in indexes)
                    row+=block if sgn==1 else block.translate(str.maketrans('+-','-+'))
                yield row
        return
    z,phases,m={'v':(20,6,57),'w':(12,4,119),'u':(28,32,11)}[kind]
    require(len(main)==4*phases*m and len(parts)==6 and order==z+len(main),'multisegment dimensions')
    words=[[main[(g*phases+l)*m:(g*phases+l+1)*m] for l in range(phases)] for g in range(4)]
    width=z+(32 if kind=='u' else 4*phases)
    require(len(parts[1])==z*width,'top seed membership')
    require(all(len(p)==phases*z for p in parts[2:]),'left seed membership')
    for i in range(z):
        top=parts[1][i*width:(i+1)*width]
        controls=top[z:]
        yield top[:z]+''.join(controls[2*(w//8)+(w%2) if kind=='u' else w]*m for w in range(4*phases))
    sigma=[0,2,1,3,5,4]
    for g in range(4):
        for actual_h in range(phases):
            h=(actual_h+1)%phases if fault=='phase' else actual_h
            for k in range(m):
                row=parts[2+g][h*z:(h+1)*z]
                for j in range(4):
                    group,sgn,trans=TBL[g][j]
                    for l in range(phases):
                        if kind=='v': s=3*((l//3+h//3)%2)+(l%3+(2 if j==g else 1)*h)%3
                        elif kind=='w': s=l^h
                        else: s=8*((l//8)^(h//8))+(l%8+(7 if j==g else 1)*h)%8
                        if trans and kind=='v': s=sigma[s]
                        if trans and kind=='u': s=8*(s//8)+(-s)%8
                        block=''.join(words[group][s][((m-1-(t-k if j==g else t+k) if fault=='reversal' else -(t-k if j==g else t+k)) if trans else (t-k if j==g else t+k))%m] for t in range(m))
                        row+=block if sgn==1 else block.translate(str.maketrans('+-','-+'))
                yield row

def full_period(record,kind):
    q,m={'v':(24,57),'w':(16,119),'u':(128,11)}.get(kind,(4,len(record['parts'][0])//4))
    words=[record['parts'][0][i*m:(i+1)*m] for i in range(q)]
    divisors=[d for d in range(1,m) if m%d==0]
    require(all(any(any(w[t]!=w[(t+d)%m] for t in range(m)) for w in words) for d in divisors),'full common rotation period')
    return {'word_length':m,'proper_divisors_rejected':divisors}

def compare(rows,target,n):
    require(len(rows)==len(target)==n,'complete source/map row membership')
    bits=parse_matrix(('\n'.join(rows)+'\n').encode(),n,'signs')
    target_bits=parse_matrix(('\n'.join(target)+'\n').encode(),n,'signs')
    anchor=sign(rows[0][0]);columns=[sign(c) for c in rows[0]]
    raw_difference=None;count=0
    for i,row in enumerate(rows):
        require(len(row)==n,'source row length')
        r=sign(row[0])*anchor
        for j,c in enumerate(row):
            if c!=target[i][j] and raw_difference is None: raw_difference=[i,j,sign(c),sign(target[i][j])]
            require(r*sign(c)*columns[j]==sign(target[i][j]),'predeclared dephasing map')
            count+=1
    require(count==n*n,'complete source-map cells')
    return bits,{'source_cells':count,'map_cells':count,'raw_identity':raw_difference is None,'first_raw_difference':raw_difference}

def negative(fn,name):
    try: fn()
    except (ValueError,IndexError): return name
    raise ValueError('Accepted bad control: '+name)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--external-root',type=Path,required=True)
    ap.add_argument('--certificate',type=Path,required=True)
    ap.add_argument('--verify',action='store_true')
    args=ap.parse_args();here=Path(__file__).resolve().parent;root=args.external_root.resolve()
    manifest=json.loads((here/'RELATION_INPUTS.json').read_text())
    data={}
    for entry in manifest['source_files']:
        p=(root/entry['file']).resolve();require(p.is_relative_to(root),'source containment')
        raw=p.read_bytes();require(len(raw)==entry['bytes'] and sha256(raw).hexdigest()==entry['sha256'],'pinned complete source input')
        data[entry['file']]=raw
    payload=heading(data['author_x.data']);source=inert_derivative(data['author_decoder_actual.html'])
    require((payload+'\n').encode()==data['author_payload.signs'] and source.encode()==data['decoded_author_program_source.txt'],'exact inert extraction relationship')
    rec=records(payload,source)
    m={r['order']:r for r in json.loads((here/'MATRIX_INPUTS.json').read_text())['matrices']}
    result=[];controls=[];fault_kinds=set()
    for index,n,kind in CASES:
        entry=m[n];raw=(root/entry['file']).read_bytes()
        require(sha256(raw).hexdigest()==entry['compressed_sha256'],'pinned mirror bytes')
        csv=gzip.decompress(raw);require(sha256(csv).hexdigest()==entry['raw_sha256'],'pinned mirror content')
        target=[''.join('+' if x==b'1' else '-' for x in line.split(b',')) for line in csv.rstrip(b'\n').split(b'\n')]
        parse_matrix(csv,n,'csv')
        period=full_period(rec[index],kind)
        if kind not in fault_kinds:
            fault_kinds.add(kind)
            for fault in (['offset'] if kind=='g' else ['frames'] if kind=='h' else ['phase','reversal']):
                controls.append(negative(lambda:compare(list(source_rows(rec[index],n,kind,fault)),target,n),kind+' '+fault+' source rule'))
        rows=list(source_rows(rec[index],n,kind));bits,relation=compare(rows,target,n)
        require(not relation['raw_identity'],'declared nonidentity')
        proof=gram(bits,n)
        # One final-cell fault and one orthogonality-preserving row permutation
        # attack different contracts. These are exercised on actual large objects.
        damaged=rows.copy();damaged[-1]=damaged[-1][:-1]+('+' if damaged[-1][-1]=='-' else '-')
        controls.append(negative(lambda:compare(damaged,target,n),str(n)+' final-cell map'))
        controls.append(negative(lambda:gram(bits[:-1]+[bits[-1]^1],n),str(n)+' final-cell Gram'))
        permuted=rows.copy();permuted[-1],permuted[-2]=permuted[-2],permuted[-1]
        controls.append(negative(lambda:compare(permuted,target,n),str(n)+' fixed-order map'))
        result.append({'index':index,'order':n,'kind':kind,'payload_interval':[rec[index]['start'],rec[index]['stop']],'candidate_sha256':sha256(('\n'.join(rows)+'\n').encode()).hexdigest(),**relation,**proof,**period})
    controls.extend([
        negative(lambda:records(payload[:-1],source),'missing payload'),
        negative(lambda:records(payload+'+',source),'extra payload'),
        negative(lambda:records('0'+payload[1:],source),'invalid payload'),
        negative(lambda:records(payload,source.replace('e=$(echo ','e=$(echo a',1)),'header membership'),
        negative(lambda:inert_derivative(data['author_decoder_actual.html'].replace(b'sh /tmp/r $*',b'false')),'changed wrapper')])
    require([r['order'] for r in result]==[x[1] for x in CASES] and len(result)==10,'exact ten-member relation batch')
    report={'status':'PASS_EXACT_SOURCE_RELATIONS','objects':result,'objects_checked':10,'source_records_consumed':12,'payload_symbols_consumed':23828,'source_and_map_cells':sum(r['source_cells'] for r in result),'row_pairs_checked':sum(r['unordered_pairs_checked'] for r in result),'negative_controls':controls,'negative_controls_detected':len(controls),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'The specified scalar mathematical translations and pinned data only; no source-runtime execution, author authentication, priority or universal theorem.'}
    if args.verify: require(json.loads(args.certificate.read_text())==report,'complete serialized relation certificate')
    else:
        with args.certificate.open('x') as f: json.dump(report,f,indent=2);f.write('\n')
    print(json.dumps({k:report[k] for k in ['status','objects_checked','source_and_map_cells','row_pairs_checked','negative_controls_detected']}))

if __name__=='__main__': main()
