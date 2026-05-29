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

The diagonal reference line represents the ideal prediction condition where:

`Predicted IE% = Actual IE%`

Points closer to this line indicate better prediction performance.

## Current Limitations

The current dataset is relatively small because it is based on experimental data extracted from Article 1 and Article 2.

Therefore, the current model results should be considered as preliminary baseline results.

Although XGBoost showed the best performance in the current train-test split, the dataset size is limited and the results may depend on the selected train-test split.

In the next step, cross-validation will be applied to evaluate the models more reliably.

## Cross-Validation Results

To reduce the dependence of the model evaluation on a single train-test split, 5-fold cross-validation was applied.

The cross-validation results showed that XGBoost achieved the highest mean R2 score among the tested models. However, the relatively high standard deviation indicates that the model performance is still sensitive to data splitting, mainly due to the limited dataset size.

The cross-validation results are saved in:

`reports/cross_validation_results.csv`

This file includes the mean and standard deviation of R2, MAE, and RMSE for each model.

## Data Sources and Related Publications

The experimental dataset used in this project was manually extracted from three peer-reviewed research articles authored/co-authored by the project owner. These studies investigate the corrosion inhibition performance of quince extract and its bioactive compounds for St37/mild steel in acidic media.

The extracted dataset includes experimental variables such as inhibitor concentration, temperature, electrochemical method, acid type, and inhibition efficiency (IE%).

### Related Publications

1. **Corrosion and Electrochemical Characterization of St37 in the Presence of Quince Extract as a Green and Sustainable Inhibitor**  
   DOI: https://doi.org/10.1007/s12678-022-00788-6

2. **Quantum Chemical and Molecular Dynamics Study of Quince Extract as a Corrosion Inhibitor for St37 Steel in Acidic Solution**  
   DOI: https://doi.org/10.1016/j.rechem.2025.102107

3. **MD and DFT Computational Simulations of Caffeoylquinic Derivatives as a Bio-Corrosion Inhibitor from Quince Extract with Experimental Investigation of Corrosion Protection on Mild Steel in 1M H2SO4**  
   DOI: https://doi.org/10.1016/j.molstruc.2022.134701
   
## Project Structure

```text
project/
├── data/
│   ├── raw/              Original raw data files
│   └── processed/        Cleaned and processed data files
├── notebooks/            Jupyter notebooks for data analysis and model training
├── reports/              Model results, plots, and output files
├── README.md             Project description and instructions
├── requirements.txt      Required Python packages
└── .gitignore            Files and folders ignored by Git
```

## How to Run

Install the required packages using:

pip install -r requirements.txt

Then open and run:

notebooks/01_baseline_model.ipynb

## Next Steps

- Add Article 3 data
- Add acid type as a feature
- Apply cross-validation
- Add molecular descriptors from DFT and MD simulations

