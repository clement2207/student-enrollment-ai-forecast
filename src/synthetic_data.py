import numpy as np
import pandas as pd

def generate_synthetic_enrollment(
    start_year: int = 2012,
    end_year: int = 2025,
    initial_students: int = 30,
    seed: int = 42
) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    years = np.arange(start_year, end_year + 1)
    n = len(years)

    birth_rate_index = np.clip(1.0 + np.linspace(0.05, -0.05, n) + rng.normal(0, 0.03, n), 0.8, 1.2)
    migration_index  = np.clip(1.0 + np.linspace(0.02, -0.02, n) + rng.normal(0, 0.04, n), 0.8, 1.2)
    attractiveness   = np.clip(1.0 + rng.normal(0, 0.03, n), 0.85, 1.15)

    policy_shock = np.zeros(n)
    shock_years = rng.choice(np.arange(n), size=max(1, n // 8), replace=False)
    policy_shock[shock_years] = rng.choice([-0.03, -0.02, 0.02, 0.03], size=len(shock_years))

    base_rate = -0.010
    r = (
        base_rate
        + 0.060 * (birth_rate_index - 1.0)
        + 0.050 * (migration_index - 1.0)
        + 0.040 * (attractiveness - 1.0)
        + policy_shock
        + rng.normal(0, 0.010, n)
    )

    students = np.zeros(n, dtype=float)
    students[0] = initial_students
    for i in range(1, n):
        students[i] = np.clip(students[i-1] * (1 + r[i]), 10, 45)

    students = np.rint(students).astype(int)

    return pd.DataFrame({
        "year": years,
        "students": students,
        "annual_growth_rate_r": r,
        "birth_rate_index": birth_rate_index,
        "migration_index": migration_index,
        "school_attractiveness": attractiveness,
        "policy_shock": policy_shock
    })
    