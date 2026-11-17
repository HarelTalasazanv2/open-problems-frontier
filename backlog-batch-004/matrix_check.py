"""Exact finite Hadamard verification; upstream inputs stay external.

Authors and original construction credit are identified in REFERENCES.md.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import argparse
import copy
import gzip
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def parse(raw, order, format):
    require(type(order) is int and order > 0, "positive integral order")
    require(raw.endswith(b'\n'), "terminal newline")
    lines = raw[:-1].split(b'\n')
    require(len(lines) == order, "complete row membership")
    rows = []
    for line in lines:
        if format == 'signs':
            require(len(line) == order and set(line) <= {43, 45}, "sign-row grammar")
            digits = line.translate(bytes.maketrans(b'+-', b'10'))
        elif format == 'csv':
            tokens = line.split(b',')
            require(len(tokens) == order and all(t in {b'1', b'-1'} for t in tokens),
                    "CSV token grammar")
            digits = b''.join(b'1' if t == b'1' else b'0' for t in tokens)
        else:
            raise ValueError('Unknown format')
        rows.append(int(digits, 2))
    return rows


def gram(rows, n):
    require(len(rows) == n and all(type(x) is int and 0 <= x < 1 << n for x in rows),
            "row bit width")
    seen = 0
    for i, x in enumerate(rows):
        for y in rows[i+1:]:
            require(n - 2 * (x ^ y).bit_count() == 0, "nonorthogonal distinct rows")
            seen += 1
    require(seen == n * (n - 1) // 2, "complete pair membership")
    pairs = sorted({(0, 1), (0, n-1), (n//2-1, n//2), (n-2, n-1)}) if n > 1 else []
    for a, b in pairs:
        dot = sum((1 if rows[a] & (1 << k) else -1) *
                  (1 if rows[b] & (1 << k) else -1) for k in range(n))
        require(dot == 0, "direct signed-product cross-check")
    return {'order': n, 'unordered_pairs_checked': seen, 'row_norm_squared': n,
            'direct_signed_pairs': [list(p) for p in pairs], 'HHt_equals_nI': True,
            'HtH_equals_nI_by_square_invertibility': True}


def controls():
    good = b'++++\n+-+-\n++--\n+--+\n'
    rows = parse(good, 4, 'signs')
    gram(rows, 4)
    require(parse(b'1,1\n1,-1\n', 2, 'csv') == [3, 2], 'independent CSV canary')
    gram(parse(b'+\n', 1, 'signs'), 1)
    bad = []
    cases = [
        ('missing row', lambda: parse(good[:-5], 4, 'signs')),
        ('duplicate row', lambda: gram([rows[0], rows[0]] + rows[2:], 4)),
        ('missing final newline', lambda: parse(good[:-1], 4, 'signs')),
        ('invalid sign', lambda: parse(good.replace(b'+', b'0', 1), 4, 'signs')),
        ('wide row', lambda: parse(b'+' + good, 4, 'signs')),
        ('CSV zero', lambda: parse(b'1,0\n1,-1\n', 2, 'csv')),
        ('CSV missing column', lambda: parse(b'1\n1,-1\n', 2, 'csv')),
        ('one sign flipped', lambda: gram([rows[0] ^ 1] + rows[1:], 4)),
        ('odd order half-floor shortcut', lambda: gram([0, 1, 2], 3)),
        ('boolean order', lambda: parse(b'+\n', True, 'signs')),
    ]
    for name, fn in cases:
        try:
            fn()
        except ValueError:
            bad.append(name)
        else:
            raise ValueError('Accepted invalid control: ' + name)
    return bad


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs', type=Path, required=True)
    p.add_argument('--external-root', type=Path, required=True)
    p.add_argument('--certificate', type=Path, required=True)
    p.add_argument('--verify', action='store_true')
    args = p.parse_args()
    inputs = json.loads(args.inputs.read_text())
    expected = [2092, 2292, 716, 892, 1132, 1244, 1388, 1436, 1676, 1772, 1916, 1948, 1964, 1212, 1940]
    require([r['order'] for r in inputs['matrices']] == expected, 'exact fifteen-witness membership')
    result = []
    for entry in inputs['matrices']:
        relative = Path(entry['file'])
        require(not relative.is_absolute() and '..' not in relative.parts, 'relative input path')
        path = (args.external_root / relative).resolve()
        require(path.is_relative_to(args.external_root.resolve()), 'input containment')
        data = path.read_bytes()
        require(sha256(data).hexdigest() == entry['compressed_sha256'], 'pinned compressed input')
        raw = gzip.decompress(data)
        require(sha256(raw).hexdigest() == entry['raw_sha256'], 'pinned raw input')
        rows = parse(raw, entry['order'], entry['format'])
        result.append({**gram(rows, entry['order']),
                       'compressed_sha256': entry['compressed_sha256'],
                       'raw_sha256': entry['raw_sha256']})
    detected = controls()
    report = {'status': 'PASS_FINITE_MATRICES', 'matrices': result,
              'negative_controls': detected, 'negative_controls_detected': len(detected),
              'all_fifteen_witnesses': True,
              'unordered_pairs_checked': sum(x['unordered_pairs_checked'] for x in result),
              'code_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'claim_ceiling': 'These fifteen final matrices only. No seed-builder relationship, current least gap, novelty, priority or universal Hadamard theorem.',
              'independence': 'Fresh code; same actor/model, exposed expected inputs and Hamming-distance model, shared Python integer backend. Not a blind or external review.'}
    if args.verify:
        require(json.loads(args.certificate.read_text()) == report, 'complete saved certificate')
    else:
        with args.certificate.open('x') as output:
            json.dump(report, output, indent=2)
            output.write('\n')
    print(json.dumps({'status': report['status'], 'matrices': len(result),
                      'unordered_pairs_checked': report['unordered_pairs_checked'],
                      'negative_controls_detected': len(detected)}))


if __name__ == '__main__':
    main()
