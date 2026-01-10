"""
Central Limit Theorem (CLT) Simulation

This script performs a Monte Carlo simulation to verify the Central Limit
Theorem using Uniform(0,1) random variables. Standardized sums are generated
for different sample sizes, and convergence in distribution is analyzed
using histograms and Q-Q plots.
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

# ========================
# Parameters
# ========================
mu = 0.5                 # Mean of U[0,1]
sigma = np.sqrt(1/12)    # Std of U[0,1]
m = 1000                 # Number of experiments
n_values = [2, 5, 10, 30, 50]

# Create output directory if not exists
output_dir = "results/figures"
os.makedirs(output_dir, exist_ok=True)

# ========================
# CLT Simulation
# ========================
for n in n_values:
    # Generate m experiments, each summing n U[0,1] variables
    samples = np.random.uniform(0, 1, size=(m, n))
    sums = samples.sum(axis=1)

    # Standardization
    Z = (sums - n * mu) / (sigma * np.sqrt(n))

    # --------------------
    # Histogram + Normal PDF
    # --------------------
    plt.figure(figsize=(8, 5))
    plt.hist(Z, bins=30, density=True, alpha=0.6, label="Standardized sums")

    x = np.linspace(-4, 4, 400)
    plt.plot(x, stats.norm.pdf(x), 'r', lw=2, label="N(0,1)")

    plt.title(f"CLT Histogram (n = {n})")
    plt.xlabel("Z")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True)

    plt.savefig(f"{output_dir}/clt_histogram_n{n}.png")
    plt.close()

    # --------------------
    # Q-Q Plot
    # --------------------
    plt.figure(figsize=(6, 6))
    stats.probplot(Z, dist="norm", plot=plt)
    plt.title(f"Q-Q Plot (n = {n})")
    plt.grid(True)

    plt.savefig(f"{output_dir}/clt_qqplot_n{n}.png")
    plt.close()

print("CLT simulation completed. Figures saved in results/figures/")

