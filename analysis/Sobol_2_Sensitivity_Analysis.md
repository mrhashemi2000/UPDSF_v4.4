[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

# Expanded_Analysis_9
# Sobol Global Sensitivity Analysis Report (N=2000) Wide/Empirical Range
# **Supporting Manuscript IJA-2026-0085**


## UPDSF v4.4 — 64,000 Simulation Runs

**Run Date**: July 17, 2026  
**Baseline Conditions**: T = 68.0°C, pH = 7.5, Polymer Length = 100 bases  
**Sample Size**: 2,000 | **Total Runs**: **64,000** | **CPU Cores**: 4

---

##  Executive Summary

An other comprehensive **Sobol global sensitivity analysis** was conducted on the UPDSF v4.4 model using **64,000 simulation runs** (4 forced workers). 

The analysis confirms that the framework is **highly robust** and identifies the most critical parameters driving thymine enrichment under prebiotic conditions.

**Top Two Most Influential Parameters:**
1. **`base_catalysis_factor`** (ST = **0.632**)
2. **`A_U`** — Pre-exponential factor for Uracil hydrolysis (ST = **0.468**)

---

##  Key Results

### Total-order Sobol Indices (ST) — Enrichment

| Rank | Parameter                  | ST Value   | Influence Level |
|------|---------------------------|------------|-----------------|
| 1    | `base_catalysis_factor`   | **0.632**  | Very High       |
| 2    | `A_U`                     | **0.468**  | Very High       |
| 3    | `A_C`                     | 0.158      | Moderate        |
| 4    | `A_A`                     | 0.126      | Moderate        |
| 5    | `clay_protection`         | 0.107      | Low             |
| -    | Other parameters (Ea, UV, lipid, deamination) | 0.095–0.107 | Low |

### First-order vs Total-order (S1 vs ST)

The scatter plot shows significant **interaction effects**, especially for the top parameters. Points far from the diagonal line indicate strong higher-order interactions.

---

##  Interpretation & Scientific Insights

- **`base_catalysis_factor`** dominates because pH-dependent base catalysis strongly affects hydrolysis rates of all nucleotides.
- **`A_U`** is critical as it controls the degradation rate of uracil-rich polymers — the key differentiator between RNA-like and DNA-like systems.
- Lower influence of `clay_protection` and `lipid_protection` suggests they act as **modulators** rather than primary drivers.
- The model shows excellent **robustness**: The dominant parameters remain consistent even when parameter ranges are varied (narrow vs. wide/empirical).

This aligns perfectly with the empirical literature integrated in v4.4 (Lindahl 1993, Cleaves 2010, Shapiro 1999, Ravanat & Cadet, Deamer & Szostak, etc.).

---

##  Methodology

- **Sampling:** Saltelli method (SALib)
- **Simulation Engine:** Optimized lightweight version of `UPDSF_v4.4.py`
- **Workers:** Forced 4-core multiprocessing (no automatic reduction)
- **Outputs:** Thymine enrichment, thymine fraction, total DNA yield
- **Total Runs:** 64,000
- **Runtime:** ~3.3 hours

---

##  Files Generated

- `sobol_data_*.csv` — Raw simulation results
- `sobol_indices_*.json` — Sobol indices (S1, ST)
- `sobol_analysis.png` — Visualizations (Total-order bar chart + S1 vs ST scatter)
- `sobol_results/` — Complete output directory

---

##  Visualizations

<img width="2078" height="1184" alt="sobol_analysis" src="https://github.com/user-attachments/assets/e7623310-e356-43bb-b8a1-31dff7cab090" />




---

##  Recommendations

1. **Future Experiments:** Focus laboratory validation on `base_catalysis_factor` and `A_U`.
2. **Simulation Strategy:** Use wide ranges for exploration, narrow ranges for precise predictions.
3. **Model Strength:** The consistent identification of the same key drivers across different parameter bounds demonstrates strong **model robustness**.

---

##  References

- Lindahl, T. (1993). *Nature*
- Cleaves, H.J. (2010). *Astrobiology*
- Shapiro, R. (1999). *Chem. Rev.*
- Ravanat & Cadet (UV damage)
- Deamer & Szostak (Lipid membranes)

Full references available in `UPDSF_v4.4.py`.

---

**Conclusion:**  
The Sobol analysis validates the scientific soundness of UPDSF v4.4 and clearly highlights the physicochemical mechanisms most responsible for the chemical selection of DNA nucleotides in prebiotic environments.

*This work contributes to reproducible, empirically-grounded origins-of-life research.*

---

**License:** CC BY-NC-ND 4.0  
**DOI:** See Zenodo archives in the main repository.
