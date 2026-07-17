[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

# Expanded_Analysis_11
# Sobol Sensitivity Analysis: Global Sensitivity Analysis (SoboL) including Guanine (G) in the chemical population using Empirical Parameter Ranges
# **Supporting Manuscript IJA-2026-0085**


## UPDSF v4.4 — 76000 Simulation Runs

**Run Date**: July 17, 2026  
**Baseline Conditions**: T = 68.0°C, pH = 7.5, Polymer Length = 100 bases  
**Sample Size**: 2,000 | **Total Runs**: **76000** | **CPU Cores**: 4

**Author:** Seyed Mohammad Reza Hashemi (Reza Hashemi)

# Global Sensitivity Analysis: The Impact of Guanine (G) Integration using Empirical Parameter Ranges

##  Overview
To evaluate the robustness of the UPDSF v4.4 framework, a comprehensive Global Sensitivity Analysis (SoboL) was conducted including Guanine (G) in the chemical population. The objective was to determine if the introduction of an additional nucleobase would disrupt the established dominance of the `base_catalysis_factor` and `A_U` or introduce new critical dependencies.

---

##  1. Total-Order Effects (ST Index)
The bar chart illustrates the Total-order Index (ST), which quantifies the total contribution of each parameter to the variance of the thymine enrichment output, including its interactions with all other parameters.

### Key Findings:
- Absolute Dominance of Environmental Filters: The `base_catalysis_factor` exhibits the highest ST value ($\approx 0.65$), confirming that the external chemical environment (pH, mineral catalysis) is the primary determinant of the evolutionary filter.
- The Engine of Enrichment: The `A_U` (Uracil pre-exponential factor) remains the second most influential parameter ($\approx 0.5$). This reinforces the conclusion that the intrinsic instability of Uracil is the fundamental driver of the $U \rightarrow T$ transition.
- Negligible Influence of G-specific Parameters: Parameters such as `Ea G` and `UV resistance G` show significantly lower sensitivity indices. This proves that while Guanine is present in the system, it does not interfere with the primary selective pressure favoring Thymine.

### Figure 1

<img width="2382" height="1484" alt="sobol_analysis" src="https://github.com/user-attachments/assets/f23d2887-be75-4c4d-b032-75c7504e57d8" />


Figure 1: SoboL Sensitivity Indices for UPDSF v4.4. (Left) Total-order effects ($S_T$) showcasing the relative importance of 18 parameters on thymine enrichment. (Right) First-order ($S_1$) vs. Total-order ($S_T$) indices. Points deviating from the 45° identity line signify strong parametric interactions.
Global Sensitivity Analysis (SoboL) results for the UPDSF v4.4 model with Guanine integration. The left panel shows the Total-order effects ($S_T$), highlighting the dominance of the `base_catalysis_factor` and `A_U`. The right panel illustrates the $S_1$ vs. $S_T$ relationship, indicating strong non-linear interactions between parameters.

---

##  2. S1 vs. ST Analysis (Interaction Mapping)
The scatter plot compares the First-order index (S1) (the effect of a parameter acting alone) against the Total-order index (ST) (the effect including all interactions).

### Technical Interpretation:
- Non-Linearity & Synergies: A significant number of parameters are positioned well above the 45-degree diagonal (the $S1=ST$ line). This gap indicates strong non-linear interactions. In other words, the parameters do not act in isolation; their effect is amplified when they interact with other environmental variables.
- High-Impact Clusters: The `base_catalysis_factor` and `A_U` are the most distant from the origin, indicating they possess both high individual influence and high synergistic potential.
- Stability of the Core: The clustering of most other parameters near the origin confirms that the model is not overly sensitive to "noise" from secondary parameters, ensuring a stable and reproducible outcome.

---

##  Conclusion: Model Validation
The integration of Guanine into the simulation serves as a stress test for the framework. The results demonstrate:
1.  Structural Integrity: The hierarchy of influence remains unchanged. The "Environmental $\rightarrow$ Kinetic" axis of selection is preserved.
2.  Validation of Simplification: The fact that G-related parameters have low sensitivity justifies the strategic decision in v4.4 to focus on the $U \leftrightarrow T$ transition, as the core mechanism is independent of G-specific kinetics.
3.  Predictive Reliability:* The model consistently identifies the same primary drivers regardless of the complexity of the nucleobase population, proving its reliability as a scientific instrument for prebiotic chemistry.

---

*Analysis performed using: `SoboL` Global Sensitivity Method  
Framework: `UPDSF v4.4`  

