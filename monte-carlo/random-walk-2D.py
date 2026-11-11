import numpy as np

# Simulation parameters
num_steps = 1000
num_walks = 500

# Generate random angles (0 to 2*pi) and step sizes (l = 1)
angles = np.random.uniform(0, 2 * np.pi, size=(num_walks, num_steps))
dx = np.cos(angles)
dy = np.sin(angles)

# Cumulative sum along steps to get trajectories
x = np.cumsum(dx, axis=1)
y = np.cumsum(dy, axis=1)

# Calculate final mean squared displacement
final_distances_squared = x[:, -1] ** 2 + y[:, -1] ** 2
mean_squared_displacement = np.mean(final_distances_squared)

print(f"Average Squared Distance after {num_steps} steps: {mean_squared_displacement:.2f}")

