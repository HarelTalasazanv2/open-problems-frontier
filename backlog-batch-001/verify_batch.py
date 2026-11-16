"""Exact, read-only review of eight M12 backlog records. See REFERENCES.md.

Reuses the reviewed C197 fresh arithmetic/orbit engine as basis.py; the new
model reconstruction, finite selectors and controls are source-exposed and
nonblind. No original OPF producer/checker or external Lean code is executed.
"""
from pathlib import Path
from itertools import combinations, permutations
from collections import Counter
from copy import deepcopy
from hashlib import sha256
import json
import sys
import basis as B

D = Path(__file__).resolve().parent/'data'
P = B.PAIRS
T = B.TYPES
PERMS = tuple(permutations(range(6)))


def read(name):
    return B.load(D/(name+'.json'))


def equal(a, b, message):
    B.require(B.canonical(a) == B.canonical(b), message)


def reconstruct(m, mask, lower, common):
    edges, degree, triples, allowed, caps = B.graph(mask)
    forbidden = [i for i in range(21) if i not in allowed]
    nonedges = [e for e in P if e not in edges]
    cuts = [[a, b, z] for a, b in nonedges for z in range(6)
            if z not in (a, b)] if common else []
    eq = [('total', [1]*21, 10)]
    eq += [(f'zero:{i}', [int(j == i) for j in range(21)], 0) for i in forbidden]
    iq = [(f'lower:{v}', [-int(v in t) for t in T], degree[v]-5) for v in lower]
    iq += [(f'upper:{v}', [int(v in t) for t in T], 6-degree[v]) for v in range(6)]
    iq += [(f'cap:{i}', [int(j == i) for j in range(21)], caps[i]) for i in range(21)]
    iq += [(f'avoid:{a}:{b}', [int(a not in t and b not in t) for t in T], 4)
           for a, b in nonedges]
    iq += [(f'common:{a}:{b}:{z}',
            [int(a not in t and b not in t and z in t) for t in T], 3)
           for a, b, z in cuts]
    matrix = [row+[0]*len(iq) for _, row, _ in eq]
    matrix += [row+[int(i == j) for j in range(len(iq))]
               for i, (_, row, _) in enumerate(iq)]
    expected = {'types': [list(t) for t in T], 'edges': [list(e) for e in P if e in edges],
                'degrees': degree, 'independent_triples': [list(q) for q in triples],
                'allowed_type_indices': allowed, 'forbidden_type_indices': forbidden,
                'nonedges': [list(e) for e in nonedges], 'common_cuts': cuts,
                'equalities': [row for _, row, _ in eq], 'equality_rhs': [b for _, _, b in eq],
                'equality_labels': [s for s, _, _ in eq],
                'inequalities': [row for _, row, _ in iq], 'inequality_rhs': [b for _, _, b in iq],
                'inequality_labels': [s for s, _, _ in iq],
                'matrix': matrix, 'rhs': [b for _, _, b in eq+iq],
                'row_labels': [s for s, _, _ in eq+iq]}
    for key, value in expected.items():
        equal(m[key], value, 'model field mismatch: '+key)
    B.require(m.get('mask', m.get('relabeled_mask')) == mask and
              m['variable_domain'] == 'NONNEGATIVE_REAL' and
              m['edge_order'] == 'LEX_UNORDERED_PAIRS', 'coordinates/domain')
    B.require(m['global_target_decision'] == 'NOT_TESTED', 'global promotion')
    return expected


def certcheck(m, c, mask, lower, common):
    reconstruct(m, mask, lower, common)
    B.require(c['model_sha256'] == sha256(B.canonical(m)).hexdigest(), 'model/cert binding')
    return B.cone(m['matrix'], m['rhs'], c['row_weights'])


def point(m, witness, mask, lower, common):
    reconstruct(m, mask, lower, common)
    B.require(witness['model_sha256'] == sha256(B.canonical(m)).hexdigest(), 'point binding')
    x = witness['lifted']
    B.require(len(x) == len(m['matrix'][0]) and B.strict_ints(x) and min(x) >= 0,
              'point dimension/nonnegativity')
    equal(x, witness['counts']+witness['slacks'], 'point decomposition')
    B.require(len(witness['counts']) == 21, 'complete type point')
    equal([sum(a*b for a, b in zip(row, x)) for row in m['matrix']], m['rhs'],
          'point equations')
    return {'rows': len(m['matrix']), 'columns': len(x), 'exact_nonnegative_integer_point': True,
            'graph_realization': 'NOT_TESTED'}


def five_vertex_lemma():
    pairs = tuple(combinations(range(5), 2))
    qualifying = []
    for mask in range(1024):
        edges = [e for j, e in enumerate(pairs) if mask & (1 << j)]
        intersecting = all(set(a).intersection(b) for a, b in combinations(edges, 2))
        no_i4 = all(any(e in edges for e in combinations(q, 2))
                    for q in combinations(range(5), 4))
        if intersecting and no_i4:
            degree = sorted(sum(v in e for e in edges) for v in range(5))
            B.require(len(edges) == 3 and degree == [0, 0, 2, 2, 2], 'five-vertex lemma')
            qualifying.append(mask)
    B.require(len(qualifying) == 10, 'all ten choices of triangle')
    star = [(0, v) for v in range(1, 5)]
    cycle = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]
    B.require(all(set(a).intersection(b) for a, b in combinations(star, 2)) and
              not any(e in star for e in combinations(range(1, 5), 2)), 'star boundary')
    B.require(any(not set(a).intersection(b) for a, b in combinations(cycle, 2)),
              'cycle boundary')
    return {'five_vertex_masks': 1024, 'qualifying_masks': qualifying,
            'triangle_plus_two_isolates_only': True,
            'degree_floor_proof': 'ANALYTIC_REDERIVATION; finite lemma check supplements it'}


PRISM_EDGES = {(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5), (0, 3), (1, 4), (2, 5)}
PRISM_MASK = sum(1 << j for j, e in enumerate(P) if e in PRISM_EDGES)
PRISM_ORBIT = set(B.orbit(PRISM_MASK))


def prism_exceptions():
    triangles = [set(q) for q in combinations(range(6), 3)
                 if all(e in PRISM_EDGES for e in combinations(q, 2))]
    B.require(len(triangles) == 2 and len(PRISM_ORBIT) == 60, 'prism identity')
    result = {}
    for x in range(6):
        exceptional = []
        for t in T:
            remaining = set(range(6)) - {x} - set(t)
            if all(tuple(sorted(e)) in PRISM_EDGES for e in combinations(remaining, 2)):
                exceptional.append(t)
        target = tuple(sorted(next(q for q in triangles if x in q)-{x}))
        B.require(exceptional == [target], 'only opposite triangle exception')
        result[str(x)] = list(target)
    return {'singleton_choices': 6, 'types_per_choice': 21, 'exceptions': result,
            'analytic_contradiction': 'two singleton vertices required; each has full degree at least8>7'}


def rules(mask):
    edges, degree, triples, _, _ = B.graph(mask)
    return {'edge_budget': not (5 <= len(edges) <= 13),
            'nonedge_degree_witnesses': [[a, b, degree[a]+degree[b]] for a, b in P
                                        if (a, b) not in edges and degree[a]+degree[b] > 6],
            'independent_triple_witnesses': [list(q)+[sum(degree[a] for a in q)] for q in triples
                                            if sum(degree[a] for a in q) > 8],
            'prism_excluded': mask in PRISM_ORBIT}


def excluded(reason):
    return bool(reason['edge_budget'] or reason['nonedge_degree_witnesses'] or
                reason['independent_triple_witnesses'] or reason['prism_excluded'])


def images_new_to_old(mask):
    edges = B.graph(mask)[0]
    return [sum(1 << j for j, (a, b) in enumerate(P)
                if tuple(sorted((p[a], p[b]))) in edges) for p in PERMS]


def c188(source):
    summary = B.census(source)
    survivors = []
    member_checks = 0
    for entry in source['classes']:
        r = entry['representative']
        equal(entry['permutation_images'], images_new_to_old(r), 'oriented permutation images')
        fibers = Counter(entry['permutation_images'])
        B.require(set(fibers.values()) == {entry['stabilizer']}, 'every image fiber')
        expected = rules(r)
        equal(entry['rules'], expected, 'complete strict filter reasons')
        signature = (expected['edge_budget'], len(expected['nonedge_degree_witnesses']),
                     len(expected['independent_triple_witnesses']), expected['prism_excluded'])
        for member in entry['members']:
            rule = rules(member)
            B.require(signature == (rule['edge_budget'], len(rule['nonedge_degree_witnesses']),
                                      len(rule['independent_triple_witnesses']), rule['prism_excluded']),
                      'member-level invariant rule membership')
            member_checks += 1
        if not excluded(expected):
            survivors.append(r)
    equal(survivors, source['remaining_representatives'], 'C188 exact residual')
    summary.update({'oriented_images_checked': 84*720, 'member_rules_checked': member_checks,
                    'surviving_classes': len(survivors), 'excluded_classes': 84-len(survivors)})
    return summary


def c196_expected(representatives):
    B.require(len(representatives) == len(set(representatives)) == 51, 'C196 domain')
    mandatory = {(0, 5), (1, 4), (2, 3)}
    optional = [(0, j) for j in range(1, 5)]
    templates = {sum(1 << j for j, e in enumerate(P)
                     if e in mandatory or any(e == optional[k] and (s & (1 << k))
                                              for k in range(4))) for s in range(16)}
    triples = [(1, 2, 5), (1, 3, 5), (2, 4, 5), (3, 4, 5)]
    expected = []
    for r in representatives:
        edges, degree, _, _, _ = B.graph(r)
        witnesses = []
        for p, image in zip(PERMS, images_new_to_old(r)):
            predicate = (all(tuple(sorted((p[a], p[b]))) not in edges
                             for q in triples for a, b in combinations(q, 2)) and
                         all(tuple(sorted((p[a], p[b]))) in edges for a, b in [(1, 4), (2, 3)])
                         and degree[p[5]] > 0)
            B.require(predicate == (image in templates), 'predicate/template equivalence')
            if predicate:
                witnesses.append(list(p))
        expected.append({'representative': r, 'permutations_checked': 720,
                         'classification': 'MATCH' if witnesses else 'NO_MATCH',
                         'witnesses': witnesses,
                         'nonmatch_meaning': 'THIS_CRITERION_ONLY_NOT_FEASIBILITY'})
    return expected


def membership(batch, reps, expected):
    B.require(batch['complete'] is True and batch['input_representatives'] == reps and
              batch['permutations_per_class'] == 720 and batch['total_permutations'] == 36720,
              'C196 completeness header')
    equal(batch['records'], expected, 'C196 all decisions and witness permutations')


def set_update(prior, current, representative, source):
    pool = {e['representative']: e['members'] for e in source['classes']}
    equal(current['excluded_representatives'], [representative], 'excluded representative')
    equal(current['excluded_labeled_members'], B.orbit(representative), 'complete removed orbit')
    equal(current['remaining_representatives'],
          [r for r in prior['remaining_representatives'] if r != representative], 'residual set')
    B.require(sum(len(pool[r]) for r in prior['remaining_representatives']) ==
              prior['remaining_labeled_graphs'] and
              sum(len(pool[r]) for r in current['remaining_representatives']) ==
              current['remaining_labeled_graphs'], 'weighted residual membership')
    return {'representative': representative, 'removed': len(pool[representative]),
            'remaining_classes': len(current['remaining_representatives']),
            'remaining_labeled': current['remaining_labeled_graphs']}


def main():
    source = read('source_orbits')
    records = []
    all_lower = list(range(6))
    specs = [('c195_base_model', 663, all_lower, False, 'c195_base_certificate'),
             ('c196_model_671', 671, all_lower, False, 'c196_certificate_671'),
             ('c633_base_model', 633, all_lower, False, 'c633_base_certificate'),
             ('c633_full_model', 633, all_lower, True, 'c633_full_certificate'),
             ('c633_upper_only_model', 633, [], True, 'c633_upper_only_certificate'),
             ('c635_full_model', 635, all_lower, True, 'c635_full_certificate'),
             ('c635_upper_only_model', 635, [], True, 'c635_upper_only_certificate'),
             ('c655_full_model', 655, all_lower, True, 'c655_full_certificate')]
    for name, r, lower, common, c in specs:
        records.append({'model': name, 'representative': r,
                        **certcheck(read(name), read(c), r, lower, common)})
    points = []
    for name, witness, r, lower in [('c635_base_model', 'c635_base_witness', 635, all_lower),
                                   ('c655_base_model', 'c655_base_witness', 655, all_lower),
                                   ('c655_without_lower0_model', 'c655_without_lower0_witness', 655, [1,2,3,4,5])]:
        points.append({'model': name, **point(read(name), read(witness), r, lower, r == 655 and lower != all_lower)})
    reps = read('c195_residual')['remaining_representatives']
    expected = c196_expected(reps)
    membership(read('c196_membership'), reps, expected)
    B.require([(e['representative'], len(e['witnesses'])) for e in expected if e['witnesses']] ==
              [(671, 8)], 'C196 exact positive and witness membership')
    updates = []
    prior = read('c633_prior')
    for prefix, r in [('c633', 633), ('c635', 635), ('c655', 655), ('c195', 663), ('c196', 671)]:
        current = read(prefix+'_residual')
        updates.append(set_update(prior, current, r, source))
        prior = current
    bad = []
    def reject(name, call):
        try:
            call()
        except (ValueError, TypeError, KeyError, IndexError):
            bad.append(name)
            return
        raise ValueError('invalid control accepted: '+name)
    m = read('c635_full_model')
    for name, edit in [('wrong_degree', lambda q: q['degrees'].__setitem__(0, 3)),
                       ('missing_common_cut', lambda q: q['common_cuts'].pop()),
                       ('wrong_population', lambda q: q['rhs'].__setitem__(0, 9)),
                       ('wrong_slack', lambda q: q['matrix'][-1].__setitem__(-1, 0)),
                       ('signed_domain', lambda q: q.__setitem__('variable_domain', 'SIGNED_REAL'))]:
        q = deepcopy(m); edit(q)
        reject(name, lambda q=q: reconstruct(q, 635, all_lower, True))
    c = read('c635_full_certificate'); c['row_weights'] = [-y for y in c['row_weights']]
    reject('negated_certificate', lambda: certcheck(m, c, 635, all_lower, True))
    w = read('c635_base_witness'); w['lifted'][0] += 1
    reject('false_point', lambda: point(read('c635_base_model'), w, 635, all_lower, False))
    reject('feasible_false_cone', lambda: B.cone([[-1]], [-2], [1]))
    reject('zero_cone_margin', lambda: B.cone([[0]], [0], [1]))
    for name, edit in [('missing_class', lambda q: q['records'].pop()),
                       ('duplicate_permutation', lambda q: q['records'][0]['witnesses'].__setitem__(1, q['records'][0]['witnesses'][0])),
                       ('partial_header', lambda q: q.__setitem__('complete', False))]:
        q = read('c196_membership'); edit(q)
        reject(name, lambda q=q: membership(q, reps, expected))
    m = read('c655_full_model'); c = read('c655_full_certificate'); j = m['row_labels'].index('lower:0')
    B.require(c['row_weights'][j] == 2, 'essential lower0 multiplier')
    c['row_weights'][j] = 0
    B.require(sum(y*b for y, b in zip(c['row_weights'], m['rhs'])) == 0, 'deleted lower0 zero margin')
    reject('essential_lower0_removed', lambda: B.cone(m['matrix'], m['rhs'], c['row_weights']))
    cens = c188(source)
    print(json.dumps({'verdict': 'PASS_AT_CLAIM_CEILING', 'certificate_checks': records,
                      'feasible_relaxation_points': points, 'c196_permutation_decisions': 36720,
                      'c196_positive_class': 671, 'c196_witness_permutations': 8,
                      'residual_updates': updates, 'c186': five_vertex_lemma(),
                      'c187': prism_exceptions(), 'c188': cens,
                      'selected_invalid_controls': bad, 'optimization': sys.flags.optimize,
                      'independence': 'Reviewed C197 arithmetic/orbit engine reused; new full row/cut reconstruction and selectors. Same actor, shared data and expected outcomes, nonblind.',
                      'global_target': 'NOT_TESTED', 'formal_verification': 'NOT_TESTED',
                      'physics_empirical_verification': 'NOT_TESTED'}, indent=2))


if __name__ == '__main__':
    main()
