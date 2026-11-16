"""Read-only exact C188-to-C197 exclusion-set chain, not a graph-completion test."""
from pathlib import Path
from hashlib import sha256
import json
import basis as B

ROOT = Path(__file__).resolve().parent
D = ROOT/'data'
E = ROOT/'extended_data'


def read(path):
    return B.load(path)


def check_step(previous, current, removed, source):
    pool = {e['representative']: e['members'] for e in source['classes']}
    B.require(len(removed) == len(set(removed)) and all(r in previous for r in removed),
              'no duplicate or out-of-domain exclusion')
    members = sorted(x for r in removed for x in pool[r])
    keys = [('removed_representatives', 'removed_members'),
            ('newly_removed_representatives', 'newly_removed_members'),
            ('excluded_representatives', 'excluded_labeled_members')]
    rk, mk = next((a,b) for a,b in keys if a in current)
    B.require(current[rk] == removed and current[mk] == members, 'complete removed membership')
    remain = [r for r in previous if r not in removed]
    B.require(current['remaining_representatives'] == remain and
              current['remaining_labeled_graphs'] == sum(len(pool[r]) for r in remain),
              'exact remaining membership and count')
    return remain, {'excluded': removed, 'removed_labeled': len(members),
                    'remaining_classes': len(remain),
                    'remaining_labeled': current['remaining_labeled_graphs']}


def main():
    source = read(D/'source_orbits.json')
    previous = source['remaining_representatives']
    steps = [(E/'c189_residual_update.json',[684]),(E/'c190_residual_update.json',[617]),
             (E/'c191_residual_update.json',[632]),(E/'c192_residual_update.json',[]),
             (E/'manual_residual_first.json',[659,692,920]),(E/'manual_residual_final.json',[662]),
             (E/'c193_residual.json',[619]),(D/'c633_residual.json',[633]),
             (D/'c635_residual.json',[635]),(D/'c655_residual.json',[655]),
             (D/'c195_residual.json',[663]),(D/'c196_residual.json',[671]),
             (E/'c197_residual.json',[685])]
    summaries = []
    prev_path = D/'source_orbits.json'
    for path, removed in steps:
        current = read(path)
        if 'prior_residual_sha256' in current:
            B.require(current['prior_residual_sha256'] == sha256(prev_path.read_bytes()).hexdigest(),
                      'adjacent raw residual identity')
        previous, summary = check_step(previous,current,removed,source)
        summaries.append({'file':str(path.relative_to(ROOT)),**summary})
        prev_path=path
    B.require(len(previous) == 49 and summaries[-1]['remaining_labeled'] == 14872,
              'current C197 residual')
    first=read(E/'manual_residual_first.json');bad=dict(first)
    bad['removed_members']=bad['removed_members'][:-1]
    try:
        check_step(read(E/'c192_residual_update.json')['remaining_representatives'],bad,
                   [659,692,920],source)
    except ValueError:
        control=True
    else:
        raise ValueError('partial orbit deletion accepted')
    print(json.dumps({'verdict':'PASS_AT_CLAIM_CEILING','steps':summaries,
                      'final_representatives':previous,'final_labeled':14872,
                      'partial_orbit_control_rejected':control,
                      'limit':'Exact set bookkeeping linked to the separately reviewed proofs; no survivor feasibility or global target conclusion.'},indent=2))


if __name__ == '__main__':
    main()
