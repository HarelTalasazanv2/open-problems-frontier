"""Exact C166 CSV/canonical relationship; raw third-party CSV supplied externally."""
from pathlib import Path
from hashlib import sha256
import argparse,json
from matrix_check import gram,parse as sign_parse,require

def parse_csv(raw,n):
    require(type(n) is int and n>0,'positive integral order')
    lines=raw.splitlines();require(len(lines)==n,'complete CSV rows')
    output=[]
    for line in lines:
        parts=[x.strip() for x in line.split(b',')]
        require(len(parts)==n and all(x in {b'1',b'+1',b'-1'} for x in parts),'CSV grammar and columns')
        output.append(b''.join(b'-' if x==b'-1' else b'+' for x in parts))
    return b'\n'.join(output)+b'\n'

def rejected(fn,name):
    try:fn()
    except ValueError:return name
    raise ValueError('Accepted faulty CSV control: '+name)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--external-root',type=Path,required=True);p.add_argument('--certificate',type=Path,required=True);p.add_argument('--verify',action='store_true');args=p.parse_args()
    raw=(args.external_root/'H668.csv').read_bytes()
    require(len(raw)==1115894 and sha256(raw).hexdigest()=='5eaef5f4c814469a1f0815756876b83e8c4944ff7ccf4f023ee479de5e8f9a8b','pinned complete source CSV')
    signs=parse_csv(raw,668)
    require(len(signs)==446892 and sha256(signs).hexdigest()=='bdeb5059d77e2703211082627b60441b8c888c928a55cc6f295e011941a387b0','pinned canonical relationship')
    rows=sign_parse(signs,668,'signs');row_result=gram(rows,668)
    lines=signs.splitlines();columns=b'\n'.join(bytes(row[j] for row in lines) for j in range(668))+b'\n'
    column_result=gram(sign_parse(columns,668,'signs'),668)
    require(parse_csv(b' 1,+1\r\n1, -1\r\n',2)==b'++\n+-\n','compatible whitespace/CRLF positive control')
    controls=[rejected(lambda:parse_csv(b'1,0\n1,-1\n',2),'invalid zero'),rejected(lambda:parse_csv(b'1,1,1\n1,-1\n',2),'extra column'),rejected(lambda:parse_csv(b'1,1\n',2),'missing row'),rejected(lambda:parse_csv(b'1,x\n1,-1\n',2),'invalid symbol'),rejected(lambda:parse_csv(b'1,1\n1,-1\n1,1\n',2),'extra row'),rejected(lambda:gram(rows[:-1]+[rows[-1]^1],668),'actual final-cell damage'),rejected(lambda:gram([rows[0],rows[0]]+rows[2:],668),'actual duplicate row')]
    out={'status':'PASS_CSV668_CANONICAL_RELATION','order':668,'source_bytes':len(raw),'source_sha256':sha256(raw).hexdigest(),'canonical_bytes':len(signs),'canonical_sha256':sha256(signs).hexdigest(),'row_pairs_checked':row_result['unordered_pairs_checked'],'column_pairs_checked':column_result['unordered_pairs_checked'],'negative_controls':controls,'negative_controls_detected':len(controls),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact pinned CSV/canonical bytes and finite Hadamard identity; no author authentication, priority, complete release membership or redistribution license inferred.'}
    if args.verify:require(json.loads(args.certificate.read_text())==out,'complete serialized CSV certificate')
    else:
        with args.certificate.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({k:out[k] for k in ['status','order','row_pairs_checked','column_pairs_checked','negative_controls_detected']}))

if __name__=='__main__':main()
