# A cubic short-time law for guided positions in finite-width gravitational collapse

Daniel Fredriksen · Quantyra Inc. · [ORCID](https://orcid.org/0009-0002-9123-7435)

This preprint studies the probability of finding a guided mass farther than one initial standard deviation from the center of a harmonic trap. The finite-width gravitational collapse term drives an outward shift at third order in time. The proof treats the full retarded kernel. The finite-time example is conditional on the preparation history and terminal position readout.

[Manuscript](manuscript.pdf) · [Editable source](manuscript.md) · [Numerical audit](verify.py) · [Three-lens review](review/disposition.md) · [Lean certification plan](lean-certification-plan.md)

## Reproduce the files

From the repository root, use Python 3 and the following commands. The PDF build uses Pandoc 3.9 (included in the listed wheel), Typst 0.15.2 and a fixed document timestamp. Installed fonts can affect pagination.

```sh
python -m pip install pypandoc_binary==1.17 typst==0.15.2 python-flint==0.9.0
python build.py
python verify.py
```

The verifier uses 256-bit Arb balls to check the constants in the analytic remainder, the conditional probability separation, and the lower and upper repetition counts. The manuscript supplies the dynamical and probability proofs. The Lean plan identifies separate targets for their formal verification.

The related [point-source Comment](https://doi.org/10.5281/zenodo.24349801) concerns a singular source. This work uses a positive source width throughout. Manuscript and supporting files are licensed under [CC BY 4.0](LICENSE).
