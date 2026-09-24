# A/B Testing & Product Experimentation Analysis

**Business question:** A 50,000-user homepage A/B test reports a +13% conversion lift (p = 0.015). Should we ship to 100% of users?

This repo audits the experiment's integrity, surfaces hidden friction, and ends with an executive recommendation.

## Dataset
`data/homepage_ab_test.csv` (50,000 rows): experiment assignment, conversion events, device type, revenue, and temporal windows. *(Download from the Topfolio workspace and place here; not committed if restricted.)*

## Milestones
| # | Milestone | Notebook / Output | Status |
|---|-----------|-------------------|--------|
| 1 | Project setup | this repo | Done |
| 2 | Funnel & friction analysis (dedup, device drop-off) | `notebooks/02_funnel_analysis.ipynb` | Todo |
| 3 | Cohort retention matrices (Seaborn heatmaps) | `notebooks/03_cohort_retention.ipynb` | Todo |
| 4 | Statistical diagnostics (Z-test, CI, Welch's t, SRM, novelty) | `notebooks/04_statistical_tests.ipynb` | Todo |
| 5 | Executive decision memo (SCR framework) | `memo/executive_memo.md` | Todo |

## Structure
```
data/       raw CSV + deduplicated output (e.g. homepage_ab_test_dedup.csv)
notebooks/  one notebook per milestone
src/        reusable analysis functions
figures/    exported charts
memo/       1-page CPO memo
```

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

## Key findings
_To be completed after Milestone 4._

## Recommendation
_To be completed in Milestone 5._
