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

## Next Steps

- Add Article 3 data
- Add acid type as a feature
- Apply cross-validation
- Add molecular descriptors from DFT and MD simulations