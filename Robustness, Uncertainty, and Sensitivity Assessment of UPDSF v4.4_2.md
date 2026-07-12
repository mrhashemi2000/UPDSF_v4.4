[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
# Expanded_Analysis_6
## Robustness, Uncertainty, and Sensitivity Assessment of UPDSF v4.4_2
## Overview

This directory contains additional computational analyses performed to further evaluate the robustness of the UPDSF v4.4 stochastic kinetic model used in the manuscript:

### Environmental Selection of Thymine over Uracil in Prebiotic Chemical Evolution: Insights from a Kinetic Monte Carlo Model

These analyses were conducted as supplementary computational validation of the submitted UPDSF v4.4 model.

Importantly, no changes were made to the UPDSF v4.4 algorithm, equations, reaction network, kinetic parameters, or simulation workflow.
This repository contains the extended computational validation of the **Unified Prebiotic DNA Selection Framework (UPDSF) v4.4**.

While the core UPDSF model simulates the prebiotic chemical selection of **Thymine (T)** over **Uracil (U)**, this study evaluates whether that conclusion remains valid under realistic environmental uncertainty.

To test robustness, we performed a large-scale Monte Carlo (MC) analysis consisting of **200 independent simulations**, where key environmental variables were randomly perturbed within experimentally plausible ranges.

> **Core Thesis**
>
> Thymine selection is not an artifact of specific parameter choices.
> Instead, it emerges consistently from experimentally supported chemical kinetics.

---

# Methodology

The original UPDSF v4.4 engine was left completely unchanged.

A stochastic Monte Carlo wrapper was added around the core simulation.

### Monte Carlo Sampling

- **Number of simulations:** N = 200

### Sampled Environmental Parameters

| Parameter | Distribution |
|-----------|--------------|
| Temperature | Normal(65°C, 8°C) |
| pH | Normal(7.0, 1.2) |
| UV Exposure Factor | Normal(0.8, 0.15) |
| Lipid Concentration | Normal(0.05 M, 0.015 M) |

# Results

## 1. Statistical Convergence

The first analysis evaluates whether the final Thymine enrichment converges toward a stable statistical distribution across all simulations.

<img width="9140" height="7691" alt="sensitivity_2d_v44_lipid" src="https://github.com/user-attachments/assets/c6acd568-d274-4234-bce5-db1888dfd2ca" />

Interpretation

- Mean enrichment ≈ **2.46×**
- Distribution is unimodal and approximately Gaussian.
- Narrow 95% confidence interval demonstrates numerical stability.
- In approximately **85%** of all sampled environments, Thymine enrichment exceeds **2×**.

## 2. Sensitivity Analysis

We next quantified the influence of each environmental variable using regression and tornado analysis.


<img width="5385" height="3433" alt="tornado_plot" src="https://github.com/user-attachments/assets/05176d7a-3b5c-45b8-8b72-dd58464b36b5" />

Interpretation

- Temperature is the dominant driver of selection.
- Replication fidelity strongly amplifies the advantage of Thymine.
- Lipid concentration provides secondary stabilization.
- UV protection increases polymer survival but has weaker direct influence.

## 3. Correlation Matrix

A complete correlation matrix was computed to identify relationships between environmental variables and model outputs.


<img width="2888" height="2365" alt="correlation_matrix" src="https://github.com/user-attachments/assets/0dc09ea8-27fe-41f4-9256-368f427603f7" />

Interpretation

- Temperature positively correlates with Thymine enrichment.
- UV exposure negatively correlates with total DNA yield.
- Thymine fraction, enrichment, and molecular half-life exhibit nearly perfect positive correlation, indicating a direct stability-selection relationship.

## 4. Multi-Parameter Interaction

The final analysis identifies the environmental region that maximizes Thymine selection.


<img width="4118" height="3543" alt="uncertainty_bubbles" src="https://github.com/user-attachments/assets/7e571b25-853c-4408-afdb-6f6e0bae8a96" />

Interpretation

- Maximum enrichment occurs primarily between

  - Temperature: **65–75°C**
  - pH: **7–9**

- Lipid vesicles buffer environmental stress and preserve selected polymers.
- High-enrichment solutions appear across a broad parameter space rather than a single optimized point, demonstrating model robustness.

# Main Conclusions

The Monte Carlo validation demonstrates that:

1. The numerical implementation is stable across all 200 simulations.

2. Thymine selection is primarily controlled by activation-energy differences and intrinsic molecular stability rather than arbitrary initial conditions.

3. Elevated temperature, mildly alkaline pH, and lipid protection act synergistically to promote the emergence of DNA-like chemistry over RNA-like chemistry.

## Note: These analyses were performed after the initial manuscript submission as supplementary computational validation. They do not modify the UPDSF v4.4 algorithm, reaction network, or the scientific conclusions presented in the manuscript.

##  Citation & Reproducibility

###  AUTHOR: Seyed Mohammad Reza Hashemi (Reza Hashemi) Intelligence-Augmented (IA)

VERSION: 4.4 with Strictly Empirical Parameters + Lipid Membrane

ORCID: 0009-0002-0645-5180
