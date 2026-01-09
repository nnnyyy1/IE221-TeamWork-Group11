"""
IE221 - Probability | Team Work 4
Task: SLLN Simulation (Uniform(0,1))

This script demonstrates the Strong Law of Large Numbers (SLLN) via simulation.
We generate i.i.d. samples X1, X2, ..., Xn ~ Uniform(0,1) and compute the
cumulative sample mean:

    X̄_n = (X1 + X2 + ... + Xn) / n

According to SLLN, X̄_n -> E[X] almost surely as n -> infinity.
For Uniform(0,1), E[X] = 0.5, so the cumulative mean should converge to 0.5.

Run:
    python src/slln_simulation.py

Output:
    results/figures/slln_convergence.png
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def run_slln_simulation(n: int = 20000, seed: int = 42, mu: float = 0.5) -> Path:
    """
    Run an SLLN simulation for Uniform(0,1) and save the convergence plot.

    Parameters
    ----------
    n : int, optional
        Number of i.i.d. samples to generate (default: 20000).
        Larger n gives a clearer convergence behavior but takes longer to run.
    seed : int, optional
        Random seed used for reproducibility (default: 42).
        Using a fixed seed ensures the same plot is obtained every run.
    mu : float, optional
        Theoretical mean of the distribution (default: 0.5 for Uniform(0,1)).

    Returns
    -------
    Path
        Path to the saved figure file.
    """

    # Create a reproducible random number generator
    rng = np.random.default_rng(seed)

    # 1) Generate i.i.d. samples from Uniform(0,1)
    samples = rng.uniform(low=0.0, high=1.0, size=n)

    # 2) Compute cumulative sums: S_k = X1 + ... + Xk for k=1..n
    cumulative_sums = np.cumsum(samples)

    # 3) Compute cumulative means: X̄_k = S_k / k
    k_values = np.arange(1, n + 1)
    cumulative_means = cumulative_sums / k_values

    # 4) Prepare output directory for figures
    figures_dir = Path("results") / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    fig_path = figures_dir / "slln_convergence.png"

    # 5) Plot: cumulative mean vs. number of observations (k)
    plt.figure(figsize=(8, 5))
    plt.plot(k_values, cumulative_means, label="Cumulative mean", linewidth=1)

    # Reference line for the true mean E[X]
    plt.axhline(mu, linestyle="--", linewidth=2, label=f"True mean μ = {mu}")

    plt.xlabel("Number of observations n")
    plt.ylabel("Sample mean")
    plt.title("SLLN Simulation for Uniform(0,1)")
    plt.legend()
    plt.grid(alpha=0.4)
    plt.tight_layout()

    # Save and close the figure to avoid memory issues in repeated runs
    plt.savefig(fig_path, dpi=300)
    plt.close()

    print(f"SLLN figure saved to: {fig_path}")
    return fig_path


if __name__ == "__main__":
    # You may increase n (e.g., 50000 or 100000) to observe smoother convergence.
    run_slln_simulation(n=20000, seed=42)
