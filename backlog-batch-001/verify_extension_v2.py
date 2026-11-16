"""Read-only exact review of C189--C193 and the four E5 cap exclusions.

Reuses basis.py arithmetic and graph decoding from the reviewed C197 checker.
All pair rows, all binary records, cap lifts and the selected mixed cut are
reconstructed here. Shared actor/inputs/expected answers: nonblind.
"""
from pathlib import Path
from copy import deepcopy
from hashlib import sha256
import json
import sys
import basis as B

E = Path(__file__).resolve().parent/'extended_data'
P = B.PAIRS


def read(name):
    return B.load(E/(name+'.json'))


def equal(a, b, message):
    B.require(B.canonical(a) == B.canonical(b), message)


def pair_system(model, r):
    edges, degree, triples, _, _ = B.graph(r)
    B.require(len(edges) == 5 and model['case_id'] == model['a_mask'] == r, 'E5 identity')
    allowed = [i for i, pair in enumerate(P) if all(set(pair).intersection(q) for q in triples)]
    forbidden = [i for i in range(15) if i not in allowed]
    equal(model['pair_types'], [list(p) for p in P], 'all fifteen pairs')
    equal(model['independent_triples'], [list(q) for q in triples], 'all triples')
    equal(model['allowed_type_indices'], allowed, 'complete allowed support')
    equal([x['type_index'] for x in model['forbidden_types']], forbidden, 'forbidden membership')
    for x in model['forbidden_types']:
        q = tuple(x['independent_triple'])
        B.require(q in triples and not set(P[x['type_index']]).intersection(q), 'zero-row witness')
    matrix = [[1]*15]+[[int(v in p) for p in P] for v in range(6)]
    matrix += [[int(j == i) for j in range(15)] for i in forbidden]
    rhs = [10]+[5-d for d in degree]+[0]*len(forbidden)
    labels = ['total']+[f'degree:{v}' for v in range(6)]+[f'zero:{i}' for i in forbidden]
    for field, value in [('cross_degrees', rhs[1:7]), ('matrix', matrix), ('rhs', rhs),
                         ('row_labels', labels)]:
        equal(model[field], value, 'pair model '+field)
    if 'population' in model:
        B.require(model['population'] == 10, 'population')
    return matrix, rhs, allowed


def bound_model(model, r):
    matrix, rhs, allowed = pair_system(model, r)
    edges = B.graph(r)[0]
    caps = {i: 2 if P[i] in edges else 3 for i in allowed}
    lifted = [row+[0]*len(allowed) for row in matrix]
    for j, i in enumerate(allowed):
        lifted.append([int(k == i) for k in range(15)]+[int(k == j) for k in range(len(allowed))])
        rhs = rhs+[caps[i]]
    return lifted, rhs, allowed, caps


def binary_case(entry):
    r = entry['representative']
    m = entry['model']; _, rhs, allowed = pair_system(m, r)
    B.require(m['variable_domain'] == 'NONNEGATIVE_REAL' and
              entry['canonical_model_sha256'] == sha256(B.canonical(m)).hexdigest(), 'family binding/domain')
    expected = []
    for mask in range(64):
        w = [(mask >> v) & 1 for v in range(6)]
        sums = [sum(w[v] for v in P[i]) for i in allowed]
        cover = all(s >= 1 for s in sums)
        cost = sum(a*b for a, b in zip(w, rhs[1:7]))
        expected.append({'weight_mask': mask, 'weights': w, 'support_weights': sums,
                         'is_cover': cover, 'cost': cost, 'deficit': 10-cost,
                         'strict_obstruction': cover and cost < 10})
    equal(entry['candidates'], expected, 'complete 64 binary records')
    B.require(not any(x['strict_obstruction'] for x in expected) and entry['certificate'] is None,
              'no qualifying binary cover')
    covers = [x for x in expected if x['is_cover']]
    return {'representative': r, 'minimum': min(x['cost'] for x in covers),
            'cost_ten_boundary_masks': [x['weight_mask'] for x in covers if x['cost'] == 10],
            'allowed_types': len(allowed)}


def mixed193(model, cert):
    edges, degree, triples, allowed, _ = B.graph(619)
    matrix, rhs, labels, n_eq, _ = B.expected_system(619)
    eq = [row[:21] for row in matrix[:n_eq]]
    iq = [row[:21] for row in matrix[n_eq:]]
    cut = [int(0 not in t and 3 not in t and 5 in t) for t in B.TYPES]
    B.require((0, 3) not in edges and model['selected_common_cut'] == [0, 3, 5], 'valid selected cut')
    iq.append(cut)
    m2 = [row+[0]*len(iq) for row in eq]
    m2 += [row+[int(i == j) for j in range(len(iq))] for i, row in enumerate(iq)]
    for key, value in [('representative', 619), ('types', [list(t) for t in B.TYPES]),
                       ('edges', [list(p) for p in P if p in edges]), ('degrees', degree),
                       ('independent_triples', [list(q) for q in triples]),
                       ('allowed_type_indices', allowed),
                       ('forbidden_type_indices', [i for i in range(21) if i not in allowed]),
                       ('equalities', eq), ('equality_rhs', rhs[:n_eq]),
                       ('equality_labels', labels[:n_eq]), ('inequalities', iq),
                       ('inequality_rhs', rhs[n_eq:]+[3]),
                       ('inequality_labels', labels[n_eq:]+['common:0:3:5']),
                       ('matrix', m2), ('rhs', rhs+[3]), ('row_labels', labels+['common:0:3:5'])]:
        equal(model[key], value, 'mixed193 '+key)
    B.require(model['variable_domain'] == 'NONNEGATIVE_REAL' and
              cert['model_sha256'] == sha256(B.canonical(model)).hexdigest(), 'mixed binding/domain')
    out = B.cone(m2, rhs+[3], cert['row_weights'])
    counts = [2 if t in [(0,4),(1,5),(2,5),(3,4),(3,5)] else 0 for t in B.TYPES]
    B.require(all(sum(a*b for a, b in zip(row, counts)) == value
                  for row, value in zip(eq, rhs[:n_eq])) and
              all(sum(a*b for a, b in zip(row, counts)) <= value
                  for row, value in zip(iq[:-1], rhs[n_eq:])), 'base619 feasible point')
    B.require(sum(a*b for a, b in zip(cut, counts)) == 4 > 3, 'new cut discriminates')
    return out


def main():
    pairs = []
    for prefix, r, certificate_name in [('c189', 684, 'row_certificate'),
                                       ('c190', 617, 'cone_certificate'),
                                       ('c191', 632, 'cone_certificate')]:
        m = read(prefix+'_pair_model'); c = read(prefix+'_'+certificate_name)
        matrix, rhs, _ = pair_system(m, r)
        B.require(c['model_sha256'] == sha256((E/(prefix+'_pair_model.json')).read_bytes()).hexdigest(), 'pair certificate binding')
        y = c['weights']
        B.require(len(y) == len(matrix) and B.strict_ints(y), 'complete integer multipliers')
        value = sum(a*b for a, b in zip(y, rhs))
        if prefix == 'c189':
            B.require(all(sum(y[i]*matrix[i][j] for i in range(len(y))) == 0
                          for j in range(15)) and value != 0, 'row identity contradiction')
            pairs.append({'representative': r, 'row_identity_rhs': value})
        else:
            B.require(m['variable_domain'] == 'NONNEGATIVE_REAL', 'nonnegative count domain')
            pairs.append({'representative': r, **B.cone(matrix, rhs, y)})
            w = read(prefix+'_signed_witness')
            B.require(w['model_sha256'] == c['model_sha256'] and len(w['values']) == 15 and
                      B.strict_ints(w['values']) and min(w['values']) < 0, 'signed witness domain')
            equal([sum(a*b for a, b in zip(row, w['values'])) for row in matrix], rhs,
                  'signed equality witness')
    family = read('c192_family_ledger')
    reps = [r for r in read('c191_residual_update')['remaining_representatives']
            if len(B.graph(r)[0]) == 5]
    equal(reps, [659,662,692,920], 'all residual E5 cases')
    equal(family['case_ids'], reps, 'family header membership')
    equal([e['representative'] for e in family['cases']], reps, 'family case membership')
    B.require(family['complete'] is True and family['completed_candidates'] == 256 and
              family['remaining_pairs'] == [] and family['feasibility_claim'] == 'NOT_TESTED',
              'complete range without feasibility promotion')
    binary = [binary_case(e) for e in family['cases']]
    B.require([e['minimum'] for e in binary] == [10,11,10,10], 'binary minima')
    output = read('manual_capacity')['output']
    B.require(output['complete'] is True and output['case_ids'] == reps and
              output['completed_vertices'] == 24 and output['remaining_pairs'] == [], '24-bound completeness')
    equal([e['case_id'] for e in output['cases']], reps, 'cap case membership')
    by_id = {e['representative']:e for e in family['cases']}
    checks = []
    for entry in output['cases']:
        r = entry['case_id']; model = by_id[r]['model']
        matrix, rhs, allowed, caps = bound_model(model, r)
        edges, degree, _, _, _ = B.graph(r)
        equal(entry['allowed_types'], [{'a_edge': P[i] in edges, 'cap': caps[i],
                                        'type_index': i, 'vertices': list(P[i])} for i in allowed],
              'all pair capacities')
        B.require(len(entry['vertices']) == 6 and [x['vertex'] for x in entry['vertices']] == list(range(6)),
                  'all six capacity vertices')
        for rec in entry['vertices']:
            v = rec['vertex']; incident = [i for i in allowed if v in P[i]]
            capacity = sum(caps[i] for i in incident); required = 5-degree[v]
            for key, value in [('incident_type_indices', incident), ('capacity', capacity),
                               ('required', required), ('margin', capacity-required),
                               ('strict_deficit', capacity < required)]:
                equal(rec[key], value, 'capacity record '+key)
            if capacity < required:
                checks.append({'representative':r,'vertex':v,
                               **B.cone(matrix, rhs, rec['certificate']['row_weights'])})
            else:
                B.require(rec['certificate'] is None, 'no non-strict certificate')
    equal(output['excluded_representatives'], [659,692,920], 'individual cap exclusions')
    aggregate = read('manual_aggregate'); m = by_id[662]['model']
    matrix, rhs, _, _ = bound_model(m, 662)
    combined = B.cone(matrix, rhs, aggregate['row_weights'])
    equal([sum(aggregate['row_weights'][i]*matrix[i][j] for i in range(len(matrix)))
           for j in range(len(matrix[0]))], aggregate['combined_columns'], 'aggregate columns')
    B.require(combined['rhs'] == '-2' and aggregate['combined_rhs'] == -2, 'aggregate margin')
    mixed = mixed193(read('c193_model'), read('c193_certificate'))
    bad = []
    def reject(name, call):
        try:
            call()
        except (ValueError, KeyError, TypeError, IndexError):
            bad.append(name); return
        raise ValueError('invalid control accepted: '+name)
    entry = deepcopy(family['cases'][0]);entry['candidates'].pop()
    reject('missing_binary_weight', lambda: binary_case(entry))
    entry = deepcopy(family['cases'][0]);entry['candidates'][1] = deepcopy(entry['candidates'][0])
    reject('duplicate_binary_weight', lambda: binary_case(entry))
    entry = deepcopy(family['cases'][0]);entry['candidates'][25]['strict_obstruction'] = True
    reject('cost_ten_promoted', lambda: binary_case(entry))
    m = read('c190_pair_model');q=deepcopy(m);q['forbidden_types'].pop()
    reject('missing_pair_zero', lambda: pair_system(q,617))
    q=read('c193_model');q['selected_common_cut']=[0,1,5]
    reject('invalid_common_cut', lambda: mixed193(q,read('c193_certificate')))
    reject('wrong_cone_sign',lambda:B.cone(matrix,rhs,[-v for v in aggregate['row_weights']]))
    reject('feasible_false_cone',lambda:B.cone([[-1]],[-2],[1]))
    print(json.dumps({'verdict':'PASS_AT_CLAIM_CEILING','pair_certificates':pairs,
                      'binary_weight_decisions':256,'binary_minima':binary,'capacity_vertex_decisions':24,
                      'individual_cap_certificates':checks,'aggregate662':combined,'mixed619':mixed,
                      'removed_orbits':{str(r):len(B.orbit(r)) for r in [684,617,632,659,662,692,920,619]},
                      'selected_invalid_controls':bad,'optimization':sys.flags.optimize,
                      'limits':'Known outcomes; C197 basis engine reused. Same actor, nonblind. No full-target/novelty/external/formal/empirical-physics claim.'},indent=2))


if __name__ == '__main__':
    main()
