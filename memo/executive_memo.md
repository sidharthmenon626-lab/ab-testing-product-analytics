# Milestone 5: Executive Decision Memorandum

```
===================================================================================================
MEMORANDUM | PRODUCT & GROWTH EXECUTIVE COMMITTEE
TO:        Chief Product Officer (CPO), VP of Growth, Lead Product Manager
FROM:      Lead Product Analytics Engineer
DATE:      May 19, 2024
SUBJECT:   EXPERIMENT AUDIT & SHIP DECISION: HOMEPAGE V2 REDESIGN (EXP-2024-05)
DECISION:  DO NOT SHIP GLOBALLY; APPROVE STAGED DESKTOP ROLLOUT ONLY
===================================================================================================
```

---

### Executive Recommendation

**Recommendation: DO NOT SHIP GLOBALLY.**  
While headline signup conversion achieved nominal statistical significance ($2.84\% \rightarrow 3.21\%$, $+0.37\text{pp}$, $p = 0.0150$), shipping Homepage V2 to $100\%$ of production traffic will **destroy net platform revenue**, mask a **$-42.6\%$ novelty decay**, and inflict severe conversion damage on **Mobile users** ($50\%$ of our customer base).

Instead, leadership should authorize a **Conditional Desktop-Only Rollout** (capturing a verified $+26.9\%$ conversion lift with neutral ARPU) while immediately rolling back Mobile traffic to Control for layout remediation.

---

### 1. Executive Summary Table

| Metric / Diagnostic Gate | Control ($N=25,053$) | Variant ($N=24,947$) | Delta / Lift | Test Statistic & $p$-Value | Gate Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Metric: Signup Conversion** | $2.84\%$ ($712$) | $3.21\%$ ($802$) | **$+0.37\text{pp}$** ($+13.1\%$) | $Z = 2.43$, $p = 0.0150$ | ⚠️ Below MDE ($+0.50\text{pp}$) |
| **95% Wald Confidence Interval** | — | — | $[+0.07\text{pp}, +0.67\text{pp}]$ | $\alpha = 0.05$ | ⚠️ Lower bound near zero |
| **Desktop Segment Conversion** | $3.39\%$ ($426$) | $4.31\%$ ($535$) | **$+0.91\text{pp}$** ($+26.9\%$) | $Z = 3.75$, $p < 0.001$ | 🟢 Strong Winner |
| **Mobile Segment Conversion** | $2.29\%$ ($286$) | $2.13\%$ ($267$) | **$-0.16\text{pp}$** ($-6.9\%$) | $Z = -0.81$, $p = 0.421$ | 🔴 Regressed / Ineffective |
| **Guardrail Metric: 30-Day ARPU** | **\$3.31** | **\$2.92** | **-\$0.39** ($-11.9\%$) | Welch's $t = -2.14$, $p = 0.0323$ | 🔴 Statistically Significant Drop |
| **Sample Ratio Mismatch (SRM)** | $25,053$ ($50.1\%$) | $24,947$ ($49.9\%$) | Expected 50/50 | $\chi^2 = 0.2247$, $p = 0.6355$ | 🟢 Gate Passed (No SRM) |
| **Temporal Stability (Novelty)** | W1: $+0.47\text{pp}$ | W2: $+0.27\text{pp}$ | $-0.20\text{pp}$ Fade | $-42.6\%$ decay rate | ⚠️ Novelty Wear-Off |

---

### 2. Situation: Experiment Setup & Initial Claims
* **Experiment Scope**: Evaluated the 14-day Homepage V2 redesign across 50,000 randomized visitors ($25,053$ Control vs. $24,947$ Variant).
* **Traffic Allocation Integrity**: Pearson Chi-Square test confirmed **zero Sample Ratio Mismatch** ($\chi^2 = 0.2247, p = 0.6355$). Randomization and routing mechanisms functioned properly.
* **The Growth Team Claim**: The PM argues that because headline signup conversion rose from $2.84\%$ to $3.21\%$ ($+13.1\%$ relative lift, $p = 0.0150 < 0.05$), the redesign is a proven winner that must be shipped immediately to hit quarterly acquisition targets.

---

### 3. Complication: The 4 Fatal Audit Flaws

#### 1. MDE Gap: Lift Fails Pre-Registered Business Hurdle
The experiment's pre-registered Minimum Detectable Effect (MDE) was powered at **$+0.50\text{pp}$** to justify development, QA, and maintenance overhead. The observed point estimate of **$+0.37\text{pp}$** falls **$26\%$ short** of this hurdle. Furthermore, the 95% Wald Confidence Interval ($[+0.07\text{pp}, +0.67\text{pp}]$) shows that the true population lift may be as low as $+0.07\text{pp}$—an economically negligible gain.

#### 2. Novelty Fade: Early Lift Collapsed by 42.6%
Tracking conversion week-over-week reveals severe temporal degradation:
* **Week 1 Lift**: **$+0.47\text{pp}$** ($3.37\%$ Variant vs. $2.90\%$ Control).
* **Week 2 Lift**: **$+0.27\text{pp}$** ($3.05\%$ Variant vs. $2.78\%$ Control).
Lift degraded by **$42.6\%$** in seven days. The headline metric was artificially inflated by visual novelty and curious exploratory clicks that rapidly dissipated.

#### 3. Monetization Guardrail Breach: Statistically Significant Revenue Destruction
A primary metric lift is dangerous if it attracts non-monetizing traffic:
* Total 30-day ARPU declined from **\$3.31** to **\$2.92**, representing a net loss of **-\$0.39 per visitor (-11.9%)**.
* Welch's Two-Sample T-Test confirms this monetization loss is statistically significant (**$t = -2.14, p = 0.0323 < 0.05$**).
* Among converted users, average spend dropped by **$22.2\%$** (\$116.59 in Control vs. \$90.71 in Variant). The simplified copy attracted free-tier, low-intent users while diluting paying customer acquisition.

#### 4. Simpson's Paradox: Severe Mobile Viewport Regression
Aggregating traffic masks a stark platform divergence:
* **Desktop ($50\%$ of traffic)**: A verified winner. Conversion increased from $3.39\%$ to $4.31\%$ (**$+0.91\text{pp}$**, $+26.9\%$, $p < 0.001$), while ARPU remained stable (\$3.95 vs. \$3.92).
* **Mobile ($50\%$ of traffic)**: A regression. Conversion dropped from $2.29\%$ to $2.13\%$ (**$-0.16\text{pp}$**, $-6.9\%$, $p = 0.421$), and ARPU collapsed by **$-28.1\%$** (\$2.67 $\rightarrow$ \$1.92, a **-\$0.75 loss per user**).
* **Root Cause Synergy**: The new hero module pushes the primary signup CTA below the fold on mobile viewports. This compounds the acute mobile checkout friction uncovered in Milestone 2, where mobile users experienced a **$31.00\text{pp}$ completion deficit** at Cart-to-Checkout.

---

### 4. Defending Against Stakeholder Pushback

| Anticipated PM / Growth Pushback | Analytical Counter-Defense Grounded in Telemetry |
| :--- | :--- |
| *"P-value is 0.015 (< 0.05), so the lift is statistically real. We cannot ignore a win."* | Statistical significance only confirms the lift is non-zero; it does not confirm business viability. The $+0.37\text{pp}$ lift failed the $+0.50\text{pp}$ MDE, and true lift could be as low as $+0.07\text{pp}$ (95% CI). More critically, statistical significance also proves our **revenue dropped by $-11.9\%$ ($p = 0.0323$)**. |
| *"More signups will naturally lead to more revenue over a longer horizon."* | Our 30-day cohort telemetry refutes this. Milestone 3 proved that retention flattens after Month 3, and variant cohorts entered the funnel spending **$22.2\%$ less** (\$90.71 vs. \$116.59). Higher signup volume at lower basket value produces negative net platform ROI. |
| *"Mobile performance is flat ($p=0.421$), not a confirmed loser. Let's ship and iterate."* | Mobile conversion trended negative ($-0.16\text{pp}$) and mobile ARPU plummeted by **$-28.1\%$** ($-\$0.75$/user). Half our traffic is mobile. Rolling out an unoptimized mobile viewport that buries the primary CTA destroys monetization across half the business. |

---

### 5. Resolution & Concrete 3-Point Action Plan

#### Phase 1: Conditional Desktop-Only Staged Rollout (Immediate — Days 1–3)
* Deploy Homepage V2 exclusively to Desktop traffic ($50\%$ platform traffic).
* Realizes an estimated **$+26.9\%$ desktop signup lift** (+109 incremental signups in the test cohort: $535$ vs. $426$) with neutral monetization (\$3.95 vs. \$3.92 ARPU).

#### Phase 2: Mobile Viewport Rollback & Layout Remediation (Sprint 1)
* Revert $100\%$ of Mobile traffic to Control homepage immediately.
* Design **Mobile Homepage V2.1**:
  * Pin the primary signup CTA and value proposition above the 600px viewport fold.
  * Eliminate the bulky 3-column product showcase cards on mobile viewports.
  * Integrate fixes for the Step 3 $\rightarrow$ Step 4 mobile checkout drop-off identified in Milestone 2.
* Re-launch as a dedicated Mobile-only A/B test (EXP-2024-06) with a pre-set $+0.50\text{pp}$ MDE.

#### Phase 3: Monetization Safeguard Implementation (Sprint 2)
* Introduce in-app premium tier discovery prompts and onboarding checklists during Days 1–14 to recover the $22.2\%$ basket size drop.
* Tie executive experiment sign-off gates to **both** conversion and 30-day ARPU parity.
