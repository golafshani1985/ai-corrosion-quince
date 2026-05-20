# AI-Based Corrosion Inhibition Prediction Using Quince Extract

This project uses machine learning models to predict the corrosion inhibition efficiency (IE%) of quince extract for St37 steel in acidic environments.

## Current Stage

Initial baseline models were built using experimental data from Article 1 and Article 2.

## Input Features

- Temperature (K)
- Quince extract concentration (ppm)
- Electrochemical method code

## Target

- Inhibition efficiency (IE%)

## Models Used

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

## Evaluation Metrics

- MAE
- MSE
- RMSE
- R2 Score

## Model Comparison Results

The baseline model comparison results are saved in:

`reports/model_comparison_results.csv`

This file includes the evaluation metrics for Linear Regression, Random Forest Regressor, and XGBoost Regressor.

## XGBoost Prediction Plot

The actual versus predicted inhibition efficiency plot for the XGBoost model is saved in:

`reports/xgboost_actual_vs_predicted.png`

This plot compares the experimental IE% values with the IE% values predicted by the XGBoost model.

## Next Steps

- Add Article 3 data
- Add acid type as a feature
- Apply cross-validation
- Add molecular descriptors from DFT and MD simulations