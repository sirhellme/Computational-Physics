import numpy as np
import matplotlib.pyplot as plt

def s(t):
    return 323

def dsdt(t):
    return 0

def g(t):
    return 0

L = 0.5
dx = 0.01
Nx = int(L/dx) + 1

beta = 8.2e-5

x = np.linspace(0, L, Nx)

u = s(0) * np.exp(-x**2)
uold = u.copy()

t = 0
dt = 0.01
tf = 100

r = beta * dt / dx**2

plot_every = 80

while t < tf:

    uold = u.copy()

    u[0] = uold[0] + dsdt(t)*dt

    for i in range(1, Nx-1):
        u[i] = uold[i] + r * (
            uold[i+1] - 2*uold[i] + uold[i-1]
        ) + g(t)*dt

    u[Nx-1] = uold[Nx-1] + 2*r*(
        uold[Nx-2] - uold[Nx-1]
    ) + g(t)*dt

    t += dt

plt.plot(x, u, label=f't = {t:.2f} s')
plt.xlabel('Position (m)')
plt.ylabel('Temperature (K)')
plt.legend()
plt.grid()
plt.show()
