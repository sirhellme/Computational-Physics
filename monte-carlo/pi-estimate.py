import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("QtAgg")

def estimate_pi(N):
    x = np.random.uniform(0, 1, N)
    y = np.random.uniform(0, 1, N)
    plt.scatter(x, y)
    plt.axis([0,1,0,1])
    plt.gca().set_aspect('equal')
    circle = plt.Circle((0.5,0.5),0.5,fill=False)
    plt.gca().add_artist(circle)
    plt.show()

    insider = np.square(x-0.5)+np.square(y-0.5)<0.25
    
    # return 4 * np.sum(np.square(x - 0.5) + np.square(y - 0.5) < 0.25)/N
    return 4 * np.sum(insider)/N

print(estimate_pi(1000))