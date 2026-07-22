[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
# Expanded_Analysis_3
# Sobol Sensitivity Analysis Report - Polymer/DNA Degradation Parameters# **Supporting Manuscript IJA-2026-0085**

**Date**: July 22, 2026  
**Conditions**: Temperature = 68.0°C, pH = 7.5, Polymer length = 100 bases

---

<img width="5368" height="4570" alt="sobol_degradation_analysis" src="https://github.com/user-attachments/assets/e66eb5ad-c3a0-49d0-8a64-190df07950d2" />

This document presents the results of a *Sobol Sensitivity Analysis conducted to evaluate the impact of various degradation parameters on a biochemical system (likely DNA stability/enrichment) under specific conditions: Temperature = 68.0°C, pH = 7.5, and a Polymer length of 100 bases.

## Key Technical Metrics
- Computational Effort: 16,000 valid runs completed in 1.07 hours using 3 workers (average speed: 4.1 runs/s).
- Primary Metrics: The analysis compares First-order Sobol Indices ($S_1$), representing the direct effect of a parameter, and Total-order Indices ($S_T$), which include the direct effect plus all higher-order interactions.

## Top Influential Parameters
Based on the Total-order Index ($S_T$), the most significant parameters are:
1. $A\_U$: $S_T = 0.7756$
2. Base Catalysis Factor: $S_T = 0.6894$
3. $A\_C$: $S_T = 0.5326$

## Summary of Findings
- Critical Factor: $Ea\_T$ (Thymine activation energy) is identified as the most critical parameter.
- Significant Influences: The deamination ratio significantly affects enrichment, while lipid protection shows a moderate influence.
- Interactions: There is a substantial gap between $S_1$ and $S_T$ for several parameters, indicating that parameter interactions play a crucial role in the overall degradation process.

## Visualization Breakdown
- First-order vs. Total-order Effects: Comparative bar charts for "Enrichment" and "Thymine Fraction."
- $S_1$ vs $S_T$ Scatter Plot: Visualizes the strength of interactions; points further from the $S_1=S_T$ line indicate higher interaction effects.
- Interaction Analysis: A dedicated chart showing the interaction effect calculated as $(S_T - S_1)$.
- Parameter Ranking:* A sorted distribution of parameters based on their total sensitivity index against a significance threshold.

<img width="5368" height="4483" alt="sobol_degradation_analysis" src="https://github.com/user-attachments/assets/49523b27-b0f2-49f1-a0b9-0576f0e5a9e1" />

This analysis evaluates parameter sensitivity under stable environmental conditions (T=68.0°C, pH=7.5). Increasing the total runs to 64,000 provides a more converged and statistically robust estimation of the Sobol indices compared to previous iterations.

## Execution Statistics
- Scale: 64,000 valid runs.
- Performance: Completed in 3.32 hours using 4 workers, maintaining a processing speed of 5.4 runs/s.

## Top 3 Influential Parameters ($S_T$)
The total-order sensitivity indices identify the following as the primary drivers of variability in the system:
1.  $A\_U$: $S_T = 0.8010$ (Primary driver)
2.  Base Catalysis Factor: $S_T = 0.6844$
3.  $A\_C$: $S_T = 0.5679$

## Key Findings
- Critical Parameter: Unlike previous summaries, $A\_U$ is now explicitly highlighted as the most critical parameter in the system.
- Strong Interactions: The Base catalysis factor shows significant interaction effects, meaning its impact is highly dependent on the values of other parameters.
- Enrichment Drivers: The Deamination ratio continues to show a significant effect on enrichment outcomes.
- Moderate Factors: Lipid protection remains a moderate-influence factor.

## Comparative Visual Analysis
- $S_1$ vs $S_T$ (Scatter Plot): The high concentration of points above the identity line ($S_1 = S_T$) confirms that the system is dominated by non-linear interactions rather than simple additive effects.
- Parameter Interactions Chart: Shows that almost all parameters (especially $A\_U$ and $base\_catalysis\_factor$) have interaction indices near or above 0.5, suggesting a highly complex, interdependent degradation process.
- DNA Yield (Total-order):* The purple bar chart indicates that $A\_U$ and $base\_catalysis\_factor$ are also the dominant factors affecting the final DNA yield.

## Executive Summary

This report presents a comprehensive **variance-based Sobol sensitivity analysis** of degradation parameters affecting three key outputs: **Enrichment**, **Thymine Fraction**, and **DNA Yield**. The analysis was conducted with both 16,000 and 64,000 model runs to assess convergence and robustness.

**Top 3 Most Influential Parameters (based on 64k runs)**:

| Rank | Parameter                  | Average ST | Primary Impact Area          |
|------|---------------------------|------------|------------------------------|
| 1    | **A_U**                   | ~0.81      | All outputs (dominant)       |
| 2    | **base_catalysis_factor** | ~0.685     | All outputs (very stable)    |
| 3    | **A_C**                   | ~0.61      | Strongest on DNA Yield       |

**Key Findings**:
- **A_U** (activation energy related to Uracil/Thymine) is the most critical parameter.
- Base catalysis factor shows consistently strong influence and interactions.
- Increasing sample size to 64k significantly improved result reliability.
- Deamination ratio, lipid protection, clay protection, and UV resistance parameters exhibit moderate influence.

---

## Main Sobol Sensitivity Results with 95% CI

### 1. Enrichment

<img width="5353" height="3539" alt="sobol_ci_95_enrichment" src="https://github.com/user-attachments/assets/52fe9215-a972-4e4e-b581-330c3952210d" />


**Description**: Total-order Sobol indices (ST) with 95% confidence intervals comparing 16k and 64k runs. A_U and base_catalysis_factor are the most influential.

### 2. Thymine Fraction

<img width="5353" height="3539" alt="sobol_ci_95_thymine_fraction" src="https://github.com/user-attachments/assets/83252607-ef21-4620-bc39-d0818da8f83d" />

**Description**: Total-order Sobol indices for Thymine Fraction. A_U shows exceptionally high sensitivity (ST ≈ 0.891 at 64k runs).

### 3. DNA Yield

<img width="5353" height="3539" alt="sobol_ci_95_dna_yield" src="https://github.com/user-attachments/assets/4d3e9cc8-ed0c-4d36-acd0-70e8e61e2c4a" />

**Description**: Total-order Sobol indices for DNA Yield. A_U, base_catalysis_factor, and A_C are the dominant parameters.

---

## Convergence Analysis (16k vs 64k runs)


## 1

<img width="5250" height="3865" alt="convergence_95ci_enrichment" src="https://github.com/user-attachments/assets/cb14fea2-d028-416a-b2d0-e4850aaeefbd" />

## 2

<img width="5243" height="3865" alt="convergence_95ci_thymine_fraction" src="https://github.com/user-attachments/assets/074be21c-3d99-4e5c-8fac-9a1e81d96062" />

## 3

<img width="5220" height="3865" alt="convergence_95ci_dna_yield" src="https://github.com/user-attachments/assets/6c1173ce-6b4d-43ec-9d72-1b1da07fcd7f" />


**Description**: Side-by-side comparison of 16k and 64k runs with 95% confidence intervals. Shows good overall convergence and reduction in uncertainty.

---

## Detailed Comparative Results (16k vs 64k)

| Parameter                  | Enrichment 16k          | Enrichment 64k          | Thymine Fraction 16k    | Thymine Fraction 64k    | DNA Yield 16k           | DNA Yield 64k           | Overall Rank (64k) |
|---------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|--------------------|
| **A_U**                   | 0.776 [0.670-0.882]    | **0.801 [0.754-0.851]**| 0.776 [0.682-0.870]    | **0.891 [0.839-0.945]**| 0.773 [0.672-0.874]    | 0.741 [0.689-0.799]    | **1**              |
| **base_catalysis_factor** | 0.689 [0.598-0.780]    | 0.684 [0.634-0.734]    | 0.689 [0.595-0.783]    | 0.684 [0.640-0.728]    | 0.695 [0.600-0.790]    | 0.687 [0.639-0.739]    | **2**              |
| **A_C**                   | 0.533 [0.469-0.597]    | 0.598 [0.553-0.643]    | 0.533 [0.461-0.605]    | 0.568 [0.533-0.603]    | 0.532 [0.474-0.590]    | **0.664 [0.628-0.700]**| **3**              |
| **A_T**                   | 0.470 [0.408-0.532]    | 0.498 [0.462-0.534]    | 0.470 [0.403-0.537]    | 0.498 [0.465-0.531]    | 0.470 [0.410-0.530]    | 0.495 [0.459-0.531]    | 4-5                |
| **Ea_A**                  | 0.463 [0.401-0.525]    | 0.497 [0.464-0.530]    | 0.463 [0.399-0.527]    | 0.497 [0.463-0.531]    | 0.463 [0.399-0.527]    | 0.493 [0.462-0.524]    | 4-6                |
| **Ea_C_Deam**             | 0.486 [0.409-0.563]    | 0.506 [0.471-0.541]    | 0.486 [0.419-0.553]    | 0.506 [0.473-0.539]    | 0.486 [0.411-0.561]    | 0.504 [0.470-0.538]    | 5-6                |
| **Ea_T**                  | 0.516 [0.447-0.585]    | 0.496 [0.461-0.531]    | 0.516 [0.446-0.586]    | 0.496 [0.460-0.532]    | 0.516 [0.448-0.583]    | 0.493 [0.458-0.527]    | 6-7                |
| **AA**                    | 0.516 [0.447-0.585]    | 0.503 [0.466-0.540]    | 0.516 [0.443-0.589]    | 0.603 [0.471-0.535]    | 0.514 [0.451-0.577]    | 0.500 [0.465-0.535]    | 7-8                |
| **Deamination Ratio**     | 0.493 [0.431-0.555]    | 0.488 [0.452-0.524]    | 0.493 [0.425-0.561]    | 0.488 [0.453-0.523]    | 0.491 [0.434-0.548]    | 0.486 [0.453-0.519]    | 8-9                |
| **UV Resistance T**       | 0.459 [0.390-0.528]    | 0.499 [0.463-0.535]    | 0.459 [0.388-0.530]    | 0.499 [0.463-0.535]    | 0.456 [0.391-0.521]    | 0.495 [0.460-0.530]    | 9-10               |
| **UV Resistance C**       | 0.460 [0.407-0.513]    | 0.494 [0.460-0.528]    | 0.460 [0.402-0.518]    | 0.494 [0.463-0.525]    | 0.458 [0.401-0.515]    | 0.491 [0.459-0.523]    | 10                 |
| **UV Resistance A**       | 0.502 [0.431-0.573]    | 0.500 [0.463-0.537]    | 0.502 [0.441-0.563]    | 0.500 [0.466-0.534]    | 0.490 [0.420-0.560]    | 0.497 [0.465-0.529]    | 10-11              |
| **Lipid Protection**      | 0.439 [0.384-0.494]    | 0.496 [0.459-0.533]    | 0.439 [0.380-0.498]    | 0.496 [0.463-0.529]    | 0.438 [0.382-0.490]    | 0.495 [0.466-0.534]    | 11                 |
| **Clay Protection**       | 0.462 [0.399-0.525]    | 0.466 [0.434-0.498]    | 0.462 [0.396-0.528]    | 0.466 [0.430-0.502]    | 0.460 [0.399-0.521]    | 0.464 [0.430-0.498]    | 12                 |
| **Ea_U**                  | 0.478 [0.410-0.546]    | 0.487 [0.453-0.521]    | 0.478 [0.412-0.544]    | 0.487 [0.455-0.519]    | 0.477 [0.423-0.531]    | 0.484 [0.454-0.514]    | 13                 |

---

## Convergence Summary

- **Mean Confidence Interval Improvement**: ~45–49%
- **Significantly Changed Parameters**: Only 1 per output (6.7%)
- **Best Convergence**: Enrichment (no significant changes)
- **Max |ΔST|**: 0.132

---

## Conclusion and Recommendations

The Sobol sensitivity analysis robustly identifies **A_U** as the most influential parameter in the degradation model under the given conditions (68°C, pH 7.5). The **base_catalysis_factor** also plays a major role through both direct effects and interactions.

The transition from 16k to 64k runs confirmed excellent convergence, with substantially narrower confidence intervals and stable parameter rankings. This gives high confidence in the reliability of the results.

---
