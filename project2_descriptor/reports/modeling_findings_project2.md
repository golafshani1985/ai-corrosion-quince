# Modeling Findings — Project 2

## Project title

Descriptor-based baseline modeling of corrosion inhibition efficiency.

---

## 1. Modeling goal

The goal of this modeling step was to build simple exploratory baseline models using descriptor-based features from Article 2.

The target variable was:

`inhibition_efficiency_percent`

The selected input features were:

- temperature_K
- EHOMO_eV
- ELUMO_eV
- energy_gap_eV
- hardness_eV
- fraction_electron_transfer_deltaN
- adsorption_energy_kcal_mol

The goal was not to build a strong predictive model, but to test whether descriptor-based features show an initial signal for explaining inhibition efficiency.

---

## 2. Dataset used

Only the Article 2 clean dataset was used for baseline supervised modeling.

File:

`data/processed/article2_clean_temperature_target_v1.csv`

Dataset size:

- 6 rows
- 7 selected input features
- 1 target variable

The dataset contains three temperatures and two experimental methods:

- Polarization
- EIS

---

## 3. Models tested

Two simple regression models were tested:

1. Linear Regression
2. Ridge Regression

Both models were evaluated using:

- training performance
- Leave-One-Out cross-validation

Leave-One-Out cross-validation was selected because the dataset contains only six rows.

---

## 4. Linear Regression results

### Training performance

- MAE ≈ 2.10
- RMSE ≈ 2.34
- R² ≈ 0.78

### Leave-One-Out cross-validation performance

- MAE ≈ 4.21
- RMSE ≈ 4.68
- R² ≈ 0.13

The Linear Regression model showed much weaker performance under cross-validation than on the training data.

This indicates that the model has limited predictive ability on unseen rows.

---

## 5. Ridge Regression results

### Training performance

- MAE ≈ 2.10
- RMSE ≈ 2.34
- R² ≈ 0.78

### Leave-One-Out cross-validation performance

- MAE ≈ 4.04
- RMSE ≈ 4.47
- R² ≈ 0.21

Ridge Regression slightly improved the cross-validation metrics compared with Linear Regression.

However, the improvement was small and the model is still limited by the very small dataset size.

---

## 6. Model comparison

Ridge Regression showed slightly better Leave-One-Out cross-validation performance than Linear Regression:

- Linear Regression CV R² ≈ 0.13
- Ridge Regression CV R² ≈ 0.21

However, both models should be interpreted as exploratory baselines only.

The dataset is too small to support strong predictive conclusions.

---

## 7. Actual vs predicted interpretation

The actual vs predicted comparison showed that the Ridge model captures part of the temperature-related trend, but the row-level predictions are limited.

One important limitation is that the experimental method was not included as an input feature.

As a result, the model cannot fully distinguish between polarization and EIS rows at the same temperature.

---

## 8. Main modeling conclusion

The descriptor-based features show a limited initial signal for explaining inhibition efficiency.

However, the current dataset is too small for reliable supervised machine learning.

The modeling results should be reported as proof-of-concept baseline modeling, not as a validated predictive model.

---

## 9. Recommended next step

Future modeling should include a larger dataset with more molecules, more experimental conditions, and consistent molecule-level targets.

For the current project, the baseline models are sufficient to demonstrate the workflow:

raw data → clean descriptors → EDA → baseline modeling → scientific interpretation
