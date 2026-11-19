---
title: "A cubic short-time law for guided positions in finite-width gravitational collapse"
author: "Daniel Fredriksen"
date: "Quantyra Inc., Las Vegas, Nevada, USA"
lang: en
papersize: a4
fontsize: 10.5pt
margin:
  x: 26mm
  y: 23mm
---

**Abstract.** In Laloë’s gravitational collapse model, the actual position sources a potential that acts back on the wave. We consider one trapped mass, a Gaussian source of fixed positive width, and the same real gravitational interaction with and without the imaginary coupling. For a bare harmonic ground state and static incoming source history, the force at the initially occupied position vanishes. The next derivative produces an outward displacement proportional to the imaginary coupling and to the cube of time. We derive the coefficient for a two-sided position threshold by transporting the initial configuration distribution. A bound for the full retarded potential controls the trajectory remainder and the probability of the unresolved tail. One parameter choice gives a positive conditional change in the threshold probability, although achieving 5% error with that bit at that time would require more than $6.94\\times10^{79}$ independent final-time observations.

## Introduction

Laloë proposed that actual Bohmian positions source a gravitational potential with a small imaginary coupling [1]. His analysis of dilute systems distinguishes the probability fluid of each wave from the distribution of positions across preparations [2]. That distinction raises a quantitative question. If two versions of the model share their preparation, real gravitational field and readout, how early can the imaginary coupling change an actual position statistic?

Here a single mass starts in the ground state of its bare trap. We find a signed coefficient for the probability of a position outside a prescribed interval. The choice of a Gaussian source is Laloë’s positive-width option [1, Eq. (4)]. The related point-source analysis [3] concerns regular phase guidance at a singular source; its flux obstruction does not apply here. Stochastic localization theories also predict changes in position spread, including cubic growth from momentum diffusion [4]. In the present construction the source follows a deterministic guidance equation on each run. The change of the threshold probability is computed from that equation and a specified ensemble of initial positions.

## Model, preparation, and event

Fix one axis through the trap center. Count the bit $1_{\{|Q_1|>\sigma_0\}}$, where $Q$ is the **actual** position and $\sigma_0=\ell/\sqrt2$, $\ell=\sqrt{\hbar/(m\omega)}$. Use a fresh preparation per recorded time. The mass is the material pointer. Terminal sensing is specified below as a readout channel. Start from the real three-dimensional *bare harmonic* ground state with the initial equilibrium distribution. This is an input at time zero. The ground state of the bare trap is not a stationary wave of the always-on self-field. Common constant incoming source paths $Q(s)=q$, $s\le0$, specify retarded boundary data conditional on the initial draw $q$. Holding a hidden particle at a measured position is not a control in this construction. A physical reset achieving these joint data would require evidence.

We use the positive-width, all-pairs reading of Laloë's equations including the single self term. Use the same parameters and incoming history in the two model predictions. Only the imaginary coupling changes from zero to $10^{-3}$. The control retains the entire real gravitational interaction. Retard both parts according to Eq. (23). [Original model, Eqs. (2), (4), (5), (10)–(14), (23), (24)](https://arxiv.org/html/1905.12047v4) · [Wave density versus actual configuration measure, §4](https://doi.org/10.5802/crphys.104)

Choose $a=\ell$ and $\lambda=Gm^2/(\hbar\omega\ell)=1$. All following positions and times are in units of $\ell$ and $1/\omega$ unless labeled otherwise. The wave initially equals $g(x)=\pi^{-3/4}e^{-|x|^2/2}$; $q$ has density $g^2$. Write $s=1/\sqrt2$. For $0\le\epsilon\le10^{-3}$, write $\alpha=i+\epsilon$,
$$
  \partial_t\psi=-iH_{\rm osc}\psi+\alpha K[Q]\psi,\qquad
  \dot Q=\Im(\nabla\psi/\psi)(Q),\qquad H_{\rm osc}=(-\Delta+|x|^2)/2.
$$
Time-dependent scalar normalization has no spatial gradient. The static kernel is $K(x-q)=\operatorname{erf}(|x-q|)/|x-q|$ with $D^2K(0)=-H I,\quad\ H=4/(3\sqrt\pi)$. We retain the whole kernel. No small excursion relative to the smearing width is required.

## Short-time law

**Proposition 1 (guided-position response).** For the centered Gaussian preparation and static incoming histories, each fixed initial point has the following right-hand response. At zero time the phase is constant and the trap force cancels the quantum-potential force from $g$. The static self-field has zero gradient at $q$. Thus $\dot Q(0)=\ddot Q(0)=0$. For the wave amplitude $A$, at zero time $\dot A/A=\epsilon K+\text{scalar}$. The phase acceleration equation contains the quantum potential $-\Delta A/(2A)$. Its time derivative contributes $\epsilon\nabla(\Delta K+2\nabla\log g\cdot\nabla K)/2$ to the jerk. At $q$, $\nabla\Delta K(0)=\nabla K(0)=0$ and $\nabla\log g(q)=-q$. The initially static retarded field has zero first time derivative. Consequently
$$
  Q'''_\epsilon(0;q)=\epsilon H q,\qquad Q'''_0(0;q)=0 .
$$
**Theorem 2 (threshold probability).** For the given initial law and each fixed positive imaginary coupling in the range studied, the following expansion holds as time tends to zero from above, for any measurable assignment of bits on the unresolved tail. The signed displacement grows outwards on both sides of the detector. Applying this dilation to the *initial configuration law* gives the difference of ideal probabilities
$$
 P_\epsilon(t)-P_0(t)
 =2\phi(1)\frac{\epsilon H}{6}t^3+o(t^3),
 \quad \phi(1)=\frac{e^{-1/2}}{\sqrt{2\pi}} .
$$
The initial probability is $\operatorname{erfc}(1/\sqrt2)=0.31731050786\ldots$. The argument below justifies threshold differentiation, including tails, and supplies an explicit finite time. The dimensionful dilation coefficient multiplying $\epsilon T^3/6$ is $4Gm\omega/(3\sqrt{\pi}a^3)$, as follows by restoring units. At fixed positive coupling the ideal probability increase has a definite sign. Only the local curvature of the smooth source enters its leading coefficient.

## A finite-time bound for the full kernel including retardation

For $R\ge1$, $0<t\le 10^{-3}$, $(R+1)t\le0.01$, the following conservative path estimate holds for $|q|\le R$ in either arm:
$$
 \left|Q(t;q)-q-\frac{\epsilon Ht^3}{6}q\right|
 \le \tfrac14 C_R t^4,\qquad C_R=10^4(1+R)^2.
$$

**Field and wave representation.** Use the positive radial Fourier measure $d\mu=(2/\pi)e^{-k^2/4}dk\,d\Omega/(4\pi)$, $k=|\mathbf k|$, for $K$. With $\nu=c/(\omega\ell)$, the Fourier multiplier relative to this measure in the retarded solution is
$$
 B(t)=z(0)+\nu k\int_0^t\sin(\nu k(t-v))[z(v)-z(0)]\,dv
     =z(t)-\int_0^t\cos(\nu k(t-v))z'(v)\,dv,\quad z(v)=e^{-i\mathbf k\cdot Q(v)} .
$$
This follows from the spherical angular integral of the retarded Gaussian source, or the forced wave equation initialized with its static field and zero field velocity. In particular $|B-z(0)|\le 2k L_t$, $L_t=\int_0^t|\dot Q|\,dv$, uniformly in the light speed. This bounds the complete change from the frozen field, including the effect of retardation. It does not replace the delayed kernel with an instantaneous one.

Divide the unnormalized wave by the freely propagated ground state $e^{-3it/2}g(x)$, calling the ratio $F$. Expand the interaction by Duhamel in ordered Fourier kicks $\exp(i\mathbf k_j\cdot x)$. A product of harmonic evolutions and such kicks is a coherent state. Relative to the ground state its spatial factor is
$$
 f=\exp[(D+iP)\cdot x-|D|^2/2-iD\cdot P/2+i\theta],\quad
 D=\sum_j\mathbf k_j\sin u_j,\quad P=\sum_j\mathbf k_j\cos u_j,
$$
where $u_j=t-t_j$. The Weyl product phase $\theta$ is a signed sum of half the pairwise dot products times $\sin(u_i-u_j)$. These formulas follow from $e^{i(Px-Dp)}g=e^{iP(x-D/2)}g(x-D)$ and harmonic rotation. With $S=\sum k_j$, $|f|\le e^{|x|tS}$, $|D+iP|\le S$ in Euclidean norm. The $j$-th spatial derivative through order two adds at most a factor $S^j$. The product also carries $\alpha^n\prod B_j$; the time simplex has volume $t^n/n!$. These bounds ensure absolute local convergence and legitimate spatial differentiation. For clarity, the field phases are part of the integrals and do not reweight initial configurations.

For tilted moments $M_j=\int k^je^{0.01k}d\mu$, use $0.01k\le k^2/8+0.0002$, giving upper bounds $2,3,7,21,80,330$ for $j=0,\ldots,5$. Bootstrap $L_t\le1$. The weighted field moments up to order two are bounded by $8,17,49$. On $|x|\le R+1$, summing the simplex bounds with $|\alpha|\le2$ gives
$$
 |F-1|\le e^{16t}-1\le17t,\quad
 |\nabla F|\le34te^{16t}\le35t,\quad
 \|D^2F\|\le(98t+(34t)^2)e^{16t}\le 105t.
$$
Thus the wave is node-free in the tube and the guidance law yields $L_t\le20t^2$, closing the bootstrap. For local existence and uniqueness use the sine integral for $B$: on a bounded interval differences for two continuous paths with the same start are bounded by $\nu k^2 t\sup|Q-\widetilde Q|$. The Gaussian moment bounds and convergent Duhamel series give a locally Lipschitz velocity functional in the path supremum norm wherever $F$ is bounded away from zero, also Lipschitz in its evaluation point. Picard iteration of the integral guidance equation then works on a sufficiently short interval for each finite $\nu$; the a priori tube and speed estimates continue it to $t$ for every retained $q$. This existence argument need not be uniform in $\nu$ to obtain the uniform error bound.

**Explicit remainder.** First evaluate the frozen-field gradient at $x=q$. For one kick write $L=\sin u+i\cos u$ and $Z=(L-i)\mathbf k\cdot q-(\sin u)L k^2/2$. Its gradient integrand is $L\mathbf k e^Z$. The zeroth integral vanishes by parity. The first derivative integrates to $iHq$ since $\int\mathbf k\mathbf k^T d\mu=H I$. The second derivative is dominated after integration by
$$
 M_1+3R M_2+(4+R^2)M_3+2RM_4+M_5
 \le 418+181R+21R^2 .
$$
Indeed $|Z'|\le Rk+k^2,\ |Z''|\le Rk+2k^2$. Integrating the Taylor estimate in the kick time and multiplying by $\alpha$ gives the one-kick term $\alpha iHq\,t^2/2$ with error at most $(418+181R+21R^2)t^3$.

For two frozen kicks the integrated gradient at both ages zero vanishes by parity. Scale both ages by $v\in[0,1]$. The derivative of the gradient integrand in $v$ has absolute value at most $t e^{RtS}(S+R S^2+3S^3)$. This uses the preceding Weyl phase, $|\partial_v(D+iP)|\le tS$, and the product rule; the frozen source factors are constant in $v$. The two-measure moments of $S,S^2,S^3$ are at most $12,46,210$. Thus this term costs at most $(1284+92R)t^3$. All frozen terms with at least three kicks cost at most $6t(e^{4t}-1-4t)\le50t^3$.

For the full retarded field, replace each Fourier factor in turn. A marked difference costs at most $40 k t^2$ because $L_t\le20t^2$. Remaining factors have moments $8,17$. Summing the marked terms bounds the gradient difference at $q$ by
$$
 e^{16t}\{(2t)40t^2 M_2+(2t)^2 40t^2 M_1\,17\}<600t^3 .
$$
Here the gradient can land on the marked kick or on any other kick. Evaluating at $Q(t)$ instead of $q$ costs at most $105t\,20t^2$. Finally divide by $F(Q,t)$; $|F|\ge1-17t$ and the leading gradient has magnitude at most $Rt^2$. Taking the imaginary part gives $|\dot Q-\epsilon Hq\,t^2/2|\le C_R t^3$. Integration proves the path estimate. The bound treats the real field's entire fourth-order displacement in the control as a source of uncertainty.

**Threshold crossing.** For $|q|>R$ charge the full probability $b_R=\operatorname{erfc}(R)+2R e^{-R^2}/\sqrt\pi$ in each arm. No sample is discarded or renormalized. An unresolved path or a missing readout in that tail may be scored either way in the enclosure. Existence for all unbounded initial configurations is not needed for these worst-case bounds; a theorem of global dynamics is not claimed. On the retained ball, the path estimate couples the actual and dilated coordinates with distance at most $\delta=C_Rt^4/4$. Each of the two threshold bands has length $2\delta$; the ideal dilated marginal density is bounded by $1/\sqrt\pi$ for $\epsilon\ge0$. The event error per arm is at most $e_R=4\delta/\sqrt\pi+b_R$. For the asymptotic formula take $R=\sqrt{6\log(1/t)}$; then both $e_R=o(t^3)$ and $(R+1)t<0.01$ eventually. The ensemble differentiation therefore does not rely on Taylor expansion at just one starting position.

## One admissible model time and a calibrated record

Take $t=10^{-12}$, $R=16$. The per-arm error $e_R<1.64\,10^{-42}$ contains the higher order terms, the entire delayed-field bound and the tail (the latter is below $2\,10^{-110}$). One parameter choice in SI units is $\omega=10^{-3}\,\mathrm{s}^{-1}$, $m=(\hbar^3\omega/G^2)^{1/5}\simeq1.21\,10^{-17}\,\mathrm{kg}$, $a=\ell\simeq9.32\,10^{-8}\,\mathrm m$, $T=t/\omega=1\,\mathrm{ns}$. The characteristic speed $\omega\ell\simeq9.3\,10^{-11}\,\mathrm{m/s}$ and bare preparation energy $3\hbar\omega/2\simeq1.58\,10^{-37}\,\mathrm J$ are nonrelativistic. These specify one effective single mass and one allowed width in the hypothetical law. Treating a real composite object as that source, selecting the universal width, realizing the reset and cooling the mass are additional physical assumptions. [Constants, NIST](https://www.physics.nist.gov/cuu/pdf/wall_2022.pdf)

We allow nonzero common preparation and readout errors. In successful preparations translate the trap and the ground state together by an independent offset up to $0.01\ell$ on the chosen axis, with the same translation of the source prehistory. Translation covariance makes this an exact bound. A terminal sensor returns the threshold bit after independent additive position noise bounded by $0.01\ell$; its distribution can be unknown but must be stationary across measurement times. This is an explicit terminal response contract, not a derivation of a detector interaction or a laboratory calibration. The threshold is fixed at its original nominal value. Combining these offsets gives $|z|\le0.02$ in oscillator units. For $D=1+\epsilon Ht^3/6$, the ideal crossing probability is $g_z(D)=\Pr(|Dq_1+z|>s)$, and
$$
 g'_z(D)=
 \frac{(s-z)e^{-(s-z)^2/D^2}+(s+z)e^{-(s+z)^2/D^2}}{\sqrt\pi D^2}.
$$
For $|z|\le0.02,\ 1\le D\le1.000001$ it lies between $0.45$ and $0.52$. Average over the common offset distribution. At the chosen time $D-1=1.25375\ldots\,10^{-40}$ for the collapse arm. Without offsets the leading difference in bit probability is $6.06744\ldots\,10^{-41}$.

The preparation budget can also include continuous deviations from a static incoming history. Let the incoming source, stationary before some past time, have total path length at most $\eta=10^{-20}$ in oscillator units before reaching $q$. Extend the integration-by-parts formula for $B$ over that prehistory. It adds at most $k\eta$ to $|B-z(0)|$, at every positive time. Bootstrap $L_t\le1/2$; $2L_t+\eta<2$, so the same moments and $L_t\le20t^2$ apply. In the marked-kick estimate this adds $e^{16t}(2t M_2+4t^2 M_1\,17)\eta$ to the gradient bound. After division by $1-17t$ this costs at most $16\eta t$ in velocity and $8\eta t^2$ in position. Hence at the selected time charge $e_*=e_R+32\eta t^2/\sqrt\pi<1.82\,10^{-42}$ per arm for the combined motion, history and threshold bound. This is a finite variation tolerance; it is not inferred from ground-state cooling.

Use fresh, interleaved preparations at zero time and $T$. The observable is the change in event frequency from baseline; the coupling $\epsilon$ is a model parameter, not a laboratory switch. The time-zero reference eliminates the unknown static offset baseline even if each model fits a different stationary noise distribution. The zero-coupling increment has magnitude at most $e_*$; the collapse increment is at least $0.45(D-1)-e_*$. As an additional explicit budget, allow probability $10^{-43}$ per preparation for unrestricted failures of the wave, initial configuration law or incoming history, and $10^{-43}$ per terminal record for an arbitrary sensor failure. For scale, an ordinary 3D harmonic Gibbs preparation would have excited probability $1-(1-e^{-\hbar\omega/(k_BT_{\rm bath})})^3$. The sufficient bound $3 e^{-\hbar\omega/(k_BT_{\rm bath})}\le10^{-43}$ requires about $7.6\,10^{-17}$ K or colder at this trap frequency. This prices only that particular preparation method. These bounds can be phrased as a coupling to the specified input and response except on the charged probability. Score every failure, with worst-case bits. This adds $4\,10^{-43}$ to each model's increment uncertainty. The lower separation of the two allowed increment intervals exceeds $5.0\,10^{-41}$. Higher-order, retardation and counting errors have separate scope from these assumed preparation and detector contracts. The very small unrestricted failure budget is a sufficient assumption, not a measured error rate, and excludes uncontrolled time-dependent drift.

For two independent groups of $n$ Bernoulli records each, a midpoint decision between separated increment intervals has error at most $4\exp[-n\Delta^2/8]$, by applying Hoeffding at $\Delta/4$ per group. With $\Delta=5\,10^{-41}$ and target error 5%, $n=\lceil8\log(80)/\Delta^2\rceil$, about $1.40\,10^{82}$ fresh preparations **per time**, about $2.80\,10^{82}$ in total. This is a sufficient allocation at the chosen time. There is also a necessary lower bound for this particular bit readout. Restrict to the ideal pair of simple hypotheses with zero offsets, static history and matched preparations. The two probabilities at $T$ differ by at most $0.52(D-1)+2e_R<7\,10^{-41}$, and $p_0(1-p_0)>0.21$. The zero-time records have identical law. The Bernoulli relative entropy is at most $(p_\epsilon-p_0)^2/[p_0(1-p_0)]$ by the log inequality. Additivity and Pinsker bound the TV of the complete records by $\sqrt{n(7\,10^{-41})^2/(2\cdot0.21)}$. Error at most 5% under each hypothesis needs TV at least 0.9, hence over $6.94\,10^{79}$ independent final-time reads even with perfectly known calibration. The bound does not concern other times, observables or collective measurements.

## Practical obstruction and decision

The specified matched initial data yield a positive short-time effect in the full smoothed self-interaction, with a conditional finite-time prediction for the record. A physical measurement also requires bounds on variation in preparation and detector threshold between the two measurement times. For example, a threshold half-width drift changes the time-zero tail with derivative $-2e^{-1/2}/\sqrt\pi\simeq-0.6844$ per oscillator length. An inward change of order $9\,10^{-41}\ell$ can mimic the entire nominal increase, about $8\,10^{-48}$ m at this fixture. Equivalently a time-dependent false-positive probability of order $10^{-40}$ on otherwise zero bits can mimic it. A stationary error law can cancel in the baseline comparison, but an unrestricted differential error of this size can erase identifiability. Realizing the matched reset and maintaining that degree of differential calibration are open experimental questions. The lower bound applies to independent readings of this bit at the chosen time. It leaves other observables and later observation times open.

## Declarations

The author funded this work personally and declares no competing interests. Correspondence: dfredriksen@quantyra.org. ORCID: [0009-0002-9123-7435](https://orcid.org/0009-0002-9123-7435). AI tools assisted in drafting, checking and reviewing the analysis. The author is responsible for the manuscript. Source, reproducing code, review dispositions and certification plan are available in the [public repository](https://github.com/Quantyra/laloe-cubic-position-law).

## References

[1] F. Laloë, “A model of quantum collapse induced by gravity,” *European Physical Journal D* **74**, 25 (2020). [DOI](https://doi.org/10.1140/epjd/e2019-100434-1).

[2] F. Laloë, “Gravitational quantum collapse in dilute systems,” *Comptes Rendus Physique* (2022). [DOI](https://doi.org/10.5802/crphys.104).

[3] D. Fredriksen, “A flux obstruction for the all-pairs point source in Laloë’s collapse equations,” preprint (2026). [DOI](https://doi.org/10.5281/zenodo.24349801).

[4] M. Bilardello, S. Donadi, A. Vinante and A. Bassi, “Bounds on collapse models from cold-atom experiments,” *Physica A* **462** (2016). [Author version](https://arxiv.org/abs/1605.01891).
