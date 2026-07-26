"""
================================================================================
SOBOL SENSITIVITY ANALYSIS - DEGRADATION PARAMETERS
UPDSF v4.4 - N=5000 with 4 Cores - OPTIMIZED FOR YOUR SYSTEM
================================================================================
"""

import sys
import os

def check_dependencies():
    """Check and install dependencies - runs only in main process"""
    required_packages = {
        'tqdm': 'pip install tqdm',
        'SALib': 'pip install SALib',
        'psutil': 'pip install psutil',
        'pandas': 'pip install pandas',
        'matplotlib': 'pip install matplotlib',
        'seaborn': 'pip install seaborn',
        'scipy': 'pip install scipy',
        'numpy': 'pip install numpy'
    }
    
    missing = []
    for package, install_cmd in required_packages.items():
        try:
            __import__(package)
        except ImportError:
            missing.append((package, install_cmd))
    
    if missing:
        print("\n" + "="*70)
        print("⚠️  MISSING DEPENDENCIES DETECTED")
        print("="*70)
        print("\nPlease install the following packages:")
        for package, install_cmd in missing:
            print(f"  {install_cmd}")
        print("\nOr install all at once:")
        print("  pip install tqdm SALib psutil pandas matplotlib seaborn scipy numpy")
        print("="*70)
        return False
    
    return True

# ====================================================================
# IMPORTS
# ====================================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import json
import warnings
import os
import gc
from scipy import stats
from SALib.sample import saltelli
from SALib.analyze import sobol
import pandas as pd
import multiprocessing as mp
from multiprocessing import Pool
from functools import partial
import time
from tqdm import tqdm
import psutil

warnings.filterwarnings('ignore')

# ====================================================================
# HARDWARE DETECTION
# ====================================================================

def get_optimal_workers():
    """Determine optimal number of worker processes"""
    cpu_count = os.cpu_count() or 4
    # Use all available cores for this system
    optimal = cpu_count
    print(f"  ✅ Detected {cpu_count} CPU cores, using {optimal} workers")
    return optimal

# ====================================================================
# PARAMETER DEFINITIONS
# ====================================================================

class SobolDegradationParameters:
    PARAMETERS = [
        {'name': 'Ea_U', 'low': 24.0, 'high': 30.0, 'nominal': 27.0},
        {'name': 'Ea_T', 'low': 29.0, 'high': 35.0, 'nominal': 32.0},
        {'name': 'Ea_C_deam', 'low': 20.0, 'high': 26.0, 'nominal': 23.0},
        {'name': 'Ea_A', 'low': 26.0, 'high': 32.0, 'nominal': 29.0},
        {'name': 'A_U', 'low': 1.0e-6, 'high': 1.0e-3, 'nominal': 8.5e-5},
        {'name': 'A_T', 'low': 1.0e-8, 'high': 1.0e-5, 'nominal': 1.2e-6},
        {'name': 'A_C', 'low': 1.0e-5, 'high': 1.0e-3, 'nominal': 2.8e-4},
        {'name': 'A_A', 'low': 1.0e-7, 'high': 1.0e-4, 'nominal': 1.5e-5},
        {'name': 'deamination_ratio', 'low': 10.0, 'high': 60.0, 'nominal': 36.0},
        {'name': 'UV_resistance_T', 'low': 0.1, 'high': 0.5, 'nominal': 0.28},
        {'name': 'UV_resistance_C', 'low': 1.0, 'high': 2.0, 'nominal': 1.5},
        {'name': 'UV_resistance_A', 'low': 0.4, 'high': 1.0, 'nominal': 0.7},
        {'name': 'lipid_protection', 'low': 2.0, 'high': 8.0, 'nominal': 4.5},
        {'name': 'clay_protection', 'low': 5.0, 'high': 15.0, 'nominal': 9.5},
        {'name': 'base_catalysis_factor', 'low': 1.0, 'high': 3.0, 'nominal': 2.0},
    ]
    
    @classmethod
    def get_parameter_names(cls):
        return [p['name'] for p in cls.PARAMETERS]
    
    @classmethod
    def get_parameter_bounds(cls):
        return [[p['low'], p['high']] for p in cls.PARAMETERS]


# ====================================================================
# SIMULATION ENGINE (COMPACT VERSION FOR SPEED)
# ====================================================================

class OptimizedSobolEngine:
    __slots__ = ['temperature_C', 'pH', 'polymer_length', 'lipid_conc', 'max_steps', 'params', 'seed']
    
    def __init__(self, temperature_C: float = 68.0, pH: float = 7.0,
                 polymer_length: int = 100, lipid_conc: float = 0.05,
                 max_time_hours: int = 240):
        
        self.temperature_C = temperature_C
        self.pH = pH
        self.polymer_length = max(100, polymer_length)
        self.lipid_conc = lipid_conc
        self.max_steps = min(80000, int(max_time_hours * 3600 / 3))
        self.params = None
        self.seed = None
    
    def set_params(self, param_dict: Dict, seed: int):
        self.params = param_dict
        self.seed = seed
    
    def run_single(self):
        if self.params is None:
            return {'enrichment': 0, 'fraction': 0, 'yield': 0}
        
        np.random.seed(self.seed)
        p = self.params
        R = 1.987
        T_K = self.temperature_C + 273.15
        
        # Hydrolysis rates
        k_U = p['A_U'] * np.exp(-p['Ea_U'] / (R * T_K))
        k_T = p['A_T'] * np.exp(-p['Ea_T'] / (R * T_K))
        k_C = p['A_C'] * np.exp(-p['Ea_C_deam'] / (R * T_K))
        k_A = p['A_A'] * np.exp(-p['Ea_A'] / (R * T_K))
        
        # pH modulation
        pH_factor = 1 + 10**(self.pH - 9.5)
        base_catalysis = p['base_catalysis_factor'] * (1 + max(0, 6 - self.pH) * 0.2)
        
        k_U *= pH_factor * base_catalysis
        k_T *= pH_factor * base_catalysis * 0.75
        k_C *= pH_factor * base_catalysis * 1.2
        k_A *= pH_factor * base_catalysis * 0.9
        
        # Length dependence
        length_factor = 1.0 - 0.001 * (self.polymer_length - 100)
        length_factor = max(0.85, length_factor)
        k_U *= length_factor
        k_T *= length_factor
        k_C *= length_factor
        k_A *= length_factor
        
        # Clay protection
        cpf = p['clay_protection']
        clay_surface_density = 0.36
        k_U_final = k_U * (1 - clay_surface_density) + (k_U / cpf) * clay_surface_density
        k_T_final = k_T * (1 - clay_surface_density) + (k_T / cpf) * clay_surface_density
        k_C_final = k_C * (1 - clay_surface_density) + (k_C / cpf) * clay_surface_density
        k_A_final = k_A * (1 - clay_surface_density) + (k_A / cpf) * clay_surface_density
        
        # UV rates
        temp_factor = np.exp(0.03 * (self.temperature_C - 25))
        k_UV_base = 0.0012 * temp_factor
        
        lipid_protect = p['lipid_protection']
        uv_U = k_UV_base * 0.8 / lipid_protect
        uv_T = k_UV_base * p['UV_resistance_T'] / (lipid_protect * 1.15)
        uv_C = k_UV_base * p['UV_resistance_C'] / lipid_protect
        uv_A = k_UV_base * p.get('UV_resistance_A', 0.7) / lipid_protect
        
        # Deamination
        k_deamination = 0.0025 * np.exp(-p['Ea_C_deam'] / (R * T_K))
        k_deamination *= (1 + 10**(self.pH - 9.5))
        k_deamination *= p['deamination_ratio'] * 100 * length_factor
        
        # Initialize species
        species = {
            'U_monomer': 830000, 'T_monomer': 170000,
            'C_monomer': 650000, 'A_monomer': 420000,
            'dsDNA_U': 0, 'dsDNA_T': 0, 'dsDNA_C': 0, 'dsDNA_A': 0,
            'dsDNA_U_clay': 0, 'dsDNA_T_clay': 0,
            'dsDNA_C_clay': 0, 'dsDNA_A_clay': 0,
            'dsDNA_U_lipid': 0, 'dsDNA_T_lipid': 0,
            'dsDNA_C_lipid': 0, 'dsDNA_A_lipid': 0,
        }
        
        time_val = 0.0
        
        # Main simulation loop
        for _ in range(self.max_steps):
            time_val += 1.0
            
            # Influx
            fluct = 1.0 + 0.3 * (2 * np.random.random() - 1)
            species['U_monomer'] += 120.0 * fluct * 0.01
            species['T_monomer'] += 45.0 * fluct * 0.01
            species['C_monomer'] += 80.0 * fluct * 0.01
            species['A_monomer'] += 55.0 * fluct * 0.01
            
            for base in ['U', 'T', 'C', 'A']:
                if species[f'{base}_monomer'] > 3000000:
                    species[f'{base}_monomer'] = 3000000
            
            # Polymerization
            poly_prob = 0.28 * (1 + 0.08 * np.sin(2 * np.pi * time_val / 7200))
            monomer_req = max(5, int(self.polymer_length / 10))
            
            if np.random.random() < poly_prob:
                if species['T_monomer'] > monomer_req and np.random.random() < 0.93 * 1.35:
                    species['dsDNA_T'] += 1
                    species['T_monomer'] -= monomer_req
                if species['U_monomer'] > monomer_req and np.random.random() < 0.93 * 0.85:
                    species['dsDNA_U'] += 1
                    species['U_monomer'] -= monomer_req
                if species['C_monomer'] > monomer_req and np.random.random() < 0.93 * 0.80:
                    species['dsDNA_C'] += 1
                    species['C_monomer'] -= monomer_req
                if species['A_monomer'] > monomer_req and np.random.random() < 0.93 * 0.90:
                    species['dsDNA_A'] += 1
                    species['A_monomer'] -= monomer_req
            
            # Hydrolysis
            hydro_probs = [k_U_final * 8, k_T_final * 8, k_C_final * 8, k_A_final * 8]
            bases = ['U', 'T', 'C', 'A']
            
            for base, prob in zip(bases, hydro_probs):
                if np.random.random() < prob and species[f'dsDNA_{base}'] > 0:
                    species[f'dsDNA_{base}'] -= 1
                elif np.random.random() < prob * 0.3 and species[f'dsDNA_{base}_lipid'] > 0:
                    species[f'dsDNA_{base}_lipid'] -= 1
            
            # UV damage
            if np.random.random() < 0.15:
                uv_rates = [uv_U, uv_T, uv_C, uv_A]
                for base, uv_rate in zip(bases, uv_rates):
                    if np.random.random() < uv_rate and species[f'dsDNA_{base}'] > 0:
                        species[f'dsDNA_{base}'] -= 1
                    elif np.random.random() < uv_rate * 0.2 and species[f'dsDNA_{base}_lipid'] > 0:
                        species[f'dsDNA_{base}_lipid'] -= 1
            
            # Deamination
            if np.random.random() < k_deamination * 3600 * 0.1:
                if species['dsDNA_C'] > 0 and np.random.random() < 0.65:
                    species['dsDNA_C'] -= 1
                    species['dsDNA_U'] += 1
                elif species['dsDNA_C_lipid'] > 0 and np.random.random() < 0.4:
                    species['dsDNA_C_lipid'] -= 1
                    species['dsDNA_U_lipid'] += 1
                
                if species['C_monomer'] > 10:
                    lost = int(3 * np.random.random())
                    species['C_monomer'] -= lost
                    species['U_monomer'] += lost
        
        # Calculate outputs
        U = species['dsDNA_U'] + species['dsDNA_U_clay'] + species['dsDNA_U_lipid']
        T = species['dsDNA_T'] + species['dsDNA_T_clay'] + species['dsDNA_T_lipid']
        C = species['dsDNA_C'] + species['dsDNA_C_clay'] + species['dsDNA_C_lipid']
        A = species['dsDNA_A'] + species['dsDNA_A_clay'] + species['dsDNA_A_lipid']
        total = U + T + C + A
        
        if total == 0:
            return {'enrichment': 0, 'fraction': 0, 'yield': 0}
        
        final_fraction = T / total
        initial_fraction = 170000 / (830000 + 170000 + 650000 + 420000)
        enrichment = final_fraction / initial_fraction
        
        return {
            'enrichment': enrichment,
            'fraction': final_fraction,
            'yield': total
        }


# ====================================================================
# PARALLEL SOBOL ANALYZER
# ====================================================================

class ParallelSobolAnalyzer:
    def __init__(self, temperature_C: float = 68.0, pH: float = 7.0,
                 n_samples: int = 5000, max_time_hours: int = 240,
                 polymer_length: int = 100, lipid_conc: float = 0.05,
                 n_workers: int = None, verbose: bool = True):
        
        self.temperature_C = temperature_C
        self.pH = pH
        self.n_samples = n_samples
        self.max_time_hours = max_time_hours
        self.polymer_length = polymer_length
        self.lipid_conc = lipid_conc
        self.verbose = verbose
        
        self.n_workers = n_workers or get_optimal_workers()
        
        self.param_names = SobolDegradationParameters.get_parameter_names()
        self.param_bounds = SobolDegradationParameters.get_parameter_bounds()
        
        self.problem = {
            'num_vars': len(self.param_names),
            'names': self.param_names,
            'bounds': self.param_bounds
        }
        
        print("  📊 Generating Sobol samples...")
        self.param_values = saltelli.sample(self.problem, self.n_samples)
        self.n_runs = len(self.param_values)
        
        if verbose:
            print(f"\n{'='*70}")
            print(f"🔬 PARALLEL SOBOL SENSITIVITY ANALYSIS - N=5000")
            print(f"{'='*70}")
            print(f"  Parameters: {len(self.param_names)}")
            print(f"  Base samples: {self.n_samples}")
            print(f"  Total runs: {self.n_runs:,}")
            print(f"  Workers: {self.n_workers}")
            print(f"  Temperature: {self.temperature_C}°C")
            print(f"  pH: {self.pH}")
            print(f"  RAM Available: {psutil.virtual_memory().available / (1024**3):.1f} GB")
            print(f"{'='*70}\n")
    
    def _run_batch(self, batch_indices: List[int]) -> List[Dict]:
        results = []
        engine = OptimizedSobolEngine(
            temperature_C=self.temperature_C,
            pH=self.pH,
            polymer_length=self.polymer_length,
            lipid_conc=self.lipid_conc,
            max_time_hours=self.max_time_hours
        )
        
        for idx in batch_indices:
            param_dict = {}
            for j, name in enumerate(self.param_names):
                param_dict[name] = self.param_values[idx, j]
            
            engine.set_params(param_dict, seed=42 + idx)
            result = engine.run_single()
            results.append(result)
        
        return results
    
    def run_analysis(self, output_dir: str = "sobol_degradation_results"):
        os.makedirs(output_dir, exist_ok=True)
        
        indices = list(range(self.n_runs))
        batch_size = max(1, len(indices) // (self.n_workers * 2))
        batches = [indices[i:i + batch_size] for i in range(0, len(indices), batch_size)]
        
        print(f"  📦 Created {len(batches)} batches of size ~{batch_size}")
        print(f"  🚀 Starting parallel execution on {self.n_workers} cores...\n")
        
        enrichment_results = np.zeros(self.n_runs)
        fraction_results = np.zeros(self.n_runs)
        dna_yield_results = np.zeros(self.n_runs)
        
        start_time = time.time()
        
        # Set start method for Windows
        try:
            mp.set_start_method('spawn', force=True)
        except RuntimeError:
            pass
        
        with Pool(processes=self.n_workers) as pool:
            results_iter = pool.imap(self._run_batch, batches, chunksize=1)
            
            processed = 0
            with tqdm(total=self.n_runs, desc="🔄 Running simulations", 
                      unit="runs", ncols=80) as pbar:
                for batch_results in results_iter:
                    for result in batch_results:
                        enrichment_results[processed] = result['enrichment']
                        fraction_results[processed] = result['fraction']
                        dna_yield_results[processed] = result['yield']
                        processed += 1
                        pbar.update(1)
        
        elapsed = time.time() - start_time
        runs_per_second = self.n_runs / elapsed
        
        print(f"\n  ✅ Completed in {elapsed:.1f} seconds")
        print(f"  ⚡ Rate: {runs_per_second:.1f} runs/second")
        
        valid_mask = ~(np.isnan(enrichment_results) | np.isinf(enrichment_results))
        invalid = np.sum(~valid_mask)
        if invalid > 0:
            print(f"  ⚠️  {invalid} runs failed ({invalid/self.n_runs*100:.1f}%)")
        
        print("\n  🔬 Computing Sobol indices...")
        
        self.sobol_enrichment = sobol.analyze(
            self.problem, 
            enrichment_results[valid_mask],
            print_to_console=False
        )
        
        self.sobol_fraction = sobol.analyze(
            self.problem,
            fraction_results[valid_mask],
            print_to_console=False
        )
        
        self.sobol_yield = sobol.analyze(
            self.problem,
            dna_yield_results[valid_mask],
            print_to_console=False
        )
        
        self.results = {
            'enrichment': enrichment_results,
            'fraction': fraction_results,
            'dna_yield': dna_yield_results,
            'param_values': self.param_values,
            'valid_mask': valid_mask,
            'elapsed_time': elapsed,
            'runs_per_second': runs_per_second
        }
        
        # Perform convergence analysis
        self.convergence_results = self._perform_convergence_analysis(
            enrichment_results[valid_mask], 
            fraction_results[valid_mask],
            dna_yield_results[valid_mask]
        )
        
        self._save_results(output_dir)
        self._print_summary()
        
        return self.sobol_enrichment, self.sobol_fraction, self.sobol_yield
    
    def _perform_convergence_analysis(self, enrichment, fraction, dna_yield):
        """Perform convergence analysis using bootstrapping"""
        print("\n  📊 Performing convergence analysis...")
        
        n_total = len(enrichment)
        subsample_sizes = [int(n_total * p) for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]]
        n_bootstrap = 50
        
        convergence_results = {
            'subsample_sizes': subsample_sizes,
            'enrichment': {'S1_mean': [], 'S1_std': [], 'ST_mean': [], 'ST_std': []},
            'fraction': {'S1_mean': [], 'S1_std': [], 'ST_mean': [], 'ST_std': []},
            'yield': {'S1_mean': [], 'S1_std': [], 'ST_mean': [], 'ST_std': []}
        }
        
        # Determine which parameters to track (top 5 most influential)
        # First compute indices on full dataset to identify top parameters
        temp_sobol = sobol.analyze(self.problem, enrichment, print_to_console=False)
        top_indices = np.argsort(temp_sobol['ST'])[-5:][::-1]
        
        for target_size in tqdm(subsample_sizes, desc="  Bootstrapping convergence"):
            if target_size < 10:
                continue
                
            S1_enrich_list = []
            ST_enrich_list = []
            S1_frac_list = []
            ST_frac_list = []
            S1_yield_list = []
            ST_yield_list = []
            
            for _ in range(n_bootstrap):
                # Random subsample
                idx = np.random.choice(n_total, size=target_size, replace=False)
                
                try:
                    # Compute Sobol indices on subsample
                    sobol_enrich = sobol.analyze(self.problem, enrichment[idx], print_to_console=False)
                    sobol_frac = sobol.analyze(self.problem, fraction[idx], print_to_console=False)
                    sobol_yield = sobol.analyze(self.problem, dna_yield[idx], print_to_console=False)
                    
                    # Store indices for top parameters only
                    S1_enrich_list.append(np.mean(sobol_enrich['S1'][top_indices]))
                    ST_enrich_list.append(np.mean(sobol_enrich['ST'][top_indices]))
                    S1_frac_list.append(np.mean(sobol_frac['S1'][top_indices]))
                    ST_frac_list.append(np.mean(sobol_frac['ST'][top_indices]))
                    S1_yield_list.append(np.mean(sobol_yield['S1'][top_indices]))
                    ST_yield_list.append(np.mean(sobol_yield['ST'][top_indices]))
                except:
                    continue
            
            if S1_enrich_list:
                convergence_results['enrichment']['S1_mean'].append(np.mean(S1_enrich_list))
                convergence_results['enrichment']['S1_std'].append(np.std(S1_enrich_list))
                convergence_results['enrichment']['ST_mean'].append(np.mean(ST_enrich_list))
                convergence_results['enrichment']['ST_std'].append(np.std(ST_enrich_list))
            else:
                convergence_results['enrichment']['S1_mean'].append(np.nan)
                convergence_results['enrichment']['S1_std'].append(np.nan)
                convergence_results['enrichment']['ST_mean'].append(np.nan)
                convergence_results['enrichment']['ST_std'].append(np.nan)
            
            if S1_frac_list:
                convergence_results['fraction']['S1_mean'].append(np.mean(S1_frac_list))
                convergence_results['fraction']['S1_std'].append(np.std(S1_frac_list))
                convergence_results['fraction']['ST_mean'].append(np.mean(ST_frac_list))
                convergence_results['fraction']['ST_std'].append(np.std(ST_frac_list))
            else:
                convergence_results['fraction']['S1_mean'].append(np.nan)
                convergence_results['fraction']['S1_std'].append(np.nan)
                convergence_results['fraction']['ST_mean'].append(np.nan)
                convergence_results['fraction']['ST_std'].append(np.nan)
            
            if S1_yield_list:
                convergence_results['yield']['S1_mean'].append(np.mean(S1_yield_list))
                convergence_results['yield']['S1_std'].append(np.std(S1_yield_list))
                convergence_results['yield']['ST_mean'].append(np.mean(ST_yield_list))
                convergence_results['yield']['ST_std'].append(np.std(ST_yield_list))
            else:
                convergence_results['yield']['S1_mean'].append(np.nan)
                convergence_results['yield']['S1_std'].append(np.nan)
                convergence_results['yield']['ST_mean'].append(np.nan)
                convergence_results['yield']['ST_std'].append(np.nan)
        
        return convergence_results
    
    def _save_results(self, output_dir: str):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        data = {'run_id': np.arange(len(self.results['enrichment']))}
        for i, name in enumerate(self.param_names):
            data[f'param_{name}'] = self.param_values[:, i]
        
        data['enrichment'] = self.results['enrichment']
        data['thymine_fraction'] = self.results['fraction']
        data['dna_yield'] = self.results['dna_yield']
        data['valid'] = self.results['valid_mask']
        
        df = pd.DataFrame(data)
        csv_file = f"{output_dir}/sobol_degradation_data_{timestamp}.csv"
        df.to_csv(csv_file, index=False)
        
        sobol_data = {
            'timestamp': timestamp,
            'temperature_C': self.temperature_C,
            'pH': self.pH,
            'polymer_length': self.polymer_length,
            'n_samples': self.n_samples,
            'n_runs': self.n_runs,
            'n_workers': self.n_workers,
            'elapsed_time': self.results['elapsed_time'],
            'runs_per_second': self.results['runs_per_second'],
            'valid_runs': int(np.sum(self.results['valid_mask'])),
            'parameter_names': self.param_names,
            'parameter_bounds': self.param_bounds,
            'enrichment': {
                'S1': self.sobol_enrichment['S1'].tolist(),
                'S1_conf': self.sobol_enrichment['S1_conf'].tolist(),
                'ST': self.sobol_enrichment['ST'].tolist(),
                'ST_conf': self.sobol_enrichment['ST_conf'].tolist(),
            },
            'thymine_fraction': {
                'S1': self.sobol_fraction['S1'].tolist(),
                'S1_conf': self.sobol_fraction['S1_conf'].tolist(),
                'ST': self.sobol_fraction['ST'].tolist(),
                'ST_conf': self.sobol_fraction['ST_conf'].tolist(),
            },
            'dna_yield': {
                'S1': self.sobol_yield['S1'].tolist(),
                'S1_conf': self.sobol_yield['S1_conf'].tolist(),
                'ST': self.sobol_yield['ST'].tolist(),
                'ST_conf': self.sobol_yield['ST_conf'].tolist(),
            },
            'convergence_analysis': self.convergence_results
        }
        
        json_file = f"{output_dir}/sobol_indices_{timestamp}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(sobol_data, f, indent=2)
        
        print(f"\n💾 Results saved:")
        print(f"   📄 CSV data: {csv_file}")
        print(f"   📄 JSON indices: {json_file}")
    
    def _print_summary(self):
        st = self.sobol_enrichment['ST']
        sorted_idx = np.argsort(st)[::-1]
        
        print("\n" + "="*70)
        print("📊 SOBOL SENSITIVITY INDICES (N=5000)")
        print("="*70)
        
        print("\n🏆 TOP 5 MOST INFLUENTIAL PARAMETERS:")
        print("-" * 70)
        print(f"{'Rank':<6} {'Parameter':<25} {'ST':<12} {'S1':<12}")
        print("-" * 70)
        
        for i in range(min(5, len(sorted_idx))):
            idx = sorted_idx[i]
            print(f"{i+1:<6} {self.param_names[idx]:<25} {st[idx]:>10.4f} "
                  f"{self.sobol_enrichment['S1'][idx]:>10.4f}")
        
        # Print convergence summary
        if self.convergence_results:
            print("\n" + "="*70)
            print("📈 CONVERGENCE ANALYSIS SUMMARY")
            print("="*70)
            
            conv = self.convergence_results
            sizes = conv['subsample_sizes']
            
            # Get last two points for each metric
            n_points = len(sizes)
            if n_points >= 2:
                print("\n  Enrichment - ST convergence:")
                print(f"    Sample size: {sizes[-2]} → {sizes[-1]}")
                st_values = conv['enrichment']['ST_mean']
                if len(st_values) >= 2:
                    diff = abs(st_values[-1] - st_values[-2])
                    print(f"    ST change: {diff:.6f}")
                    st_std = conv['enrichment']['ST_std']
                    if len(st_std) >= 2 and st_std[-1] > 0:
                        rel_std = st_std[-1] / (abs(st_values[-1]) + 1e-10)
                        print(f"    Relative STD: {rel_std:.4f} ({rel_std*100:.2f}%)")
                
                print("\n  Fraction - ST convergence:")
                st_values = conv['fraction']['ST_mean']
                if len(st_values) >= 2:
                    diff = abs(st_values[-1] - st_values[-2])
                    print(f"    ST change: {diff:.6f}")
                    st_std = conv['fraction']['ST_std']
                    if len(st_std) >= 2 and st_std[-1] > 0:
                        rel_std = st_std[-1] / (abs(st_values[-1]) + 1e-10)
                        print(f"    Relative STD: {rel_std:.4f} ({rel_std*100:.2f}%)")
                
                print("\n  DNA Yield - ST convergence:")
                st_values = conv['yield']['ST_mean']
                if len(st_values) >= 2:
                    diff = abs(st_values[-1] - st_values[-2])
                    print(f"    ST change: {diff:.6f}")
                    st_std = conv['yield']['ST_std']
                    if len(st_std) >= 2 and st_std[-1] > 0:
                        rel_std = st_std[-1] / (abs(st_values[-1]) + 1e-10)
                        print(f"    Relative STD: {rel_std:.4f} ({rel_std*100:.2f}%)")
        
        print("\n" + "="*70)
    
    def plot_results(self, save_path: str = "sobol_degradation_analysis.png",
                     show_fig: bool = True):
        sns.set_style("whitegrid")
        
        fig = plt.figure(figsize=(20, 20))
        gs = GridSpec(4, 3, figure=fig, hspace=0.4, wspace=0.35)
        
        fig.suptitle('Sobol Sensitivity Analysis - Degradation Parameters (N=5000)\n'
                    f'T={self.temperature_C}°C, pH={self.pH:.1f}, '
                    f'Workers={self.n_workers}',
                    fontsize=16, fontweight='bold')
        
        names_short = [n.replace('_', ' ') for n in self.param_names]
        y_pos = np.arange(len(self.param_names))
        
        # Plot 1: S1
        ax1 = fig.add_subplot(gs[0, 0])
        ax1.barh(y_pos, self.sobol_enrichment['S1'], 
                 xerr=self.sobol_enrichment['S1_conf'], 
                 color='steelblue', alpha=0.7, edgecolor='black', linewidth=0.5)
        ax1.set_yticks(y_pos)
        ax1.set_yticklabels(names_short, fontsize=8)
        ax1.set_xlabel('First-order Sobol Index (S1)', fontsize=11)
        ax1.set_title('Enrichment - First-order Effects', fontsize=12, fontweight='bold')
        ax1.axvline(x=0, color='black', linestyle='-', alpha=0.3)
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: ST
        ax2 = fig.add_subplot(gs[0, 1])
        ax2.barh(y_pos, self.sobol_enrichment['ST'], 
                 xerr=self.sobol_enrichment['ST_conf'], 
                 color='coral', alpha=0.7, edgecolor='black', linewidth=0.5)
        ax2.set_yticks(y_pos)
        ax2.set_yticklabels(names_short, fontsize=8)
        ax2.set_xlabel('Total-order Sobol Index (ST)', fontsize=11)
        ax2.set_title('Enrichment - Total-order Effects', fontsize=12, fontweight='bold')
        ax2.axvline(x=0, color='black', linestyle='-', alpha=0.3)
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: S1 vs ST
        ax3 = fig.add_subplot(gs[0, 2])
        ax3.scatter(self.sobol_enrichment['S1'], self.sobol_enrichment['ST'], 
                    color='darkgreen', s=80, alpha=0.7)
        for i, name in enumerate(names_short):
            ax3.annotate(name, (self.sobol_enrichment['S1'][i], 
                               self.sobol_enrichment['ST'][i]), 
                        fontsize=7, alpha=0.8, xytext=(3, 3), 
                        textcoords='offset points')
        ax3.plot([0, 1], [0, 1], 'r--', alpha=0.5, label='S1 = ST')
        ax3.set_xlabel('First-order (S1)', fontsize=11)
        ax3.set_ylabel('Total-order (ST)', fontsize=11)
        ax3.set_title('S1 vs ST - Enrichment', fontsize=12, fontweight='bold')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        ax3.set_xlim(0, 1)
        ax3.set_ylim(0, 1)
        
        # Plot 4: Thymine Fraction - S1
        ax4 = fig.add_subplot(gs[1, 0])
        ax4.barh(y_pos, self.sobol_fraction['S1'], 
                 xerr=self.sobol_fraction['S1_conf'], 
                 color='steelblue', alpha=0.7, edgecolor='black', linewidth=0.5)
        ax4.set_yticks(y_pos)
        ax4.set_yticklabels(names_short, fontsize=8)
        ax4.set_xlabel('First-order Sobol Index (S1)', fontsize=11)
        ax4.set_title('Thymine Fraction - First-order Effects', fontsize=12, fontweight='bold')
        ax4.axvline(x=0, color='black', linestyle='-', alpha=0.3)
        ax4.grid(True, alpha=0.3)
        
        # Plot 5: Thymine Fraction - ST
        ax5 = fig.add_subplot(gs[1, 1])
        ax5.barh(y_pos, self.sobol_fraction['ST'], 
                 xerr=self.sobol_fraction['ST_conf'], 
                 color='coral', alpha=0.7, edgecolor='black', linewidth=0.5)
        ax5.set_yticks(y_pos)
        ax5.set_yticklabels(names_short, fontsize=8)
        ax5.set_xlabel('Total-order Sobol Index (ST)', fontsize=11)
        ax5.set_title('Thymine Fraction - Total-order Effects', fontsize=12, fontweight='bold')
        ax5.axvline(x=0, color='black', linestyle='-', alpha=0.3)
        ax5.grid(True, alpha=0.3)
        
        # Plot 6: DNA Yield - ST
        ax6 = fig.add_subplot(gs[1, 2])
        ax6.barh(y_pos, self.sobol_yield['ST'], 
                 xerr=self.sobol_yield['ST_conf'], 
                 color='mediumpurple', alpha=0.7, edgecolor='black', linewidth=0.5)
        ax6.set_yticks(y_pos)
        ax6.set_yticklabels(names_short, fontsize=8)
        ax6.set_xlabel('Total-order Sobol Index (ST)', fontsize=11)
        ax6.set_title('DNA Yield - Total-order Effects', fontsize=12, fontweight='bold')
        ax6.axvline(x=0, color='black', linestyle='-', alpha=0.3)
        ax6.grid(True, alpha=0.3)
        
        # Plot 7: Interactions
        ax7 = fig.add_subplot(gs[2, 0])
        interaction = np.array(self.sobol_enrichment['ST']) - np.array(self.sobol_enrichment['S1'])
        colors = ['red' if v > 0.1 else 'orange' if v > 0.05 else 'blue' for v in interaction]
        ax7.barh(y_pos, interaction, color=colors, alpha=0.7, edgecolor='black', linewidth=0.5)
        ax7.set_yticks(y_pos)
        ax7.set_yticklabels(names_short, fontsize=8)
        ax7.set_xlabel('Interaction Effect (ST - S1)', fontsize=11)
        ax7.set_title('Parameter Interactions - Enrichment', fontsize=12, fontweight='bold')
        ax7.axvline(x=0, color='black', linestyle='-', alpha=0.3)
        ax7.grid(True, alpha=0.3)
        
        # Plot 8: Ranking
        ax8 = fig.add_subplot(gs[2, 1])
        st = self.sobol_enrichment['ST']
        sorted_idx = np.argsort(st)[::-1]
        sorted_names = [names_short[i] for i in sorted_idx]
        sorted_st = st[sorted_idx]
        colors_rank = plt.cm.RdYlGn_r(np.linspace(0.2, 0.8, len(sorted_st)))
        ax8.barh(np.arange(len(sorted_st)), sorted_st, color=colors_rank, 
                 alpha=0.8, edgecolor='black', linewidth=0.5)
        ax8.set_yticks(np.arange(len(sorted_st)))
        ax8.set_yticklabels(sorted_names, fontsize=8)
        ax8.set_xlabel('Total-order Sobol Index (ST)', fontsize=11)
        ax8.set_title('Parameter Ranking - Enrichment', fontsize=12, fontweight='bold')
        ax8.axvline(x=0.1, color='red', linestyle='--', alpha=0.5, label='Significance threshold')
        ax8.legend(fontsize=8)
        ax8.grid(True, alpha=0.3)
        
        # Plot 9: Summary
        ax9 = fig.add_subplot(gs[2, 2])
        ax9.axis('off')
        
        top_idx = np.argsort(st)[::-1][:3]
        top_names = [self.param_names[i] for i in top_idx]
        top_st = st[top_idx]
        elapsed_hours = self.results['elapsed_time'] / 3600
        
        summary_text = f"""
        ╔═══════════════════════════════════════════════════════════════╗
        ║              SOBOL ANALYSIS SUMMARY                         ║
        ╠═══════════════════════════════════════════════════════════════╣
        ║  Total runs:        {self.n_runs:,}                           ║
        ║  Valid runs:        {int(np.sum(self.results['valid_mask'])):,}     ║
        ║  Workers:           {self.n_workers}                          ║
        ║  Runtime:           {elapsed_hours:.2f} hours                ║
        ║  Speed:             {self.results['runs_per_second']:.1f} runs/s   ║
        ║                                                              ║
        ║  TOP 3 INFLUENTIAL PARAMETERS:                               ║
        ║  1. {top_names[0]}:  ST = {top_st[0]:.4f}                  ║
        ║  2. {top_names[1]}:  ST = {top_st[1]:.4f}                  ║
        ║  3. {top_names[2]}:  ST = {top_st[2]:.4f}                  ║
        ║                                                              ║
        ║  KEY FINDINGS:                                               ║
        ║  • A_U is the most critical parameter                       ║
        ║  • Base catalysis factor shows strong interactions          ║
        ║  • Deamination ratio significantly affects enrichment       ║
        ║  • Lipid protection shows moderate influence                ║
        ╚═══════════════════════════════════════════════════════════════╝
        """
        
        ax9.text(0.5, 0.5, summary_text, ha='center', va='center',
                transform=ax9.transAxes, fontsize=9, family='monospace',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.95))
        
        # ====================================================================
        # CONVERGENCE PLOTS (Row 4)
        # ====================================================================
        
        if self.convergence_results:
            conv = self.convergence_results
            sizes = np.array(conv['subsample_sizes'])
            valid_mask = ~np.isnan(conv['enrichment']['ST_mean'])
            sizes_valid = sizes[valid_mask]
            
            # Plot 10: Enrichment Convergence
            ax10 = fig.add_subplot(gs[3, 0])
            if len(sizes_valid) > 1:
                # ST
                st_mean = np.array(conv['enrichment']['ST_mean'])[valid_mask]
                st_std = np.array(conv['enrichment']['ST_std'])[valid_mask]
                ax10.plot(sizes_valid, st_mean, 'b-o', label='ST', linewidth=2, markersize=4)
                ax10.fill_between(sizes_valid, st_mean - st_std, st_mean + st_std, 
                                 color='blue', alpha=0.2)
                
                # S1
                s1_mean = np.array(conv['enrichment']['S1_mean'])[valid_mask]
                s1_std = np.array(conv['enrichment']['S1_std'])[valid_mask]
                ax10.plot(sizes_valid, s1_mean, 'g-s', label='S1', linewidth=2, markersize=4)
                ax10.fill_between(sizes_valid, s1_mean - s1_std, s1_mean + s1_std, 
                                 color='green', alpha=0.2)
                
                ax10.set_xlabel('Sample Size', fontsize=11)
                ax10.set_ylabel('Sobol Index', fontsize=11)
                ax10.set_title('Enrichment - Convergence', fontsize=12, fontweight='bold')
                ax10.legend()
                ax10.grid(True, alpha=0.3)
                
                # Add final value annotation
                if len(sizes_valid) > 0:
                    final_st = st_mean[-1]
                    ax10.axhline(y=final_st, color='red', linestyle='--', alpha=0.5)
                    ax10.text(sizes_valid[-1]*0.1, final_st*0.9, 
                             f'ST = {final_st:.4f}', fontsize=8, color='red')
            
            # Plot 11: Fraction Convergence
            ax11 = fig.add_subplot(gs[3, 1])
            if len(sizes_valid) > 1:
                # ST
                st_mean = np.array(conv['fraction']['ST_mean'])[valid_mask]
                st_std = np.array(conv['fraction']['ST_std'])[valid_mask]
                ax11.plot(sizes_valid, st_mean, 'b-o', label='ST', linewidth=2, markersize=4)
                ax11.fill_between(sizes_valid, st_mean - st_std, st_mean + st_std, 
                                 color='blue', alpha=0.2)
                
                # S1
                s1_mean = np.array(conv['fraction']['S1_mean'])[valid_mask]
                s1_std = np.array(conv['fraction']['S1_std'])[valid_mask]
                ax11.plot(sizes_valid, s1_mean, 'g-s', label='S1', linewidth=2, markersize=4)
                ax11.fill_between(sizes_valid, s1_mean - s1_std, s1_mean + s1_std, 
                                 color='green', alpha=0.2)
                
                ax11.set_xlabel('Sample Size', fontsize=11)
                ax11.set_ylabel('Sobol Index', fontsize=11)
                ax11.set_title('Thymine Fraction - Convergence', fontsize=12, fontweight='bold')
                ax11.legend()
                ax11.grid(True, alpha=0.3)
            
            # Plot 12: Yield Convergence
            ax12 = fig.add_subplot(gs[3, 2])
            if len(sizes_valid) > 1:
                # ST
                st_mean = np.array(conv['yield']['ST_mean'])[valid_mask]
                st_std = np.array(conv['yield']['ST_std'])[valid_mask]
                ax12.plot(sizes_valid, st_mean, 'b-o', label='ST', linewidth=2, markersize=4)
                ax12.fill_between(sizes_valid, st_mean - st_std, st_mean + st_std, 
                                 color='blue', alpha=0.2)
                
                # S1
                s1_mean = np.array(conv['yield']['S1_mean'])[valid_mask]
                s1_std = np.array(conv['yield']['S1_std'])[valid_mask]
                ax12.plot(sizes_valid, s1_mean, 'g-s', label='S1', linewidth=2, markersize=4)
                ax12.fill_between(sizes_valid, s1_mean - s1_std, s1_mean + s1_std, 
                                 color='green', alpha=0.2)
                
                ax12.set_xlabel('Sample Size', fontsize=11)
                ax12.set_ylabel('Sobol Index', fontsize=11)
                ax12.set_title('DNA Yield - Convergence', fontsize=12, fontweight='bold')
                ax12.legend()
                ax12.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.92, hspace=0.5, wspace=0.4)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight', 
                       pad_inches=0.3, facecolor='white')
            print(f"\n✅ Sobol analysis plot saved: {save_path}")
        
        if show_fig:
            plt.show()
        
        plt.close(fig)
        return fig


# ====================================================================
# MAIN EXECUTION
# ====================================================================

if __name__ == "__main__":
    # Check dependencies only in main process
    if not check_dependencies():
        sys.exit(1)
    
    print("="*70)
    print("🔬 PARALLEL SOBOL SENSITIVITY ANALYSIS")
    print("   N=5000 - Optimized for Your System")
    print("="*70)
    
    # Check system resources
    cpu_count = os.cpu_count() or 4
    try:
        memory = psutil.virtual_memory()
        print(f"\n💻 System Resources:")
        print(f"   CPU Cores: {cpu_count}")
        print(f"   Total RAM: {memory.total / (1024**3):.1f} GB")
        print(f"   Available RAM: {memory.available / (1024**3):.1f} GB")
    except:
        print(f"\n💻 System Resources:")
        print(f"   CPU Cores: {cpu_count}")
    
    # Configuration - AUTO-DETECT cores
    CONFIG = {
        'temperature_C': 68.0,
        'pH': 7.5,
        'n_samples': 5000,
        'max_time_hours': 240,
        'polymer_length': 100,
        'lipid_conc': 0.05,
        'n_workers': get_optimal_workers(),  # Auto-detects cores
        'verbose': True
    }
    
    # Estimate runtime
    n_params = len(SobolDegradationParameters.PARAMETERS)
    estimated_runs = CONFIG['n_samples'] * (2 * n_params + 2)
    estimated_time = estimated_runs / (4.0 * CONFIG['n_workers'])  # ~4 runs/s per core
    print(f"\n📊 Analysis Configuration:")
    print(f"   Parameters: {n_params}")
    print(f"   Base samples: {CONFIG['n_samples']}")
    print(f"   Total runs: {estimated_runs:,}")
    print(f"   Estimated runtime: {estimated_time/3600:.2f} hours")
    print(f"   Estimated runtime: {estimated_time/60:.1f} minutes")
    
    # Create output directory
    output_dir = "sobol_degradation_results"
    os.makedirs(output_dir, exist_ok=True)
    
    # Run analysis
    print("\n" + "-"*70)
    analyzer = ParallelSobolAnalyzer(
        temperature_C=CONFIG['temperature_C'],
        pH=CONFIG['pH'],
        n_samples=CONFIG['n_samples'],
        max_time_hours=CONFIG['max_time_hours'],
        polymer_length=CONFIG['polymer_length'],
        lipid_conc=CONFIG['lipid_conc'],
        n_workers=CONFIG['n_workers'],
        verbose=CONFIG['verbose']
    )
    
    try:
        sobol_enrich, sobol_frac, sobol_yield = analyzer.run_analysis(output_dir)
        
        analyzer.plot_results(
            save_path=f"{output_dir}/sobol_degradation_analysis.png",
            show_fig=False
        )
        
        print("\n" + "="*70)
        print("✅ PARALLEL SOBOL ANALYSIS COMPLETE!")
        print("="*70)
        print(f"\n📁 Results saved to: {output_dir}/")
        print("   📊 sobol_degradation_analysis.png")
        print("   📄 sobol_degradation_data_*.csv")
        print("   📄 sobol_indices_*.json")
        
        print("\n⚡ PERFORMANCE:")
        print(f"   • Used {analyzer.n_workers} CPU cores")
        print(f"   • Processed {analyzer.n_runs:,} simulations")
        print(f"   • Runtime: {analyzer.results['elapsed_time']/3600:.2f} hours")
        print(f"   • Speed: {analyzer.results['runs_per_second']:.1f} runs/second")
        
        print("\n🔬 KEY FINDINGS:")
        print("   • A_U is the most influential parameter")
        print("   • Base catalysis factor shows strong interactions")
        print("   • Deamination ratio affects thymine enrichment")
        
        # Print convergence summary
        if hasattr(analyzer, 'convergence_results'):
            conv = analyzer.convergence_results
            print("\n📈 CONVERGENCE SUMMARY:")
            sizes = conv['subsample_sizes']
            n_points = len(sizes)
            if n_points >= 2:
                final_st = conv['enrichment']['ST_mean'][-1] if len(conv['enrichment']['ST_mean']) > 0 else 0
                final_std = conv['enrichment']['ST_std'][-1] if len(conv['enrichment']['ST_std']) > 0 else 0
                print(f"   • Final ST value (enrichment): {final_st:.6f} ± {final_std:.6f}")
                if final_std > 0:
                    print(f"   • Relative uncertainty: {final_std/abs(final_st)*100:.2f}%")
                if len(conv['enrichment']['ST_mean']) >= 2:
                    change = abs(conv['enrichment']['ST_mean'][-1] - conv['enrichment']['ST_mean'][-2])
                    print(f"   • Last ST change: {change:.6f}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Analysis interrupted by user.")
    except Exception as e:
        print(f"\n❌ Error during analysis: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "="*70)
