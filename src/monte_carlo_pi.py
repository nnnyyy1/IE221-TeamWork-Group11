import random
import math
import matplotlib.pyplot as plt
import os

def estimate_pi_monte_carlo(N):
    """
    Estimates the value of pi using the Monte Carlo simulation method.

    Parameters:
    N (int): Number of random points generated in the simulation.

    Returns:
    None. Displays and saves a convergence plot of the pi estimation.
    """

    # Create folders if they do not exist
    os.makedirs("results/figures", exist_ok=True)

    inside_circle = 0
    pi_estimates = []
    points = []

    for i in range(1, N + 1):
        # Generate a random point in the unit square [0,1] x [0,1]
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # Check whether the point lies inside the quarter circle
        if x**2 + y**2 <= 1:
            inside_circle += 1

        # Monte Carlo estimation of pi using area ratio
        pi_hat = 4 * inside_circle / i
        pi_estimates.append(pi_hat)
        points.append(i)

    # Plot the convergence of the Monte Carlo estimation
    plt.figure()
    plt.plot(points, pi_estimates, label="Monte Carlo π Estimate")
    plt.axhline(y=math.pi, linestyle="--", label="True π")
    plt.xlabel("Number of Points")
    plt.ylabel("π Estimate")
    plt.title("Monte Carlo Estimation of π")
    plt.legend()

    # Save and show the plot
    plt.savefig("results/figures/pi_estimation.png")
    plt.show()


# Run the simulation
estimate_pi_monte_carlo(10000)
