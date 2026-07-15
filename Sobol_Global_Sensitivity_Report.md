[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

# Expanded_Analysis_7
## Sobol Global Sensitivity Analysis Report  
# **Supporting Manuscript IJA-2026-0085**
## UPDSF v4.4 — 16,000 Simulation Runs

## Overview
This report presents the results of a **Global Sensitivity Analysis** using the Sobol method performed on the UPDSF v4.4 model. The analysis was conducted to evaluate the robustness of the model predictions and to identify the parameters with the greatest influence on thymine enrichment under prebiotic conditions.

## Methodology
- **Model**: UPDSF v4.4 (strictly empirical with lipid membrane module)
- **Method**: Sobol variance-based global sensitivity analysis (first-order S1 and total-order ST indices)
- **Sample size**: 16,000 simulation runs
- **Baseline conditions**: T = 68.0°C, pH = 7.5, polymer length = 100 bases
- **Framework**: Stability-Kinetics Ratio ($S_r = \tau_{stable} / \kappa_{poly}$)

## Key Findings

### Dominant Parameters (Total-order Sensitivity Index - ST)
- **Uracil hydrolysis prefactor ($A_U$)**: ST ≈ 0.78 (highest influence)
- **Base catalysis factor**: ST ≈ 0.69
- **A_C (related to deamination)**: ST ≈ 0.53
- Significant parameter interactions were observed, particularly between hydrolysis kinetics, lipid protection, and UV resistance.

### Interpretation
The high total-order indices for hydrolysis-related parameters confirm that differential stability between uracil and thymine is the primary driver of selection. Environmental factors (lipid vesicles, UV exposure) exert moderate but synergistic effects through parameter interactions.

### Parameter-Output Correlation Analysis

<img width="5352" height="2369" alt="parameter_correlations" src="https://github.com/user-attachments/assets/3f34958b-7066-40f3-aca3-ef2e024bc589" />

## Figure 1 Analysis 
Pearson correlation coefficients between key model parameters and simulation outputs in UPDSF v4.4.

- **Left**: Correlation with Thymine enrichment
- **Middle**: Correlation with final Thymine fraction  
- **Right**: Correlation with total DNA yield

**Key Insight**: The uracil hydrolysis prefactor (`A_U`) and base catalysis factor show the strongest positive correlations with thymine selection. These results are consistent with the Sobol global sensitivity analysis and confirm that differential hydrolysis kinetics are the primary driver of thymine enrichment under prebiotic conditions.

<img width="5368" height="4570" alt="sobol_degradation_analysis" src="https://github.com/user-attachments/assets/52b13478-fd79-4b61-a7c4-b4bfd1902212" />

## Figure 2 Analysis
The Sobol global sensitivity analysis presented in Figure 2 provides a dual-layer validation of the model's robustness:

- First-Order vs. Total-Order Effects ($S_1$ vs. $S_T$): The analysis identifies the individual contribution ($S_1$) and the total contribution including interactions ($S_T$) for each parameter. The uracil hydrolysis prefactor ($A_U$) and the base catalysis factor emerge as the dominant drivers across all key outputs (Enrichment, Thymine Fraction, and DNA Yield).
- Interaction and Parameter Ranking (Bottom Row): The significant gap between $S_1$ and $S_T$ (visualized in the $S_1$ vs $S_T$ scatter plot and the Parameter Interactions plot) confirms that non-linear interactions between hydrolysis kinetics, pH-dependent catalysis, and environmental factors are crucial. All key parameters comfortably exceed the significance threshold (red dashed line in the ranking plot).

These findings statistically validate the Stability-Kinetics Ratio framework by showing that prebiotic thymine selection is robustly driven by differential degradation kinetics rather than parameter tuning.

## Relation to Manuscript
These Sobol results are fully consistent with:
- The **Stability-Kinetics Ratio** framework presented in the main text
- Environmental case studies (Section 3)
- Supplementary Figure S1 (heatmap of thymine selection across environments)
- Supplementary Table S1 (literature-derived parameters)

The analysis demonstrates that the reported preference for thymine is **statistically robust** and not an artifact of specific parameter choices.

## Conclusion
The Sobol global sensitivity analysis strongly supports the central conclusion of the manuscript: heterogeneous prebiotic environments, through well-constrained physicochemical kinetics, could have imposed selective pressures favoring thymine in emerging DNA-like systems.

**Files included**:
- `sobol_indices_20260714_113848.json` (raw data)
- `sobol_degradation_analysis.png` (visual summary)
- This report

**Reproducibility**: All analyses were generated from the public repository [mrhashemi2000/UPDSF_v4.4](https://github.com/mrhashemi2000/UPDSF_v4.4).
