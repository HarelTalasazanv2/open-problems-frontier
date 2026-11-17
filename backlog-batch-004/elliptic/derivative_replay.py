# Explicit guard adaptation of the reviewed native producer; see CODE_LINEAGE.json.
"""Fixed389a1 completed second derivative; stdlib Decimal directed intervals."""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json, time, sys
P = 30
loctx = Context(prec=P, rounding=ROUND_FLOOR)
hictx = Context(prec=P, rounding=ROUND_CEILING)
near = Context(prec=P, rounding=ROUND_HALF_EVEN)

def down(x):
    return loctx.divide(D(x.numerator), D(x.denominator))

def up(x):
    return hictx.divide(D(x.numerator), D(x.denominator))

class I:

    def __init__(self, a, b=None):
        self.a = D(a)
        self.b = D(a if b is None else b)
        if not (self.a.is_finite() and self.b.is_finite() and (self.a <= self.b)):
            raise ValueError('Derivative guard: self.a.is_finite() and self.b.is_finite() and (self.a <= self.b)')

    def __add__(x, y):
        y = asI(y)
        return I(loctx.add(x.a, y.a), hictx.add(x.b, y.b))
    __radd__ = __add__

    def __neg__(x):
        return I(x.b.copy_negate(), x.a.copy_negate())

    def __sub__(x, y):
        return x + -asI(y)

    def __rsub__(x, y):
        return asI(y) + -x

    def __mul__(x, y):
        y = asI(y)
        a = [loctx.multiply(u, v) for u in (x.a, x.b) for v in (y.a, y.b)]
        b = [hictx.multiply(u, v) for u in (x.a, x.b) for v in (y.a, y.b)]
        return I(min(a), max(b))
    __rmul__ = __mul__

    def __truediv__(x, y):
        y = asI(y)
        if not not y.a <= 0 <= y.b:
            raise ValueError('Derivative guard: not y.a <= 0 <= y.b')
        return x * I(loctx.divide(D(1), y.b), hictx.divide(D(1), y.a))

    def exp(x):
        return I(near.next_minus(near.exp(x.a)), near.next_plus(near.exp(x.b)))

    def ln(x):
        if not x.a > 0:
            raise ValueError('Derivative guard: x.a > 0')
        return I(near.next_minus(near.ln(x.a)), near.next_plus(near.ln(x.b)))

    def pair(x):
        return [str(x.a), str(x.b)]

def asI(x):
    return x if isinstance(x, I) else I(x)

def fracI(x):
    return I(down(x), up(x))

def atan(x, k):
    s = sum(((-1) ** j * x ** (2 * j + 1) / F(2 * j + 1) for j in range(k)), F(0))
    t = (-1) ** k * x ** (2 * k + 1) / F(2 * k + 1)
    return I(down(min(s, s + t)), up(max(s, s + t)))

def constants():
    pi = 16 * atan(F(1, 5), 25) - 4 * atan(F(1, 239), 8)
    scale = 10 ** 35
    r = isqrt(389 * scale ** 2)
    sq = I(down(F(r, scale)), up(F(r + 1, scale)))
    if not r * r < 389 * scale ** 2 < (r + 1) ** 2:
        raise ValueError('Derivative guard: r * r < 389 * scale ** 2 < (r + 1) ** 2')
    c = 2 * pi / sq
    if not c.a > D('.3'):
        raise ValueError("Derivative guard: c.a > D('.3')")
    return (pi, sq, c)

def primes(K):
    return [p for p in range(2, K + 1) if all((p % d for d in range(2, isqrt(p) + 1)))]

def coefficients(K):
    ps = primes(K)
    ap = {}
    counts = {}
    for p in ps:
        count = 1 + sum((1 for x in range(p) for y in range(p) if (y * y + y - x * x * x - x * x + 2 * x) % p == 0))
        counts[p] = count
        ap[p] = p + 1 - count
        if not abs(ap[p]) <= p:
            raise ValueError('Derivative guard: abs(ap[p]) <= p')
    a = [0] * (K + 1)
    a[1] = 1
    for n in range(2, K + 1):
        p = next((p for p in ps if n % p == 0))
        m = n // p
        a[n] = ap[p] * a[m] - (p * a[m // p] if m % p == 0 else 0)
    return (a, ap, counts)

def coefficients_other(K):
    ps = primes(K)
    a = [0] * (K + 1)
    a[1] = 1
    for p in ps:
        if p == 2:
            count = 5
        else:
            count = p + 1 + sum((0 if (z := ((1 + 4 * (x * x * x + x * x - 2 * x)) % p)) == 0 else 1 if pow(z, (p - 1) // 2, p) == 1 else -1 for x in range(p)))
        ap = p + 1 - count
        power = [(1, 1), (p, ap)]
        prev, cur = (1, ap)
        n = p
        while n * p <= K:
            n *= p
            prev, cur = (cur, ap * cur - p * prev)
            power.append((n, cur))
        b = [0] * (K + 1)
        for m in range(1, K + 1):
            if a[m]:
                for n, v in power:
                    if m * n <= K:
                        b[m * n] += a[m] * v
        a = b
    return a

def check_contract(cert, reference):
    if not (cert['center'] == 1 and cert['root_sign'] == 1):
        raise ValueError("Derivative guard: cert['center'] == 1 and cert['root_sign'] == 1")
    if not cert['normalization'] == 'raw_Lsecond_not_divided_by_factorial':
        raise ValueError("Derivative guard: cert['normalization'] == 'raw_Lsecond_not_divided_by_factorial'")
    if not cert['coefficient_indices'] == list(range(1, 101)):
        raise ValueError("Derivative guard: cert['coefficient_indices'] == list(range(1, 101))")
    if not cert['coefficients'] == reference[1:]:
        raise ValueError("Derivative guard: cert['coefficients'] == reference[1:]")
    if not cert['grid'] == {'first': 0, 'last': 7899, 'count': 7900, 'denominator': 100}:
        raise ValueError("Derivative guard: cert['grid'] == {'first': 0, 'last': 7899, 'count': 7900, 'denominator': 100}")
    if not (cert['coefficient_tail_included'] and cert['integration_tail_included']):
        raise ValueError("Derivative guard: cert['coefficient_tail_included'] and cert['integration_tail_included']")
    if not cert['rounding'] == 'directed_basic_and_oneulp_exp_ln':
        raise ValueError("Derivative guard: cert['rounding'] == 'directed_basic_and_oneulp_exp_ln'")
    if not cert['raw_Lsecond'] == cert['recomputed_raw_Lsecond']:
        raise ValueError("Derivative guard: cert['raw_Lsecond'] == cert['recomputed_raw_Lsecond']")
    a, b = map(D, cert['raw_Lsecond'])
    if not (a < b and a > 0):
        raise ValueError('Derivative guard: a < b and a > 0')
    return True

def recompute():
    start = time.time()
    pi, sq, c = constants()
    a, ap, counts = coefficients(100)
    other = coefficients_other(100)
    if not a == other:
        raise ValueError('Derivative guard: a == other')
    if not 93 ** 2 % 389 == 91:
        raise ValueError('Derivative guard: 93 ** 2 % 389 == 91')
    bad_count = 1 + sum((1 for x in range(389) for y in range(389) if (y * y + y - x * x * x - x * x + 2 * x) % 389 == 0))
    if not bad_count == 389:
        raise ValueError('Derivative guard: bad_count == 389')
    s = I(0)
    for j in range(7900):
        y = I(D(100 + j) / D(100), D(101 + j) / D(100))
        q = (-c * y).exp()
        v = I(a[100])
        for n in range(99, 0, -1):
            v = v * q + a[n]
        fy = v * q
        l = y.ln()
        s = s + fy * l * l * I('.01')
    K = 100
    r = F(3, 4)
    tail = r ** (K + 1) * (F((K + 1) ** 2, 1) / (1 - r) + F(2 * (K + 1), 1) * r / (1 - r) ** 2 + r * (1 + r) / (1 - r) ** 3)
    et = fracI(79 * 25 * tail)
    yt = 3 * I(-24).exp() * fracI(F(80 ** 2, 1) / F(3, 10) + F(160, 1) / F(3, 10) ** 2 + F(2, 1) / F(3, 10) ** 3)
    err = hictx.add(et.b, yt.b)
    integral = s + I(err.copy_negate(), err)
    completed = 2 * integral
    raw = completed * c
    cert = {'schema': 'OPF_389A1_SECOND_DERIVATIVE_C061_V1', 'center': 1, 'root_sign': 1, 'fricke_eigenvalue': -1, 'bad_projective_count': bad_count, 'normalization': 'raw_Lsecond_not_divided_by_factorial', 'pi': pi.pair(), 'sqrt389': sq.pair(), 'c': c.pair(), 'precision': P, 'coefficient_indices': list(range(1, 101)), 'coefficients': a[1:], 'prime_counts': counts, 'prime_coefficients': ap, 'coefficient_oracle_agreement': True, 'grid': {'first': 0, 'last': 7899, 'count': 7900, 'denominator': 100}, 'finite_integral': s.pair(), 'coefficient_tail_bound': et.pair(), 'integration_tail_bound': yt.pair(), 'coefficient_tail_included': True, 'integration_tail_included': True, 'rounding': 'directed_basic_and_oneulp_exp_ln', 'integral': integral.pair(), 'completed_second': completed.pair(), 'raw_Lsecond': raw.pair(), 'recomputed_raw_Lsecond': raw.pair(), 'half_second': (raw / 2).pair(), 'seconds': time.time() - start, 'python': sys.version}
    if not check_contract(cert, a):
        raise ValueError('Derivative guard: check_contract(cert, a)')
    return cert
