# Antigravity (AGY) manuscript review

AI-generated referee reports. See the [editorial disposition](disposition.md) for the author-side checks and corrections.

## First manuscript

Supplied manuscript SHA-256: `7d2e3aaf18b4f0f45f96ae39edb9f8db3d90347d5b79baab24f6360177d81c63`.

### Referee Report

**Manuscript Title:** A cubic short-time law for guided positions in finite-width gravitational collapse
**Author:** Daniel Fredriksen
**Source SHA256:** `7d2e3aaf18b4f0f45f96ae39edb9f8db3d90347d5b79baab24f6360177d81c63`
**Verdict for Release:** **Revise** (Acceptable for public preprint release after minor revisions addressing sign clarity, conceptual attribution, and diffusion comparisons).

---

### 1. Source-Access Limits
This evaluation is based exclusively on the supplied manuscript text. External repository contents (`github.com/Quantyra/laloe-cubic-position-law`) and unpublished preprint citations (Ref. [3]) were not accessed, fetched, or computationally verified.

---

### 2. Physical Source Interpretation, Novelty, and Editorial Significance
The manuscript investigates short-time Bohmian trajectories in Laloë’s gravitational collapse framework equipped with a Gaussian-smeared kernel and complex coupling $\alpha = i + \epsilon$.

* **Novelty:** The short-time asymptotic calculation demonstrating an initial jerk $Q'''(0) = \epsilon H q$ and a cubic displacement $\Delta Q \propto \epsilon t^3$ is mathematically sound and novel. The uniform control over the full retarded field using a Duhamel expansion in ordered Fourier kicks provides rigorous analytical backing.
* **Editorial Significance:** High for the foundational and mathematical physics community. Rather than promoting an experimental test, the paper provides a devastatingly candid reality check: detecting this cubic shift against baseline drift at $1\,\mathrm{ns}$ requires over $10^{79}$ independent measurements and sub-$10^{-47}\,\mathrm{m}$ detector threshold stability. This cleanly reframes the effect as an in-principle property of the model rather than a viable laboratory protocol.

---

### 3. Evaluation of Model, Mechanics, and Limits

#### A. Attribution to Laloë vs. Author’s Additions
* Laloë’s collapse model (EPJD 2020; *C. R. Physique* 2022) primarily focuses on dilute, multi-particle systems to describe macroscopic localization without self-energy pathologies.
* Applying this dynamics to a *single trapped particle sourcing its own collapse potential* ("all-pairs reading... including the single self term") is the author’s own idealization. While mathematically consistent with the smoothed kernel, single-particle gravitational self-action is not a standard feature of Laloë's physical program and must be clearly signposted as an authorial extension.

#### B. Actual Configurations vs. Wave Densities
The distinction is maintained cleanly throughout: the potential is sourced by the Bohmian coordinate $Q(t)$, avoiding the non-linear semiclassical pathology of Schrödinger–Newton equations ($|\psi|^2$ sourcing). Ensemble statistics are correctly obtained by averaging over the initial Born-rule measure $g^2(q)$.

#### C. Operational Sense of Histories and Readout
* **Histories:** Specifying static incoming boundary conditions $Q(s) = q$ for $s \le 0$ serves as Cauchy data for the retarded D'Alembertian, but physically preparing a hidden Bohmian variable at rest contradicts standard quantum control. The author notes this, but it should be explicitly stated as a formal mathematical boundary condition.
* **Readout:** The binary threshold observable $1_{\{|Q_1| > \sigma_0\}}$ assumes ideal readout of the Bohmian coordinate at time $T$. The manuscript would benefit from acknowledging that measuring Bohmian positions directly is an idealized operational surrogate for a fast terminal detector coupling.

#### D. Comparison with Known Diffusion Results
The manuscript mentions cubic growth from momentum diffusion in continuous collapse models (CSL, Diósi–Penrose; Ref. [4]). However, in CSL/DP, the cubic dependence appears in the *position variance* ($\langle \Delta x^2 \rangle \sim D t^3$) via stochastic momentum diffusion. Here, the cubic displacement $\Delta Q \propto \epsilon t^3 q$ is a *deterministic trajectory dilation* arising from the back-reaction on the phase gradient through the time-dependent quantum potential. This fundamental distinction between deterministic trajectory jerk and stochastic momentum diffusion should be highlighted.

---

### 4. Equation-Level Checks, Errors, and Clarity

* **Proposition 1 Sign Description (Clarity / Minor Severity):**
  In the text preceding Proposition 1, the author writes:
  $$\text{"The phase acceleration equation contains the quantum potential } -\Delta A/(2A)\text{. Its time derivative contributes } \epsilon\nabla(\Delta K+2\nabla\log g\cdot\nabla K)/2 \text{ to the jerk."}$$
  In the Bohmian Hamilton–Jacobi equation ($\partial_t S + \frac{1}{2}(\nabla S)^2 + V + Q_{\rm Bohm} = 0$ with $Q_{\rm Bohm} = -\frac{\Delta A}{2A}$), $\partial_t S$ enters with $+ \frac{\Delta A}{2A}$. While the resulting formula and subsequent signs ($Q''' = +\epsilon H q$) are correct, referring to $-\Delta A/(2A)$ in the sentence introducing a positive derivative contribution creates unnecessary sign ambiguity.

---

### 5. Requested Changes

1. **[Clarity – Minor]** In Proposition 1, harmonize the definition of $Q_{\rm Bohm}$ with its $+ \Delta A/(2A)$ contribution to $\partial_t S$ to eliminate apparent sign discrepancies.
2. **[Clarity – Moderate]** In the Introduction, explicitly contrast the deterministic trajectory dilation derived here with the stochastic momentum diffusion variance ($\langle x^2 \rangle \sim t^3$) found in CSL/DP models.
3. **[Limits & Scope – Moderate]** Explicitly state in Section 2 that single-particle self-collapse and static prehistories ($Q(s)=q, s \le 0$) are formal Cauchy specifications of this paper rather than operational features of Laloë's dilute-system theory.

## Revised manuscript

Supplied manuscript SHA-256: `f657e70abb1b6c19be5bac9e12fc05c2baaea2207562f360d2762b0fec2d899f`.

### Referee Report (Second Review)

**Manuscript Title:** A cubic short-time law for guided positions in finite-width gravitational collapse
**Author:** Daniel Fredriksen
**Source SHA256:** `f657e70abb1b6c19be5bac9e12fc05c2baaea2207562f360d2762b0fec2d899f`
**Verdict for Release:** **Ready** (Acceptable for public preprint release without further revisions).

---

### 1. Source-Access Limits
This evaluation is based strictly on the revised manuscript text supplied. External repository contents (`github.com/Quantyra/laloe-cubic-position-law`) and unpublished preprint citations (Ref. [3]) were not accessed, fetched, or computationally verified.

---

### 2. Physical Source Interpretation, Novelty, and Editorial Significance
The manuscript analyzes short-time Bohmian trajectories in Laloë’s gravitational collapse framework equipped with a Gaussian-smoothed kernel and complex coupling $\alpha = i + \epsilon$.
* **Novelty:** The short-time asymptotic expansion establishing an initial outward jerk $Q'''(0) = \epsilon H q$ and deterministic cubic displacement $\Delta Q = \frac{1}{6}\epsilon H q t^3$, controlled uniformly against retarded field back-reaction via a Duhamel expansion in ordered Fourier kicks, is mathematically rigorous and novel.
* **Editorial Significance:** High for the foundations and mathematical physics communities. The paper couples rigorous analytical control of the retarded non-linear guidance law with a transparent operational reality check: resolving the resulting threshold probability increment ($\Delta P \sim 6 \times 10^{-41}$) requires $> 6.94 \times 10^{79}$ independent terminal measurements and detector threshold stability exceeding $8 \times 10^{-48}\,\mathrm{m}$. This reframes the cubic displacement as an in-principle structural property of the model rather than a viable laboratory protocol.

---

### 3. Verification of Addressed Concerns

1. **Sign Harmonization in Proposition 1 (Previous Severity: Minor Clarity):**
   *Addressed.* The text preceding Proposition 1 now defines the quantum force as $-\nabla U_{\mathrm{B}}$ with $U_{\mathrm{B}} = -\Delta A / (2A)$, noting that differentiating this force formally gives $+\frac{1}{2}\epsilon\nabla(\Delta K + 2\nabla\log g\cdot\nabla K)$. This removes the earlier apparent sign discrepancy and connects directly to the positive outward jerk coefficient $+\epsilon H q$.

2. **Contrast with Stochastic Diffusion (Previous Severity: Moderate Clarity):**
   *Addressed.* The Introduction now explicitly distinguishes continuous collapse models (CSL, Diósi–Penrose), where momentum diffusion manifests as cubic growth in the *position variance* ($\langle \Delta x^2 \rangle \sim D t^3$), from the present mechanism, where the cubic shift is a *deterministic trajectory dilation* $\Delta Q \propto \epsilon t^3 q$ caused by the back-reaction of the imaginary coupling on the quantum potential.

3. **Laloë Attribution, Configurations, and Operational Limits (Previous Severity: Moderate Limits & Scope):**
   *Addressed.* Section 2 clearly delineates Laloë’s dilute-gas framework from the author's single-particle self-collapse idealization. The author explicitly identifies the static incoming history ($Q(s) = q$ for $s \le 0$) and bare ground-state reset as formal Cauchy data chosen for analytical tractability rather than physical features of Laloë's program or operational laboratory preparations.

4. **Configurations, Readout, and Calibration:**
   The distinction between actual Bohmian positions $Q(t)$ and wave densities $|\psi|^2$ is maintained rigorously throughout. The readout model treats terminal sensing as an explicit contract with bounded stationary noise ($|z| \le 0.02\ell$), while the calibration analysis demonstrates that an unmodeled differential threshold drift of $9 \times 10^{-41}\ell$ ($\approx 8 \times 10^{-48}\,\mathrm{m}$) would completely mimic the collapse signal.

---

### 4. Equation-Level Checks and New Issues

* **Proposition 1 & Kernel Curvature:** The contraction $\int \mathbf{k}\mathbf{k}^T d\mu = H I$ with $H = 4/(3\sqrt{\pi})$ combined with $\nabla\log g(q) = -q$ correctly gives $\lim_{t\downarrow0} 6(Q_\epsilon - q)/t^3 = \epsilon H q$.
* **Theorem 2 & Probability Derivative:** The marginal crossing derivative $g'_0(1) = 2\phi(1) = 2e^{-1/2}/\sqrt{2\pi}$ is exact for the standard harmonic ground state with threshold $\sigma_0 = 1/\sqrt{2}$. Tail bounds ($b_R = \operatorname{erfc}(R) + 2R e^{-R^2}/\sqrt{\pi}$) and the error envelope ($e_R < 1.64\times 10^{-42}$) are mathematically sound.
* **Information Bounds:** The required sample sizes ($n \approx 1.40 \times 10^{82}$ via Hoeffding; lower bound $> 6.94 \times 10^{79}$ via Pinsker’s inequality with $TV \ge 0.9$ and baseline variance $p_0(1-p_0) > 0.21$) are verified.
* **New Issues:** No new mathematical errors, ambiguities, or unsupported claims were introduced in the revision.

---

### 5. Final Recommendation
**Ready for Release.** The revisions fully resolve all previous concerns regarding sign clarity, physical attribution, operational limits, and diffusion comparisons. The manuscript is mathematically rigorous, physically candid about its idealizations, and well suited for public preprint release.

## Final targeted check

Supplied manuscript SHA-256: `1465fb59834c7f0cbaeb4b95bc0f50c2d45557a6356296a2348767da30979e76`.

**Verdict: Ready for public preprint release.**

The author has satisfactorily resolved all three referee concerns from the initial report:

1. **Sign and Potential Clarity:** Proposition 1 harmonizes the definition of the quantum potential $U_{\mathrm{B}} = -\Delta A/(2A)$ with its force contribution $-\nabla U_{\mathrm{B}} = +\nabla(\Delta A/(2A))$, eliminating the earlier sign ambiguity in the phase evolution equation.
2. **Diffusion Distinction:** The Introduction now explicitly contrasts continuous collapse models (CSL/DP)—where cubic growth appears in the stochastic position variance ($\langle \Delta x^2 \rangle \sim t^3$) via momentum diffusion—with the deterministic trajectory dilation ($\Delta Q \propto \epsilon t^3 q$) derived here.
3. **Cauchy Data and Attribution:** Section 2 explicitly signposts single-particle self-collapse and static incoming histories ($Q(s) = q, s \le 0$) as authorial Cauchy specifications rather than standard features of Laloë’s dilute-system framework.

The mathematical treatment carefully separates exact tensor moments (e.g., $\int \mathbf{k}\mathbf{k}^T d\mu = H I$) from explicit numerical upper bounds on the tilted Fourier moments ($M_j$). Furthermore, Proposition 1 rigorously formulates the initial jerk as an asymptotic cubic right-limit ($\lim_{t\downarrow0} 6(Q_\epsilon - q)/t^3 = \epsilon H q$) rather than postulating a classical $C^3$ third time derivative at $t=0$.

No material defects remain; the manuscript is mathematically sound.
