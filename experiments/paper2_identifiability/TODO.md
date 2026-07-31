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

## ✅ Done — noise-as-instrument on the real Stage 2 system (2026-07-31, same day)

`noise_as_instrument_stage2.py` applies the exact same method to a system this project did not design to make it work: the trained Stage 2 PettingZoo speaker/listener (paper's "best config" — dual auxiliary loss, `entropy_coef=0.02`, B=8, 20000 episodes). **Result: the instrument fails, and the failure is itself the finding.**

**Setup.** Retrained the best-config policy from scratch (reproducibility check: this run's direct-intervention numbers — real $-15.87$, ablated $-16.45$ ($z{=}{+}0.50$), randomised $-18.19$ ($z{=}{+}1.82$) — are *identical* to the numbers already in the paper, confirming the training is deterministic-enough to reproduce). Then, for 150 fixed goals (env seeds) × 20 independent redraws of the Gumbel channel's own logistic noise per goal (injected externally, decoupled from torch's global RNG; listener acts greedily so noise is the only source of within-goal trajectory variation), ran the full 25-step episode and recorded (mean message, mean injected noise, episode return) per rollout — 3000 full rollouts total.

**Outcome:**

| | value |
|---|---|
| Naive OLS (return on mean message) | $+5.150$, 95% CI $[+2.660, +7.628]$ |
| IV estimate (noise-as-instrument) | $+9.538$, 95% CI $[-715, +886]$ |
| First-stage F-statistic | **0.2** — far below the $F\gtrsim10$ threshold established in the toy demo |

The instrument is unusable here, and the diagnostic caught it correctly rather than silently reporting the (meaningless) point estimate. **Root cause, confirmed by direct variance decomposition**: across the 20 noise-only resamples of the same goal, the message barely moves at all — within-goal (noise-driven) variance is **0.3%** of total message variance; across-goal (goal-driven) variance is **99.7%**. The scatter plot (`paper2_noise_as_instrument_stage2.png`) shows why visually: messages cluster into two tight, near-discrete bands by goal, with almost no horizontal spread within a band.

**Why**: a heavily auxiliary-supervised straight-through Gumbel encoder (this system's `aux_coef=200` pushes speaker encoding to $R^2\approx0.9$) is trained to push its logits to confident extremes, because that's what makes the hard threshold reliable and the auxiliary reconstruction loss converge. But confident logits sit far from the sigmoid's decision boundary, so the channel's own per-step logistic noise essentially never flips the hard output. **The training objective that makes the message informative is the same thing that starves the channel's noise of relevance as an instrument.** This is a real, previously undocumented boundary condition on the method, not a bug — verified by the variance decomposition, not merely inferred from the low F-stat.

**Implication for the paper and for future use of this method**: the toy demonstration (first entry, above) still stands — the method is mathematically sound and works when the instrument has genuine bite. But applying it to *any* trained discrete-communication system carries a specific, checkable risk: well-optimized encoders trend toward low-entropy, saturated codes, which is exactly the regime where transmission noise stops being informative about the message, independent of whether real functional coupling is present or absent. **Always compute the first-stage F before trusting an IV estimate on a trained system** — this result is the demonstration of why that rule exists, not just a restatement of it. Human/biological channels (speech, EEG artifact, TMS jitter) are not "trained" to be maximally decodable through a threshold the way this Gumbel channel is, so this specific failure mode may be less severe for the hyperscanning application than for learned discrete emergent-communication channels — but that is a claim to check, not assume, before trying real hyperscanning data.

Outputs: `experiments/results/logs/paper2_noise_as_instrument_stage2_seed42.json`, `experiments/results/plots/paper2_noise_as_instrument_stage2.png`.

**Fed back into the paper**: `paper2/main.tex` Remark 2 and Limitations updated with this result — see main text.

## 🔜 Next (not started)

- [ ] Identify a concrete exogenous-noise source in a public hyperscanning corpus (`ds007764`, `ds007471` — see `experiments/paper2_hyperscanning/TODO.md`) and check whether the independence-from-shared-history assumption is remotely plausible before trying it on real data. Given the Stage 2 finding above, also explicitly check the corpus's channel-noise first-stage F/instrument strength before trusting any resulting estimate — real speech/EEG channels are the test of whether the saturation failure mode found here is specific to trained discrete emergent-communication channels or more general.
- [ ] Consider whether an *undertrained* or intentionally noise-injected (e.g. channel dropout during training, or a colder Gumbel temperature) version of the Stage 2 speaker would restore instrument strength — testing directly whether the saturation diagnosis is correct and whether it's fixable, rather than just diagnosed.
