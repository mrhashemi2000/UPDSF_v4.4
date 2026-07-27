[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
# Expanded_Analysis_7
# Sobol Global Sensitivity Analysis - UPDSF v4.4 
**Supporting Manuscript IJA-2026-0085**

**Date**: July 27, 2026  
# Alignment of Sobol Sensitivity Results with the UPDSF v4.4 Manuscript ID: IJA-2026-0085 Findings

**Sobol Analysis Conditions**  
N = 5000 (160,000 total evaluations) | T = 68.0 °C | pH = 7.5 | Polymer length = 100 bases

**Manuscript**  
*Environmental Selection of Thymine over Uracil in Prebiotic Chemical Evolution: Insights from a Kinetic Monte Carlo Model*  
(International Journal of Astrobiology – Draft)
# Higher-Order Interactions in the Sobol Sensitivity Analysis of UPDSF v4.4

**Supporting Manuscript:** IJA-2026-0085  
**Analysis Conditions:** N = 5,000 (160,000 total evaluations) | T = 68.0 °C | pH = 7.5 | Polymer length = 100 bases  


---

## 1. Definition of Higher-Order Interactions

In Sobol sensitivity analysis:

- **S1 (First-order index):** Measures the direct, independent contribution of a parameter to output variance.
- **ST (Total-order index):** Measures the total contribution of a parameter, including all its interactions with other parameters.
- **ST − S1:** Quantifies the magnitude of higher-order interactions (pairwise, three-way, and higher).

A large ST − S1 value indicates a strongly non-additive system, where the effect of one parameter depends on the values of others.

---

## 2. Quantitative Observations

Under the tested conditions (T = 68 °C, pH = 7.5):

- Nearly all parameters exhibit substantial higher-order interactions, with **ST − S1 typically in the range of 0.45–0.55**.
- The system is highly non-additive.
- **`base_catalysis_factor`** displays the strongest interaction signature (high ST combined with a comparatively moderate S1).
- **`A_U`** also shows significant interactions, although it retains a strong first-order effect.
- Parameters related to UV resistance and certain activation energies show weaker direct effects but still participate in interactions.

**Key numerical insight:**  
A large fraction of the output variance (thymine enrichment) arises from parameter interactions rather than independent main effects.

---

## 3. Mechanistic Interpretation

The strong higher-order interactions observed in UPDSF v4.4 have clear mechanistic origins in the model structure:

### 3.1 Multiplicative Role of `base_catalysis_factor`
- This factor multiplies nearly all hydrolysis rates (`k_U`, `k_T`, `k_C`, `k_A`) and the cytosine deamination rate.
- Consequently, variation in `base_catalysis_factor` non-linearly modulates the effective impact of `A_U`, `A_C`, activation energies, and the deamination ratio.
- This multiplicative structure is the primary source of the large interaction terms.

### 3.2 Parallel and Competing Degradation Pathways
The model includes several concurrent processes:
- Uracil hydrolysis
- Cytosine deamination (C → U)
- UV-induced damage
- Protective effects from lipid membranes and clay surfaces

These pathways compete and interfere with one another. Changing the rate of one pathway shifts the balance among the others, thereby altering the apparent effect of remaining parameters.

### 3.3 Non-linear Dependence on pH and Temperature
pH- and temperature-dependent factors themselves act non-linearly on the kinetic rates and combine with `base_catalysis_factor`, further amplifying interaction effects.

---

## 4. Scientific Implications

| Aspect                              | Interpretation                                                                 | Implication for the Manuscript                          |
|-------------------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------|
| Support for Stability-Kinetics Ratio | Strong $$\(\tau_{\text{stable}}\)$$ is governed by a network of interacting processes | Reinforces the central theoretical framework            |
| Environmental selection             | Thymine selection depends on combinations of conditions, not single parameters | Consistent with environment-dependent filters           |
| Model behaviour                     | Highly non-additive                                                            | Simple linear sensitivity rankings are insufficient     |
| Parameter reduction                 | Low-influence parameters may be fixed; strongly interacting ones must be retained | Supports efficient future uncertainty quantification    |

**Important note:**  
The presence of strong higher-order interactions is **not a model deficiency**. It reflects the realistic chemical structure of prebiotic degradation and protection networks, where rates typically act multiplicatively and competitively.

---

## 5. Summary

- Higher-order interactions in UPDSF v4.4 are large and statistically robust (ST − S1 ≈ 0.45–0.55 for most parameters).
- The dominant source is the multiplicative action of `base_catalysis_factor` combined with parallel degradation pathways.
- This interaction structure is fully consistent with the mechanistic narrative of the manuscript, particularly the emphasis on hydrolytic stability differences and base-catalyzed processes.
- Convergence diagnostics confirm that the interaction estimates are stable at N = 5,000.

**Conclusion**  
Higher-order interactions demonstrate that thymine selection emerges from an interconnected kinetic network rather than from isolated parameter effects. This feature increases the chemical realism of the model and provides additional quantitative support for the Stability-Kinetics Ratio framework presented in the manuscript.

---
