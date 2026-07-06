[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

## UPDSF v4.4: Unified Prebiotic DNA Selection Framework 

Environment: 🐍 Python 3.8+

## Author: Seyed Mohammad Reza Hashemi (Reza Hashemi)

## ORCID:0009-0002-0645-5180

https://doi.org/10.5281/zenodo.17273763

https://doi.org/10.5281/zenodo.18137476

https://doi.org/10.5281/zenodo.18092867

https://doi.org/10.5281/zenodo.18080826

https://doi.org/10.5281/zenodo.20988680

https://doi.org/10.5281/zenodo.20825578

https://doi.org/10.5281/zenodo.20733760

https://doi.org/10.5281/zenodo.20759622

https://doi.org/10.5281/zenodo.20771213

https://doi.org/10.5281/zenodo.18594133

https://doi.org/10.5281/zenodo.17280179

https://doi.org/10.5281/zenodo.17964430

https://doi.org/10.5281/zenodo.15290482

https://doi.org/10.5281/zenodo.15428322

https://doi.org/10.5281/zenodo.15428322

https://doi.org/10.5281/zenodo.15428338

https://doi.org/10.5281/zenodo.15428356

https://doi.org/10.5281/zenodo.15428367


## Overview
UPDSF v4.4 is a high-fidelity computational engine designed to model the chemical selection and evolutionary dominance of DNA nucleotides (specifically Thymine) under prebiotic conditions. Developed by Seyed Mohammad Reza Hashemi, this framework operates under the Matter World Hypothesis (MWH) and represents a case study in Intelligence-Augmented (IA) Science.This version is Lipid Membrane added.

Unlike theoretical models, v4.4 is strictly empirical, utilizing kinetic parameters, activation energies ($E_a$), and half-lives derived exclusively from peer-reviewed prebiotic chemistry literature.

DESCRIPTION:
    A high-fidelity simulation engine designed to model the chemical selection 
    of DNA nucleotides under prebiotic conditions. This framework uses ONLY 
    experimentally-verified parameters from peer-reviewed literature.

NEW FEATURES v4.4:
    - Strictly Empirical Parameters: All values from published papers
    - Literature-Based Calibration: Lindahl (1993), Shapiro (1999), Cleaves (2010)
    - Experimentally Verified Half-lives: RNA (hours) vs DNA (days) at 90°C
    - Validated Deamination: 36x higher for Cytosine (Shen et al.)
    - Verified UV Resistance: 3-4x for Thymine (Ravanat, Cadet)
    - Lipid Membrane Integration: Prebiotic vesicle protection (Deamer, Szostak)

CORE FEATURES:
    - 2D Sensitivity Analysis: Multi-parameter optimization (Temp × pH).
    - Empirically-Calibrated Kinetics: Literature-based parameters.
    - UV Damage: Experimentally verified photostability ratios.
    - Long Polymer Physics: Persistence length and conformational dynamics.
    - Langevin Dynamics: Brownian forces and thermal fluctuations.
    - Template-Directed Polymerization: Base-pairing fidelity.
    - 4-Base System: U, T, C, A with cytosine deamination.
    - Lipid Membrane: Prebiotic vesicle formation and protection.
    - Data Export: JSON and CSV output for further analysis.


## Installation & Setup

To run the UPDSF v4.4 simulation on your local machine, follow these steps:

1. Clone the repository:
   git clone https://github.com/mrhashemi2000/UPDSF_v4.4.git
   cd UPDSF_v4.4
   
2. Install the dependencies:
   It is recommended to use a virtual environment. You can install all required libraries using the provided `requirements.txt` file:
   pip install -r requirements.txt
   
3. Run the simulation:
   python UPDSF_v4.4.py

## Methodology: IA-Augmented Discovery
This project utilizes a recursive collaboration between human reasoning and AI-assisted modeling. The framework evolves through continuous feedback loops, allowing for rapid interdisciplinary discovery at the intersection of astrobiology, physical chemistry, and computational physics.

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
