# Comparison with Related Works

## Overview

The transition from an RNA world to a DNA-based genetic system required the replacement of uracil (U) by thymine (T). While the superior chemical stability of thymine has long been recognized, quantitative models that examine how prebiotic environmental conditions could have driven this selection remain scarce.

UPDSF v4.4 is a stochastic kinetic Monte Carlo framework that simulates the direct competition between uracil and thymine across four archetypal prebiotic environments (hydrothermal vents, cryogenic eutectic phases with lipid vesicles, UV-exposed tidal pools, and wet–dry cycling regimes). Molecular fitness is quantified by the Stability–Kinetics Ratio:

$$
S_r = \dfrac{\tau_{\mathrm{stable}}}{\kappa_{\mathrm{poly}}}
$$

where $$\(\tau_{\mathrm{stable}}\)$$ is the effective lifetime under the dominant degradation pathways and $$\(\kappa_{\mathrm{poly}}\)$$ is the effective polymerization rate constant.

The model uses strictly literature-derived kinetic parameters and is accompanied by extensive uncertainty and sensitivity analyses (200 independent Monte Carlo realizations, variance-based Sobol global sensitivity analysis with 160 000 model evaluations, Monte Carlo variance decomposition, higher-order interaction analysis, and targeted deamination-knockout experiments).

Below we place UPDSF v4.4 in the context of the most relevant previous studies.

## Detailed Comparison Table

| Work | Year | Primary Method | Explicit U vs T Competition | Environments / Conditions | Sensitivity & Uncertainty Analysis | Main Finding Relevant to Thymine Selection | Relationship to UPDSF v4.4 |
|------|------|----------------|-----------------------------|---------------------------|------------------------------------|--------------------------------------------|----------------------------|
| **Hashemi (UPDSF v4.4)** | 2026 | Stochastic Kinetic Monte Carlo | Yes – direct competition | Hydrothermal (80–100 °C), cryogenic eutectic + lipids (−20 °C), UV tidal pools, wet–dry cycles | 200 MC runs + Sobol GSA (N = 5 000, 160 000 evaluations) + variance decomposition + deamination knockout | Strong environment-dependent selection; T preferred in high-T / UV / wet–dry regimes; U retains kinetic advantage only in cold lipid-assisted eutectic phases. A_U and base_catalysis_factor dominate enrichment variance. Deamination modulates magnitude (~25 %) but is not required for selection. | — |
| Walker, Grover & Hud | 2012 | Spatially explicit hybrid Kinetic Monte Carlo | No (sequence-level) | Hydration–dehydration cycles on mineral surfaces | Limited parameter exploration | Environmental cycles allow continuous exploration of sequence space and establishment of functional polymers | Methodological foundation. UPDSF adopts the cyclic environmental driving force and extends it to base-specific degradation kinetics. |
| Castanedo & Matta | 2022 | Quantum-chemical thermodynamics (DFT) | Thermodynamic preference only | Gas-phase and implicit solvent | None | Thermodynamics favor incorporation of uracil into RNA and thymine into DNA | Complementary thermodynamic perspective. UPDSF quantifies the kinetic and environmental filters that can realize this preference. |
| Pearce & Pudritz | 2016 | Thermodynamic & kinetic modeling of meteorite parent-body chemistry | Synthesis & survival (C deamination, T formation route) | Aqueous alteration inside planetesimals | Temperature and water/rock ratio variation | Cytosine is unstable under aqueous conditions; thymine has a favorable formation pathway from uracil + formaldehyde + formic acid | Provides synthesis constraints used as background assumptions in UPDSF. |
| Frisch, Bishop & Roth | 1977 | Early Monte Carlo of self-replicating macromolecules | No | Abstract model | None | Cooperativity and specificity can stabilize replicating systems | Historical precursor of stochastic polymer models. |
| Calaça Serrão / Schwintek | 2024 | Theory + experiment on cyclic phase separation | Sequence selection via coacervation | Temperature-driven phase cycles | Experimental enrichment factors | Complementary sequences are preferentially enriched in the dense phase | Orthogonal physical selection mechanism that can operate in parallel with the chemical stability filters of UPDSF. |
| Deamer / Damer & Deamer | 2017–2023 | Experimental wet–dry cycles and fatty-acid vesicles | Polymer survival & encapsulation | Geothermal wet–dry cycles, protocell environments | Empirical protection factors (typically 2–5×) | Amphiphiles suppress depurination and protect polymers; wet–dry cycles drive polymerization | Lipid-protection factor (2–5×) and ratchet effect are directly incorporated into the UPDSF vesicle module. |
| Cadet & Ravanat | 1995–2005 | Experimental photochemistry | Photodimerization rates | UV-irradiated aqueous solutions | Dose–response measurements | Thymine forms cyclobutane pyrimidine dimers 3–4× less efficiently than uracil | Source of the UV-resistance parameters used in the tidal-pool simulations. |
| Lindahl | 1993 | Experimental hydrolysis kinetics | Hydrolytic stability | Aqueous solutions, varied T and pH | Half-life data | Thymine has ~15 kJ mol⁻¹ higher activation energy for hydrolysis than uracil | Core kinetic parameters (Eₐ_T vs Eₐ_U) of the UPDSF degradation network. |
| Shen et al. | 1994 | Experimental deamination rates | C → U conversion | Double-stranded DNA | Rate constants | 5-methylcytosine deaminates ~2.2× faster than cytosine in dsDNA at 37 °C | Provides the experimental basis for cytosine deamination kinetics. Controlled knockout experiments in UPDSF show that this pathway modulates but does not create the selective advantage of thymine. |
| Sutherland group | 2015–2023 | Prebiotic synthetic chemistry | Co-synthesis of RNA and DNA precursors | One-pot cyanosulfidic / formose-type pathways | Yield and selectivity under different conditions | Both uracil and thymine precursors can be formed; environmental conditions can bias product distribution | Supports the premise that both bases were available prebiotically. UPDSF examines how subsequent environmental filters can preferentially preserve thymine. |

## Key Distinguishing Features of UPDSF v4.4

1. **Direct kinetic competition** between uracil and thymine rather than sequence-level or purely thermodynamic analysis.
2. **Multi-environment scope** covering the major proposed prebiotic niches in a single consistent framework.
3. **Stability–Kinetics Ratio (\(S_r\))** as an explicit quantitative fitness metric linking molecular lifetime to polymerization potential.
4. **Comprehensive global sensitivity analysis** (Sobol indices, higher-order interactions, variance decomposition) that identifies A_U (pre-exponential factor for uracil hydrolysis) and base_catalysis_factor as the dominant drivers of thymine enrichment.
5. **Mechanistic isolation of cytosine deamination**: controlled experiments demonstrate that C → U conversion affects the magnitude of enrichment (~25 %) but is not required for the qualitative selective advantage of thymine.
6. **Strict literature-derived parameterization** with public code and data (GitHub + Zenodo), enabling full reproducibility and further extension.

## Summary

Previous studies have established the thermodynamic preference for thymine in DNA, the synthetic accessibility of thymine under certain prebiotic conditions, the protective role of lipids and wet–dry cycles, and the power of environmental cycling to drive sequence evolution. UPDSF v4.4 integrates these insights into a single stochastic kinetic framework that quantifies how heterogeneous prebiotic environments can act as deterministic physicochemical filters favoring thymine over uracil.
