[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
# Expanded_Analysis_8
**Supporting Manuscript IJA-2026-0085**

**Date**: July 27, 2026  

**Manuscript**  
*Environmental Selection of Thymine over Uracil in Prebiotic Chemical Evolution: Insights from a Kinetic Monte Carlo Model*  
(International Journal of Astrobiology – Draft)
# Monte Carlo Variance Decomposition in UPDSF v4.4

## Supporting Manuscript: IJA-2026-0085  
Analysis Conditions: $N = 5,000$ (160,000 total evaluations) | $T = 68.0$ °C | $\text{pH} = 7.5$ | Polymer length = 100 bases  


---

## 1. Core Concept

Monte Carlo variance decomposition (the foundation of Sobol sensitivity analysis) addresses a fundamental question:

> How much of the total variance in a model output can be attributed to each input parameter, and how much arises from their interactions?

The total variance of an output $Y$ is decomposed as:

$V(Y) = \sum_{i} V_i + \sum_{i < j} V_{ij} + \sum_{i < j < k} V_{ijk} + \dots + V_{1,2,\dots,d}$

Where:
- $V_i$ = main-effect (first-order) variance of parameter $i$
- $V_{ij}$ = second-order interaction variance between parameters $i$ and $j$
- Higher-order terms = higher-order interactions

---

## 2. Sobol Indices as Normalized Variance Contributions

Sobol indices are the normalized forms of these variance components:

First-order index:
$S_i = \frac{V_i}{V(Y)}$

Second-order index:
$S_{ij} = \frac{V_{ij}}{V(Y)}$

Total-order index:
$S_{T_i} = \frac{V_i + \text{all interactions involving } i}{V(Y)}$

The interaction contribution of parameter $i$ is therefore:  
$S_{T_i} - S_i$

---

## 3. Application to UPDSF v4.4 (Enrichment Output)

From the Sobol analysis performed at $T = 68$ °C and $\text{pH} = 7.5$:

| Parameter | Approximate Role in Variance Decomposition | Observed Behaviour |
| :--- | :--- | :--- |
| $A_U$ | Dominates first-order and interaction variance of uracil hydrolysis | Highest $S_T$ ($\approx 0.775$) |
| `base_catalysis_factor` | Strongly multiplies multiple rates $\rightarrow$ large interaction terms | High $S_T$ ($\approx 0.672$) with large $S_T - S_1$ |
| $A_C$ | Contributes via the cytosine deamination pathway ($C \rightarrow U$) | Moderate-to-high total-order contribution |
| Other parameters | Contribute primarily through interactions | $S_T - S_1 \approx 0.45 \text{--} 0.55$ |

Key quantitative finding:
A substantial fraction of the total variance in thymine enrichment is carried by interaction terms*, not by independent main effects. This explains the consistently large $S_T - S_1$ values.

---

## 4. Why the Variance Structure Appears This Way

The observed decomposition reflects the mathematical structure of the UPDSF v4.4 model:

### 4.1 Multiplicative Kinetics
`base_catalysis_factor` multiplies nearly all hydrolysis rates ($k_U, k_T, k_C, k_A$) and the deamination rate. Any variation in this factor non-linearly scales the effects of $A_U, A_C$, and related parameters, generating large interaction variances.

### 4.2 Parallel and Competing Degradation Pathways
The model contains several concurrent processes:
- Uracil hydrolysis
- Cytosine deamination (producing additional $U$)
- UV-induced damage
- Protective effects from lipid membranes and clay surfaces

These pathways are not independent. Changing the rate of one pathway shifts the relative importance of the others.

### 4.3 Non-linear Environmental Modulation

Temperature and pH enter the rate equations non-linearly (Arrhenius terms + pH-dependent factors) and combine with `base_catalysis_factor`, further amplifying cross-terms in the variance expansion.

---

## 5. Practical Consequences of the Decomposition

| Observation | Implication |
| :--- | :--- |
| Large $S_T - S_1$ values | The model is strongly non-additive. One-at-a-time (OAT) sensitivity analysis would be misleading. |
| Dominance of $A_U$ + `base_catalysis_factor` | These are the primary "leverage points" of the system. |

---

## 6. Relation to the Manuscript’s Theoretical Framework

The Stability-Kinetics Ratio defined in the manuscript is:

$S_r = \frac{\tau_{\text{stable}}}{\kappa_{\text{poly}}}$

The Monte Carlo variance decomposition shows that, under the tested conditions, the dominant contribution to variance in enrichment originates from parameters controlling $\tau_{\text{stable}}$ (especially those governing uracil lifetime). This provides a direct quantitative link between the global sensitivity results and the manuscript’s central claim that thymine is preferentially selected due to superior molecular stability.

---

## 7. Consistency with Code, Manuscript, and Supplementary Material

The variance decomposition is fully consistent with:
- The multiplicative kinetic structure implemented in `UPDSF_v4.4.py`
- The ranking of influential parameters reported in the Sobol analysis
- The Stability-Kinetics Ratio framework and environmental selection narrative presented in the manuscript (IJA-2026-0085)
- The literature-derived parameter values listed in the Supplementary Information

No contradictions were identified between the variance structure and the published model, code, or scientific claims.

---

## 8. Summary

Monte Carlo variance decomposition of UPDSF v4.4 reveals a system in which:
- Output variance is not a simple sum of independent parameter effects.
- Higher-order interactions carry a large share of the total variance.
- The interaction structure is mechanistically expected from the multiplicative and competitive nature of the kinetic network.
- The dominant variance contributors align closely with the stability-driven selection mechanism proposed in the manuscript.

This decomposition therefore serves both as a diagnostic of model behaviour and as independent computational support for the scientific narrative of environmental selection of thymine over uracil.

