# 🔬 Paper 2 Identifiability — computational demonstrations

## ✅ Done — noise-as-instrument (2026-07-31)

`noise_as_instrument.py` converts `paper2/main.tex` Remark 2 (§4.1, "an underexploited inversion") from an argued claim into a demonstrated method, per `handoff.md` §5's top research debt ("inject noise independent of the shared latent into the existing testbed, recover the known ground-truth coupling via IV, and confirm it matches the interventional estimate").

**Construction.** Two linear-Gaussian dyads, matching Theorem 1's proof structure but continuous so 2SLS applies: a shared latent $C$ (the convention), a transmitted message $M = C + N$ with $N$ exogenous channel noise independent of $C$ (the instrument), and behaviour $U$ defined two ways:
- **coupled**: $U = \kappa M + \varepsilon$ — behaviour causally depends on the message.
- **confounded**: $U = \kappa' C + \varepsilon$ — behaviour depends only on the shared latent; $M$ is present and correlated with $U$ but does no causal work.

$\kappa'$ is calibrated so $\mathrm{Cov}(M,U)$ matches exactly between the two dyads — the observational relationship is made indistinguishable by construction, the continuous analogue of $P_1 = P_2$ in Theorem 1.

**Result** (`n=2000` trials, 200 seeds, $\sigma_N=1.0$):

| | ground truth | naive observational estimate | IV estimate |
|---|---|---|---|
| coupled | 0.800 | 0.800 ± 0.005 | 0.800 ± 0.007 |
| confounded | 0.000 | 0.799 ± 0.019 | −0.003 ± 0.034 |

Observational gap between the two dyads: **0.0011** (statistically zero — confirms the naive measure genuinely cannot tell them apart). IV-recovered gap: **0.8022**, matching the true $\kappa=0.8$. The instrument recovers ground truth exactly where the observational statistic is, by construction, blind to it.

**Weak-instrument honesty check.** Swept $\sigma_N \in \{0.02, 0.1, 0.3, 1.0, 3.0\}$ and reported the first-stage F-statistic alongside each IV estimate. At $\sigma_N=0.02$ (F=1.6, well below the F<10 rule of thumb), the IV estimate is worthless (std of 1.66 and 9.45 on the two conditions — larger than the effect itself). At $\sigma_N=0.1$ (F=20.6) it starts working; by $\sigma_N \geq 0.3$ (F>180) it's essentially exact. **The method is real but not free** — it requires the channel to carry genuine exogenous variance, not just any noise, and the diagnostic (first-stage F) is cheap to compute and should always be reported alongside the estimate.

Outputs: `experiments/results/logs/paper2_noise_as_instrument.json`, `experiments/results/plots/paper2_noise_as_instrument.png`.

**Fed back into the paper**: `paper2/main.tex` Remark 2 (§4.1) and the corresponding limitations-section caveat updated to report this as demonstrated rather than asserted; recompiled clean.

**What this does *not* yet establish**: this is a linear-Gaussian toy matching the theorem's proof structure, not a demonstration on real (nonlinear, non-Gaussian) hyperscanning or RL data. The natural next step — flagged but not started — is applying the same instrument logic to the existing `experiments/paper1_rl/` Stage 2 system (its trained-channel noise, e.g. from the Gumbel-Softmax relaxation temperature or dropout, could serve as a real instrument) or to a real hyperscanning corpus's channel dropout/jitter, to check the method survives contact with a system that wasn't built to make it work.

## 🔜 Next (not started)

- [ ] Apply the same instrument to `experiments/paper1_rl/`'s trained Stage 2 system — does channel noise there recover the known-near-zero functional coupling found in that system's own oracle control?
- [ ] Identify a concrete exogenous-noise source in a public hyperscanning corpus (`ds007764`, `ds007471` — see `experiments/paper2_hyperscanning/TODO.md`) and check whether the independence-from-shared-history assumption is remotely plausible before trying it on real data.
