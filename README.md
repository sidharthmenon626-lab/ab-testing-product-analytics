# A/B Testing & Product Experimentation Analytics: PulseFlow

**Business Question:** *A 50,000-user homepage A/B test reports a +13% conversion lift ($p = 0.015$). Should we ship to 100% of users?*

This repository delivers an end-to-end product analytics audit evaluating experimental validity, funnel friction, longitudinal cohort retention, and monetization guardrails to produce an executive go/no-go rollout decision.

---

## Project Milestones

| # | Milestone | Primary Deliverables | Status |
|---|---|---|:---:|
| **1** | **Project Setup & Repository Architecture** | Repository scaffolding, dependencies, virtual environment | ✅ Done |
| **2** | **Funnel & Friction Analysis** | [`notebook/02_funnel_analysis.ipynb`](notebook/02_funnel_analysis.ipynb)<br>[`findings/02_funnel_friction.md`](findings/02_funnel_friction.md) | ✅ Done |
| **3** | **Cohort Retention Dynamics** | [`notebook/03_cohort_retention.ipynb`](notebook/03_cohort_retention.ipynb)<br>[`findings/03_retention_dynamics.md`](findings/03_retention_dynamics.md) | ✅ Done |
| **4** | **A/B Test Statistical Diagnostics** | [`notebook/04_ab_test_evaluation.ipynb`](notebook/04_ab_test_evaluation.ipynb)<br>[`findings/04_experiment_diagnostics.md`](findings/04_experiment_diagnostics.md) | ✅ Done |
| **5** | **Executive Decision Memorandum** | [`memo/executive_memo.md`](memo/executive_memo.md) | ✅ Done |

---

## Repository Structure

```
ab-testing-product-analytics/
├── data/
│   └── homepage_ab_test.csv        # 50,000-user A/B test telemetry log
├── figures/
│   ├── funnel_overall_dropoff.png         # Step-by-step conversion waterfall
│   ├── funnel_conversion_by_device.png    # Mobile vs. Desktop stage completion
│   ├── funnel_cumulative_divergence.png   # Stage-by-stage platform divergence
│   ├── cohort_retention_heatmap.png       # Annotated triangular retention matrix
│   ├── cohort_retention_curves.png        # Longitudinal retention decay curves
│   ├── ab_test_conversion_ci.png          # Primary lift with 95% Wald CI error bars
│   ├── ab_test_segment_breakdown.png      # Simpson's slice: Desktop vs. Mobile
│   └── ab_test_weekly_novelty.png         # Temporal novelty decay (Week 1 vs. Week 2)
├── findings/
│   ├── 02_funnel_friction.md       # Drop-off analysis & mobile friction hypothesis
│   ├── 03_retention_dynamics.md    # Asymptotic flattening & PMF curve assessment
│   └── 04_experiment_diagnostics.md # Statistical audit summary & failure-mode checks
├── memo/
│   └── executive_memo.md           # 1-page CPO executive decision memo (Minto SCR)
├── notebook/
│   ├── 02_funnel_analysis.ipynb    # In-memory clickstream deduplication & funnel stages
│   ├── 03_cohort_retention.ipynb   # Feature engineering, matrix pivot, & Seaborn heatmap
│   └── 04_ab_test_evaluation.ipynb # Z-test, Wald CI, Welch's t-test, SRM, novelty audit
├── src/
│   └── stats_util.py               # Reusable two-proportion Z-test & Wald CI helpers
├── requirements.txt                # Python environment specifications
└── README.md                       # Project overview, findings, & recommendations
```

---

## Key Findings (Milestones 2–4 Audit)

### 1. Funnel Friction & Mobile Regressions (Milestone 2)
* **Overall Conversion:** Platform baseline conversion from Homepage Landing to Signup Completion is **$13.01\%$** ($1,301$ completions across $10,000$ unique visitors: 5,004 Desktop, 4,996 Mobile).
* **Mobile Checkout Collapse:** The primary friction point is **Step 3 $\rightarrow$ Step 4 (Add to Cart to Checkout Start)**. Mobile step completion drops to **$30.14\%$** ($69.86\%$ drop-off) versus **$61.14\%$ on Desktop**—a staggering **$31.00\text{pp}$ deficit** on mobile.
* **Cumulative Platform Disparity:** End-to-end cumulative conversion exhibits a **$2.9\times$ disparity**: Desktop converts at **$19.26\%$** ($964$ users) versus only **$6.75\%$** ($337$ users) on Mobile ($+12.51\text{pp}$ gap).
* **Root Cause:** Mobile viewports force critical payment information and primary CTAs below the fold, driving premature cart abandonment.

### 2. Longitudinal Cohort Retention Dynamics (Milestone 3)
* **Product-Market Fit Baseline:** Tracking 1,200 users across 6 cohorts (Jan–Jun 2024) reveals an **Asymptotic Flattening Retention Curve** stabilizing at **$26.37\%–31.84\%$** from Month 4 onwards.
* **Bucket Leak Audit:** The bucket is **not** leaking faster. Month 1 retention across newer cohorts (Apr: $51.2\%$, May: $49.2\%$, Jun: $52.0\%$) matches or exceeds older cohorts (Jan: $47.9\%$, Feb: $46.4\%$).
* **Leverage Point:** Over **$68.6\%$** of all cumulative churn occurs in Month 1 (~$50.4\%$ initial drop-off), demonstrating that onboarding and Day 1–14 activation are the primary growth levers.

### 3. A/B Test Statistical Audit (Milestone 4)
Auditing the Growth Team's claim (*"Conversion lifted from 2.8% to 3.2%, p=0.015, ship immediately!"*) revealed that the global winner is an illusion driven by three critical failure modes:

| Diagnostic Gate | Control ($N=25,053$) | Variant ($N=24,947$) | Delta / Lift | Test Statistic & $p$-Value | Status / Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Metric (Signup Conversion)** | $2.84\%$ ($712$) | $3.21\%$ ($802$) | **$+0.37\text{pp}$** ($+13.1\%$) | $Z = 2.43$, $p = 0.0150$ | ⚠️ Below MDE ($+0.50\text{pp}$) |
| **95% Wald Confidence Interval** | — | — | $[+0.07\text{pp}, +0.67\text{pp}]$ | $\alpha = 0.05$ | ⚠️ Lower bound near zero |
| **Desktop Segment Conversion** | $3.39\%$ ($426$) | $4.31\%$ ($535$) | **$+0.91\text{pp}$** ($+26.9\%$) | $Z = 3.75$, $p < 0.001$ | 🟢 Strong Winner |
| **Mobile Segment Conversion** | $2.29\%$ ($286$) | $2.13\%$ ($267$) | **$-0.16\text{pp}$** ($-6.9\%$) | $Z = -0.81$, $p = 0.421$ | 🔴 Regressed / Ineffective |
| **Guardrail Metric: 30-Day ARPU** | **\$3.31** | **\$2.92** | **-\$0.39** ($-11.9\%$) | Welch's $t = -2.14$, $p = 0.0323$ | 🔴 Statistically Significant Drop |
| **Sample Ratio Mismatch (SRM)** | $25,053$ ($50.1\%$) | $24,947$ ($49.9\%$) | Expected 50/50 | $\chi^2 = 0.2247$, $p = 0.6355$ | 🟢 Gate Passed (No SRM) |
| **Temporal Stability (Novelty)** | W1: $+0.47\text{pp}$ | W2: $+0.27\text{pp}$ | $-0.20\text{pp}$ Fade | $-42.6\%$ decay rate | ⚠️ Novelty Wear-Off |

#### The Three Fatal Failure Modes:
1. **MDE Underperformance & Novelty Fade:** The $+0.37\text{pp}$ lift failed to clear the business case $+0.50\text{pp}$ MDE. Lift decayed by **$42.6\%$** in Week 2, signaling visual novelty wear-off.
2. **Monetization Guardrail Breach:** 30-day ARPU declined by **$11.9\%$** (\$3.31 $\rightarrow$ \$2.92, $p = 0.0323$), driven by a **$22.2\%$ drop in spend per converted user** (\$116.59 $\rightarrow$ \$90.71).
3. **Simpson's Paradox / Mobile Failure:** Desktop was a verified winner ($+0.91\text{pp}$, $+26.9\%$, $p < 0.001$), while Mobile regressed ($-0.16\text{pp}$, $-6.9\%$, $p = 0.421$) and mobile ARPU cratered by $-28.1\%$.

---

## Executive Recommendation

### Verdict: **DO NOT SHIP GLOBALLY**

Deploying Homepage V2 platform-wide would decrease net platform revenue and harm mobile user conversion.

### 3-Point Action Plan:
1. **Conditional Desktop-Only Rollout:** Ship Homepage V2 strictly to desktop traffic to capture the verified $+26.9\%$ conversion lift with neutral ARPU.
2. **Mobile Rollback & Viewport Remediation:** Revert mobile traffic to Control immediately. Redesign the mobile hero container to pin the primary signup CTA above the fold, remediating the friction discovered in Milestone 2.
3. **Monetization Safeguards:** Re-engineer the onboarding experience for variant signups to introduce premium tier discovery hooks before considering any future global deployment.

*(Read the complete CPO Executive Decision Memorandum in [`memo/executive_memo.md`](memo/executive_memo.md).)*

---

## Setup & Reproduction

```bash
# 1. Clone repository
git clone https://github.com/sidharthmenon626-lab/ab-testing-product-analytics.git
cd ab-testing-product-analytics

# 2. Initialize virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Jupyter Lab
jupyter lab
```
