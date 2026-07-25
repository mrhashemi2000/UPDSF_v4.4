# Alignment of Sobol Sensitivity Results with the UPDSF v4.4 Manuscript ID: IJA-2026-0085 Findings

**Sobol Analysis Conditions**  
N = 5000 (160,000 total evaluations) | T = 68.0 °C | pH = 7.5 | Polymer length = 100 bases

**Manuscript**  
*Environmental Selection of Thymine over Uracil in Prebiotic Chemical Evolution: Insights from a Kinetic Monte Carlo Model*  
(International Journal of Astrobiology – Draft)

---

## 1. Theoretical Framework Correspondence

The manuscript defines molecular fitness via the **Stability-Kinetics Ratio**:

\[
S_r = \frac{\tau_{\text{stable}}}{\kappa_{\text{poly}}}
\]

where:
- \(\tau_{\text{stable}}\) = half-life under dominant degradation pathways (hydrolysis, deamination, UV damage)
- \(\kappa_{\text{poly}}\) = effective polymerization rate constant

### Sobol Mapping to \(S_r\)

| Sobol Rank | Parameter                  | ST     | Primary Influence on \(S_r\)              | Manuscript Interpretation                          |
|------------|----------------------------|--------|-------------------------------------------|----------------------------------------------------|
| 1          | **A_U**                    | 0.7751 | Controls \(\tau_{\text{stable}}\) of U    | Dominant driver of the T/U stability differential |
| 2          | **base_catalysis_factor**  | 0.6718 | Amplifies all degradation rates           | Strong modulator of hydrolytic and deamination pathways |
| 3          | **A_C**                    | 0.5434 | Controls cytosine deamination (C → U)     | Indirect reduction of thymine enrichment via U production |
| —          | deamination_ratio          | —      | Scales C → U conversion (literature 36×)  | Explicitly cited (Shen et al., 1994)               |

**Key Insight**  
Under the tested conditions (68 °C, pH 7.5), output variance (thymine enrichment) is overwhelmingly controlled by parameters that govern \(\tau_{\text{stable}}\), not \(\kappa_{\text{poly}}\). This quantitatively supports the manuscript’s central claim that thymine is preferentially selected due to superior resistance to hydrolysis, deamination, and photodimerization.

---

## 2. Alignment with Environmental Case Studies

The Sobol analysis was performed at conditions intermediate between the manuscript’s **Tidal Pool** and **Hydrothermal** regimes.

| Manuscript Environment              | Key Conditions          | Reported Outcome                          | Sobol Alignment (68 °C, pH 7.5)                          |
|-------------------------------------|-------------------------|-------------------------------------------|----------------------------------------------------------|
| Hydrothermal Vents                  | 80–100 °C              | \(\tau_T / \tau_U \approx 124\)           | A_U and base_catalysis_factor dominate → thermal-hydrolytic selection confirmed |
| Tidal Pools + UV Exposure           | Surface, high UV       | Thymine preferred (photochemical shield)  | UV_resistance_T shows moderate influence; hydrolysis (A_U) remains primary |
| Wet-Dry Cycles                      | Mineral surfaces       | Ratchet effect favoring thymine           | clay_protection exhibits moderate ST → consistent with surface stabilization |
| Cryogenic Eutectic + Lipid          | −20 °C + vesicles      | Kinetic advantage for uracil              | Outside Sobol temperature range; lipid_protection shows only moderate effect |

**Interpretation**  
At 68 °C the system lies in the regime where hydrolytic stability differences (controlled by A_U and base catalysis) outweigh polymerization kinetics or low-temperature concentration effects. This matches the manuscript’s finding that high-temperature and UV-exposed environments impose deterministic filters favoring thymine.

---

## 3. Interaction Structure

Sobol results reveal substantial higher-order interactions across nearly all parameters (ST − S1 ≈ 0.45–0.55), with **base_catalysis_factor** displaying the strongest interaction signature.

This is mechanistically consistent with the model structure described in the manuscript:
- Base catalysis multiplies the rates of hydrolysis (U, T, C, A) and cytosine deamination.
- Consequently, variation in `base_catalysis_factor` modulates the effective impact of A_U, A_C, and related parameters — producing the strong non-additive behaviour observed in the Sobol analysis.

---

## 4. Parameter Importance Groups vs. Manuscript Emphasis

**Critical parameters (retain for future work)**  
- `A_U` — primary control of uracil degradation (core of the T/U stability gap)
- `base_catalysis_factor` — universal amplifier of degradation pathways
- `A_C` + `deamination_ratio` — cytosine deamination route to uracil

**Moderate parameters**  
- `lipid_protection`, `clay_protection` — correspond to vesicle and mineral-surface effects discussed in the manuscript
- `UV_resistance_T` — relevant to the tidal-pool/UV case study
- `A_T` / `Ea_T` — secondary contributors to the stability differential

**Low-influence parameters (can be fixed at nominal values)**  
- Activation energies and pre-factors for less dominant pathways (`Ea_U`, `Ea_A`, `Ea_C_deam`, `A_A`, `UV_resistance_C`, `UV_resistance_A`)

This screening is fully compatible with the manuscript’s emphasis on a small set of literature-derived kinetic differences (especially the 15 kJ mol⁻¹ higher hydrolysis activation energy of thymine and the 36× deamination ratio).

---

## 5. Convergence and Robustness

Bootstrap convergence analysis confirms that both first-order (S1) and total-order (ST) indices stabilize after approximately 80,000–100,000 evaluations. The final ST for Enrichment converges to ≈ 1.0018, indicating that the full output variance is captured.

Thus the ranking and interaction structure reported above are numerically robust and can be confidently mapped onto the mechanistic narrative of the manuscript.

---

## 6. Summary of Alignment

| Sobol Finding                              | Corresponding Manuscript Claim                                      | Strength of Alignment |
|--------------------------------------------|---------------------------------------------------------------------|-----------------------|
| A_U is the dominant parameter              | Higher Ea and longer half-life of thymine vs. uracil                | Very High             |
| base_catalysis_factor shows strong interactions | Base-catalyzed hydrolysis and deamination in high-T regimes     | Very High             |
| A_C and deamination_ratio are influential  | 36× cytosine deamination (Shen et al., 1994)                        | High                  |
| lipid & clay protection are moderate       | Vesicle protection (2–5×) and mineral-surface effects               | High                  |
| UV effects secondary at 68 °C              | Hydrolysis dominates over photodamage at moderate temperature       | Consistent            |
| Strong non-additive interactions           | Environment-dependent, non-linear selection filters                 | Very High             |

**Overall Conclusion**  
The Sobol sensitivity analysis performed at T = 68 °C and pH = 7.5 provides quantitative, parameter-level support for the central thesis of the manuscript: under intermediate-to-high temperature prebiotic conditions, thymine selection is driven primarily by differences in molecular stability (\(\tau_{\text{stable}}\)), especially the hydrolytic degradation rate of uracil, rather than by polymerization kinetics. The observed importance ranking and interaction structure are fully consistent with the Stability-Kinetics Ratio framework and the environmental case studies presented in the paper.

---
