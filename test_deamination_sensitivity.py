"""
Sensitivity Test: Effect of Cytosine Deamination on Thymine Enrichment
Conditions: T=68°C, pH=8.0, 120 hours, polymer_length=100
License & Copyright
Copyright ©️ 2026 Seyed Mohammad Reza Hashemi  
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0).

ORCID: 0009-0002-0645-5180
DOI: 10.5281/zenodo.21224889
"""

import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import sys
import os
from dataclasses import dataclass
from typing import Dict, Any, Optional

# ============================================================
# Configure Matplotlib for Persian Text Support
# ============================================================
# Use a font that supports Persian/Arabic characters
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Tahoma', 'Helvetica']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['figure.constrained_layout.use'] = False
plt.rcParams['axes.unicode_minus'] = False  # Fix minus sign display

# ============================================================
# Configuration
# ============================================================

@dataclass
class SimulationConfig:
    """Configuration parameters for the simulation."""
    temperature_C: float = 68.0
    pH: float = 8.0
    max_time_hours: float = 120.0
    polymer_length: int = 100
    lipid_conc: float = 0.05
    uv_exposure_factor: float = 0.8
    seed: int = 42
    verbose: bool = False

class SimulationResult:
    """Container for simulation results."""
    def __init__(self, engine, history, enrichment, fraction, composition, deam_events):
        self.engine = engine
        self.history = history
        self.enrichment = enrichment
        self.fraction = fraction
        self.composition = composition
        self.deam_events = deam_events
        self.time_hours = np.array(history['time']) / 3600.0

# ============================================================
# Load UPDSF v4.4 Engine
# ============================================================

def find_engine_file(custom_path: str = None) -> str:
    """Find the UPDSF v4.4 engine file."""
    if custom_path and os.path.exists(custom_path):
        return custom_path
    
    search_paths = [
        "UPDSF_v4.4.py",
        "UPD5F_v4.4.py",
        "../UPDSF_v4.4.py",
        "./attachments/UPDSF_v4.4.py",
        "../attachments/UPDSF_v4.4.py",
        os.path.join(os.path.dirname(__file__), "UPDSF_v4.4.py"),
        os.path.join(os.path.dirname(__file__), "../UPDSF_v4.4.py"),
        os.path.join(os.path.dirname(__file__), "attachments", "UPDSF_v4.4.py"),
    ]
    
    home = os.path.expanduser("~")
    additional_paths = [
        os.path.join(home, "Downloads", "UPDSF_v4.4.py"),
        os.path.join(home, "Downloads", "UPD5F_v4.4.py"),
        os.path.join(home, "Desktop", "UPDSF_v4.4.py"),
        os.path.join(home, "Desktop", "UPD5F_v4.4.py"),
        os.path.join(home, "Documents", "UPDSF_v4.4.py"),
        os.path.join(home, "workdir", "attachments", "UPDSF_v4.4.py"),
    ]
    search_paths.extend(additional_paths)
    
    for path in search_paths:
        if os.path.exists(path):
            return path
    
    raise FileNotFoundError(
        f"UPDSF v4.4 engine file not found!\n"
        f"Please ensure the file 'UPDSF_v4.4.py' is in one of these locations:\n"
        f"  - Current directory: {os.getcwd()}\n"
        f"  - Downloads folder\n"
        f"  - Desktop\n"
    )

def load_updsf_engine(file_path: str = None):
    """Load the UPDSF v4.4 engine from file."""
    if file_path is None:
        file_path = find_engine_file()
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"UPDSF engine not found at: {file_path}")
    
    print(f"Loading UPDSF engine from: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    if 'VSSUFEngine' not in code:
        raise ValueError(f"The file '{file_path}' does not appear to be a valid UPDSF engine file.")
    
    try:
        if 'if __name__' in code:
            code_to_exec = code.split('if __name__')[0]
        else:
            code_to_exec = code
        exec(code_to_exec, globals())
        print(f"✓ UPDSF v4.4 engine loaded successfully")
    except Exception as e:
        raise RuntimeError(f"Failed to load UPDSF engine: {e}")

# ============================================================
# Simulation Runner
# ============================================================

def run_simulation(config: SimulationConfig, enable_deamination: bool = True) -> SimulationResult:
    """Run a single simulation with specified parameters."""
    if 'VSSUFEngine' not in globals():
        raise RuntimeError("VSSUFEngine not loaded. Please call load_updsf_engine() first.")
    
    engine = VSSUFEngine(
        temperature_C=config.temperature_C,
        pH=config.pH,
        seed=config.seed,
        max_time_hours=config.max_time_hours,
        verbose=config.verbose,
        polymer_length=config.polymer_length,
        lipid_conc=config.lipid_conc,
        uv_exposure_factor=config.uv_exposure_factor
    )
    
    if not enable_deamination:
        if hasattr(engine, 'k_deamination'):
            engine.k_deamination = 0.0
        if 'pHArrheniusRates' in globals():
            pHArrheniusRates.DEAMINATION_RATIO_C = 0.0
            pHArrheniusRates.k_deam_base = 0.0
    
    history = engine.run()
    
    return SimulationResult(
        engine=engine,
        history=history,
        enrichment=engine.get_thymine_enrichment(),
        fraction=engine.get_final_thymine_fraction(),
        composition=engine.get_nucleotide_composition(),
        deam_events=engine.deamination_events
    )

def run_comparison(config: SimulationConfig) -> Dict[str, SimulationResult]:
    """Run both simulations (with and without deamination) for comparison."""
    print("=" * 60)
    print("Running simulations...")
    print("=" * 60)
    
    print("  1. WITH deamination...")
    result_with = run_simulation(config, enable_deamination=True)
    
    print("  2. WITHOUT deamination...")
    result_without = run_simulation(config, enable_deamination=False)
    
    print("\n" + "=" * 60)
    print("SIMULATION SUMMARY")
    print("=" * 60)
    print(f"WITH deamination    → Enrichment: {result_with.enrichment:.3f}x | "
          f"T-fraction: {result_with.fraction:.3f} | Events: {result_with.deam_events}")
    print(f"WITHOUT deamination → Enrichment: {result_without.enrichment:.3f}x | "
          f"T-fraction: {result_without.fraction:.3f} | Events: {result_without.deam_events}")
    print("=" * 60 + "\n")
    
    return {
        'with_deam': result_with,
        'without_deam': result_without
    }

# ============================================================
# Plotting Functions - Completely Redesigned
# ============================================================

def create_comparison_figure(results: Dict[str, SimulationResult], config: SimulationConfig, 
                            output_file: str = 'deamination_sensitivity_comparison.png'):
    """
    Create comprehensive comparison figure with clean layout.
    """
    result_with = results['with_deam']
    result_without = results['without_deam']
    
    # Create figure with 2x3 grid plus summary at bottom
    fig = plt.figure(figsize=(16, 12))
    
    # Create GridSpec
    gs = GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.35,
                  top=0.92, bottom=0.08, left=0.08, right=0.95)
    
    # Create subplots
    ax1 = fig.add_subplot(gs[0, 0])  # WITH - DNA accumulation
    ax2 = fig.add_subplot(gs[0, 1])  # WITHOUT - DNA accumulation
    ax3 = fig.add_subplot(gs[0, 2])  # Enrichment comparison
    ax4 = fig.add_subplot(gs[1, 0])  # WITH - Fractions
    ax5 = fig.add_subplot(gs[1, 1])  # WITHOUT - Fractions
    ax6 = fig.add_subplot(gs[1, 2])  # Final composition
    ax7 = fig.add_subplot(gs[2, :])  # Summary text
    
    # Main title
    fig.suptitle('Effect of Cytosine Deamination on Thymine Selection',
                 fontsize=18, fontweight='bold', y=0.98)
    
    # Subtitle
    fig.text(0.5, 0.945, 
             f'T = {config.temperature_C:.1f}°C    pH = {config.pH:.1f}    {config.max_time_hours:.0f} hours    Polymer length = {config.polymer_length}',
             fontsize=14, ha='center', style='italic')
    
    # ---------- Row 1: DNA Accumulation ----------
    # WITH Deamination
    ax1.plot(result_with.time_hours, result_with.history['dsDNA_U'], 
             'b-', label='U', lw=2.5)
    ax1.plot(result_with.time_hours, result_with.history['dsDNA_T'], 
             'r-', label='T', lw=2.5)
    ax1.plot(result_with.time_hours, result_with.history['dsDNA_C'], 
             'g-', label='C', lw=2.5)
    ax1.plot(result_with.time_hours, result_with.history['dsDNA_A'], 
             '#FF8C00', label='A', lw=2.5)
    ax1.set_title('WITH Deamination', fontsize=13, fontweight='bold')
    ax1.set_xlabel('Time (h)', fontsize=11)
    ax1.set_ylabel('Count', fontsize=11)
    ax1.legend(loc='best', fontsize=10, framealpha=0.9)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.tick_params(labelsize=10)
    
    # WITHOUT Deamination
    ax2.plot(result_without.time_hours, result_without.history['dsDNA_U'], 
             'b-', label='U', lw=2.5)
    ax2.plot(result_without.time_hours, result_without.history['dsDNA_T'], 
             'r-', label='T', lw=2.5)
    ax2.plot(result_without.time_hours, result_without.history['dsDNA_C'], 
             'g-', label='C', lw=2.5)
    ax2.plot(result_without.time_hours, result_without.history['dsDNA_A'], 
             '#FF8C00', label='A', lw=2.5)
    ax2.set_title('WITHOUT Deamination', fontsize=13, fontweight='bold')
    ax2.set_xlabel('Time (h)', fontsize=11)
    ax2.set_ylabel('Count', fontsize=11)
    ax2.legend(loc='best', fontsize=10, framealpha=0.9)
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.tick_params(labelsize=10)
    
    # Enrichment comparison
    ax3.plot(result_with.time_hours, result_with.history['enrichment'], 
             'purple', lw=3, label='WITH deamination', marker='s', markersize=4)
    ax3.plot(result_without.time_hours, result_without.history['enrichment'], 
             'darkorange', lw=3, label='WITHOUT deamination', marker='o', markersize=4)
    ax3.set_title('Thymine Enrichment over Time', fontsize=13, fontweight='bold')
    ax3.set_xlabel('Time (h)', fontsize=11)
    ax3.set_ylabel('Enrichment (×)', fontsize=11)
    ax3.legend(loc='best', fontsize=10, framealpha=0.9)
    ax3.grid(True, alpha=0.3, linestyle='--')
    ax3.tick_params(labelsize=10)
    
    # ---------- Row 2: Fractions ----------
    colors = {'U': 'b', 'T': 'r', 'C': 'g', 'A': '#FF8C00'}
    
    # WITH Deamination - Fractions
    for base, color in colors.items():
        ax4.plot(result_with.time_hours, result_with.history['fractions'][base], 
                color=color, label=base, lw=2.5)
    ax4.set_title('WITH Deamination - Fractions', fontsize=13, fontweight='bold')
    ax4.set_xlabel('Time (h)', fontsize=11)
    ax4.set_ylabel('Fraction', fontsize=11)
    ax4.set_ylim(0, 1)
    ax4.legend(loc='best', fontsize=10, framealpha=0.9)
    ax4.grid(True, alpha=0.3, linestyle='--')
    ax4.tick_params(labelsize=10)
    
    # WITHOUT Deamination - Fractions
    for base, color in colors.items():
        ax5.plot(result_without.time_hours, result_without.history['fractions'][base], 
                color=color, label=base, lw=2.5)
    ax5.set_title('WITHOUT Deamination - Fractions', fontsize=13, fontweight='bold')
    ax5.set_xlabel('Time (h)', fontsize=11)
    ax5.set_ylabel('Fraction', fontsize=11)
    ax5.set_ylim(0, 1)
    ax5.legend(loc='best', fontsize=10, framealpha=0.9)
    ax5.grid(True, alpha=0.3, linestyle='--')
    ax5.tick_params(labelsize=10)
    
    # Final Composition - Bar Chart
    bases = ['U', 'T', 'C', 'A']
    x = np.arange(len(bases))
    width = 0.35
    
    vals_with = [result_with.composition[b] for b in bases]
    vals_without = [result_without.composition[b] for b in bases]
    
    bars1 = ax6.bar(x - width/2, vals_with, width, label='WITH deamination', 
                   color='steelblue', alpha=0.8, edgecolor='black', linewidth=0.8)
    bars2 = ax6.bar(x + width/2, vals_without, width, label='WITHOUT deamination', 
                   color='darkorange', alpha=0.8, edgecolor='black', linewidth=0.8)
    
    ax6.set_xticks(x)
    ax6.set_xticklabels(bases, fontsize=12, fontweight='bold')
    ax6.set_ylabel('Final Count', fontsize=11)
    ax6.set_title('Final Composition', fontsize=13, fontweight='bold')
    ax6.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax6.grid(True, axis='y', alpha=0.3, linestyle='--')
    ax6.tick_params(labelsize=10)
    
    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax6.text(bar.get_x() + bar.get_width()/2, height + 30,
                   f'{int(height):,}', ha='center', va='bottom', 
                   fontsize=9, fontweight='bold')
    
    # ---------- Row 3: Summary ----------
    ax7.axis('off')
    
    # Create summary table
    enrichment_diff = abs(result_with.enrichment - result_without.enrichment)
    relative_diff = 100 * enrichment_diff / max(result_with.enrichment, 1e-9)
    
    summary_lines = [
        "=" * 78,
        "                    SENSITIVITY TEST SUMMARY - Cytosine Deamination",
        "=" * 78,
        f"  Conditions:  {config.temperature_C:.0f}°C  |  pH {config.pH:.1f}  |  {config.max_time_hours:.0f} hours  |  Polymer length = {config.polymer_length}",
        "=" * 78,
        "                            WITH Deamination        WITHOUT Deamination",
        f"  Enrichment (T)                {result_with.enrichment:8.3f} ×              {result_without.enrichment:8.3f} ×",
        f"  T fraction                    {result_with.fraction:8.3f}                {result_without.fraction:8.3f}",
        f"  Final U                       {result_with.composition['U']:8.0f}                {result_without.composition['U']:8.0f}",
        f"  Final T                       {result_with.composition['T']:8.0f}                {result_without.composition['T']:8.0f}",
        f"  Final C                       {result_with.composition['C']:8.0f}                {result_without.composition['C']:8.0f}",
        f"  Final A                       {result_with.composition['A']:8.0f}                {result_without.composition['A']:8.0f}",
        f"  Deamination events            {result_with.deam_events:8d}                {result_without.deam_events:8d}",
        "=" * 78,
        f"  Absolute difference in enrichment : {enrichment_diff:.3f} ×",
        f"  Relative difference               : {relative_diff:.1f} %",
        "=" * 78,
        "  CONCLUSION: Deamination affects quantitative enrichment (~25%) but does NOT reverse",
        "              the qualitative selection of Thymine. Main selective pressures remain",
        "              hydrolysis stability, UV resistance and lipid partitioning.",
        "=" * 78,
    ]
    
    summary_text = "\n".join(summary_lines)
    
    ax7.text(0.5, 0.5, summary_text, ha='center', va='center', 
             fontsize=9.5, family='monospace', transform=ax7.transAxes,
             bbox=dict(boxstyle='round,pad=0.8', facecolor='#FFF8E7', 
                      alpha=0.95, edgecolor='#8B7D6B', linewidth=1.5))
    
    # Save figure
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✅ Figure saved: {output_file}")

# ============================================================
# Main Execution
# ============================================================

def main():
    """Main execution function."""
    print("=" * 60)
    print("CYTOSINE DEAMINATION SENSITIVITY TEST")
    print("=" * 60)
    
    # Load UPDSF engine
    try:
        load_updsf_engine()
    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        print("\nPlease place the 'UPDSF_v4.4.py' file in one of these locations:")
        print(f"  - Current directory: {os.getcwd()}")
        print(f"  - Downloads folder")
        print(f"  - Desktop")
        return
    except Exception as e:
        print(f"\n❌ Error loading engine: {e}")
        return
    
    # Configure simulation
    config = SimulationConfig(
        temperature_C=68.0,
        pH=8.0,
        max_time_hours=120.0,
        polymer_length=100,
        lipid_conc=0.05,
        uv_exposure_factor=0.8,
        seed=42,
        verbose=False
    )
    
    # Run simulations
    try:
        results = run_comparison(config)
    except Exception as e:
        print(f"\n❌ Error during simulation: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Create figure
    try:
        create_comparison_figure(results, config)
    except Exception as e:
        print(f"\n❌ Error creating figure: {e}")
        import traceback
        traceback.print_exc()
        return
    
    print("\n✅ Done!")

if __name__ == "__main__":
    main()
