# EDA Findings — Project 2

## Project title

Descriptor and simulation-based corrosion inhibition analysis of quince-derived inhibitors.

---

## 1. Dataset overview

Two clean datasets were created from the raw descriptor workbook.

### Article 2 clean dataset

File:

`data/processed/article2_clean_temperature_target_v1.csv`

This dataset contains temperature-dependent data for 4-O-CQA / quince extract at 308, 318, and 328 K.

Each temperature appears twice because two experimental methods were used:

- Polarization
- EIS

Dataset shape:

- 6 rows
- 43 columns

### Article 3 clean dataset

File:

`data/processed/article3_clean_molecular_ranking_v1.csv`

This dataset contains molecule-level QM descriptors and adsorption energies for four CQA derivatives:

- 3-O-CQA
- 4-O-CQA
- 5-O-CQA
- 5-O-CQA-H+

Dataset shape:

- 4 rows
- 32 columns

---

## 2. Missing value check

For Article 2, selected key descriptor and target columns were complete, except for method-specific experimental values:

- `icorr` is missing in EIS rows.
- `Rct` is missing in polarization rows.

This is expected because `icorr` belongs to polarization measurements, while `Rct` belongs to EIS measurements.

For Article 3, the selected descriptor and adsorption-energy columns had no missing values.

---

## 3. Article 2: Inhibition efficiency vs temperature

The inhibition efficiency decreases as temperature increases from 308 K to 328 K.

Polarization data show a decrease from about 91% at 308 K to about 81% at 328 K.

EIS data show a decrease from about 88.5% at 308 K to about 78% at higher temperatures. The EIS values are almost stable between 318 K and 328 K.

This suggests that the protective inhibition effect becomes weaker at higher temperature.

---

## 4. Article 2: Adsorption energy vs temperature

The adsorption energy becomes more negative as temperature increases.

This suggests stronger predicted adsorption in the simulation data at higher temperature.

However, this trend does not directly match the experimental inhibition efficiency, which decreases with increasing temperature.

Therefore, adsorption energy alone cannot fully explain the experimental inhibition efficiency trend. Temperature-dependent electrochemical kinetics and protective film stability are likely important additional factors.

---

## 5. Article 3: Adsorption energy ranking

Based on adsorption energy, the molecular adsorption strength ranking is:

1. 5-O-CQA
2. 3-O-CQA
3. 5-O-CQA-H+
4. 4-O-CQA

The strongest predicted adsorption on Fe(110) was observed for 5-O-CQA.

---

## 6. Article 3: HOMO-LUMO gap and hardness

5-O-CQA-H+ showed the lowest HOMO-LUMO energy gap and the lowest chemical hardness.

This suggests that 5-O-CQA-H+ has the highest electronic reactivity among the studied molecules.

However, 5-O-CQA-H+ did not show the strongest adsorption energy.

This means that adsorption strength and electronic reactivity do not necessarily follow the same molecular ranking.

---

## 7. Correlation analysis

Correlation analysis was performed as an exploratory step.

### Article 2

Temperature showed a strong negative correlation with inhibition efficiency, consistent with the observed decrease in inhibition efficiency at higher temperature.

Adsorption energy showed a positive correlation with inhibition efficiency, but this must be interpreted carefully because adsorption energy values are negative.

The Article 2 correlation results are exploratory only because the dataset contains only six rows.

### Article 3

Energy gap and hardness showed moderate negative correlations with adsorption energy.

EHOMO and fraction of electron transfer showed moderate positive correlations with adsorption energy.

These correlations are exploratory only because the Article 3 dataset contains only four molecules.

---

## 8. Main scientific conclusion

The EDA suggests that corrosion inhibition behavior cannot be explained by a single descriptor.

Adsorption energy describes molecule-surface interaction strength.

HOMO-LUMO gap and hardness describe electronic reactivity.

Temperature strongly affects experimental inhibition efficiency.

Therefore, this project should be interpreted as a multi-descriptor corrosion inhibition analysis rather than a simple one-feature prediction problem.

---

## 9. Next step

The next step is to build baseline models carefully, with strong attention to the small dataset size and scientific limitations.
