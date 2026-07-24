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


## Overview



#### UPDSF_v4.4 is a high-fidelity computational engine designed to model the chemical selection and evolutionary dominance of DNA nucleotides (specifically Thymine) under prebiotic conditions. Developed by Seyed Mohammad Reza Hashemi, this framework operates under the Matter World Hypothesis (MWH) and represents a case study in Intelligence-Augmented (IA) Science.This version is Lipid Membrane added.

Unlike theoretical models, v4.4 is strictly empirical, utilizing kinetic parameters, activation energies ($E_a$), and half-lives derived exclusively from peer-reviewed prebiotic chemistry literature.

UPDSF v4.4 is a stochastic kinetic Monte Carlo simulation framework that models the competition between **Uracil (U)** and **Thymine (T)** in various prebiotic environments. 

This model was developed to quantitatively investigate the environmental selection mechanisms that may have favored thymine in the transition from RNA to DNA-based heredity.

## **Manuscript**: "Environmental Selection of Thymine over Uracil in Prebiotic Chemical Evolution: Insights from a Kinetic Monte Carlo Model"  
## **Journal**: *International Journal of Astrobiology* (Submitted - IJA-2026-0085)

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

Full report and plots: [`Sobol_2_Sensitivity_Analysis_Report.md`](Sobol_2_Sensitivity_Analysis_Report.md)

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
