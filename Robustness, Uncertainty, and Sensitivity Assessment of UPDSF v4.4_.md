
[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
# Expanded_Analysis_5
## Robustness, Uncertainty, and Sensitivity Assessment of UPDSF v4.4
## Overview

This directory contains additional computational analyses performed to further evaluate the robustness of the UPDSF v4.4 stochastic kinetic model used in the manuscript:

### Environmental Selection of Thymine over Uracil in Prebiotic Chemical Evolution: Insights from a Kinetic Monte Carlo Model

These analyses were conducted as supplementary computational validation of the submitted UPDSF v4.4 model.

Importantly, no changes were made to the UPDSF v4.4 algorithm, equations, reaction network, kinetic parameters, or simulation workflow.

The purpose of these analyses is solely to quantify the stability of the model predictions under parameter uncertainty and to identify the dominant parameters controlling thymine enrichment.

## Objectives

### The expanded analyses address three important computational questions:

#### How sensitive are the final predictions to uncertainty in model parameters?

#### Which parameters exert the greatest influence on thymine selection?

#### Are the conclusions reported in the manuscript statistically robust?

## Analysis 1
Monte Carlo Uncertainty Analysis

A Monte Carlo uncertainty analysis was performed by repeatedly sampling uncertain model parameters within predefined ranges while keeping the reaction network unchanged.

For each realization, the complete stochastic simulation was executed and the final thymine fraction was recorded.

The analysis provides:

Distribution of final thymine fraction
Mean prediction
Standard deviation
Percentile intervals
Cumulative distribution
Box-plot statistics
Main observations
The Monte Carlo mean remained close to the deterministic reference simulation.
Parameter uncertainty produced only moderate variation in the final thymine fraction.
No evidence of unstable or divergent model behaviour was observed.
The distribution remained unimodal without significant outliers.

These results indicate that the principal conclusions of the model are robust with respect to realistic parameter uncertainty.

## Analysis 2
Local Parameter Sensitivity (Tornado Analysis)

A one-at-a-time sensitivity analysis was performed by perturbing each major model parameter while keeping all others fixed.

The resulting change in final thymine fraction was measured relative to the baseline simulation.

The analysis identifies the parameters exerting the strongest influence on model behaviour.

## Major findings

The dominant parameters were:

Replication Fidelity
Thymine Activation Energy
Clay Protection Efficiency
Uracil Activation Energy

Secondary influence was observed for

Lipid Protection
UV Resistance
Initial Monomer Pools
Cytosine Deamination Rate

## The analysis demonstrates that thymine selection is primarily governed by reaction kinetics and molecular stability rather than by arbitrary initial concentrations.

## Interpretation

The Monte Carlo and Tornado analyses complement the simulations presented in the manuscript.

Together they demonstrate that

the model is numerically stable,
predictions remain consistent under parameter perturbation,
the observed thymine enrichment is not an artifact of a single parameter choice,
and the principal conclusions remain unchanged over a realistic parameter space.

## Reproducibility

All analyses were generated directly from the publicly available UPDSF v4.4 source code without modification of the core simulation engine.

Only additional post-processing scripts were used to compute uncertainty statistics and sensitivity metrics.

Therefore, these analyses constitute supplementary validation rather than a new model version.

## Relation to the Manuscript

These analyses are supplementary computational validation of the submitted manuscript.

They are provided for transparency and reproducibility and do not alter the scientific conclusions or the implementation of UPDSF v4.4.


## Analysis 1 – Monte Carlo Uncertainty Analysis


<img width="4441" height="2955" alt="mc_plots_20260712_072756" src="https://github.com/user-attachments/assets/24ec65e2-db15-455f-a99a-03e1c6f7410d" />



The distribution of the final thymine fraction remained unimodal and centered near the baseline prediction. The Monte Carlo mean was consistent with the deterministic simulation, indicating that the model is numerically stable under parameter uncertainty. No significant outliers or multimodal behavior were observed, supporting the robustness of the stochastic predictions.The baseline simulation falls well within the Monte Carlo distribution, indicating that the deterministic solution is representative of the broader parameter space explored during uncertainty analysis.



## Analysis 2 – Tornado Sensitivity Analysis

### Tornado Sensitivity Analysis

<img width="3568" height="2969" alt="tornado_plot_20260712_072756" src="https://github.com/user-attachments/assets/5095f4f3-1830-495c-aed8-9cf8e8e4f262" />


The tornado plot identifies the dominant parameters controlling thymine enrichment. Replication fidelity and thymine activation energy produced the largest response, whereas initial nucleotide pools and UV resistance exerted comparatively smaller effects. The ranking demonstrates that the principal conclusions arise from physically meaningful kinetic processes rather than arbitrary parameter choices.The asymmetric responses observed for several parameters reflect the nonlinear nature of the underlying reaction kinetics rather than numerical instability>



## Conclusions

The expanded analyses demonstrate that the principal conclusions of UPDSF v4.4 remain stable under realistic parameter uncertainty. Monte Carlo uncertainty analysis confirms statistical robustness, while the tornado sensitivity analysis identifies the dominant kinetic mechanisms responsible for thymine selection. These supplementary analyses provide additional computational validation without modifying the underlying UPDSF v4.4 model or the conclusions reported in the submitted manuscript.

## Note: These analyses were performed after the initial manuscript submission as supplementary computational validation. They do not modify the UPDSF v4.4 algorithm, reaction network, or the scientific conclusions presented in the manuscript.
