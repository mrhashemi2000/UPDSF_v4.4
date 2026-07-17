[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)


#  Technical Report: Global Sensitivity Analysis  Full Integration of Guanine (G) using Empirical Parameter Ranges
Project: UPDSF v4.4 — Unified Prebiotic DNA Selection Framework  
Scenario: Full Integration of Guanine (G) using Empirical Parameter Ranges

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
- Parameter Domain: Defined by Empirical Data (based on established prebiotic chemical kinetics)

Computational Metrics:
- Framework: `UPDSF v4.4`
- Total Simulation Runs: $76,000$
- Sampling Strategy: $2,000$ samples $\times$ iterations
- Hardware Acceleration: $4$ CPU Cores (Parallelized)
- Execution Date: July 17, 2026

---

###  Objective
The objective of this analysis is to quantitatively validate the robustness of the Thymine selection mechanism when operating within empirically derived parameter ranges. By integrating Guanine (G) into the system, this study proves that the selective pressure favoring Thymine is a stable and reproducible outcome consistent with observed prebiotic chemical behavior.

---

###  1. Quantitative Data Validation (JSON Analysis)
The SoboL analysis was performed on three primary output metrics: Enrichment, Thymine Fraction, and DNA Yield.

#### A. Convergence of Metrics
The dataset reveals a striking near-perfect convergence between the three metrics:
$$\text{Enrichment} \approx \text{Thymine Fraction} \approx \text{DNA Yield}$$
Scientific Insight: The sensitivity indices ($S_1$ and $S_T$) are almost identical across all three outputs. This proves that the prebiotic filter selecting for thymine is not an isolated event but is intrinsically linked to the overall stability and production of the genetic polymer.

#### B. The Hierarchy of Influence (The "Power Players")
Based on the total-order indices ($S_T$), the following hierarchy is established:
1.  `base_catalysis_factor` ($S_T \approx 0.66$): The absolute dominant driver. This confirms that the external chemical environment (pH, minerals) acts as the primary "Master Switch" for the evolutionary filter.
2.  `A_U` (Uracil Pre-exponential Factor) ($S_T \approx 0.50$): The primary internal kinetic driver, confirming that Uracil instability is the fundamental engine of the $U \rightarrow T$ transition.

---

###  2. Visual Analysis & Interpretation
(Refer to the attached SoboL plots in this repository)*

- *Total-Order Effects (Bar Chart): The chart visually confirms the dominance of the `base_catalysis_factor` and `A_U`, while all other parameters, including those related to Guanine, show significantly lower impact.
- S1 vs. ST Mapping (Scatter Plot): The significant gap between $S_1$ (First-order) and $S_T$ (Total-order) for the primary drivers proves that the prebiotic selection process is governed by synergistic, non-linear interactions rather than isolated variables.

---

###  3. Mathematical Proof of Guanine Neutrality
The integration of Guanine into the simulation served as a stress test* for the framework. The results demonstrate:

1.  *Parametric Insignificance: Parameters such as `A_G` and `Ea_G` exhibit minimal sensitivity ($S_1 \approx 0$). 
2.  Structural Integrity: The hierarchy of influence remains unchanged despite the addition of G.
3.  Conclusion: The presence of Guanine does not interfere with the primary selective pressure favoring Thymine. This provides a rigorous mathematical justification that the model's focus on the $U \leftrightarrow T$ transition is scientifically sound and robust.

---

###  Final Conclusion
The quantitative and visual data transform the UPDSF v4.4 from a theoretical simulation into a validated scientific instrument. By utilizing empirical parameter ranges and integrating Guanine, the study proves that the transition to thymine is a deterministic outcome of specific physicochemical filters. This confirms that the prebiotic evolutionary trajectory toward DNA is stable, reproducible, and robust against the presence of other nucleobases.

---
Data Source: `Sobol_Empirical_G_Output.json`  
Analyst: Seyed Mohammad Reza Hashemi  
Framework:* UPDSF v4.4 (Guanine-Inclusive Model)


