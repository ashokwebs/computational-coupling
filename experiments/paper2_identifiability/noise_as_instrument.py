"""
noise_as_instrument.py
=======================
Demonstrates Remark 2 of paper_main/main.tex ("On (ii): an underexploited
inversion"): exogenous channel noise, independent of a dyad's shared
convention, satisfies the instrumental-variable conditions and recovers
functional coupling where observational statistics cannot.

This is a direct, quantitative instance of Theorem 1's proof. Two dyads are
built so that a sender's state C ("shared convention") drives a transmitted
message M = C + N, where N is exogenous channel noise independent of C:

  Dyad "coupled"    (D1): U = kappa * M + eps      -- receiver acts on the message
  Dyad "confounded" (D2): U = kappa' * C + eps      -- receiver acts on C directly,
                                                        M is present but causally inert

kappa and kappa' are chosen so Cov(M, U) is equal across the two dyads --
i.e. the naive observational relationship between message and behaviour is
made indistinguishable by construction, mirroring P_1 = P_2 in Theorem 1's
proof. The true causal effect of do(M) on U is kappa in D1 and exactly 0 in
D2 (M is not a cause of U in D2 at all -- only a correlate, via C).

The instrument N lets us recover this distinction without ever intervening:
    IV estimate = Cov(U, N) / Cov(M, N)
which is standard 2SLS (single instrument, single endogenous regressor).
We verify the IV estimate against ground truth by also simulating the direct
interventional query do(M = m), which is available here only because we
built the generative model and would not be in a real observational corpus.

Author: Ashok Pasala (VIT-AP University)
Program: Computational Coupling Research Program
"""

from __future__ import annotations
import json
import numpy as np


# ---------------------------------------------------------------------------
# Generative model
# ---------------------------------------------------------------------------

def simulate_dyad(n, condition, kappa, sigma_C=1.0, sigma_N=1.0, sigma_U=0.3, seed=0):
    """Simulate n i.i.d. trials of a dyad under the coupled or confounded structure.

    condition: "coupled" (D1, U causally depends on M) or
               "confounded" (D2, U causally depends on C, M is inert w.r.t. U)
    kappa: causal weight (on M in D1, on C in D2)
    sigma_N: std of the exogenous channel noise -- the instrument's strength.
    """
    rng = np.random.default_rng(seed)
    C = sigma_C * rng.standard_normal(n)
    N = sigma_N * rng.standard_normal(n)          # exogenous, independent of C by construction
    M = C + N
    eps = sigma_U * rng.standard_normal(n)

    if condition == "coupled":
        U = kappa * M + eps
    elif condition == "confounded":
        U = kappa * C + eps
    else:
        raise ValueError(condition)

    return {"C": C, "N": N, "M": M, "U": U}


def calibrate_kappa_confounded(kappa_coupled, sigma_C, sigma_N):
    """Choose kappa' for the confounded dyad so Cov(M,U) matches the coupled dyad.

    Coupled:    Cov(M, U) = kappa_coupled * Var(M) = kappa_coupled * (sigma_C^2 + sigma_N^2)
    Confounded: Cov(M, U) = kappa' * Cov(M, C)      = kappa' * sigma_C^2
    Solve kappa' * sigma_C^2 = kappa_coupled * (sigma_C^2 + sigma_N^2).
    """
    return kappa_coupled * (sigma_C ** 2 + sigma_N ** 2) / (sigma_C ** 2)


# ---------------------------------------------------------------------------
# Estimators
# ---------------------------------------------------------------------------

def cov(x, y):
    return float(np.cov(x, y, ddof=1)[0, 1])


def var(x):
    return float(np.var(x, ddof=1))


def naive_ols(M, U):
    """Observational regression coefficient of U on M -- what every
    correlation/MI/TE-style observational measure ultimately reduces to in
    the linear-Gaussian case: Cov(U,M) / Var(M)."""
    return cov(M, U) / var(M)


def iv_estimate(M, U, N):
    """Two-stage-least-squares point estimate with a single instrument:
    IV = Cov(U,N) / Cov(M,N). Equivalent to (reduced form) / (first stage)."""
    return cov(U, N) / cov(M, N)


def first_stage_f_stat(M, N):
    """First-stage F-statistic (instrument strength check). Rule of thumb:
    F < 10 flags a weak instrument and the IV estimate should not be trusted."""
    n = len(N)
    beta = cov(M, N) / var(N)
    alpha = np.mean(M) - beta * np.mean(N)
    resid = M - (alpha + beta * N)
    ss_res = np.sum(resid ** 2)
    ss_tot = np.sum((M - np.mean(M)) ** 2)
    r2 = 1 - ss_res / ss_tot
    dof = n - 2
    f = (r2 / (1 - r2)) * dof if r2 < 1 else np.inf
    return float(f)


def interventional_ground_truth(condition, kappa):
    """The true causal effect of do(M=m) on E[U], derived directly from the
    structural equations -- available here only because we know the
    generative model; this is what an observational corpus could never hand
    us, and what the IV estimate above should recover without ever
    intervening."""
    return kappa if condition == "coupled" else 0.0


# ---------------------------------------------------------------------------
# Experiment
# ---------------------------------------------------------------------------

def run_condition(condition, kappa, n, sigma_C, sigma_N, sigma_U, n_seeds=200):
    naive_vals, iv_vals, f_vals = [], [], []
    for seed in range(n_seeds):
        d = simulate_dyad(n, condition, kappa, sigma_C, sigma_N, sigma_U, seed=seed)
        naive_vals.append(naive_ols(d["M"], d["U"]))
        iv_vals.append(iv_estimate(d["M"], d["U"], d["N"]))
        f_vals.append(first_stage_f_stat(d["M"], d["N"]))
    truth = interventional_ground_truth(condition, kappa)
    return {
        "condition": condition,
        "truth": truth,
        "naive_mean": float(np.mean(naive_vals)),
        "naive_std": float(np.std(naive_vals)),
        "iv_mean": float(np.mean(iv_vals)),
        "iv_std": float(np.std(iv_vals)),
        "first_stage_f_mean": float(np.mean(f_vals)),
    }


def sweep_instrument_strength(kappa_coupled, n, sigma_C, sigma_U, n_seeds, sigma_N_grid):
    """Show the IV estimate degrade as the instrument weakens (sigma_N -> 0),
    the honest caveat: this route needs genuine exogenous variance in the
    channel, not just any noise."""
    rows = []
    for sigma_N in sigma_N_grid:
        kappa_confounded = calibrate_kappa_confounded(kappa_coupled, sigma_C, sigma_N)
        for condition, kappa in [("coupled", kappa_coupled), ("confounded", kappa_confounded)]:
            res = run_condition(condition, kappa, n, sigma_C, sigma_N, sigma_U, n_seeds)
            res["sigma_N"] = sigma_N
            rows.append(res)
    return rows


def main():
    kappa_coupled = 0.8
    n = 2000
    sigma_C = 1.0
    sigma_U = 0.3
    n_seeds = 200

    # --- Headline result at a well-powered instrument strength ---
    sigma_N_main = 1.0
    kappa_confounded = calibrate_kappa_confounded(kappa_coupled, sigma_C, sigma_N_main)
    headline = []
    for condition, kappa in [("coupled", kappa_coupled), ("confounded", kappa_confounded)]:
        headline.append(run_condition(condition, kappa, n, sigma_C, sigma_N_main, sigma_U, n_seeds))

    print("=== Headline: naive observational estimate cannot distinguish the dyads; IV can ===")
    print(f"{'condition':<12} {'truth':>8} {'naive (obs.)':>22} {'IV (instrument)':>22} {'1st-stage F':>12}")
    for r in headline:
        print(f"{r['condition']:<12} {r['truth']:>8.3f} "
              f"{r['naive_mean']:>10.3f} +/- {r['naive_std']:.3f}   "
              f"{r['iv_mean']:>10.3f} +/- {r['iv_std']:.3f}   "
              f"{r['first_stage_f_mean']:>10.1f}")

    naive_gap = abs(headline[0]["naive_mean"] - headline[1]["naive_mean"])
    iv_gap = abs(headline[0]["iv_mean"] - headline[1]["iv_mean"])
    print(f"\nObservational gap between dyads: {naive_gap:.4f} (should be ~0 -- indistinguishable by construction)")
    print(f"IV-recovered gap between dyads:  {iv_gap:.4f} (should be ~{kappa_coupled:.3f} -- matches ground truth)")

    # --- Weak-instrument sweep ---
    sigma_N_grid = [0.02, 0.1, 0.3, 1.0, 3.0]
    sweep = sweep_instrument_strength(kappa_coupled, n, sigma_C, sigma_U, n_seeds, sigma_N_grid)

    summary = {
        "config": {
            "kappa_coupled": kappa_coupled, "n": n, "sigma_C": sigma_C,
            "sigma_U": sigma_U, "n_seeds": n_seeds, "sigma_N_main": sigma_N_main,
        },
        "headline": headline,
        "observational_gap": naive_gap,
        "iv_recovered_gap": iv_gap,
        "instrument_strength_sweep": sweep,
    }
    out_path = "../results/logs/paper2_noise_as_instrument.json"
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nWrote {out_path}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

        ax = axes[0]
        conds = [r["condition"] for r in headline]
        x = np.arange(len(conds))
        width = 0.35
        ax.bar(x - width / 2, [r["naive_mean"] for r in headline], width,
               yerr=[r["naive_std"] for r in headline], label="Naive (observational)", color="#d95f5f")
        ax.bar(x + width / 2, [r["iv_mean"] for r in headline], width,
               yerr=[r["iv_std"] for r in headline], label="IV (noise-as-instrument)", color="#4a7fb5")
        ax.scatter(x, [r["truth"] for r in headline], color="black", zorder=5, marker="x", s=80, label="Ground truth")
        ax.set_xticks(x); ax.set_xticklabels(conds)
        ax.set_ylabel("Estimated effect of M on U")
        ax.set_title("Observational measures can't tell the dyads apart; IV can")
        ax.legend(fontsize=8)

        ax = axes[1]
        sigmas = sorted(set(r["sigma_N"] for r in sweep))
        for condition in ["coupled", "confounded"]:
            means = [next(r for r in sweep if r["sigma_N"] == s and r["condition"] == condition)["iv_mean"] for s in sigmas]
            stds = [next(r for r in sweep if r["sigma_N"] == s and r["condition"] == condition)["iv_std"] for s in sigmas]
            truth = [next(r for r in sweep if r["sigma_N"] == s and r["condition"] == condition)["truth"] for s in sigmas]
            ax.errorbar(sigmas, means, yerr=stds, marker="o", label=f"{condition} (IV est.)")
            ax.plot(sigmas, truth, "--", color="black", alpha=0.4)
        ax.set_xscale("log")
        ax.set_xlabel(r"Instrument strength $\sigma_N$ (log scale)")
        ax.set_ylabel("IV estimate")
        ax.set_title("Weak instruments fail; strong ones recover truth", fontsize=11)
        ax.legend(fontsize=8)

        fig.tight_layout()
        plot_path = "../results/plots/paper2_noise_as_instrument.png"
        fig.savefig(plot_path, dpi=150)
        print(f"Wrote {plot_path}")
    except ImportError:
        print("matplotlib not available -- skipped plot, JSON summary still written.")


if __name__ == "__main__":
    main()
