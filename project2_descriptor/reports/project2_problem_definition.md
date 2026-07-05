# Project 2 Problem Definition

## Project title

Descriptor and simulation-based analysis of quince-derived corrosion inhibitors.

---

## 1. Scientific question

Can quantum chemical descriptors and molecular simulation adsorption data explain or rank the corrosion inhibition behavior of quince-derived molecules?

The project aims to connect three scientific layers:

1. Molecular electronic structure
2. Adsorption behavior on Fe(110) surface
3. Experimental corrosion inhibition performance

---

## 2. Main scientific idea

In corrosion inhibition, organic molecules can protect steel by adsorbing on the metal surface and forming a protective layer. Molecules with suitable electronic properties and stronger adsorption may show better inhibition behavior.

In this project, the following relationship is investigated:

molecular descriptors -> adsorption behavior -> corrosion inhibition performance

The main descriptors include:

- EHOMO
- ELUMO
- HOMO-LUMO energy gap
- ionization potential
- electron affinity
- electronegativity
- hardness
- softness
- fraction of electron transfer
- adsorption energy

---

## 3. Data sources

This project currently uses two articles.

## Article 2

Article 2 studies quince extract as a corrosion inhibitor for St37 steel in 1 M HCl at different temperatures.

Main extracted data:

- Quantum chemical descriptors from Supplementary Table S3
- MD/MC adsorption-related energies from Supplementary Table S1
- Polarization targets from Table 2
- EIS targets from Table 3

Article 2 is mainly used for temperature-dependent descriptor-target analysis.

## Article 3

Article 3 studies caffeoylquinic acid derivatives from quince extract as corrosion inhibitors for mild steel in 1 M H2SO4.

Main extracted data:

- Molecular descriptors from Table 9
- Adsorption energies from Table 8
- Polarization target from Table 2
- EIS target from Table 3

Article 3 is mainly used for molecule-level ranking and interpretation.

---

## 4. Important distinction between Article 2 and Article 3

Article 2 and Article 3 should not be mixed blindly.

In Article 2, the computational and experimental data are more directly connected through temperature-dependent analysis of 4-O-CQA / QE.

In Article 3, the QM and MD data are calculated for individual molecules:

- 3-O-CQA
- 4-O-CQA
- 5-O-CQA
- 5-O-CQA-H+

However, the experimental inhibition efficiency belongs to the whole quince extract, not to each individual molecule.

Therefore, Article 3 molecular descriptors should not be directly assigned to the experimental extract-level inhibition efficiency unless this assumption is clearly stated.

---

# 5. Clean dataset 1: Article 2 temperature-dependent target dataset

## File

data/processed/article2_clean_temperature_target_v1.csv

## Purpose

This dataset is used to analyze how temperature-dependent QM and MD descriptors relate to experimental inhibition efficiency.

## Row definition

Each row represents:

one molecule / one temperature / one experimental method

Because Article 2 has two experimental methods, each temperature appears twice:

- Polarization
- EIS

Expected rows:

- 308 K / Polarization
- 308 K / EIS
- 318 K / Polarization
- 318 K / EIS
- 328 K / Polarization
- 328 K / EIS

## Main features

### Quantum chemical features

- EHOMO_eV
- ELUMO_eV
- energy_gap_eV
- ionization_potential_eV
- electron_affinity_eV
- electronegativity_eV
- hardness_eV
- fraction_electron_transfer_deltaN

### MD / adsorption features

- adsorption_energy_kcal_mol
- total_energy_kcal_mol
- deformation_energy_kcal_mol
- rigid_adsorption_energy_kcal_mol
- binding_energy_kcal_mol

### Experimental condition features

- temperature_K
- acid_medium
- concentration_ppm
- method

## Target variable

Primary target:

- inhibition_efficiency_percent

Secondary target or supporting variables:

- icorr
- Rct

## Recommended analysis

This dataset is suitable for:

1. Small-scale EDA
2. Correlation analysis
3. Scientific trend analysis
4. Very simple baseline modeling only with strong limitations

## Main limitation

The dataset is very small. It should not be treated as a strong predictive ML dataset. It is mainly useful for scientific interpretation and proof-of-concept modeling.

---

# 6. Clean dataset 2: Article 3 molecular ranking dataset

## File

data/processed/article3_clean_molecular_ranking_v1.csv

## Purpose

This dataset is used to compare and rank individual caffeoylquinic acid derivatives based on molecular descriptors and adsorption energy.

## Row definition

Each row represents:

one molecule / one simulation condition

Expected rows:

- 3-O-CQA
- 4-O-CQA
- 5-O-CQA
- 5-O-CQA-H+

## Main features

### Quantum chemical features

- EHOMO_eV
- ELUMO_eV
- energy_gap_eV
- ionization_potential_eV
- electron_affinity_eV
- electronegativity_eV
- hardness_eV
- fraction_electron_transfer_deltaN

### Adsorption features

- adsorption_energy_kcal_mol
- total_energy_kcal_mol

## Ranking target

Primary ranking target:

- adsorption_strength_rank

The ranking is based on adsorption_energy_kcal_mol.

More negative adsorption energy means stronger predicted adsorption.

## Recommended analysis

This dataset is suitable for:

1. Molecule ranking
2. Descriptor comparison
3. Scientific interpretation
4. Understanding which molecular descriptors may explain stronger adsorption

## Main limitation

The experimental inhibition efficiency in Article 3 belongs to the whole quince extract, not to the individual molecules. Therefore, this dataset should not be used for direct supervised prediction of experimental IE% for each molecule.

---

# 7. Current modeling strategy

## Strategy A — Article 2

Use Article 2 for temperature-dependent descriptor-target analysis.

Possible question:

Can temperature-dependent QM and MD descriptors explain the decrease in inhibition efficiency with increasing temperature?

Possible target:

- inhibition_efficiency_percent

Possible features:

- temperature_K
- EHOMO_eV
- ELUMO_eV
- energy_gap_eV
- hardness_eV
- fraction_electron_transfer_deltaN
- adsorption_energy_kcal_mol

Recommended models:

- Linear Regression
- Ridge Regression
- Random Forest Regressor only as exploratory model

Important warning:

Because the dataset is very small, model results should be interpreted cautiously.

---

## Strategy B — Article 3

Use Article 3 for molecule-level ranking.

Possible question:

Which caffeoylquinic acid derivative has the strongest predicted adsorption on Fe(110)?

Possible ranking variable:

- adsorption_strength_rank

Possible features:

- EHOMO_eV
- ELUMO_eV
- energy_gap_eV
- hardness_eV
- fraction_electron_transfer_deltaN
- adsorption_energy_kcal_mol

Recommended analysis:

- Ranking table
- Descriptor comparison
- Scatter plots
- Correlation between QM descriptors and adsorption energy

Recommended models:

No supervised ML model at this stage.
Use ranking and interpretation first.

---

# 8. Final project decision

This project will not be treated as a large predictive machine learning project at this stage.

Instead, it will be treated as:

1. A descriptor-based scientific data project
2. A computational corrosion interpretation project
3. A small proof-of-concept AI/corrosion portfolio project

The goal is to show the ability to connect:

- corrosion science
- quantum chemical descriptors
- molecular simulation
- experimental inhibition efficiency
- structured data analysis

---

# 9. Next step after this document

The next step is to create the first EDA notebook:

notebooks/01_descriptor_eda.ipynb

The EDA notebook should include:

1. Loading clean datasets
2. Checking dataset shapes
3. Displaying Article 2 descriptor-target table
4. Displaying Article 3 molecule-ranking table
5. Plotting inhibition efficiency vs temperature for Article 2
6. Plotting adsorption energy ranking for Article 3
7. Writing initial scientific observations
