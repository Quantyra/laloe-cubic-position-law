"""Interval audit for the finite-width cubic position law. Requires python-flint 0.9.0."""

from flint import arb, ctx

ctx.prec = 256
pi = arb.pi()
one = arb(1)
eps = one / 1000
sqrt_pi = pi.sqrt()
max_time = one / 1000
time = arb("1e-12")
radius = arb(16)
cut = one / arb(2).sqrt()


def check(test, description):
    if not test:
        raise ArithmeticError(description)


def gaussian_tail(r):
    return r.erfc() + 2 * r * (-r**2).exp() / sqrt_pi


def main():
    # The full smeared kernel is a Gaussian mixture of plane waves. Check the
    # moment majorants used for every order, including the tilted remainder.
    moments = [2, 3, 7, 21, 80, 330]
    for j, bound in enumerate(moments):
        exponent = arb(j + 1) / 2
        value = arb("0.0002").exp() * arb(8)**exponent * exponent.gamma() / pi
        check(value < bound, f"tilted radial moment {j}")

    # Compare the radial Fourier second moment with the Hessian of erf(r)/r.
    hessian = 4 / (3 * sqrt_pi)
    radial_second = (2 / pi) * 4 * (arb(3) / 2).gamma()
    check((radial_second / 3 - hessian).contains(0), "kernel curvature")

    m0, m1, m2, m3, m4, m5 = moments
    one_kick = (m1 + 4 * m3 + m5, 3 * m2 + 2 * m4, m3)
    check(all(x <= y for x, y in zip(one_kick, (418, 181, 21))),
          "one-kick second derivative coefficients in the retained radius")
    pair_moments = (2*m0*m1, 2*m0*m2 + 2*m1**2, 2*m0*m3 + 6*m1*m2)
    check(pair_moments == (12, 46, 210), "product-measure moment bounds")
    check(2*(pair_moments[0] + 3*pair_moments[2]) <= 1284
          and 2*pair_moments[1] <= 92, "two-kick remainder coefficients")

    exp_majorant = (16 * max_time).exp()
    min_wave = 1 - 17 * max_time
    check(exp_majorant - 1 < 17 * max_time, "wave denominator")
    check(34 * exp_majorant < 35, "gradient")
    check((98 + 34**2 * max_time) * exp_majorant < 105, "Hessian")
    check(35 / min_wave < 40, "path speed / time")
    check(6 * ((4 * max_time).exp() - 1 - 4 * max_time) / max_time**2 < 50,
          "three and higher frozen kicks")
    check(exp_majorant * (80 * moments[2] + 160 * max_time * moments[1] * 17) < 600,
          "moving and delayed field correction")
    history_speed = exp_majorant * (2 * moments[2] + 4 * max_time * moments[1] * 17) / min_wave
    check(history_speed < 16, "bounded incoming-history variation")
    # Coefficientwise bound after division by F. Also covers all R >= 1.
    raw_constant = 418 + 1284 + 50 + 600 + 105 * 20
    for raw, budget in zip((raw_constant, 181 + 92 + 17, 21), (10000, 20000, 10000)):
        check(raw / min_wave < budget, "final logarithmic gradient remainder")

    dilation = eps * hessian * time**3 / 6
    delta = 10000 * (1 + radius)**2 * time**4 / 4
    tail = gaussian_tail(radius)
    threshold_error = 4 * delta / sqrt_pi + tail
    prepared_error = threshold_error + 32 * arb("1e-20") * time**2 / sqrt_pi
    check(tail < arb("2e-110"), "tail including arbitrary outcomes")
    check(threshold_error < arb("1.64e-42"), "per-arm threshold error")
    check(prepared_error < arb("1.82e-42"), "per-arm threshold and prehistory error")

    offset = arb("0.02")
    max_dilation = arb("1.000001")
    lower_slope = 2 * (cut - offset) * (-(cut + offset)**2).exp() / (sqrt_pi * max_dilation**2)
    upper_slope = 2 * (cut + offset) * (-((cut - offset) / max_dilation)**2).exp() / sqrt_pi
    check(lower_slope > arb("0.45") and upper_slope < arb("0.52"), "offset response")
    reference = cut.erfc()
    initial_slope = 2 * cut * (-cut**2).exp() / sqrt_pi
    allowed_failures = arb("1e-43")
    gap = arb("0.45") * dilation - 2 * prepared_error - 8 * allowed_failures
    certified = arb("5e-41")
    check(gap > certified, "preparation and terminal-readout budgets")
    per_time = 8 * arb(80).log() / certified**2
    upper_ideal_gap = arb("0.52") * dilation + 2 * threshold_error
    check(upper_ideal_gap < arb("7e-41"), "ideal upper contrast")
    null_low = reference - threshold_error
    null_high = reference + threshold_error
    check(null_low * (1 - null_high) > arb("0.21"), "Bernoulli variance lower bound")
    necessary = 2 * arb("0.21") * arb("0.9")**2 / arb("7e-41")**2

    print("initial probability", reference)
    print("epsilon t^3 coefficient", initial_slope * hessian / 6)
    print("nominal cubic increase", initial_slope * dilation)
    print("tail charge", tail, "threshold error per arm", threshold_error)
    print("threshold plus prehistory error per arm", prepared_error)
    print("separation after stated errors (lower bound)", gap)
    print("sufficient shots per time before rounding up", per_time)
    print("necessary time-T shots for ideal simple hypotheses (lower bound)", necessary)


if __name__ == "__main__":
    main()
