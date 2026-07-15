[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

# Sobol Global Sensitivity Analysis Report (N=2000)
## UPDSF v4.4 — 64,000 Simulation Runs

**Run Date**: July 15, 2026  
**Baseline Conditions**: T = 68.0°C, pH = 7.5, Polymer Length = 100 bases  
**Sample Size**: 2,000 | **Total Runs**: **64,000** | **CPU Cores**: 4

---

### Overview
This report presents the results of a **Global Sensitivity Analysis** using the Sobol method on the UPDSF v4.4 model. The analysis evaluates model robustness and identifies the most influential parameters affecting thymine enrichment under prebiotic conditions.

### Methodology
- **Model**: UPDSF v4.4 (strictly empirical with lipid membrane module)
- **Method**: Sobol variance-based global sensitivity analysis (S1 and ST indices)
- **Sampling**: Saltelli with N=2000
- **Total Simulations**: 64,000 fully parallel runs
- **Runtime**: ≈3.32 hours (5.35 runs/second)

### Key Findings

#### Dominant Parameters (Total-order Sensitivity Index - ST)
| Rank | Parameter                        | ST Index   | S1 Index   | Interpretation |
|------|----------------------------------|------------|------------|----------------|
| **1** | **A_U** (Uracil hydrolysis prefactor) | **0.801** | 0.316     | **Most dominant** |
| **2** | **base_catalysis_factor**        | **0.684** | 0.177     | Base catalysis |
| **3** | **A_C** (Deamination)            | **0.568** | 0.061     | Cytosine deamination |
| 4    | Ea_T                             | ≈0.496    | 0.027     | Thymine stability |
| 5    | A_T                              | ≈0.498    | <0.01     | - |

**Other parameters** (lipid_protection, clay_protection, UV resistance): ST between 0.46–0.50

### Interpretation
- **A_U** alone explains over 31% of first-order variance and nearly 80% of total variance (including interactions). This is the strongest statistical evidence for the selective advantage of thymine through faster uracil degradation.
- Strong **parameter interactions** (large gap between S1 and ST) indicate non-linear model behavior.
- Lipid and clay protection show moderate direct effects but important synergistic contributions.

### Parameter-Output Correlation Analysis

**Key Insight**: `A_U` and `base_catalysis_factor` show the strongest positive correlations with thymine enrichment and fraction, while negatively affecting total DNA yield.

### Figure 1 Analysis (Sobol Plots)
(Insert `sobol_degradation_analysis.png` here)

<img width="5368" height="4483" alt="sobol_degradation_analysis" src="https://github.com/user-attachments/assets/25354532-ed88-4855-bffa-4a386df453bb" />


- **A_U** and **base_catalysis_factor** dominate across all outputs (Enrichment, Thymine Fraction, DNA Yield).
- All key parameters exceed the significance threshold.
- Significant non-linear interactions between hydrolysis kinetics and environmental factors were confirmed.

### Relation to Manuscript
These results fully support the **Stability-Kinetics Ratio** framework and demonstrate that the reported thymine preference is **statistically robust** and not an artifact of specific parameter choices.

### Conclusion
The Sobol global sensitivity analysis with 64,000 simulations strongly confirms that **differential degradation kinetics** (primarily driven by A_U) is the main driver of thymine selection in heterogeneous prebiotic environments. Lipid membranes play an important stabilizing and protective role.

**Attached Files**:
- `sobol_indices_20260715_083806.json` (raw data)
- `sobol_degradation_analysis.png` (visual summary)


**Reproducibility**: Full code and data available in the public repository [mrhashemi2000/UPDSF_v4.4](https://github.com/mrhashemi2000/UPDSF_v4.4).

---
*Generated with UPDSF v4.4 Sobol Analyzer*
