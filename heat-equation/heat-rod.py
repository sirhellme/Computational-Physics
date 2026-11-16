
import numpy as np
import matplotlib.pyplot as plt

def variasi(T, dt):

    L = 0.5
    dx = 0.01
    Nx = int(L/dx) + 1

    beta = 8.2e-5

    x = np.linspace(0, L, Nx)

    u = np.full(Nx, 27.0)
    uold = u.copy()

    r = beta * dt / dx**2

    if r > 0.5:
        raise ValueError("Simulasi tidak stabil")

    Nt = int(round(T / dt))

    for i in range(Nt):
        uold = u.copy()

        u[1:-1] = uold[1:-1] + r * (uold[2:] - 2*uold[1:-1] + uold[:-2])

        u[0] = 100.0                  # ujung kiri: suhu tetap
        u[-1] = uold[-1] + 2*r * (uold[-2] - uold[-1])  # ujung kanan: terisolasi

    return x, u


# Variasi T
for T in [10, 30, 50, 100, 200]:

    x, u = variasi(T, 0.01)
    plt.plot(x, u, label=f'T = {T} s')

plt.xlabel('Position (m)')
plt.ylabel('Temperature (°C)')
plt.title('Variation of Simulation Time')
plt.legend()
plt.grid()
plt.show()


# Variasi dt
for dt in [0.001, 0.01, 0.05, 0.1, 0.5]:

    x, u = variasi(100, dt)
    plt.plot(x, u, label=f'dt = {dt} s')

plt.xlabel('Position (m)')
plt.ylabel('Temperature (°C)')
plt.title('Variation of Time Step')
plt.legend()
plt.grid()
plt.show()
