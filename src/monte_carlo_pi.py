import random
import math
import matplotlib.pyplot as plt
import os

# Create folders if they do not exist
os.makedirs("results/figures", exist_ok=True)

# Number of random points
N = 10000

inside_circle = 0
pi_estimates = []
points = []

for i in range(1, N + 1):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if x**2 + y**2 <= 1:
        inside_circle += 1

    pi_hat = 4 * inside_circle / i
    pi_estimates.append(pi_hat)
    points.append(i)

# Plot
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
Add Monte Carlo pi simulation code

