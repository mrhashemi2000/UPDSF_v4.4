
#  Technical Report: Expanded Global Sensitivity Analysis Full Integration of Guanine (G) into the Nucleobase Population
Project: UPDSF v4.4 — Unified Prebiotic DNA Selection Framework  
Focus: SoboL Sensitivity Analysis (Narrow vs. Wide Parameter Ranges)  
Scenario: Full Integration of Guanine (G) into the Nucleobase Population

---

###  Document Metadata
| Field | Details |
| :--- | :--- |
| Document ID | `Expanded_Analysis_10` |
| Supporting Manuscript | `IJA-2026-0085` |
| Author | Seyed Mohammad Reza Hashemi (Reza Hashemi) |
| Analysis Date | July 17, 2026 |
| License | `CC BY-NC-ND 4.0` |
| DOI | 10.5281/zenodo.21224889 |

---

###  Simulation Configuration
Baseline Environmental Conditions:
- Temperature: $68.0^\circ\text{C}$
- pH Level: $7.5$
- Polymer Length: $100$ bases
- Chemical Scope: Uracil (U), Thymine (T), Adenine (A), Cytosine (C), and Guanine (G)

Computational Metrics:
- Framework: `UPDSF v4.4`
- Total Simulation Runs: $76,000$
- Sampling Strategy: $2,000$ samples $\times$ iterations
- Hardware Acceleration: $4$ CPU Cores (Parallelized)
- Execution Date:* July 17, 2026

---

###  Objective
The primary goal of this specific run is to validate the structural stability of the Thymine selection mechanism in the presence of Guanine, comparing the sensitivity indices across both narrow and wide empirical parameter ranges to ensure the model captures real-world biochemical "Regime Shifts."


# Quantitative Validation: SoboL Sensitivity Analysis (With Guanine Integration)

##  Executive Summary
This document provides a detailed quantitative interpretation of the Sobol Global Sensitivity Analysis (GSA) conducted on the UPDSF v4.4 framework, specifically in the scenario where Guanine (G) is integrated into the chemical population. By analyzing 76,000 independent simulations, this study proves that the inclusion of an additional nucleobase does not disrupt the core selection mechanism, but rather validates the model's structural robustness.

---

##  1. Convergence of Output Metrics
The dataset reveals a striking near-perfect convergence between three critical metrics:
- Enrichment $\approx$ Thymine Fraction $\approx$ DNA Yield

Scientific Insight: Even with the added complexity of Guanine, the sensitivity indices ($S_1$ and $S_T$) for all three outputs remain almost identical. This proves that the prebiotic filter selecting for thymine is intrinsically linked to the overall survival and yield of the genetic polymer, regardless of the presence of other bases.

---

##  2. The Hierarchy of Influence (The "Power Players")

Despite the inclusion of Guanine, the hierarchy of influence remains dominated by two primary drivers:

### A. The Deterministic Driver: `base_catalysis_factor`
- $S_1 \approx 0.43$ | $S_T \approx 0.66$
- Analysis: Accounting for roughly 66% of the total variance, this parameter remains the absolute master switch. It confirms that the external chemical environment (pH and mineral catalysis) is the most critical factor in the evolutionary filter, outweighing the specific effects of individual base additions.

### B. The Kinetic Engine: `A_U` (Uracil Pre-exponential Factor)
- $S_1 \approx 0.29$ | $S_T \approx 0.50$
- Analysis: The high $S_T$ value confirms that the intrinsic instability of Uracil is the fundamental internal driver of the $U \rightarrow T$ transition.

---

##  3. Mathematical Proof of Guanine Neutrality
One of the most important results of this analysis is the quantitative insignificance of Guanine-specific parameters:

- Low Sensitivity of G-Parameters: Parameters such as `A_G` and `Ea_G` exhibit minimal sensitivity indices ($S_1 \approx 0$ and low $S_T$).
- Conclusion: This provides a rigorous mathematical justification that while Guanine is a natural part of the system, it does not interfere with the primary selective pressure favoring Thymine. This proves that the model's focus on the $U \leftrightarrow T$ transition is scientifically sound and not an oversimplification.

---

##  4. Computational Rigor
The validity of these results is supported by high-fidelity simulation metrics:
- Sample Size: $n = 76,000$ runs (ensuring statistical significance).
- Dimensionality: 18-dimensional parameter space explored.
- Computational Effort: $\approx 4.6$ hours of multi-threaded execution.

##  Final Conclusion
The integration of Guanine serves as a stress test for the UPDSF v4.4 framework. The results demonstrate that the transition to thymine is a deterministic outcome of specific physicochemical filters and is robust against the presence of other nucleobases*. This confirms that the model is a reliable scientific instrument for predicting prebiotic evolutionary trajectories.

---

*Data Source: `Sobol_Analysis_With_G_Output.json`  
