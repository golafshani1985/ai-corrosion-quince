# Descriptor Dictionary — Project 2

## Project title

Descriptor and simulation-based corrosion inhibition analysis of quince-derived inhibitors.

## Purpose

This file defines the meaning, unit, source, and role of each variable used in Project 2.  
The project connects quantum chemical descriptors, molecular simulation adsorption data, and experimental corrosion inhibition performance.

---

# 1. Identification columns

## source_article
Meaning: Indicates which article the data came from.  
Type: text  
Examples: Article 2, Article 3  
Role: metadata  
Source: all extracted tables

## molecule_id
Meaning: Internal ID assigned to each molecule or extract entry.  
Type: text  
Examples: A2_M1, A3_M1, A3_EXTRACT  
Role: key for merging datasets  
Source: created manually during data extraction

## molecule_name
Meaning: Name of the inhibitor molecule or extract.  
Type: text  
Examples: 4-O-CQA, 3-O-CQA, 5-O-CQA, 5-O-CQA-H+, Quince Extract (QE)  
Role: molecule identifier  
Source: Article 2 and Article 3

## temperature_K
Meaning: Experimental or simulation temperature in Kelvin.  
Type: numeric  
Unit: K  
Examples: 298.15, 308, 318, 328  
Role: feature / merge key  
Source: Article 2 and Article 3

---

# 2. Quantum chemical descriptor columns

## EHOMO_eV
Meaning: Energy of the highest occupied molecular orbital.  
Type: numeric  
Unit: eV  
Scientific role: Higher HOMO energy usually indicates stronger electron-donating ability from inhibitor to metal surface.  
Role in ML: molecular descriptor  
Source: Article 2 Table S3; Article 3 Table 9

## ELUMO_eV
Meaning: Energy of the lowest unoccupied molecular orbital.  
Type: numeric  
Unit: eV  
Scientific role: Lower LUMO energy can indicate stronger ability to accept electrons from the metal surface.  
Role in ML: molecular descriptor  
Source: Article 2 Table S3; Article 3 Table 9

## energy_gap_eV
Meaning: HOMO-LUMO energy gap.  
Type: numeric  
Unit: eV  
Scientific role: Smaller gap usually indicates higher molecular reactivity and easier charge transfer.  
Role in ML: molecular descriptor  
Source: Article 2 Table S3; Article 3 Table 9

## ionization_potential_eV
Meaning: Ionization potential, calculated as I = -EHOMO.  
Type: numeric  
Unit: eV  
Scientific role: Indicates the tendency of the molecule to lose electrons.  
Role in ML: molecular descriptor  
Source: Article 2 Table S3; Article 3 Table 9

## electron_affinity_eV
Meaning: Electron affinity, calculated as A = -ELUMO.  
Type: numeric  
Unit: eV  
Scientific role: Indicates the tendency of the molecule to accept electrons.  
Role in ML: molecular descriptor  
Source: Article 2 Table S3; Article 3 Table 9

## electronegativity_eV
Meaning: Molecular electronegativity.  
Type: numeric  
Unit: eV  
Role in ML: molecular descriptor  
Source: Article 2 Table S3; Article 3 Table 9

## hardness_eV
Meaning: Chemical hardness.  
Type: numeric  
Unit: eV  
Scientific role: Higher hardness usually indicates lower molecular reactivity.  
Role in ML: molecular descriptor  
Source: Article 2 Table S3; Article 3 Table 9

## softness_eV_inv
Meaning: Chemical softness, usually calculated as inverse of hardness.  
Type: numeric  
Unit: eV^-1  
Scientific role: Higher softness usually indicates higher molecular reactivity.  
Role in ML: derived descriptor  
Source: calculated during cleaning if needed

## fraction_electron_transfer_deltaN
Meaning: Fraction of electron transfer between inhibitor molecule and metal surface.  
Type: numeric  
Unit: dimensionless  
Role in ML: molecular descriptor  
Source: Article 2 Table S3; Article 3 Table 9

## dipole_moment_D
Meaning: Dipole moment of the molecule.  
Type: numeric  
Unit: Debye  
Role in ML: molecular descriptor if available  
Source: not consistently available in current extracted tables

---

# 3. MD / adsorption simulation columns

## surface_model
Meaning: Metal surface used in molecular simulation.  
Type: text  
Examples: Fe(110)  
Role: simulation condition  
Source: Article 2 Table S1; Article 3 Table 8

## medium
Meaning: Corrosive solution or simulation medium.  
Type: text  
Examples: 1 M HCl, 1 M H2SO4  
Role: experimental/simulation condition  
Source: Article 2 and Article 3

## adsorption_energy_kcal_mol
Meaning: Adsorption energy of inhibitor molecule on Fe(110) surface.  
Type: numeric  
Unit: kcal/mol  
Scientific role: More negative adsorption energy generally indicates stronger and more stable adsorption.  
Role in ML: key simulation descriptor  
Source: Article 2 Table S1; Article 3 Table 8

## total_energy_kcal_mol
Meaning: Total energy of the simulation system.  
Type: numeric  
Unit: kcal/mol  
Role in ML: simulation descriptor / metadata  
Source: Article 2 Table S1; Article 3 Table 8

## simulation_method
Meaning: Simulation method used for adsorption calculation.  
Type: text  
Examples: MD/MC, Monte Carlo / MD  
Role: metadata  
Source: computational details section

---

# 4. Experimental target columns

## acid_medium
Meaning: Acidic corrosive environment used experimentally.  
Type: text  
Examples: 1 M HCl, 1 M H2SO4  
Role: experimental condition  
Source: Article 2 and Article 3

## metal
Meaning: Metal substrate used in corrosion test.  
Type: text  
Examples: St37 steel, mild steel  
Role: experimental condition  
Source: article experimental sections

## concentration_ppm
Meaning: Concentration of quince extract inhibitor.  
Type: numeric  
Unit: ppm  
Role: experimental condition  
Source: Article 2 Table 2 and Table 3; Article 3 Table 2 and Table 3

## method
Meaning: Experimental electrochemical method used to obtain target.  
Type: text  
Examples: Polarization, EIS  
Role: target source identifier  
Source: Article 2 Table 2 and Table 3; Article 3 Table 2 and Table 3

## inhibition_efficiency_percent
Meaning: Corrosion inhibition efficiency.  
Type: numeric  
Unit: %  
Scientific role: Main experimental performance target.  
Role in ML: target variable  
Source: Article 2 Table 2 and Table 3; Article 3 Table 2 and Table 3

## icorr
Meaning: Corrosion current density from polarization test.  
Type: numeric  
Unit: mA/cm2  
Scientific role: Lower icorr indicates lower corrosion rate and better inhibition.  
Role in ML: experimental target/supporting variable  
Source: Article 2 Table 2; Article 3 Table 2

## Rct
Meaning: Charge transfer resistance from EIS.  
Type: numeric  
Unit: ohm.cm2  
Scientific role: Higher Rct indicates better corrosion protection.  
Role in ML: experimental target/supporting variable  
Source: Article 2 Table 3; Article 3 Table 3

## performance_rank_in_paper
Meaning: Qualitative rank or note based on the article’s reported best performance.  
Type: text  
Role: interpretation label  
Source: manually assigned from article results

## performance_class_raw
Meaning: Initial qualitative performance class.  
Type: text  
Examples: high, medium-high  
Role: possible classification target after cleaning  
Source: manually assigned from inhibition efficiency values

---

# 5. Dataset limitations

1. Article 2 provides temperature-dependent QM, MD, and experimental target data for 4-O-CQA / QE at 308, 318, and 328 K.

2. Article 3 provides molecular descriptors and adsorption energies for individual caffeoylquinic acid derivatives, but the experimental inhibition efficiency belongs to the whole quince extract, not to each individual molecule.

3. Article 3 molecular descriptors should not be directly assigned to the experimental QE target without clearly stating the assumption.

4. Article 2 can be used for temperature-dependent descriptor-target analysis.

5. Article 3 is more suitable for molecule-level ranking based on QM descriptors and adsorption energy.

---

# 6. Suggested target definitions

Regression target: inhibition_efficiency_percent

Classification target: performance_class_raw

Ranking target: adsorption_strength_rank

---

# 7. Recommended first modeling strategy

1. Use Article 2 for temperature-dependent descriptor-target exploration.
2. Use Article 3 for molecule-level ranking and descriptor interpretation.
3. Do not mix Article 2 and Article 3 targets blindly because their experimental target definitions are not equivalent.
