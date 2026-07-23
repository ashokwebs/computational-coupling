"""
run_experiments.py
==================
Proof-of-concept validation of the Theory of Computational Coupling.

Runs three experiments in the NumPy ground-truth sandbox (coupling_lab.py),
one per falsifiable prediction, across multiple random seeds, and produces:

  * JSON run logs in experiments/results/logs/
  * publication figures in figures/ and paper/figures/
  * a console summary table

All randomness is seeded; re-running reproduces the numbers exactly.

Usage:
    python3 experiments/paper1_rl/run_experiments.py
"""

from __future__ import annotations
import os, json, datetime
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import coupling_lab as cl

# --- house style -----------------------------------------------------------
NAVY   = "#1F4E78"
STEEL  = "#2E75B6"
CORAL  = "#E05A47"
GOLD   = "#E0A82E"
GREEN  = "#3C8C5A"
PALETTE = [NAVY, STEEL, CORAL, GREEN, GOLD]
plt.rcParams.update({
    "figure.dpi": 140, "savefig.dpi": 160,
    "font.size": 11, "axes.titlesize": 12, "axes.labelsize": 11,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.25, "grid.linewidth": 0.6,
    "legend.frameon": False, "font.family": "DejaVu Sans",
})

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
LOG_DIR   = os.path.join(ROOT, "experiments", "results", "logs")
PLOT_DIR  = os.path.join(ROOT, "experiments", "results", "plots")
FIG_DIR   = os.path.join(ROOT, "figures")
PAPER_FIG = os.path.join(ROOT, "paper", "figures")
for d in (LOG_DIR, PLOT_DIR, FIG_DIR, PAPER_FIG):
    os.makedirs(d, exist_ok=True)

SEEDS = [42, 43, 44, 45, 46]


def savefig(fig, name):
    """Save every figure as PNG (for the reportlab compiler) and PDF (Overleaf)."""
    for target in (FIG_DIR, PAPER_FIG, PLOT_DIR):
        fig.savefig(os.path.join(target, name + ".png"), bbox_inches="tight")
    fig.savefig(os.path.join(FIG_DIR, name + ".pdf"), bbox_inches="tight")
    plt.close(fig)


def dump_log(payload, name):
    payload = {"timestamp": datetime.datetime.now().isoformat(),
               "author": "Ashok Pasala (VIT-AP University)", **payload}
    with open(os.path.join(LOG_DIR, name + ".json"), "w") as f:
        json.dump(payload, f, indent=2, default=float)


# ===========================================================================
# Experiment 1 -- Prediction 1: Capacity-Bandwidth Saturation Law
# ===========================================================================

def experiment_1():
    print("\n[Experiment 1] Capacity-Bandwidth Saturation Law (Prediction 1)")
    B_grid = [0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32]
    dA = 16
    receiver_dims = [2, 4, 8]
    kappa = 0.7

    curves = {}       # dB -> dict(mean, std, d_eff)
    for dB in receiver_dims:
        mat = np.zeros((len(SEEDS), len(B_grid)))
        d_eff_meas = []
        for si, seed in enumerate(SEEDS):
            for bi, B in enumerate(B_grid):
                s = cl.simulate_coupled(dA=dA, dB=dB, total_bits=B,
                                        kappa_AB=kappa, T=6000, seed=seed + 100 * bi)
                mat[si, bi] = cl.predictive_gain_te(s["zA"], s["zB"], direction="A->B")
            d_eff_meas.append(cl.effective_dim(s["zB"])["pca_thresh"])
        curves[dB] = {"mean": mat.mean(0), "std": mat.std(0),
                      "d_eff": int(round(np.mean(d_eff_meas)))}
        print(f"   dB={dB} (d_eff~{curves[dB]['d_eff']}): "
              f"ceiling = {curves[dB]['mean'][-1]:.2f} +/- {curves[dB]['std'][-1]:.2f} bits")

    # Embedded-manifold robustness: ambient dim fixed at 16, effective rank varied.
    embed = {}
    for eff in [2, 4, 8]:
        vals = []
        for seed in SEEDS:
            s = cl.simulate_coupled(dA=16, dB=16, eff_dim_A=eff, eff_dim_B=eff,
                                    total_bits=32, kappa_AB=kappa, T=6000, seed=seed)
            vals.append(cl.predictive_gain_te(s["zA"], s["zB"], direction="A->B"))
        embed[eff] = {"ceiling_mean": float(np.mean(vals)), "ceiling_std": float(np.std(vals)),
                      "participation": float(cl.effective_dim(s["zB"])["participation"])}
        print(f"   embedded eff-rank {eff} in ambient-16: ceiling = "
              f"{embed[eff]['ceiling_mean']:.2f} bits (PR~{embed[eff]['participation']:.1f})")

    # ---- Figure: the saturation law ----
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.2),
                                   gridspec_kw={"width_ratios": [1.55, 1]})
    for i, dB in enumerate(receiver_dims):
        c = PALETTE[i]
        m, sd = curves[dB]["mean"], curves[dB]["std"]
        ax1.plot(B_grid, m, "-o", color=c, ms=4, lw=1.8,
                 label=f"receiver $d_{{\\mathrm{{eff}}}}={dB}$")
        ax1.fill_between(B_grid, m - sd, m + sd, color=c, alpha=0.15)
        ax1.axhline(m[-1], color=c, ls=":", lw=1, alpha=0.7)
    ax1.set_xlabel("channel bandwidth $B$ (bits / step)")
    ax1.set_ylabel(r"coupling capacity $\hat{C}(A\!\to\!B)$ (bits / step)")
    ax1.set_title("Coupling saturates below raw channel bandwidth")
    ax1.plot(B_grid, B_grid, color="0.6", ls="--", lw=1, label="raw channel limit ($C=B$)")
    ax1.set_ylim(0, max(6, max(B_grid) * 0.4))
    ax1.legend(loc="upper left", fontsize=9)

    # ceiling vs effective dimensionality
    dims = receiver_dims
    ceils = [curves[d]["mean"][-1] for d in dims]
    ceil_sd = [curves[d]["std"][-1] for d in dims]
    ax2.errorbar(dims, ceils, yerr=ceil_sd, fmt="o", color=NAVY, ms=7, capsize=3, lw=1.8)
    coef = np.polyfit(dims, ceils, 1)
    xs = np.linspace(min(dims) - 0.5, max(dims) + 0.5, 50)
    ax2.plot(xs, np.polyval(coef, xs), "--", color=CORAL, lw=1.6,
             label=f"linear fit\n(slope={coef[0]:.2f} bits/dim)")
    ax2.set_xlabel(r"receiver effective dimensionality $d_{\mathrm{eff}}(\mathcal{M}_B)$")
    ax2.set_ylabel("saturated capacity $C^\\ast$ (bits / step)")
    ax2.set_title("Ceiling scales with $d_{\\mathrm{eff}}$, not $B$")
    ax2.set_xticks(dims)
    ax2.legend(loc="upper left", fontsize=9)
    fig.suptitle("Prediction 1 -- Capacity--Bandwidth Saturation Law", fontsize=13, y=1.02)
    savefig(fig, "fig2_capacity_bandwidth_law")

    dump_log({"experiment": "P1_capacity_bandwidth_saturation",
              "B_grid": B_grid, "dA": dA, "kappa": kappa, "seeds": SEEDS,
              "curves": {str(k): {"mean": v["mean"].tolist(), "std": v["std"].tolist(),
                                  "d_eff": v["d_eff"]} for k, v in curves.items()},
              "embedded_manifold": embed,
              "ceiling_vs_dim_slope_bits_per_dim": float(coef[0])},
             "P1_capacity_bandwidth")
    return curves, coef[0]


# ===========================================================================
# Experiment 2 -- Prediction 2: Self-Predictive Accuracy Governs Efficiency
# ===========================================================================

def experiment_2():
    print("\n[Experiment 2] Self-Predictive Accuracy Governs Capacity Efficiency (Prediction 2)")
    rhos = [0.1, 0.3, 0.5, 0.7, 0.85, 0.95]
    B = 6
    R_vals, CB_mean, CB_std = [], [], []
    for rho in rhos:
        cbs, rs = [], []
        for seed in SEEDS:
            s = cl.simulate_coupled(dA=16, dB=6, total_bits=B, kappa_AB=0.6,
                                    rho_A=rho, rho_B=rho, T=6000, seed=seed)
            cbs.append(cl.predictive_gain_te(s["zA"], s["zB"], direction="A->B") / B)
            rs.append(0.5 * (cl.self_predictive_accuracy(s["zA"]) +
                             cl.self_predictive_accuracy(s["zB"])))
        R_vals.append(float(np.mean(rs)))
        CB_mean.append(float(np.mean(cbs)))
        CB_std.append(float(np.std(cbs)))
        print(f"   R~{R_vals[-1]:.3f} -> C/B = {CB_mean[-1]:.3f} +/- {CB_std[-1]:.3f}")

    corr = float(np.corrcoef(R_vals, CB_mean)[0, 1])

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.errorbar(R_vals, CB_mean, yerr=CB_std, fmt="o-", color=STEEL, ms=6,
                lw=1.9, capsize=3)
    ax.set_xlabel(r"self-predictive accuracy $R$ (joint world-model quality)")
    ax.set_ylabel(r"coupling efficiency $\hat{C}/B$ (bits per channel bit)")
    ax.set_title(f"Prediction 2 -- better world models couple more per bit\n"
                 f"(Pearson $r={corr:.2f}$)")
    savefig(fig, "fig4_selfpredictive_efficiency")

    dump_log({"experiment": "P2_selfpredictive_efficiency",
              "rho_grid": rhos, "B": B, "seeds": SEEDS,
              "R_values": R_vals, "CB_mean": CB_mean, "CB_std": CB_std,
              "pearson_r": corr}, "P2_selfpredictive_efficiency")
    return R_vals, CB_mean, corr


# ===========================================================================
# Experiment 3 -- Prediction 3: Asymmetry Tracks Role
# ===========================================================================

def experiment_3():
    print("\n[Experiment 3] Directional Asymmetry Tracks Task Role (Prediction 3)")
    roles = [0.1, 0.2, 0.35, 0.5, 0.65, 0.8, 0.9]
    A_mean, A_std = [], []
    for r in roles:
        kab, kba = r, 1.0 - r
        a = []
        for seed in SEEDS:
            s = cl.simulate_coupled(dA=8, dB=8, total_bits=8,
                                    kappa_AB=kab, kappa_BA=kba, T=6000, seed=seed)
            te_ab = cl.predictive_gain_te(s["zA"], s["zB"], direction="A->B")
            te_ba = cl.predictive_gain_te(s["zA"], s["zB"], direction="B->A")
            a.append((te_ab - te_ba) / (te_ab + te_ba + 1e-12))
        A_mean.append(float(np.mean(a)))
        A_std.append(float(np.std(a)))
        print(f"   role r={r:.2f} -> asymmetry A = {A_mean[-1]:+.3f} +/- {A_std[-1]:.3f}")

    corr = float(np.corrcoef(roles, A_mean)[0, 1])

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.axhline(0, color="0.7", lw=0.8)
    ax.errorbar(roles, A_mean, yerr=A_std, fmt="o-", color=CORAL, ms=6,
                lw=1.9, capsize=3)
    coef = np.polyfit(roles, A_mean, 1)
    xs = np.linspace(0.05, 0.95, 40)
    ax.plot(xs, np.polyval(coef, xs), "--", color=NAVY, lw=1.4, alpha=0.8)
    ax.set_xlabel(r"task role $r=\kappa_{A\to B}/(\kappa_{A\to B}+\kappa_{B\to A})$")
    ax.set_ylabel(r"asymmetry index $A$")
    ax.set_title(f"Prediction 3 -- coupling asymmetry tracks role\n"
                 f"(Pearson $r={corr:.2f}$)")
    ax.set_ylim(-1.05, 1.05)
    savefig(fig, "fig3_asymmetry_index")

    dump_log({"experiment": "P3_asymmetry_tracks_role",
              "role_grid": roles, "seeds": SEEDS,
              "asymmetry_mean": A_mean, "asymmetry_std": A_std,
              "pearson_r": corr}, "P3_asymmetry_role")
    return roles, A_mean, corr


# ===========================================================================
# Cross-check -- model-free KSG estimator agrees on low-dim instances
# ===========================================================================

def crosscheck_ksg():
    print("\n[Cross-check] Model-free KSG vs predictive-gain estimator (low-dim)")
    rows = []
    for kappa in [0.0, 0.3, 0.6, 0.9]:
        pgs, ksgs = [], []
        for seed in SEEDS:
            s = cl.simulate_coupled(dA=4, dB=1, total_bits=8, kappa_AB=kappa,
                                    T=8000, seed=seed)
            pgs.append(cl.predictive_gain_te(s["zA"], s["zB"], direction="A->B"))
            ete, _, _ = cl.effective_te(cl.ksg_transfer_entropy, s["zA"], s["zB"],
                                        n_surrogate=4, k=6, seed=seed)
            ksgs.append(ete)
        rows.append({"kappa": kappa,
                     "predictive_gain": float(np.mean(pgs)),
                     "ksg_effective": float(np.mean(ksgs))})
        print(f"   kappa={kappa:.1f} | predictive-gain={rows[-1]['predictive_gain']:.3f} "
              f"| KSG ETE={rows[-1]['ksg_effective']:.3f} bits")

    pg = np.array([r["predictive_gain"] for r in rows])
    ks = np.array([r["ksg_effective"] for r in rows])
    corr = float(np.corrcoef(pg, ks)[0, 1])
    mae = float(np.mean(np.abs(pg - ks)))

    fig, ax = plt.subplots(figsize=(5.6, 4.3))
    lim = max(pg.max(), ks.max()) * 1.15 + 0.05
    ax.plot([0, lim], [0, lim], "--", color="0.6", lw=1, label="identity")
    ax.scatter(pg, ks, s=70, color=NAVY, zorder=3)
    for r in rows:
        ax.annotate(f"$\\kappa$={r['kappa']:.1f}",
                    (r["predictive_gain"], r["ksg_effective"]),
                    textcoords="offset points", xytext=(7, -3), fontsize=8.5, color="0.3")
    ax.set_xlabel("predictive-gain estimate (bits)")
    ax.set_ylabel("model-free KSG estimate (bits)")
    ax.set_title(f"Two independent estimators agree\n(Pearson $r={corr:.3f}$, mean abs. diff {mae:.3f} bits)")
    ax.set_xlim(0, lim); ax.set_ylim(0, lim)
    ax.set_aspect("equal")
    savefig(fig, "fig5_estimator_agreement")

    dump_log({"experiment": "crosscheck_ksg_vs_predictive_gain", "rows": rows,
              "pearson_r": corr, "mean_abs_diff_bits": mae}, "crosscheck_ksg")
    print(f"   agreement: Pearson r={corr:.3f}, mean abs diff={mae:.3f} bits")
    return rows


if __name__ == "__main__":
    print("=" * 70)
    print("Computational Coupling -- Proof-of-Concept Validation")
    print("=" * 70)
    curves, slope = experiment_1()
    R_vals, CB, r2 = experiment_2()
    roles, A_mean, r3 = experiment_3()
    ksg = crosscheck_ksg()

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"P1  ceiling-vs-dimension slope : {slope:.2f} bits/effective-dim "
          f"(ceiling set by d_eff, not B)")
    print(f"P2  corr(R, C/B)               : {r2:+.2f}  (world-model quality raises efficiency)")
    print(f"P3  corr(role, asymmetry)      : {r3:+.2f}  (asymmetry tracks role)")
    print("Figures -> figures/  and  paper/figures/")
    print("Logs    -> experiments/results/logs/")
