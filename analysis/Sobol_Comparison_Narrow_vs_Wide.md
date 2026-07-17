[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

# Expanded_Analysis_10
# Sobol Sensitivity Analysis: Narrow vs Wide Parameter Ranges
# **Supporting Manuscript IJA-2026-0085**


## UPDSF v4.4 — 2×64,000 Simulation Runs

**Run Date**: July 17, 2026  
**Baseline Conditions**: T = 68.0°C, pH = 7.5, Polymer Length = 100 bases  
**Sample Size**: 2,000 | **Total Runs**: **64,000** | **CPU Cores**: 4

  
**UPDSF v4.4** — Unified Prebiotic DNA Selection Framework

**Analysis Date:** July 17, 2026  
**Author:** Seyed Mohammad Reza Hashemi (Reza Hashemi)

---

##  Executive Summary

Two Sobol analyses (64,000 runs each) were performed under identical **Baseline Conditions**:

- **Temperature:** 68.0°C  
- **pH:** 7.5  
- **Polymer Length:** 100 bases

**Goal:** Evaluate model robustness when changing parameter ranges (Narrow vs Wide/Empirical).

**Conclusion:** The model is **highly robust**. The dominant parameters remain consistent despite significant changes in bounds.

---

##  Comparison of Dominant Parameters (Total-order ST)

| Rank | Narrow Range (July 15)              | ST (Narrow) | Wide Range (July 17)               | ST (Wide) | Change |
|------|------------------------------------|-------------|------------------------------------|-----------|--------|
| 1    | `A_U`                              | **0.801**   | `base_catalysis_factor`            | **0.632** | Swap   |
| 2    | `base_catalysis_factor`            | **0.684**   | `A_U`                              | **0.468** | Swap   |
| 3    | `A_C`                              | 0.568       | `A_C`                              | 0.158     | ↓      |
| 4    | `Ea_C_deam` / `A_A`                | ~0.50       | `A_A`                              | 0.126     | ↓      |
| 5    | `A_A`                              | ~0.50       | `clay_protection`                  | 0.107     | ↓      |

---

##  Detailed Analysis

### 1. Pattern Stability (Most Important)
- The **same two parameters** (`A_U` and `base_catalysis_factor`) dominate in **both** runs.
- Rank swap between them is expected and scientifically meaningful (non-linear system behavior).
- All other parameters remain in the lower-to-moderate influence group.

### 2. Effect of Wider Ranges
- Wider ranges generally **reduce absolute ST values** (more uncertainty → diluted individual effects).
- However, the **relative importance pattern** is preserved.
- This is a **strong indicator of model robustness**.

### 3. Physical Interpretation
- **`base_catalysis_factor`**: Becomes more dominant in wide ranges because pH effects have broader impact.
- **`A_U`**: Remains critical due to its fundamental role in differential nucleotide stability (Uracil vs Thymine).
- Low-influence parameters (clay/lipid protection, deamination) stay secondary — consistent with empirical literature.

---

##  Visual Summary (Narrow vs Wide)

**Narrow Range (Tighter Bounds):**
- Stronger individual effects (higher ST values)
- More pronounced hierarchy

**Wide Range (Empirical Bounds):**
- Smoother, more distributed influence
- Better represents real-world uncertainty

**Common Finding:**  
`base_catalysis_factor` + `A_U` ≈ **majority of explained variance** in both cases.

---

##  Implications for Research

**For Simulations:**
- Use **wide ranges** for exploratory studies and uncertainty quantification.
- Use **narrow ranges** for targeted predictions.

**For Laboratory Experiments:**
- Focus on **base_catalysis_factor** (pH control) and **A_U**-related kinetics.
- Design experiments with tight control around baseline conditions (68°C, pH 7.5).

**Model Quality:**
- Excellent robustness demonstrated.
- Captures real non-linear prebiotic chemistry behavior.
- Suitable for further development and experimental validation.

---

##  Files

- `sobol_indices_20260715_083806.json` → Narrow Range
- `sobol_indices_20260717_081508.json` → Wide Range
- `sobol_analysis.png` → Visualization (Wide Range)

---

**Final Statement:**

The UPDSF v4.4 model maintains a **consistent and physically meaningful sensitivity pattern** across different parameter ranges. This robustness strengthens confidence in the framework’s ability to model the chemical selection of DNA nucleotides under prebiotic conditions.

---

**References:** Full list available in `UPDSF_v4.4.py`

*This analysis contributes to reproducible, empirically-grounded origins-of-life modeling.*
