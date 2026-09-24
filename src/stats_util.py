"""Reusable statistical helpers for the A/B test audit."""
from __future__ import annotations

from typing import Tuple

import numpy as np
from scipy import stats


def two_prop_ztest(x1: int, n1: int, x2: int, n2: int) -> Tuple[float, float]:
    """Two-sided pooled two-proportion z-test. Returns (z, p_value)."""
    p_pool = (x1 + x2) / (n1 + n2)
    se = np.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    z = (x2 / n2 - x1 / n1) / se if se > 0 else np.nan
    return z, 2 * (1 - stats.norm.cdf(abs(z)))


def wald_ci(x1: int, n1: int, x2: int, n2: int, alpha: float = 0.05) -> Tuple[float, float]:
    """Wald CI for difference in proportions (treatment - control)."""
    p1, p2 = x1 / n1, x2 / n2
    se = np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    z = stats.norm.ppf(1 - alpha / 2)
    d = p2 - p1
    return d - z * se, d + z * se
