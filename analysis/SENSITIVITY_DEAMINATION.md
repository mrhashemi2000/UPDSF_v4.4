[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
# Expanded_Analysis_9
**Supporting Manuscript IJA-2026-0085**

**Date**: July 29, 2026  

**Manuscript**  
*Environmental Selection of Thymine over Uracil in Prebiotic Chemical Evolution: Insights from a Kinetic Monte Carlo Model*  
(International Journal of Astrobiology – Draft)
 

# Sensitivity Analysis: Effect of Cytosine Deamination on Thymine Selection  
**UPDSF v4.4 – Unified Prebiotic DNA Selection Framework**

---

## Overview

This report presents a controlled sensitivity test examining the influence of cytosine deamination on the primary outcome of the UPDSF v4.4 model — the chemical enrichment of thymine (T) relative to uracil (U) under prebiotic conditions.

The test isolates the deamination process while keeping all other parameters identical, allowing a direct assessment of its contribution to the observed thymine selection.

---

## Simulation Conditions

| Parameter              | Value          |
|------------------------|----------------|
| Temperature            | 68.0 °C        |
| pH                     | 8.0            |
| Simulation duration    | 120 hours      |
| Polymer length         | 100 bases      |
| Lipid concentration    | 0.05 M         |
| UV exposure factor     | 0.8            |
| Random seed            | 42             |

Two parallel runs were performed:

- **WITH deamination** — default empirical parameters (including `DEAMINATION_RATIO_C = 36.0`)
- **WITHOUT deamination** — deamination rate and ratio set to zero

---

## Results Summary

| Metric                      | WITH Deamination | WITHOUT Deamination | Difference |
|----------------------------|------------------|---------------------|------------|
| Thymine Enrichment         | 2.748 ×          | 3.433 ×             | +0.685 ×   |
| Final T Fraction           | 0.226            | 0.282               | +0.056     |
| Final U count              | 22,951           | 7,676               | –15,275    |
| Final T count              | 9,093            | 9,065               | ≈ 0        |
| Final C count              | 222              | 6,537               | +6,315     |
| Final A count              | 8,019            | 8,878               | +859       |
| Deamination events         | 96,095           | 0                   | —          |
| Relative change in enrichment | —             | —                   | **+24.9 %**|

---

## Key Observations from the Figure


<img width="4439" height="3401" alt="deamination_sensitivity_comparison" src="https://github.com/user-attachments/assets/a9a0af24-0f2a-4039-9046-760cca0566f6" />



<img width="4439" height="3401" alt="deamination_sensitivity_comparison" src="https://github.com/user-attachments/assets/e0be4c4a-3104-475b-8877-19a18db160f1" />


### 1. DNA Accumulation
- **WITH deamination**: Uracil accumulates strongly due to continuous conversion of cytosine → uracil. Cytosine is nearly depleted.
- **WITHOUT deamination**: All four nucleotides accumulate more evenly. Cytosine persists at significant levels.

### 2. Nucleotide Fractions
- With deamination active, the U fraction stabilizes near ~0.55 while the T fraction remains around 0.23.
- Without deamination, the T fraction rises to ~0.28 and the system maintains a more balanced composition.

### 3. Enrichment Trajectory
- Both conditions produce positive thymine enrichment throughout the simulation.
- The enrichment curve without deamination consistently lies above the curve with deamination.
- The absolute difference remains approximately 0.68× (≈ 25 % relative).

### 4. Final Composition
- Absolute thymine counts are nearly identical in both runs (~9,070–9,090).
- The main compositional difference is the redistribution between C and U caused by deamination.

---

## Interpretation

1. **Qualitative robustness**  
   Thymine enrichment occurs in both scenarios. Deamination does **not** reverse or eliminate the selective advantage of thymine.

2. **Quantitative influence**  
   Deamination reduces the observed enrichment by ~25 %. This occurs because the conversion of C → U artificially inflates the uracil pool, thereby lowering the relative T/U ratio.

3. **Primary selective pressures**  
   The persistence of thymine enrichment even when deamination is completely disabled indicates that the dominant drivers in the model are:
   - Higher hydrolytic stability of thymine (higher \(E_a\) and lower pre-exponential factor)
   - Greater UV resistance of thymine
   - Preferential partitioning of thymine into lipid membranes

4. **Role of the deamination parameter**  
   While the 36× deamination ratio affects the magnitude of enrichment, it is not required for the core qualitative conclusion of the framework.

---

## Conclusions

- Cytosine deamination modulates the **strength** of thymine enrichment but does not determine its **occurrence**.
- The main selective advantage of thymine in UPDSF v4.4 arises from differential stability and membrane interactions rather than from the C → U conversion pathway.
- The result supports the robustness of the model’s central claim (prebiotic chemical selection of thymine) under variation of the deamination parameter.
- For future refinements, the deamination ratio should be updated to values more consistent with the primary literature (Shen et al., 1994 reports a much smaller factor for 5-methylcytosine vs cytosine).

---

## Reproducibility

The exact script used to generate the figure and numerical results is available in this repository (`test_deamination_sensitivity.py`).  

All simulations were performed with the original UPDSF v4.4 engine under identical random seeds to ensure direct comparability.

---

