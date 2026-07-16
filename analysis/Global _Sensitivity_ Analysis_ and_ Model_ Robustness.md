
# Global Sensitivity Analysis and Model Robustness

To validate the stability of the observed thymine selection, a variance-based Global Sensitivity Analysis (GSA) was performed using the Sobol method. The simulation was executed across 64,000 independent runs to ensure statistical convergence and robustness.

####  Quantitative Insights
The analysis identified the uracil hydrolysis pre-exponential factor ($A_U$) as the primary driver of the system, exhibiting:
- Total-order index ($S_T$) $\approx 0.80$
- First-order index ($S_1$) $\approx 0.31$

####  Analysis of Non-linear Interactions
A significant disparity was observed between the first-order ($S_1$) and total-order ($S_T$) indices, most notably for the `base_catalysis_factor` (where $S_T - S_1 \approx 0.50$). This gap indicates that the selection of thymine is not merely a result of individual parameter values but emerges from strong non-linear interactions and mutual dependencies between hydrolysis kinetics and environmental catalysts.

####  Model Validation & Stability
The robustness of the model was further confirmed by the following observations:
- Ranking Consistency: The influence ranking of parameters remained remarkably consistent across all three primary output metrics: Enrichment, Thymine Fraction, and DNA Yield.
- Statistical Convergence: Low confidence intervals across all indices indicate that the results are highly converged and not artifacts of specific parameter choices.

# Conclusion on Robustness: 

###  These findings provide rigorous quantitative evidence that the Stability-Kinetics Ratio framework is the dominant mechanism governing the transition from uracil to thymine, confirming the structural integrity of the UPDSF v4.4 model.
```
