# Fixed-curve height determinant: analytic contract

Use E:y^2+y=x^3+x^2-2x, P=(0,0), Q=(1,0), R=P+Q=(-2,-1).
Let H(T)=lim 4^-n h_x(2^nT), with h_x=log max(abs(a),b) for reduced x=a/b,
b>0. H(O)=0. Natural logarithms, no hidden half-height convention.
The pairing is (H(P+Q)-H(P)-H(Q))/2 and D_H is its two-by-two determinant.

The author-hosted corrected second edition of Cremona, Chapter3, physical10
(printed71), gives exactly this height, pairing and regulator convention.
Physical11 (printed72) warns that the alternative half-height convention
rescales the rank-r determinant by 2^-r. Thus in rank2 the determinant for
the consistently halved quadratic height is D_H/4. This is a convention
change, not an alternative numerical result. We do not adopt a database's
convention without checking it. Physical16 (printed77), Proposition3.5.1,
is the imported uniform two-sided height theorem. Its proof is not reproduced.

For our integral model b2=4, c4=112, c6=-856, Delta=389. Write N0=112^3=1404928.
Then j=N0/389>1, h(j)<=log N0, and mu=(log N0)/6+log2.
Since N0<2^21 and log2<7/10, mu+107/50<529/100<53/10,
and h(j)/12+mu+961/500<6297/1000<63/10.
The elementary inequality log2<7/10 follows from the first four positive
terms of exp(7/10), whose sum is 12013/6000>2.
Consequently -63/10 <= H(T)-h_x(T) <= 53/10 for every rational T.
Apply this to 2^nT, and use H(2^nT)=4^nH(T), to obtain the correctly directed
interval [(h_x(2^nT)-63/10)/4^n,(h_x(2^nT)+53/10)/4^n].
This supplies the entire infinite-limit error; consecutive agreement is not used.

For reduced x=a/b the exact duplication is obtained by substituting the tangent
slope (3x^2+2x-2)/(2y+1) and (2y+1)^2=4x^3+4x^2-8x+1:

    x(2T)=(x^4+4x^2-2x+3)/(4x^3+4x^2-8x+1).

Hence its integer homogeneous numerator is a^4+4a^2b^2-2ab^3+3b^4,
and denominator b(4a^3+4a^2b-8ab^2+b^3), followed by sign/gcd reduction.
Zero denominator represents the identity and must not be divided by. The fixed
sequences are checked to avoid it. The confirmation law uses the independent
short model X=x+1/3, Y=y+1/2, Y^2=X^3-(7/3)X+107/108.

For integer M>=1, write M=2^k*r, 1<=r<2. Exact leading-bit truncation bounds r
between rational endpoints; discarded bits are not rounded to nearest. For
1<=s<=2 put z=(s-1)/(s+1) in [0,1/3]. Integrating a geometric series gives

    log s = 2 sum(j>=0) z^(2j+1)/(2j+1).

After m terms, the remainder is nonnegative and at most
2*z^(2m+1)/((2m+1)*(1-z^2)); this includes z=0. Monotonicity of log and
log M=k*log2+log r propagate the two endpoints. Python arbitrary integers and
Fraction perform exact rational operations. Decimal-form output is generated
only by exact floor/ceiling of rational endpoints. There is no floating error.

For interval heights p,q,r, first bound c=(r-p-q)/2 by signed endpoint
arithmetic, then square c with zero included when its interval crosses zero.
The product p*q uses all four products; subtract the square with reversed
endpoints. This elementary interval dependency enlargement is conservative.
It can widen, but cannot shrink, the enclosing interval. The target is width
less than 1/1000, not optimality or new mathematics.

A successful certificate bounds the named-point determinant under the imported
height theorem. Its interpretation as the full regulator in Cremona's convention
additionally inherits the Cycle090 full-basis result, not re-proved in this run.
It does not establish Sha's order/finiteness, an L-value equality, the full BSD
formula, or any universal elliptic-curve statement. No external human review or
formal verification is claimed.
