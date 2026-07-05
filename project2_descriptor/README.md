\# Project 2 — Descriptor- and Simulation-Based Corrosion Inhibition Analysis



\## Overview



This project investigates whether quantum chemical descriptors and molecular simulation data can help explain corrosion inhibition behavior of quince-derived inhibitor molecules.



The project connects three scientific layers:



1\. Molecular electronic descriptors

2\. Adsorption behavior on Fe(110) surface

3\. Experimental corrosion inhibition efficiency



This project is part of a broader AI + corrosion science portfolio.



\---



\## Scientific Question



Can molecular descriptors and adsorption simulation results explain or rank the corrosion inhibition behavior of quince-derived inhibitors?



\---



\## Data Sources



The project uses data extracted from two corrosion inhibition studies related to quince extract and caffeoylquinic acid derivatives.



\### Article 2



Article 2 provides temperature-dependent data for quince extract / 4-O-CQA at 308 K, 318 K, and 328 K.



Extracted data include:



\- Quantum chemical descriptors

\- MD/MC adsorption-related energies

\- Polarization inhibition efficiency

\- EIS inhibition efficiency



Article 2 is used for temperature-dependent descriptor-target analysis and baseline modeling.



\### Article 3



Article 3 provides molecule-level descriptor and adsorption data for four CQA derivatives:



\- 3-O-CQA

\- 4-O-CQA

\- 5-O-CQA

\- 5-O-CQA-H+



Article 3 is used for molecular ranking and descriptor interpretation.



\---



\## Important Scientific Limitation



Article 3 contains molecular descriptors for individual molecules, but the experimental inhibition efficiency belongs to the whole quince extract.



Therefore, the experimental inhibition efficiency from Article 3 should not be directly assigned to individual molecules without clearly stating this assumption.



For this reason:



\- Article 2 is used for baseline supervised modeling.

\- Article 3 is used for molecular ranking and descriptor interpretation.



\---



\## Project Structure



```text

project2\_descriptor/

│

├── data/

│   ├── raw/

│   │   └── descriptor\_raw\_data\_v1.xlsx

│   │

│   └── processed/

│       ├── article2\_clean\_temperature\_target\_v1.csv

│       └── article3\_clean\_molecular\_ranking\_v1.csv

│

├── notebooks/

│   ├── 01\_descriptor\_eda.ipynb

│   └── 02\_descriptor\_models.ipynb

│

├── reports/

│   ├── descriptor\_dictionary.md

│   ├── project2\_problem\_definition.md

│   ├── eda\_findings\_project2.md

│   ├── modeling\_findings\_project2.md

│   ├── model\_comparison\_project2.csv

│   ├── article2\_actual\_vs\_predicted\_project2.csv

│   ├── article2\_ie\_correlations.csv

│   ├── article3\_adsorption\_correlations.csv

│   └── article3\_descriptor\_adsorption\_comparison.csv

│

└── references/

