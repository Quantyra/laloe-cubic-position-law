# Grok manuscript review

AI-generated referee reports. See the [editorial disposition](disposition.md) for the author-side checks and corrections.

## First manuscript

Supplied manuscript SHA-256: `7d2e3aaf18b4f0f45f96ae39edb9f8db3d90347d5b79baab24f6360177d81c63`.

**Verdict: revise.** The displayed short-time law, dilation coefficient, retarded multiplier, and numerical constants check out. No sign or normalization error was found in those claims. Proposition 1’s prose justification is not yet a complete derivation and can be read as flipping the Madelung sign. That should be rewritten before release. It is not a reason to hold the result.

**What was reconstructed.** With \(\alpha=i+\epsilon\) the equation is \(i\partial_t=(-\Delta+|x|^2)/2-K+i\epsilon K\). Attractive real gravity and growth of \(A\) where \(K\) is larger are the right signs. For \(\psi=Ae^{iS}\),
\[
\partial_t S=-\tfrac12|\nabla S|^2+\frac{\Delta A}{2A}-\frac{|x|^2}{2}+\Phi,\qquad
\partial_t\log A=-\nabla S\cdot\nabla\log A-\tfrac12\Delta S+\epsilon\Phi.
\]
At \(t=0\), \(S\) is flat, \(\nabla\Phi(q)=0\), and the oscillator identity \(\Delta g/(2g)=|x|^2/2-3/2\) gives \(\dot Q(0)=\ddot Q(0)=0\). Also \(\partial_t\Phi(0)=0\) for a static incoming history with \(\dot Q(0)=0\), so the field does not enter the jerk. Only
\[
\partial_t\log A\big|_{t=0}=\epsilon K+\text{scalar}
\]
does. Then
\[
\partial_t\Bigl(\frac{\Delta A}{2A}\Bigr)=\frac\epsilon2\bigl(\Delta K+2\nabla\log g\cdot\nabla K\bigr).
\]
Here \(K=\mathrm{erf}(\rho)/\rho=(2/\sqrt\pi)-(2/(3\sqrt\pi))\rho^2+O(\rho^4)\), so \(D^2K(0)=-HI\) with \(H=4/(3\sqrt\pi)\). Thus \(\nabla K=-Hr+O(r^3)\). The gradients of \(\Delta K\) and of \(\nabla K\) vanish at the source, but
\[
\nabla(\nabla\log g\cdot\nabla K)\big|_q=Hq
\]
because \(\nabla\log g(q)=-q\) contracts with the Hessian. The jerk is \(\epsilon Hq\), outward, and \(Q(t)=q\bigl(1+\epsilon H t^3/6\bigr)+O(t^4)\). The manuscript’s displayed formula is right; the sentence that the phase equation “contains the quantum potential \(-\Delta A/(2A)\)” is not. The standard quantum potential is \(-\Delta A/(2A)\) and enters \(\partial_t S\) with a minus. As written, that clause contradicts the positive contribution \(\epsilon\nabla(\cdots)/2\) printed immediately afterward.

The threshold arithmetic is consistent with this sign. The marginal of \(g^2\) is \(\pi^{-1/2}e^{-x^2}\), the threshold \(1/\sqrt2\) is one standard deviation, and
\[
\frac{d}{dD}\Pr(|Dq_1|>s)\Big|_{D=1}=2\phi(1)=\sqrt{2/\pi}\,e^{-1/2}.
\]
So \(P_\epsilon-P_0=2\phi(1)(\epsilon H/6)t^3+o(t^3)\). Restoring \(\lambda=Gm^2/(\hbar\omega\ell)=1\) and \(a=\ell\) turns \(H\omega^3\) into \(4Gm\omega/(3\sqrt\pi a^3)\). Both are correct, as are \(D-1=1.25375\ldots\times10^{-40}\), the ideal gap \(6.06744\ldots\times10^{-41}\), \(m\simeq1.21\times10^{-17}\,\mathrm{kg}\), and \(\ell\simeq9.32\times10^{-8}\,\mathrm{m}\).

**Retarded multiplier and remainders.** The mode \(B\) solves \(\partial_{tt}B+(\nu k)^2 B=(\nu k)^2 z\) with static initial data, and both printed formulas agree. \(|B-z(0)|\le 2k L_t\) is uniform in \(\nu\). The coherent parameters \(D=\sum k_j\sin u_j\), \(P=\sum k_j\cos u_j\) match a momentum kick rotated by the oscillator. The measure \(d\mu=(2/\pi)e^{-k^2/4}\,dk\,d\Omega/(4\pi)\) reproduces \(K(0)=2/\sqrt\pi\) and \(\int kk^T\,d\mu=HI\). The moment bounds \(2,3,7,21,80,330\) follow from \(0.01k\le k^2/8+0.0002\). The weights \(8,17,49\) and the majorants \(e^{16t}\), \(34te^{16t}\), and \((98t+(34t)^2)e^{16t}\) match \(|\alpha|\le2\) and \(L_t\le1\). One-kick expansion gives \(\alpha i Hq\,t^2/2\), whose imaginary part is the jerk integral \(\epsilon Hq\,t^2/2\). The domination \(M_1+3RM_2+(4+R^2)M_3+2RM_4+M_5\le418+181R+21R^2\) matches \(|Z'|\le Rk+k^2\) and \(|Z''|\le Rk+2k^2\). The factor from Taylor integration times \(|\alpha|\) is at most \(1/3\), so that \(t^3\) estimate is valid and loose. The two-kick moments \(12,46,210\) are exactly \(\int S^j e^{0.01S}\,d\mu^{\otimes2}\), and \(1284+92R=2(12+46R+630)\). The tail \(b_R=\mathrm{erfc}(R)+2Re^{-R^2}/\sqrt\pi\) is the exact three-dimensional Gaussian tail. At \(t=10^{-12}\), \(R=16\), \(e_R<1.64\times10^{-42}\) and \(e_*<1.82\times10^{-42}\) reproduce the printed band arithmetic. Hoeffding \(n=\lceil8\ln80/\Delta^2\rceil\simeq1.40\times10^{82}\) and the Pinsker necessary bound \(>6.94\times10^{79}\) are correct. \(C_R=10^4(1+R)^2\) covers the summed velocity errors on the stated domain.

**Requested changes.** (1) Replace the Proposition 1 paragraph with the phase equation above, the Hessian contraction, and the conclusion \(Q'''(0)=\epsilon Hq\). Severity: moderate for the writeup, not a wrong theorem. (2) State that the one-kick constant absorbs \(|\alpha|\le2\) and \(\int_0^t u^2/2\,du\), and that the \(n\ge3\) weights \(4\) and \(6\) are \(\int|\alpha|e^{0.01k}\,d\mu\) and \(\int|\alpha|ke^{0.01k}\,d\mu\). Severity: low. (3) Write \(\ln\) in the sample-size formula. Severity: negligible.

**Limits, not errors.** The \(o(t^3)\) law is only as \(t\to0\), with the explicit tube \((R+1)t\le0.01\), \(t\le10^{-3}\). Real gravity is entirely inside the \(O(t^4)\) budget. Existence is not claimed for all \(q\), nor is the Picard constant uniform in \(\nu\). The \(\epsilon=10^{-3}\), \(\lambda=1\), \(10^{-43}\) failure budget, and \(0.01\ell\) noise model are sufficient assumptions. The paper correctly treats \(10^{-48}\,\mathrm m\) threshold drift as able to mimic the bit.

**Source access.** This review uses only the manuscript. Laloë’s Eq. (4), the cited DOIs, NIST values, and the repository were not opened, so the external identification of \(K\) is unchecked. The internal Fourier representation of the printed kernel was checked.

## Final targeted check

Supplied manuscript SHA-256: `1465fb59834c7f0cbaeb4b95bc0f50c2d45557a6356296a2348767da30979e76`.

**Verdict: ready.** The three requested writeup changes are in place, and none leaves a material defect in the short-time claim.

The phase equation is now \(\partial_t S=-|\nabla S|^2/2+\Delta A/(2A)-|x|^2/2+K[Q]\). That puts \(+\Delta A/(2A)\) in the phase law and identifies the quantum force as \(-\nabla U_{\mathrm B}\) with \(U_{\mathrm B}=-\Delta A/(2A)\). The formal jerk \(\epsilon\nabla(\Delta K+2\nabla\log g\cdot\nabla K)/2\), the vanishing of \(\nabla K\) and \(\nabla\Delta K\) at the source, and the contraction \(D^2K(0)\nabla\log g(q)=(-HI)(-q)=Hq\) recover the outward coefficient. Proposition 1 states the right-hand limit \(\lim_{t\downarrow0}6(Q_\epsilon(t;q)-q)/t^3=\epsilon Hq\) and says this limit does not assume a continuous third derivative. That is the exact cubic response; it is not a claim that \(Q'''(0)\) exists classically.

The one-kick paragraph records \(\int_0^t u^2/2\,du=t^3/6\) and the factor \(|\alpha|\le2\), and separates the term \(\alpha i Hq\,t^2/2\) from the upper bound \((418+181R+21R^2)t^3\). The \(n\ge3\) weights are given as at most \(4\) and \(6\), including \(|\alpha|\). The sample size uses \(\ln\). The path inequality with \(C_R t^4/4\) remains an upper bound, distinct from the limit. No sign error remains in the rewritten justification.
