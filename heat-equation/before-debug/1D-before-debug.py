import numpy as np 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("QtAgg")

# Function
def s(t):
    return 323

def dsdt(t):
    return 0

def g(t):
    return 0

# Define Parameters
L = 0.5
dx = 0.01
Nx = int(L / dx) 
beta = 8.2E-5

# Temperature array
u = np.zeros(Nx)
u[:] = s(0)*np.exp(-(np.linspace(0,L,Nx))**2)
u_old = u

# Time Parameter
t = 0
dt = 0.01
tf = 100

plot_every = 80

while t < tf:
    # kondisi batas kiri
    u[0] = u_old[0] + dsdt(t) * dt 
    # perhitungan titik interior
    for i in range(1, Nx - 1):
        u[i] = u_old[i] + beta / dx**2 * (u_old[i+1] - 2 * u_old[i] + u_old[i-1]) + g(t)
    # kondisi batas kanan
    u[Nx-1] = u_old[Nx-1] + 2 * beta / dx**2 * (u_old[Nx-2] - u_old[Nx-1]) + g(t)
    # update time
    t = t + dt 
    # update old temperature into current temperature
    u_old = u 

plt.plot(u, label = 't = '+str(t))
plt.legend()
plt.show()