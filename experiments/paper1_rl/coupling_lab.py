"""
coupling_lab.py
===============
A self-contained, dependency-light (NumPy-only) laboratory for measuring
*coupling capacity* between two coupled dynamical systems joined by a
bandwidth-limited interface.

This is the ground-truth sandbox behind the paper's Proof-of-Concept section.
Unlike a full multi-agent RL run, everything here has a *known* generative
structure, so the theory's predictions can be checked against quantities we
control exactly (the receiver's effective dimensionality, the injected coupling
gain, and the channel's bit budget).

Three independent transfer-entropy estimators are implemented so that no single
estimator's idiosyncrasies can drive a result:

  1. Gaussian / Geweke directed measure   -- closed form for linear-Gaussian systems
  2. Predictive-gain estimator            -- the paper's own L_self - L_joint estimator
                                              (here with ridge-linear predictors)
  3. KSG k-nearest-neighbour estimator     -- fully model-free (Kraskov et al. 2004)

Author: Ashok Pasala (VIT-AP University)
Program: Computational Coupling Research Program
"""

from __future__ import annotations
import numpy as np


# ---------------------------------------------------------------------------
# Small numerical helpers
# ---------------------------------------------------------------------------

def digamma(x):
    """Vectorised digamma (psi) function via recurrence + asymptotic series.

    Accurate to ~1e-8 for x > 0, which is all the KSG estimator needs.
    Avoids a SciPy dependency.
    """
    x = np.asarray(x, dtype=float)
    result = np.zeros_like(x)
    # Push argument up so the asymptotic expansion is accurate (x >= 6).
    small = x < 6
    xs = x.copy()
    while np.any(xs < 6):
        m = xs < 6
        result[m] -= 1.0 / xs[m]
        xs[m] += 1.0
    inv = 1.0 / xs
    inv2 = inv * inv
    # Asymptotic series: ln(x) - 1/(2x) - 1/(12x^2) + 1/(120x^4) - 1/(252x^6)
    series = (np.log(xs) - 0.5 * inv
              - inv2 * (1.0 / 12.0
                        - inv2 * (1.0 / 120.0
                                  - inv2 * (1.0 / 252.0))))
    return result + series


def orthogonal_transition(dim, spectral_radius, rng):
    """Random stable linear transition matrix with a given spectral radius.

    Built as spectral_radius * Q where Q is a Haar-random orthogonal matrix, so
    every eigenvalue has modulus exactly `spectral_radius` < 1 and the driven
    VAR(1) process is guaranteed stationary.
    """
    a = rng.standard_normal((dim, dim))
    q, r = np.linalg.qr(a)
    # Fix the sign ambiguity of QR so Q is properly Haar-distributed.
    q *= np.sign(np.diag(r))
    return spectral_radius * q


# ---------------------------------------------------------------------------
# The bandwidth-limited interface (channel)
# ---------------------------------------------------------------------------

def quantization_noise_var(signal_var, bits):
    """Per-dimension reconstruction-noise variance for a `bits`-bit channel.

    Uses the standard high-resolution / rate-distortion model for a Gaussian
    source: each additional bit halves the quantisation step, quartering the
    error power, so the channel signal-to-noise ratio is 2^(2*bits). We floor
    the reconstruction SNR so that a 0-bit channel transmits nothing:

        Var(reconstruction error) = Var(signal) / 2^(2*bits)      (bits > 0)
                                  = +inf  (signal replaced by its mean)  (bits = 0)

    This keeps the injected signal *power* constant across bit-depths and lets
    only fidelity improve with bandwidth -- so coupling rises monotonically and
    saturates, rather than being confounded by amplitude artefacts of literal
    rounding.
    """
    if bits <= 0:
        return np.inf
    return signal_var / (2.0 ** (2.0 * bits))


def allocate_bits(total_bits, n_ch):
    """Spread a total per-step bit budget across n_ch channel dimensions.

    Water-fills as evenly as possible: the first (total % n_ch) dimensions get
    one extra bit. Returns an integer array of length n_ch.
    """
    base = total_bits // n_ch
    extra = total_bits % n_ch
    bits = np.full(n_ch, base, dtype=int)
    bits[:extra] += 1
    return bits


# ---------------------------------------------------------------------------
# The coupled two-system simulator
# ---------------------------------------------------------------------------

def simulate_coupled(dA=16, dB=8, total_bits=8,
                     kappa_AB=0.6, kappa_BA=0.0,
                     rho_A=0.6, rho_B=0.6,
                     sigma_A=1.0, sigma_B=1.0,
                     eff_dim_A=None, eff_dim_B=None,
                     T=6000, burn_in=500, seed=0):
    """Simulate two coupled linear-Gaussian systems through a quantised channel.

    Each system i has a latent state z_i(t) evolving as a stationary VAR(1)
    process. System A emits a channel signal from the first n_ch = min(dA, dB)
    coordinates of its state; the signal passes through a `total_bits`-bit/step
    channel (high-resolution quantisation-noise model) and is injected into B's
    dynamics (and symmetrically B -> A if kappa_BA > 0).

    Effective dimensionality control
    --------------------------------
    If `eff_dim_i` is set (< d_i), the process noise is confined to that many
    leading directions (the remaining directions are strongly damped), so the
    state lives on a lower-dimensional manifold of that effective rank while the
    *ambient* dimension stays d_i. This lets us test whether coupling saturates
    at the *effective* dimensionality rather than the ambient one.
    """
    rng = np.random.default_rng(seed)
    # The receiver can be driven only along its *active* manifold directions, so
    # the usable channel width is the smaller effective dimensionality.
    eff_A = eff_dim_A if eff_dim_A is not None else dA
    eff_B = eff_dim_B if eff_dim_B is not None else dB
    n_ch = min(eff_A, eff_B)

    M_A = orthogonal_transition(dA, rho_A, rng)
    M_B = orthogonal_transition(dB, rho_B, rng)

    # Anisotropic process-noise scaling to set an effective manifold dimension:
    # directions beyond the effective rank are near-frozen (and, crucially, are
    # neither transmitted nor injected), so the state genuinely lives on a
    # lower-dimensional manifold inside the ambient space.
    def noise_scale(d, eff):
        s = np.ones(d)
        if eff is not None and eff < d:
            s[eff:] = 0.02
        return s
    nsA = noise_scale(dA, eff_dim_A)
    nsB = noise_scale(dB, eff_dim_B)

    # Injection maps: the n_ch channel dimensions enter the first n_ch
    # coordinates of the receiver's state (rank exactly n_ch -- the receiver can
    # absorb exogenous drive along at most n_ch of its directions).
    U_AB = np.zeros((dB, n_ch)); U_AB[:n_ch, :] = np.eye(n_ch)
    U_BA = np.zeros((dA, n_ch)); U_BA[:n_ch, :] = np.eye(n_ch)

    bits_per_dim = allocate_bits(total_bits, n_ch)

    # Stationary per-coordinate signal variance ~ sigma^2 / (1 - rho^2).
    var_A = (sigma_A ** 2) / max(1e-6, 1 - rho_A ** 2)
    var_B = (sigma_B ** 2) / max(1e-6, 1 - rho_B ** 2)
    qnoise_std_A = np.sqrt([quantization_noise_var(var_A, b) for b in bits_per_dim])
    qnoise_std_B = np.sqrt([quantization_noise_var(var_B, b) for b in bits_per_dim])
    # bits=0 -> inf std -> signal is replaced by pure noise, i.e. transmits nothing.
    live_A = np.isfinite(qnoise_std_A)
    live_B = np.isfinite(qnoise_std_B)

    steps = T + burn_in
    zA = np.zeros((steps, dA))
    zB = np.zeros((steps, dB))

    # Pre-draw all stochastic terms (vectorised).
    xiA = (sigma_A * nsA) * rng.standard_normal((steps, dA))
    xiB = (sigma_B * nsB) * rng.standard_normal((steps, dB))
    qA = np.where(live_A, qnoise_std_A, 0.0) * rng.standard_normal((steps, n_ch))
    qB = np.where(live_B, qnoise_std_B, 0.0) * rng.standard_normal((steps, n_ch))

    for t in range(1, steps):
        # Channel A -> B, built from A's previous state + reconstruction noise.
        sA = np.where(live_A, zA[t - 1, :n_ch] + qA[t], 0.0)
        sB = np.where(live_B, zB[t - 1, :n_ch] + qB[t], 0.0)

        zA[t] = M_A @ zA[t - 1] + kappa_BA * (U_BA @ sB) + xiA[t]
        zB[t] = M_B @ zB[t - 1] + kappa_AB * (U_AB @ sA) + xiB[t]

    return {
        "zA": zA[burn_in:],
        "zB": zB[burn_in:],
        "dA": dA, "dB": dB, "n_ch": n_ch,
        "eff_dim_A": eff_dim_A, "eff_dim_B": eff_dim_B,
        "total_bits": total_bits, "bits_per_dim": bits_per_dim,
        "kappa_AB": kappa_AB, "kappa_BA": kappa_BA,
    }


# ---------------------------------------------------------------------------
# Effective dimensionality
# ---------------------------------------------------------------------------

def effective_dim(X, threshold=0.95):
    """Effective (participation-ratio-style) dimensionality of a trajectory.

    Two conventions are returned:
      - `pca_thresh`: number of PCs to reach `threshold` cumulative variance.
      - `participation`: (sum lambda)^2 / sum(lambda^2), a smooth effective rank.
    """
    Xc = X - X.mean(0, keepdims=True)
    cov = np.cov(Xc, rowvar=False)
    w = np.linalg.eigvalsh(cov)
    w = np.clip(w, 0, None)[::-1]
    total = w.sum() + 1e-12
    cum = np.cumsum(w) / total
    pca_thresh = int(np.searchsorted(cum, threshold) + 1)
    participation = (w.sum() ** 2) / (np.sum(w ** 2) + 1e-12)
    return {"pca_thresh": pca_thresh, "participation": float(participation)}


# ---------------------------------------------------------------------------
# Estimator 1 & 2: linear predictive-gain / Gaussian directed measure
# ---------------------------------------------------------------------------

def _ridge_residual_cov(Y, X, ridge=1e-6):
    """Residual covariance of the least-squares fit Y ~ X (with intercept)."""
    n = X.shape[0]
    Xa = np.hstack([X, np.ones((n, 1))])
    gram = Xa.T @ Xa + ridge * np.eye(Xa.shape[1])
    beta = np.linalg.solve(gram, Xa.T @ Y)
    resid = Y - Xa @ beta
    return (resid.T @ resid) / n


def predictive_gain_te(zA, zB, lag=1, history=1, direction="A->B", ridge=1e-6):
    """Transfer entropy via predictive gain L_self - L_joint (in bits).

    For linear-Gaussian systems this equals the Gaussian/Geweke directed
    information and is a consistent estimator of transfer entropy. The receiver
    predicts its own future from its own past (self model) versus from its past
    plus the source's state (joint model); the log-det ratio of residual
    covariances is the coupling in bits.
    """
    if direction == "A->B":
        src, tgt = zA, zB
    else:
        src, tgt = zB, zA

    def stack_history(Z, t0, h):
        return np.hstack([Z[t0 - j] for j in range(h)])

    T = tgt.shape[0]
    t_start = max(history, 1)
    future = tgt[t_start + lag - 1: T]
    tgt_past = np.hstack([tgt[t_start - 1 - j: T - lag - j] for j in range(history)])
    src_past = np.hstack([src[t_start - 1 - j: T - lag - j] for j in range(history)])

    n = future.shape[0]
    tgt_past = tgt_past[:n]
    src_past = src_past[:n]

    cov_self = _ridge_residual_cov(future, tgt_past, ridge)
    cov_joint = _ridge_residual_cov(future, np.hstack([tgt_past, src_past]), ridge)

    sign_s, logdet_self = np.linalg.slogdet(cov_self)
    sign_j, logdet_joint = np.linalg.slogdet(cov_joint)
    te_nats = 0.5 * (logdet_self - logdet_joint)
    te_bits = te_nats / np.log(2)
    return max(te_bits, 0.0)


def self_predictive_accuracy(zB, history=1, ridge=1e-6):
    """R^2 of the receiver's self-model: how well its own past predicts its future.

    A proxy for the quality of the system's internal world model (Prediction 2).
    """
    T = zB.shape[0]
    future = zB[history:T]
    past = np.hstack([zB[history - 1 - j: T - 1 - j] for j in range(history)])[:future.shape[0]]
    cov_self = _ridge_residual_cov(future, past, ridge)
    var_total = np.cov(future, rowvar=False)
    r2 = 1.0 - np.trace(cov_self) / (np.trace(np.atleast_2d(var_total)) + 1e-12)
    return float(np.clip(r2, 0, 1))


# ---------------------------------------------------------------------------
# Estimator 3: KSG k-NN transfer entropy (model-free cross-check)
# ---------------------------------------------------------------------------

def _chebyshev_knn_radius(points, k):
    """For each point, the Chebyshev distance to its k-th nearest neighbour."""
    n = points.shape[0]
    radii = np.empty(n)
    # Brute force is fine for the sample sizes used in the cross-check (~1500).
    for i in range(n):
        d = np.max(np.abs(points - points[i]), axis=1)
        d[i] = np.inf
        radii[i] = np.partition(d, k - 1)[k - 1]
    return radii


def _count_within(points, radii):
    """Count neighbours strictly within `radii` (Chebyshev), excluding self."""
    n = points.shape[0]
    counts = np.empty(n, dtype=int)
    for i in range(n):
        d = np.max(np.abs(points - points[i]), axis=1)
        counts[i] = np.sum(d < radii[i]) - 1
    return counts


def ksg_transfer_entropy(src, tgt, k=6, lag=1, seed=0, max_samples=3500,
                         src_coord=0, tgt_coord=0):
    """Model-free KSG transfer entropy src -> tgt (in bits), scalar projections.

    Estimates TE = I(src_past ; tgt_future | tgt_past) with the
    Kraskov-Stoegbauer-Grassberger k-NN estimator (their conditional-MI form).
    The source is projected onto its transmitted channel coordinate `src_coord`
    (the dimension actually sent over the interface) and the target onto
    `tgt_coord`; using the channel coordinate rather than PC1 removes the large
    negative bias k-NN estimators otherwise suffer here.
    """
    rng = np.random.default_rng(seed)
    s = src[:, src_coord] - src[:, src_coord].mean()
    y = tgt[:, tgt_coord] - tgt[:, tgt_coord].mean()
    T = len(y)
    yf = y[lag:T]
    yp = y[:T - lag]
    sp = s[:T - lag]

    n = len(yf)
    if n > max_samples:
        idx = rng.choice(n, max_samples, replace=False)
        yf, yp, sp = yf[idx], yp[idx], sp[idx]

    # Tiny jitter breaks ties so k-NN counts are well-defined.
    jit = 1e-10
    yf = yf + jit * rng.standard_normal(len(yf))
    yp = yp + jit * rng.standard_normal(len(yp))
    sp = sp + jit * rng.standard_normal(len(sp))

    joint = np.column_stack([yf, yp, sp])
    radii = _chebyshev_knn_radius(joint, k)

    n_yp = _count_within(np.column_stack([yp]), radii)
    n_yf_yp = _count_within(np.column_stack([yf, yp]), radii)
    n_sp_yp = _count_within(np.column_stack([sp, yp]), radii)

    te_nats = (digamma(k)
               + np.mean(digamma(n_yp + 1))
               - np.mean(digamma(n_yf_yp + 1))
               - np.mean(digamma(n_sp_yp + 1)))
    return max(te_nats / np.log(2), 0.0)


def effective_te(estimator_fn, src, tgt, n_surrogate=8, seed=0, **kwargs):
    """Effective TE = raw TE minus the mean of block-shuffled surrogates.

    Removes finite-sample bias / spurious coupling (the ETE convention in the
    reproducibility protocol).
    """
    raw = estimator_fn(src, tgt, **kwargs)
    rng = np.random.default_rng(seed)
    T = src.shape[0]
    surr = []
    block = max(10, T // 20)
    for s in range(n_surrogate):
        n_blocks = T // block
        order = rng.permutation(n_blocks)
        idx = np.concatenate([np.arange(b * block, (b + 1) * block) for b in order])
        idx = idx[:T]
        surr.append(estimator_fn(src[idx], tgt, **kwargs))
    return max(raw - np.mean(surr), 0.0), raw, float(np.mean(surr))
