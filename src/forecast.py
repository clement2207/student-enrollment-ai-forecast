import numpy as np
import pandas as pd
from .coefficient_model import CoefficientParams, compute_growth_rate

def forecast_enrollment(
    df_hist: pd.DataFrame,
    years_ahead: int = 3,
    params: CoefficientParams = CoefficientParams(),
    scenario_adjustment: float = 0.0
) -> pd.DataFrame:
    df = df_hist.copy()
    last_year = int(df["year"].iloc[-1])
    last_students = float(df["students"].iloc[-1])

    base_r = compute_growth_rate(df.tail(1), params)[0] + scenario_adjustment

    future_years = np.arange(last_year + 1, last_year + years_ahead + 1)
    students = []
    current = last_students
    for _ in future_years:
        current = np.clip(current * (1 + base_r), 10, 60)
        students.append(int(round(current)))

    return pd.DataFrame({
        "year": future_years,
        "students_forecast": students,
        "assumed_growth_rate_r": [base_r] * len(future_years),
        "scenario_adjustment": [scenario_adjustment] * len(future_years),
    })

if __name__ == "__main__":
    import pandas as pd

    print("Running forecast module...")

    df = pd.read_csv("data/synthetic_enrollment.csv")
    print("Loaded data:")
    print(df.tail())

    out = forecast_enrollment(df, years_ahead=3)
    print("\nForecast result:")
    print(out)