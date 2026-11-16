"""Read-only, standard-library, exact review of the C197 release data.

Fresh source-exposed implementation. No Lean code or original OPF checker is
imported. See REFERENCES.md for provenance and limits. Python >= 3.10.
"""
from pathlib import Path
from itertools import combinations, permutations
from fractions import Fraction
from hashlib import sha256
from copy import deepcopy
import argparse
import json
import sys

PAIRS = tuple(combinations(range(6), 2))
PAIR_INDEX = {e: i for i, e in enumerate(PAIRS)}
TYPES = tuple((v,) for v in range(6)) + PAIRS
PERM_MAPS = tuple(tuple(PAIR_INDEX[tuple(sorted((p[a], p[b])))]
                        for a, b in PAIRS) for p in permutations(range(6)))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def object_pairs(pairs):
    out = {}
    for key, value in pairs:
        require(key not in out, 'duplicate JSON key')
        out[key] = value
    return out


def load(path):
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=object_pairs)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':')).encode()


def strict_ints(values):
    return all(type(value) is int for value in values)


def graph(mask):
    require(type(mask) is int and 0 <= mask < 32768, '15-bit graph mask')
    edges = frozenset(e for i, e in enumerate(PAIRS) if mask & (1 << i))
    degrees = [sum(v in e for e in edges) for v in range(6)]
    triples = tuple(t for t in combinations(range(6), 3)
                    if not any(e in edges for e in combinations(t, 2)))
    allowed = [j for j, t in enumerate(TYPES)
               if all(set(t).intersection(q) for q in triples)]
    capacities = [2 if len(t) == 2 and t in edges else 3 for t in TYPES]
    return edges, degrees, triples, allowed, capacities


def record(mask):
    _, degree, _, allowed, capacity = graph(mask)
    vertices = []
    for v in range(6):
        outside = [j for j in allowed if v not in TYPES[j]]
        caps = [capacity[j] for j in outside]
        total = sum(caps)
        vertices.append({'vertex': v, 'induced_degree': degree[v],
                         'crossdegree_upper': 6-degree[v],
                         'outside_allowed_type_indices': outside,
                         'capacities': caps, 'capacity_sum': total,
                         'upper_plus_capacity': 6-degree[v]+total,
                         'margin': total-degree[v]-4})
    negative = [v['vertex'] for v in vertices if v['margin'] < 0]
    return {'representative': mask, 'vertices': vertices,
            'negative_vertices': negative,
            'classification': ('EXCLUDED_BY_THIS_INEQUALITY' if negative else
                               'NOT_ADMITTED_NOT_FEASIBILITY')}


def expected_system(mask):
    edges, degree, _, allowed, caps = graph(mask)
    forbidden = [j for j in range(21) if j not in allowed]
    eq = [('total', [1]*21, 10)]
    eq += [(f'zero:{j}', [int(i == j) for i in range(21)], 0)
           for j in forbidden]
    iq = []
    for sign, kind, bound in [(-1, 'lower', 5), (1, 'upper', 6)]:
        iq += [(f'{kind}:{v}', [sign*int(v in t) for t in TYPES],
                sign*(bound-degree[v])) for v in range(6)]
    iq += [(f'cap:{j}', [int(i == j) for i in range(21)], caps[j])
           for j in range(21)]
    iq += [(f'avoid:{a}:{b}', [int(a not in t and b not in t) for t in TYPES], 4)
           for a, b in PAIRS if (a, b) not in edges]
    matrix = [row+[0]*len(iq) for _, row, _ in eq]
    matrix += [row+[int(i == j) for j in range(len(iq))]
               for i, (_, row, _) in enumerate(iq)]
    return matrix, [rhs for _, _, rhs in eq+iq], [n for n, _, _ in eq+iq], len(eq), iq


def cone(matrix, rhs, weights):
    require(matrix and matrix[0] and len(matrix) == len(rhs) == len(weights),
            'cone dimensions')
    require(all(len(row) == len(matrix[0]) for row in matrix), 'ragged matrix')
    require(strict_ints(rhs) and strict_ints(weights) and
            all(strict_ints(row) for row in matrix), 'exact integer input')
    columns = [sum((Fraction(y)*row[j] for row, y in zip(matrix, weights)),
                   Fraction(0)) for j in range(len(matrix[0]))]
    value = sum((Fraction(y)*b for y, b in zip(weights, rhs)), Fraction(0))
    norm = sum(abs(y) for y in weights)
    require(min(columns) >= 0 and value < 0 and norm > 0, 'strict cone contradiction')
    return {'rows': len(matrix), 'columns': len(matrix[0]),
            'rhs': str(value), 'multiplier_l1': norm,
            'residual_bound': str(-value/norm),
            'nonzero_columns': [j for j, value in enumerate(columns) if value]}


def certificate(model, cert):
    r = cert['representative']
    require(type(r) is int and r == 685 and cert['vertex'] == 5, 'literal witness')
    require(cert['model_sha256'] == sha256(canonical(model)).hexdigest(), 'model hash')
    matrix, rhs, labels, n_eq, iq = expected_system(r)
    require(model['matrix'] == matrix and model['rhs'] == rhs and
            model['row_labels'] == labels, 'independently reconstructed system')
    require(model['types'] == [list(t) for t in TYPES] and
            model['variable_domain'] == 'NONNEGATIVE_REAL', 'type/domain convention')
    full = cone(matrix, rhs, cert['row_weights'])
    drops = [n_eq+i for i, (name, _, _) in enumerate(iq) if name.startswith('lower:')]
    cols = [21+i for i, (name, _, _) in enumerate(iq) if name.startswith('lower:')]
    require(all(cert['row_weights'][i] == 0 for i in drops), 'lower-bound dependence')
    stripped = cone([[v for j, v in enumerate(row) if j not in cols]
                     for i, row in enumerate(matrix) if i not in drops],
                    [v for i, v in enumerate(rhs) if i not in drops],
                    [v for i, v in enumerate(cert['row_weights']) if i not in drops])
    require(full['rhs'] == '-2' and full['multiplier_l1'] == 17 and
            full['residual_bound'] == '2/17', 'certificate margin')
    return {'full': full, 'without_lower_degree_rows': stripped}


def orbit(mask):
    positions = [j for j in range(15) if mask & (1 << j)]
    return sorted({sum(1 << mapping[j] for j in positions) for mapping in PERM_MAPS})


def audit(batch, representatives):
    require(len(representatives) == len(set(representatives)) == 50 and
            strict_ints(representatives), '50 distinct representatives')
    require(batch['complete'] is True and batch['vertex_decisions'] == 300 and
            batch['input_representatives'] == representatives, 'complete audit header')
    expected = [record(r) for r in representatives]
    require(canonical(batch['records']) == canonical(expected), 'all 300 records')
    return [r['representative'] for r in expected if r['negative_vertices']]


def census(source):
    require(source['n'] == 6 and source['edge_order'] == 'LEX_UNORDERED_PAIRS' and
            source['predicate'] == 'NO_K4_AND_NO_I4', 'census convention')
    quartet_masks = [sum(1 << PAIR_INDEX[e] for e in combinations(q, 2))
                     for q in combinations(range(6), 4)]
    expected = {r for r in range(32768)
                if all((r & q) not in (0, q) for q in quartet_masks)}
    seen = set()
    reps = []
    for item in source['classes']:
        r, members = item['representative'], item['members']
        require(strict_ints(members) and members == orbit(r) and
                r == min(members) and not seen.intersection(members),
                'complete disjoint canonical orbit')
        require(item['stabilizer'] == 720//len(members), 'stabilizer')
        seen.update(members)
        reps.append(r)
    require(len(reps) == len(set(reps)) == 84 and expected == seen,
            'complete 32768-mask census membership')
    require(source['admissible_masks'] == sorted(expected), 'explicit admissible mask membership')
    return {'mask_domain': 32768, 'admissible_masks': len(expected), 'orbits': len(reps),
            'permutations_per_orbit': 720, 'all_members_recomputed': True}


def verify(data):
    prior, batch = data['prior_residual'], data['audit']
    source, residual, result = data['source_orbits'], data['residual'], data['result']
    positive = audit(batch, prior['remaining_representatives'])
    require(positive == [685], 'exact positive class membership')
    require(prior['remaining_labeled_graphs'] == 15232, 'prior count')
    by_rep = {e['representative']: e['members'] for e in source['classes']}
    require(sum(len(by_rep[r]) for r in prior['remaining_representatives']) == 15232,
            'prior weighted membership')
    cert = certificate(data['model'], data['certificate'])
    removed = orbit(685)
    require(len(removed) == 360 and removed == by_rep[685], '685 orbit')
    remain = [r for r in prior['remaining_representatives'] if r not in positive]
    require(residual['excluded_representatives'] == positive and
            residual['excluded_labeled_members'] == removed and
            residual['remaining_representatives'] == remain and
            residual['remaining_labeled_graphs'] == sum(len(by_rep[r]) for r in remain)
            == 14872 and len(remain) == 49, 'exact residual partition')
    require(result['positive_classes'] == positive and result['negative_classes'] == remain and
            result['excluded_labeled'] == 360 and result['remaining_classes'] == 49 and
            result['remaining_labeled'] == 14872 and result['vertex_decisions'] == 300,
            'saved summary')
    require(residual['global_target_decision'] == result['global_target_decision'] ==
            'NOT_TESTED', 'unsupported global promotion')
    return {'verdict': 'PASS_AT_CLAIM_CEILING', 'certificate': cert,
            'classes': 50, 'vertex_decisions': 300, 'excluded_classes': positive,
            'excluded_labeled': len(removed), 'remaining_classes': len(remain),
            'remaining_labeled': 14872, 'census': census(source),
            'formal_verification': 'NOT_TESTED', 'external_expert_review': 'NOT_TESTED'}


def controls(data):
    rejected = []
    def reject(name, call):
        try:
            call()
        except (ValueError, KeyError, TypeError, IndexError):
            rejected.append(name)
            return
        raise ValueError('accepted invalid control: '+name)
    for name, edit in [
            ('missing_class', lambda d: d['audit']['records'].pop()),
            ('duplicate_class', lambda d: d['audit']['records'].__setitem__(1, d['audit']['records'][0])),
            ('missing_vertex', lambda d: d['audit']['records'][0]['vertices'].pop()),
            ('duplicate_vertex', lambda d: d['audit']['records'][0]['vertices'].__setitem__(1, d['audit']['records'][0]['vertices'][0])),
            ('wrong_capacity_sum', lambda d: d['audit']['records'][0]['vertices'][5].__setitem__('capacity_sum', 3)),
            ('wrong_population', lambda d: d['model']['rhs'].__setitem__(0, 9)),
            ('negative_certificate', lambda d: d['certificate'].__setitem__('row_weights', [-y for y in d['certificate']['row_weights']])),
            ('short_certificate', lambda d: d['certificate']['row_weights'].pop()),
            ('missing_orbit', lambda d: d['residual']['excluded_labeled_members'].pop()),
            ('duplicate_orbit', lambda d: d['residual']['excluded_labeled_members'].__setitem__(1, d['residual']['excluded_labeled_members'][0])),
            ('global_promotion', lambda d: d['result'].__setitem__('global_target_decision', 'PROVED')),
            ('missing_source_mask', lambda d: d['source_orbits']['admissible_masks'].pop()),
            ('duplicate_source_mask', lambda d: d['source_orbits']['admissible_masks'].__setitem__(1, d['source_orbits']['admissible_masks'][0]))]:
        mutated = deepcopy(data)
        edit(mutated)
        reject(name, lambda: verify(mutated))
    reject('feasible_false_cone', lambda: cone([[-1]], [-2], [1]))
    reject('zero_cone_margin', lambda: cone([[0]], [0], [1]))
    reject('float_matrix', lambda: cone([[1.0]], [-1], [1]))
    reject('boolean_weight', lambda: cone([[1]], [-1], [True]))
    require(min(v['margin'] for v in record(655)['vertices']) == 0 and
            not record(655)['negative_vertices'], 'strict zero-margin boundary')
    return {'selected_invalid_controls': len(rejected), 'rejected': rejected,
            'zero_margin_655_not_excluded': True,
            'limit': 'Selected cases, not exhaustive software verification.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, default=Path(__file__).resolve().parent/'data')
    args = parser.parse_args()
    data = {n: load(args.data/(n+'.json')) for n in
            ['prior_residual', 'audit', 'model', 'certificate', 'source_orbits', 'residual', 'result']}
    result = verify(data)
    result['controls'] = controls(data)
    result['python'] = sys.version.split()[0]
    result['optimization'] = sys.flags.optimize
    result['independence'] = 'Fresh code; same actor, exposed original conclusions and inputs; nonblind.'
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
