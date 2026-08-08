[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.21224889-blue)](https://doi.org/10.5281/zenodo.21224889) [![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
# Expanded_Analysis_12
**Supporting Manuscript IJA-2026-0085**

**Date**: August 8, 2026  

**Manuscript**  
*Environmental Selection of Thymine over Uracil in Prebiotic Chemical Evolution: Insights from a Kinetic Monte Carlo Model*  
(International Journal of Astrobiology – Draft)

# 🧬 Sequence-Level DNA Evolution Simulator
### A Prebiotic Evolution Framework with Thymine Enrichment, Catalytic Motif Detection, and Population Dynamics

---

<img width="5370" height="3322" alt="sequence_evolution" src="https://github.com/user-attachments/assets/98237f53-031b-437b-b29a-ec5203f5e74a" />

## 📊 Interpretation of Simulation Results

The 12-panel visualization provides a comprehensive snapshot of the evolutionary trajectory of DNA sequences under prebiotic constraints. Below is a detailed scientific analysis of the observed dynamics.

### 1. Fitness & Convergence (The "S-Curve")
- Fitness Evolution: We observe a rapid, sigmoidal increase in both mean and max fitness. The population reaches a plateau around Generation 50, indicating that the "optimal" sequence for the given environment was discovered early.
- Population Diversity: A dramatic Selective Sweep occurs between Generations 70 and 100. The diversity crashes from 2,000 unique sequences to just 2, signaling the total dominance of the fittest genotype.

### 2. The Thymine Advantage & Base Dynamics
- Thymine Enrichment: The "T Enrichment" plot shows a high initial spike followed by stabilization. The final enrichment factor of 3.04x proves that the environment (UV flux, high temperature, and deamination) creates a deterministic filter favoring Thymine over Uracil.
- Base Composition: The system evolves toward a perfect equimolar distribution (25% each for A, T, C, G).
- Uracil Elimination: The `Final Base Composition` bar chart shows U = 0.000. This confirms that the combined pressure of C $\to$ U deamination and the hydrolytic instability of Uracil leads to its complete exclusion from the winning sequences.

### 3. Structural & Catalytic Co-evolution
- Stability vs. Catalytic Potential: Both metrics converge to 1.0 almost simultaneously. This indicates that the winning sequences did not trade off stability for function; instead, they achieved maximal structural stability and maximal catalytic potential concurrently.
- Structure Energy: The mean energy drops sharply and stabilizes at $\sim -60 \text{ kcal/mol}$, crossing the "Stable Threshold." This represents the formation of highly ordered, low-energy secondary structures (stems and loops).
- T Fraction vs. Fitness: The scatter plot reveals a critical insight: while high Thymine fractions are initially associated with survival, the highest fitness is achieved at a balanced T-fraction ($\sim 0.25$), optimizing the sequence for both chemistry and function.

### 4. Emergence of Catalytic Motifs
- Catalytic Motifs Over Time: The simulation captures the "birth" of functional DNA. `DNAzyme_8_17` and `DNAzyme_E2` show exponential growth during the first 50 generations. These motifs reach a massive population count (~50,000 copies), proving that once a catalytic motif is discovered, it provides a massive evolutionary advantage, driving the sequence toward the global fitness maximum.

---


### 🏁 Final Summary Table

| Metric | Observation | Scientific Implication |
| :--- | :--- | :--- |
| Final T Fraction | 0.250 | Optimal balance for stability and folding |
| Final Diversity | 2 | Strong natural selection (Genetic Bottleneck) |
| Uracil Content | 0% | Complete replacement of U by T |
| Top Motifs | 8_17, E2 | Emergence of cleavage and ligation functions |
| Max Fitness | 1.097 | Achievement of theoretical functional peak |

---

### 💡 Conclusion for the "Matter World Hypothesis" 


### 📜 Perspective
The transition from non-living chemistry to organized biological systems remains one of science’s most difficult theoretical problems. This project introduces the Matter World Hypothesis (MWH), a physics-based framework proposing that life emerged through selection processes acting on heterogeneous molecular mixtures under prebiotic environmental conditions.

### 🔬 The "Chemical Darwinism" Computational Series
The MWH is validated through a series of stochastic computational simulations. These models demonstrate that:
- Molecular Selection: Prebiotic filters naturally isolate stable and functional polymers.
- Cooperation: Simple molecular interactions can evolve into cooperative networks.
- Protocellular Organization: Complex organization emerges naturally from basic physicochemical dynamics.

### 🤖 Intelligence-Augmented (IA) Science
This work serves as a primary case study in Intelligence-Augmented (IA) science. It represents a new paradigm of discovery where:
$$\text{Human Reasoning} \longleftrightarrow \text{AI-Assisted Modeling} \longrightarrow \text{Accelerated Interdisciplinary Discovery}$$
The recursive collaboration between the researcher and AI has been used to bridge the gap between abstract chemical theory and high-fidelity computational simulation.
| 📄 Zenodo 18594133 | [Click to Open](https://doi.org/10.5281/zenodo.18594133) |
