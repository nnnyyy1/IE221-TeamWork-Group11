import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def run_slln_simulation(n=20000, seed=42):
    """
    Strong Law of Large Numbers (SLLN) simulation
    for Uniform(0,1) random variables.
    """

    rng = np.random.default_rng(seed)

    samples = rng.uniform(0.0, 1.0, size=n)
    cumulative_sums = np.cumsum(samples)
    n_values = np.arange(1, n + 1)
    cumulative_means = cumulative_sums / n_values

    figures_dir = Path("results") / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    fig_path = figures_dir / "slln_convergence.png"

    plt.figure(figsize=(8, 5))
    plt.plot(n_values, cumulative_means, label="Cumulative mean", linewidth=1)
    plt.axhline(0.5, linestyle="--", linewidth=2,
                label="True mean μ = 0.5")

    plt.xlabel("Number of observations n")
    plt.ylabel("Sample mean")
    plt.title("SLLN Simulation for Uniform(0,1)")
    plt.legend()
    plt.grid(alpha=0.4)
    plt.tight_layout()

    plt.savefig(fig_path, dpi=300)
    plt.close()

    print(f"SLLN figure saved to: {fig_path}")


if __name__ == "__main__":
    run_slln_simulation(n=20000)
    
