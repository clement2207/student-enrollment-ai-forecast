from dataclasses import dataclass
import numpy as np
import pandas as pd

@dataclass
class CoefficientParams:
    base_rate: float = -0.010
    w_birth: float = 0.060
    w_migration: float = 0.050
    w_attract: float = 0.040

def compute_growth_rate(df: pd.DataFrame, params: CoefficientParams) -> np.ndarray:
    return (
        params.base_rate
        + params.w_birth * (df["birth_rate_index"].to_numpy() - 1.0)
        + params.w_migration * (df["migration_index"].to_numpy() - 1.0)
        + params.w_attract * (df["school_attractiveness"].to_numpy() - 1.0)
        + df["policy_shock"].to_numpy()
    )
