[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

## UPDSF_v4.4: Unified Prebiotic DNA Selection Framework 

Environment: 🐍 Python 3.8+

## Author: Seyed Mohammad Reza Hashemi (Reza Hashemi)

## ORCID: 0009-0002-0645-5180


> **Note on File Management**
> 
> To simplify the page layout (due to the high volume of data) and improve readability, some deleted files have been removed from the current view. However, they remain fully accessible and visible within the **History** section.

## 📑 Zenodo Archive & Digital Object Identifiers (DOIs)
To ensure full transparency and reproducibility, the computational data and various versions of this framework are archived on Zenodo.

| Resource / DOI | Link |
| :--- | :--- |
| 📄 Zenodo 17273763 | [Click to Open](https://doi.org/10.5281/zenodo.17273763) |
| 📄 Zenodo 18137476 | [Click to Open](https://doi.org/10.5281/zenodo.18137476) |
| 📄 Zenodo 18092867 | [Click to Open](https://doi.org/10.5281/zenodo.18092867) |
| 📄 Zenodo 18080826 | [Click to Open](https://doi.org/10.5281/zenodo.18080826) |
| 📄 Zenodo 20988680 | [Click to Open](https://doi.org/10.5281/zenodo.20988680) |
| 📄 Zenodo 20825578 | [Click to Open](https://doi.org/10.5281/zenodo.20825578) |
| 📄 Zenodo 20733760 | [Click to Open](https://doi.org/10.5281/zenodo.20733760) |
| 📄 Zenodo 20759622 | [Click to Open](https://doi.org/10.5281/zenodo.20759622) |
| 📄 Zenodo 20771213 | [Click to Open](https://doi.org/10.5281/zenodo.20771213) |
| 📄 Zenodo 18594133 | [Click to Open](https://doi.org/10.5281/zenodo.18594133) |
| 📄 Zenodo 17280179 | [Click to Open](https://doi.org/10.5281/zenodo.17280179) |
| 📄 Zenodo 17964430 | [Click to Open](https://doi.org/10.5281/zenodo.17964430) |
| 📄 Zenodo 15290482 | [Click to Open](https://doi.org/10.5281/zenodo.15290482) |
| 📄 Zenodo 15428322 | [Click to Open](https://doi.org/10.5281/zenodo.15428322) |
| 📄 Zenodo 15428338 | [Click to Open](https://doi.org/10.5281/zenodo.15428338) |
| 📄 Zenodo 15428356 | [Click to Open](https://doi.org/10.5281/zenodo.15428356) |
| 📄 Zenodo 15428367 | [Click to Open](https://doi.org/10.5281/zenodo.15428367) |


---

## 🌍 Scientific Motivation

This study addresses **one of the fundamental questions in origin-of-life (OoL) research**:

> **Why did DNA evolve to use thymine rather than uracil as its canonical pyrimidine base?**

Rather than proposing a definitive historical reconstruction, this work develops and quantitatively tests a **mechanistic hypothesis** in which **prebiotic environmental selection**, acting through **molecular stability** and **reaction kinetics**, could have biased this transition **before the emergence of enzymatic evolution**.

Using the **UPDSF v4.4 Monte Carlo framework**, the study evaluates how environmental factors—including temperature, pH, ultraviolet radiation, lipid membrane protection, wet–dry cycling, and hydrothermal conditions—collectively influence the relative persistence and evolutionary selection of thymine over uracil.

The accompanying open-source repository provides the complete computational framework, datasets, reproducibility scripts, and complementary validation analyses supporting this hypothesis in accordance with the principles of **Open Science**.

## Overview



#### UPDSF_v4.4 is a high-fidelity computational engine designed to model the chemical selection and evolutionary dominance of DNA nucleotides (specifically Thymine) under prebiotic conditions. Developed by Seyed Mohammad Reza Hashemi, this framework operates under the Matter World Hypothesis (MWH) and represents a case study in Intelligence-Augmented (IA) Science.This version is Lipid Membrane added.

Unlike theoretical models, v4.4 is strictly empirical (literature based), utilizing kinetic parameters, activation energies ($E_a$), and half-lives derived exclusively from peer-reviewed prebiotic chemistry literature.

UPDSF v4.4 is a stochastic kinetic Monte Carlo simulation framework that models the competition between **Uracil (U)** and **Thymine (T)** in various prebiotic environments. 

This model was developed to quantitatively investigate the environmental selection mechanisms that may have favored thymine in the transition from RNA to DNA-based heredity.

## **Manuscript**: "Environmental Selection of Thymine over Uracil in Prebiotic Chemical Evolution: Insights from a Kinetic Monte Carlo Model"  
## **Journal**: *International Journal of Astrobiology* (Submitted - IJA-2026-0085)

##  Computational Framework

### Primary Simulation Engine

`UPDSF_v4.4.py` is the **primary Monte Carlo simulation engine** used to generate all scientific results reported in the manuscript.

The model simulates the environmental selection of thymine over uracil under a range of prebiotic conditions, including:

-  Temperature
-  pH
-  UV radiation
-  Lipid membrane protection
-  Clay mineral protection
-  Wet–dry cycling
-  Hydrothermal environments

All figures, statistical analyses, and conclusions presented in the manuscript are derived directly from this simulation framework.

---

### Complementary Global Sensitivity Analysis

The repository also contains an independent **Global Sobol Sensitivity Analysis**, which serves as a **complementary validation** of the Monte Carlo model.

Its purpose is **not** to generate new scientific conclusions, but to quantitatively evaluate the robustness of the model by identifying the internal parameters that contribute most to output uncertainty.

The Sobol analysis demonstrates that the dominant parameters correspond to the same mechanistic processes proposed in the manuscript, particularly:

- the greater instability of uracil,
- base-catalyzed degradation,
- and the stability–kinetics relationship described by the manuscript's theoretical framework.

Importantly, the Sobol analysis validates the computational model at the **parameter level**, whereas the manuscript presents its scientific findings at the **environmental level** (temperature, pH, UV exposure, lipid protection, wet–dry cycles, and hydrothermal settings).

Therefore, the Sobol results should be regarded as an **independent computational validation** of the Monte Carlo model rather than as a separate source of scientific conclusions.

---

### Relationship Between the Manuscript and This Repository

| Manuscript | Repository |
|------------|------------|
| Scientific hypothesis | Monte Carlo implementation |
| Environmental analyses | Source code and reproducibility |
| Main results | Raw simulation outputs |
| Figures and tables | Figure-generation scripts |
| Supplementary information | Validation reports |
| — | Global Sobol sensitivity analysis (complementary validation) |

This organization follows the principles of **Open Science**, ensuring complete transparency, reproducibility, and independent verification of all computational results while keeping the manuscript focused on its primary scientific narrative.


#### DESCRIPTION:

    A high-fidelity simulation engine designed to model the chemical selection 
    of DNA nucleotides under prebiotic conditions. This framework uses ONLY 
    experimentally-verified parameters from peer-reviewed literature.


#### NEW FEATURES v4.4:

    - Strictly Empirical Parameters: All values from published papers
    
    - Literature-Based Calibration: Lindahl (1993), Shapiro (1999), Cleaves (2010)
    
    - Experimentally Verified Half-lives: RNA (hours) vs DNA (days) at 90°C
    
    - Validated Deamination: 36x higher for Cytosine (Shen et al.)
    
    - Verified UV Resistance: 3-4x for Thymine (Ravanat, Cadet)
    
    - Lipid Membrane Integration: Prebiotic vesicle protection (Deamer, Szostak)


#### CORE FEATURES:

    - 2D Sensitivity Analysis: Multi-parameter optimization (Temp × pH).
    
    - Empirically-Calibrated Kinetics: Literature-based parameters.
    
    - UV Damage: Experimentally verified photostability ratios.
    
    - Long Polymer Physics: Persistence length and conformational dynamics.
    
    - Langevin Dynamics: Brownian forces and thermal fluctuations.
    
    - Template-Directed Polymerization: Base-pairing fidelity.
    
    - 4-Base System: U, T, C, A with cytosine deamination.
    
    - Lipid Membrane: Prebiotic vesicle formation and protection.
    
    - Data Export: JSON and CSV output for further analysis.


###  Key Updates in v4.4

- Strictly Empirical Parameters: All values sourced from published experimental data.
  
- Literature-Based Calibration: Based on Lindahl (1993), Shapiro (1999), and Cleaves (2010).
  
- Verified Half-lives: Comparative analysis of RNA (hours) vs DNA (days) at 90°C.
  
- Validated Deamination: Incorporating 36x higher rates for Cytosine (Shen et al.).
  
- Verified UV Resistance: 3-4x stability for Thymine (Ravanat, Cadet).
  
- Lipid Membrane Integration: Modeling prebiotic vesicle protection (Deamer, Szostak).
  

###  Core Features

- 2D Sensitivity Analysis: Multi-parameter optimization (Temperature $\times$ pH).
  
- Empirically-Calibrated Kinetics: Literature-based kinetic constants.
  
- UV Damage Modeling: Experimentally verified photostability ratios.
  
- Polymer Physics: Integration of persistence length and conformational dynamics.
  
- Langevin Dynamics: Modeling Brownian forces and thermal fluctuations.
  
- Template-Directed Polymerization: High-fidelity base-pairing simulations.
  
- 4-Base System: U, T, C, A with detailed cytosine deamination pathways.
  
- Data Export: Robust output in JSON and CSV formats for external analysis.


## Sobol Global Sensitivity Analysis

Two independent Sobol sensitivity analyses were performed to evaluate parameter importance in UPDSF v4.4:

- **N = 5,000 samples** (~160,000 total simulations)
  
- **N = 10,000 samples** (~320,000 total simulations)

Key Findings (Consistent across both runs)
- **Most influential parameter**: `A_U` (pre-exponential factor for Uracil hydrolysis) — dominant driver of thymine enrichment.
 
- **Second**: `base_catalysis_factor` — strong interaction effects.
  
- **Third**: `A_C` (Cytosine-related).
  
- Lipid protection and clay surface effects show moderate but significant influence.

**Conclusion**: Results are highly robust and confirm that **uracil degradation kinetics** and **pH-dependent base catalysis** are the primary drivers of thymine selection under prebiotic conditions.



## Analysis Timeline & Versioning
A complementary Sobol sensitivity analysis was subsequently performed to further validate the robustness of the model parameters.

📂 **Results Access**:

The detailed reports and raw data for the Sobol analysis can be found in the **[📄 Full Sobol Report & Plots](analysis/analysis/Sobol_2_Sensitivity_Analysis_Report.md)**

📂 **Results 2 Access**: 

The detailed reports and raw data for the Sobol analysis can be found in the **[📄 Full Sobol Report 2 & Plots](analysis/analysis/analysis/analysis/Sobol_2_Sensitivity_Analysis_2_Report.md)**

📂 **Results 3 Access**: 

The detailed reports and raw data for the Sobol analysis can be found in the **[📄 Full Sobol Report 3 & Manuscript_ID_IJA-2026-0085_Findings ](analysis/analysis/analysis/analysis/Alignment_of_Sobol_Sensitivity_Results_with_the_UPDSF_v4.4_Manuscript_ID_IJA-2026-0085_Findings.md)**

### Why Are Parameters Such as `A_U` and `A_C` Not Explicitly Defined in the Manuscript?

A potential source of confusion is the distinction between **environmental variables** discussed in the manuscript and the **internal computational parameters** analyzed in the Sobol sensitivity study.

Parameters such as `A_U`, `A_C`, activation energies, and the base catalysis factor are **internal parameters of the computational model**, rather than independent environmental variables investigated by the study.
These internal parameters define the kinetic behavior of the simulation engine. Environmental variables—including temperature, pH, UV exposure, lipid protection, wet–dry cycling, and hydrothermal conditions—act by modifying these kinetic parameters during Monte Carlo simulations.

Accordingly, the manuscript reports its scientific findings at the **environmental level**, whereas the Sobol analysis evaluates the sensitivity of the **underlying computational parameters** that generate those environmental responses.

The manuscript reports its scientific findings at the **environmental level**, including:

-  Temperature
-  pH
-  UV radiation
-  Lipid membrane protection
-  Wet–dry cycling
-  Hydrothermal environments

In contrast, the Global Sobol Sensitivity Analysis evaluates how the **internal model parameters** influence simulation outputs and quantifies their contributions to model uncertainty.

Consequently, the Sobol analysis should not be interpreted as introducing new environmental drivers. Instead, it provides an **independent computational validation** demonstrating that the dominant internal parameters correspond to the same environmental mechanisms and theoretical framework presented in the manuscript.

This distinction reflects two complementary levels of analysis:

| Manuscript | Sobol Analysis |
|------------|----------------|
| Environmental mechanisms | Internal computational parameters |
| Scientific interpretation | Model validation |
| Primary Monte Carlo results | Global sensitivity assessment |
| Environmental selection | Parameter contribution and interaction |

Thus, the Sobol analysis validates the robustness of the Monte Carlo model **at the parameter level**, whereas the manuscript presents the biological and environmental interpretation **at the system level**.


## To ensure full transparency and reproducibility, the timeline of the study's computational phases is provided below:

- Initial Manuscript Submission: July 9, 2026 (Manuscript ID: IJA-2026-0085)
- Complementary Sensitivity Analysis: July 23, 2026
- Complementary 2 Sensitivity Analysis: July 25, 2026
- Purpose: This post-submission analysis was conducted to further validate the robustness of the model parameters and strengthen the primary findings.
- Computational Details: Sobol sensitivity analyses were performed using sample sizes of $N=5,000$ and $N=10,000$.
- Computational 2 Details: Sobol sensitivity analyses were performed using sample sizes of $N=5,000$ which provides adequate convergence. Increasing to N = 10,000 is not necessary.

---



##  Installation & Setup

To run the UPDSF_v4.4 simulation on your local machine, follow these steps:

1. Clone the repository:
   git clone https://github.com/mrhashemi2000/UPDSF_v4.4.git
   cd UPDSF_v4.4
   

2. Install the dependencies:
   It is recommended to use a virtual environment.
   Install all required libraries using:

   pip install -r requirements.txt
   

3. Run the simulation:
 
   python UPDSF_v4.4.py
   

---

## Methodology: IA-Augmented Discovery
This project utilizes a recursive collaboration between human reasoning and AI-assisted modeling. The framework evolves through continuous feedback loops, allowing for rapid interdisciplinary discovery at the intersection of astrobiology, physical chemistry, and computational physics.https://doi.org/10.5281/zenodo.18594133

## Repository Contents

- `UPDSF_v4.4.py` — Main simulation engine
- `Sobol_4Cores_Stable.py` — Sensitivity analysis
- High-resolution plots in `attachments/`
- Full datasets in `output_data_v44_lipid/`

**References**: Lindahl (1993), Shapiro (1999), Cleaves (2010), Deamer (2017), and others.

---

*Intelligence-Augmented Research for Origins of Life*

##  Data Archive & Reproducibility

To ensure the full transparency and reproducibility of the simulation results, the key computational data has been archived in the `/data` directory.

All simulation results were achieved using the `UPDSF_v4.4.py` engine, ensuring that the findings are computationally robust and verifiable.

## Citation

If you use this framework in your research, please cite it as:
> Reza Hashemi. (2026). mrhashemi2000/UPDSF_v4.4: Initial release. Zenodo. https://doi.org/10.5281/zenodo.21224889

## REFERENCES:


    - Lindahl, T. (1993). Nature, 362, 709-715. (DNA stability)
    
    - Shapiro, R. (1999). Chem. Rev., 99, 2501-2536. (Deamination)
    
    - Cleaves, H.J. (2010). Astrobiology, 10, 337-346. (Prebiotic chemistry)
    
    - Ravanat, J.L. (1995). J. Biol. Chem., 270, 12305-12311. (UV damage)
    
    - Shen, J.C. (1994). Biochemistry, 33, 10756-10764. (Cytosine deamination)
    
    - Ferris, J.P. (1996). Orig. Life Evol. Biosph., 26, 449-461. (Clay catalysis)
    
    - Deamer, D.W. (2017). Life, 7, 5. (Lipid membranes)
    
    - Szostak, J.W. (2010). Cold Spring Harb. Perspect. Biol., 2, a002246. (Protocells)
