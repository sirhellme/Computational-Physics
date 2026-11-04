import numpy as np
import matplotlib.pyplot as plt

# Parameters
periods = 100
simulations = 1000
start = 0

# Generate random numbers
random = np.random.randn(periods,simulations)
random[0,:] = start

#Generate random walk
random_walk = np.cumsum(random, axis=0)

# Set figure size
plt.figure(figsize=(12, 8))

# Plot the possible paths of the random walk
random_walk_plot = plt.plot(random_walk)

plt.title('A Collection of Random Walk')
plt.xlabel('Periods')
plt.ylabel('Value')
plt.show()
