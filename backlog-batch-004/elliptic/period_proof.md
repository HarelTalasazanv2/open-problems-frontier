# Exact archimedean factor for the fixed389.a1 model

Let E:y^2+y=x^3+x^2-2x and omega=dx/(2y+1). Completing the square gives
(2y+1)^2=g(x)=4x^3+4x^2-8x+1. Three disjoint sign-changing rational intervals
enclose e3<e2<e1. Degree3 then proves completeness and simplicity of these roots.
No root scan or approximate discriminant is used to assert completeness.
The real locus consists of one oval over[e3,e2] and the identity component over
[e1,infinity], whose two branches meet at infinity. Each is traversed once.
Branch points have integrable inverse-square-root endpoint singularities;
the unbounded integral decays as x^-3/2. Thus all improper integrals below exist.

On either real branch abs(omega)=abs(dx)/sqrt(g(x)). Accounting for both
branches of each loop gives the following periods, with no missing factor2:

    U = 2 integral(e1..infinity) dx/sqrt(g(x))
      = integral(0..infinity) dt/sqrt(t(t+A)(t+B)),
    A=e1-e3>0, B=e1-e2>0, C=e2-e3=A-B>0.

For the oval, V=integral(e3..e2)dx/sqrt((e1-x)(e2-x)(x-e3)).
Set t=B(x-e3)/(e2-x), so x=(e2*t+B*e3)/(t+B),
dx/dt=BC/(t+B)^2, x-e3=Ct/(t+B), e2-x=BC/(t+B),
and e1-x=B(t+A)/(t+B). Substitution gives exactly V=U.
The substitution maps the complete oval integration interval onto[0,infinity].
Consequently Omega=integral over all E(R) abs(omega)=U+V=2U.

The inspected NIST DLMF19.8.4 states, for positive a,b,
integral(0..infinity)dt/sqrt(t(t+a^2)(t+b^2))=pi/AGM(a,b).
This standard integral identity is imported, not newly proved. Hence

    U=pi/AGM(sqrt(A),sqrt(B)),
    Omega=2*pi/AGM(sqrt(A),sqrt(B)).

LMFDB's reviewed real-period definition uses the invariant differential of a
minimal Weierstrass model and the least positive real lattice period multiplied
by the number of real components. U traverses the identity circle once and is
that least real period, so Omega is the matching full-real convention. The
minimality of this integral model is inherited from060; its discriminant389
has valuation<12 at every prime. This is not an identification of a newform
period with a curve period by an unproved Manin-constant assumption. Cremona
Chapter1's newform-period quotient is used only to audit the r! and regulator
placement, not to supply an unverified differential bridge.

For a>=b>0, the finite AGM sequences a'=(a+b)/2, b'=sqrt(ab) remain positive,
a decreases, b increases and b<=a; this follows from AM>=GM. Their limits
coincide because a'-b'=(sqrt(a)-sqrt(b))^2/2 and any distinct positive limiting
pair would violate the limiting arithmetic mean identity. Thus each finite
iterate bounds M between b_n and a_n. Exact rational interval propagation
bounds the same actual sequences: the lower geometric endpoint and upper
arithmetic endpoint suffice. The finite gap is the full infinite-iteration error;
no stable decimal or unproved asymptotic remainder is used.

Square roots are enclosed by integer-square tests at fixed decimal scale S:
q=floor(sqrt(floor(x*S^2))) gives q/S<=sqrt(x)<=(q+1)/S, with equality handled
exactly for a perfect square. Inputs remain rational. Pi is bounded by finite
alternating arctangent series with explicit next-term remainders and Machin's
identity. Tangent addition gives tan(4atan(1/5)-atan(1/239))=1; the positive
first-quadrant angle is pi/4. Rational floor/ceiling alone formats endpoints.

## Different reduction for confirmation

Put x=e3+A/sin^2(theta) in U. The endpoints map to theta=0,pi/2 and give

    U = 2/sqrt(A) * integral(0..pi/2)
                 (1-m*sin^2(theta))^-1/2 dtheta, m=C/A in(0,1).

The binomial theorem and positive-term integration yield

    U = pi/sqrt(A) * sum(j>=0) c_j^2*m^j,
    c_j=binom(2j,j)/4^j.

Indeed integration by parts proves integral sin^(2j)(theta)dtheta=(pi/2)c_j.
For 0<=m<1, integrands are dominated by(1-m)^-1/2 and all expansion terms are
nonnegative. Since 0<c_j<=1, the omitted tail after n terms lies in
[0,m^n/(1-m)]. Exact bounds on m,A and pi therefore supply an independent
enclosure for Omega=2U. The confirmation uses120terms and a distinct pi identity,
pi=4(atan(1/2)+atan(1/3)); tangent addition and the first quadrant again fix it.
The confirmation also checks all roots and the full finite AGM trace.

All discovery and confirmation arithmetic is Python standard-library arbitrary
integers/Fraction. No binary floating-point constants, numerical tolerance,
quadrature discretization, omitted root/component, downloaded code or source
program is used. Source/actor/curve/rational library are shared; the integral
reduction and numerical algorithm differ. This is not blind reproduction,
external human review or formal verification.

## Inherited leading coefficient and claim ceiling

Cycle061 already supplies a corrected raw L'' interval and its exact half for
the leading Taylor coefficient. Dated artifact identity is checked this run;
the Mellin integral is not recomputed. Rejected061V1 is not a dependency.
Cycle152's determinant range is inherited separately. A rational interval for
(L''/2)/(Omega*R) is therefore a conditional factor comparison under those
inherited certificates. It is not automatically a full BSD quotient unless
torsion/Tamagawa and all conventions are separately matched, and an interval
near1 does not prove a Sha group has order1 or is finite. No such promotion is made.
The present new claim is only the fixed full-real period and exact component
relation under the named standard integral/period conventions.
