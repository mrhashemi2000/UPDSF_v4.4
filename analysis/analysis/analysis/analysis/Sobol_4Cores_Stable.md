[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
# Expanded_Analysis_5
# Sobol Global Sensitivity Analysis - UPDSF v4.4 
**Supporting Manuscript IJA-2026-0085**

**Date**: July 25, 2026  


# Sobol 2 Global Sensitivity Analysis 2 Report  
**UPDSF v4.4 – Degradation Parameters**  
**N = 5000 | T = 68.0 °C | pH = 7.5 | Polymer Length = 100 bases**

---

## 1. Overview

A global sensitivity analysis using the Sobol method was performed on the 15 degradation-related parameters of the Unified Prebiotic DNA Selection Framework (UPDSF) v4.4. The analysis quantifies the contribution of each parameter (and their interactions) to the variance of three key model outputs:

- Thymine **Enrichment**
- Thymine **Fraction**
- **DNA Yield**

The Saltelli sampling scheme was employed with a base sample size of **N = 5000**, resulting in a total of **160,000** model evaluations. All simulations were performed with a fixed polymer length of **100 bases**.

---

## 2. Full Diagnostic Figure

<img width="5368" height="5527" alt="sobol_degradation_analysis" src="https://github.com/user-attachments/assets/9434a95d-fc95-49a4-b240-ed8c00d08e03" />


**Figure Description**  
Comprehensive 12-panel diagnostic plot of the Sobol analysis (Polymer length = 100 bases):

- **Row 1**: First-order (S1) and total-order (ST) indices for Enrichment + S1 vs ST scatter plot  
- **Row 2**: S1 and ST indices for Thymine Fraction + ST indices for DNA Yield  
- **Row 3**: Interaction effects (ST − S1), parameter ranking by ST, and analysis summary box  
- **Row 4**: Convergence plots for Enrichment, Thymine Fraction, and DNA Yield showing stabilization of S1 and ST indices with increasing sample size

The convergence panels (bottom row) demonstrate that both S1 and ST indices stabilize after approximately 80,000–100,000 evaluations, confirming that N = 5,000 is sufficient.

---

## 3. Computational Setup

| Item                    | Value              |
|-------------------------|--------------------|
| Base sample size (N)    | 5,000              |
| Total model runs        | 160,000            |
| Valid runs              | 160,000 (100%)     |
| Parallel workers        | 4                  |
| Wall-clock time         | 8.25 hours         |
| Throughput              | 5.4 runs/s         |
| Temperature             | 68.0 °C            |
| pH                      | 7.5                |
| Polymer length          | 100 bases          |
| Sampling method         | Saltelli (SALib)   |
| Analysis method         | Sobol indices (S1, ST) |

---

## 4. Convergence Analysis

Convergence was assessed by bootstrap resampling (50 replicates) at subsample sizes corresponding to 10%–100% of the full dataset.

### Key Observations

- Both first-order (S1) and total-order (ST) indices stabilize after approximately **80,000–100,000** evaluations.
- At the full sample size (160,000), the indices exhibit negligible drift.
- The final ST value for Enrichment converges to **≈ 1.0018**, confirming that the total variance is fully accounted for.
- Confidence bands (shaded regions) become narrow at larger sample sizes, indicating low estimation uncertainty.

**Conclusion:**  
N = 5,000 provides sufficient convergence for reliable Sobol index estimation under the tested conditions (T = 68 °C, pH = 7.5, polymer length = 100 bases). Increasing the sample size to N = 10,000 is **not required** and would roughly double the computational cost without meaningful improvement in accuracy.

---

## 5. Sensitivity Results (Enrichment)

### Top 3 Most Influential Parameters (Total-Order Index)

| Rank | Parameter                | ST     | Interpretation                              |
|------|--------------------------|--------|---------------------------------------------|
| 1    | **A_U**                  | 0.7751 | Dominant parameter (direct + interaction)   |
| 2    | **base_catalysis_factor**| 0.6718 | Strong interactions with nearly all rates   |
| 3    | **A_C**                  | 0.5434 | Important via deamination pathway           |

### Main Findings

- **A_U** is the single most critical parameter controlling thymine enrichment.
- **base_catalysis_factor** exhibits strong higher-order interactions (ST − S1 is large).
- Most parameters show substantial interaction effects (ST − S1 ≈ 0.45–0.55), indicating a highly non-additive system.
- First-order effects (S1) are generally small except for A_U and base_catalysis_factor, confirming that parameter interactions dominate model behaviour.

---

## 6. Parameter Screening Recommendation

Based on the total-order indices, parameters can be grouped as follows:

**Critical (retain in future analyses)**  
- `A_U`  
- `base_catalysis_factor`  
- `A_C`  
- `deamination_ratio`  

**Moderate influence**  
- `lipid_protection`  
- `clay_protection`  
- `UV_resistance_T`  
- `A_T` / `Ea_T`  

**Low influence (can be fixed at nominal values)**  
- `Ea_U`, `Ea_A`, `Ea_C_deam`  
- `A_A`  
- `UV_resistance_C`, `UV_resistance_A`  

Fixing the low-influence group reduces the parameter space from 15 to approximately 7–8 dimensions while preserving the majority of output variance. This enables significantly cheaper subsequent uncertainty quantification or optimisation studies.

---

## 7. Consistency with UPDSF v4.4

All 15 parameters and their nominal values are identical to those used in the main UPDSF v4.4 simulation engine (strictly empirical, literature-derived). The Sobol analysis therefore directly quantifies the sensitivity of the published model under the stated prebiotic conditions:

- Temperature = 68.0 °C  
- pH = 7.5  
- Polymer length = 100 bases

---

## 8. Summary

- N = 5,000 yields well-converged Sobol indices.
- Further increase to N = 10,000 is unnecessary.
- Model behaviour is dominated by **A_U** and **base_catalysis_factor**, with strong parameter interactions.
- Results support a reduced-parameter approach for future computational studies.
- All results correspond to a polymer length of **100 bases**.

---

**Generated files**  
- `sobol_degradation_analysis.png` – full diagnostic figure (shown above)  
- `sobol_degradation_data_*.csv` – raw simulation results  
- `sobol_indices_*.json` – Sobol indices and convergence data  

**Reference**  
UPDSF v4.4 – Strictly Empirical Parameters + Lipid Membrane Integration  
(DOI: 10.5281/zenodo.21224889)
