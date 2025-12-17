# Student Enrollment AI Forecast

This project demonstrates how AI-inspired modeling and synthetic data can be used to forecast student enrollment under demographic and policy uncertainty.

## Project Objective
To simulate and forecast the evolution of student enrollment for a school class using:
- synthetic demographic indicators
- an explicit growth coefficient
- an AI-augmented forecasting perspective

The project focuses on **model transparency**, **interpretability**, and **AI-assisted decision support** rather than black-box prediction.

---

## Methodology

### 1. Synthetic Data Generation
Historical enrollment data is generated synthetically using:
- birth rate index
- migration index
- school attractiveness
- policy shocks

These variables are combined into an annual growth coefficient:
r(t) = base_rate
+ demographic effects
+ policy shock
+ stochastic noise


# Student Enrollment AI Forecast

This project demonstrates how AI-inspired modeling and synthetic data can be used to forecast student enrollment under demographic and policy uncertainty.

## Project Objective
To simulate and forecast the evolution of student enrollment for a school class using:
- synthetic demographic indicators
- an explicit growth coefficient
- an AI-augmented forecasting perspective

The project focuses on **model transparency**, **interpretability**, and **AI-assisted decision support** rather than black-box prediction.

---

## Methodology

### 1. Synthetic Data Generation
Historical enrollment data is generated synthetically using:
- birth rate index
- migration index
- school attractiveness
- policy shocks

These variables are combined into an annual growth coefficient:


This allows explainable and scenario-based forecasting.

---

### 2. Coefficient-Based Forecasting
Instead of directly predicting enrollment, the model predicts **growth dynamics** through a defined coefficient.

This approach mirrors real-world decision models used in:
- public policy
- education planning
- economic forecasting

---

### 3. AI-Augmented Extension (Next Step)
The project is designed to be extended with:
- LLM-assisted scenario interpretation (OpenAI / Gemini)
- AI-generated explanations of forecast drivers
- natural-language policy simulations

---

## Project Structure
student-enrollment-ai-forecast/
├── notebooks/
│ └── 01_generate_synthetic_data.ipynb
├── data/
│ └── synthetic_enrollment.csv
├── src/
│ └── (future forecasting modules)
├── README.md


---

## Tech Stack
- Python 3.12
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook

---

## Why This Project Matters
This project illustrates:
- how AI engineers think in **systems and coefficients**
- how synthetic data can replace unavailable real-world data
- how AI can support **transparent decision-making**

It bridges **data science**, **AI engineering**, and **policy-oriented modeling**.
