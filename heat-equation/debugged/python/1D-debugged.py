import numpy as np
import matplotlib.pyplot as plt



def s(t):
    return 323.0          # suhu batas kiri (K)


def g(t):
    return 0.0            # suku sumber



L = 0.5
dx = 0.01
Nx = int(round(L / dx)) + 1     # round() menghindari galat pembulatan float
beta = 8.2e-5
x = np.linspace(0, L, Nx)


u = s(0) * np.exp(-(x**2))
u_old = u.copy()                # salinan, bukan alias


t = 0.0
dt = 0.01
tf = 100
Nt = int(round(tf / dt))


plot_every = 80


plt.figure(figsize=(9, 5))
plt.title("Simulasi Difusi Panas 1D")


r = beta * dt / dx**2
n = 0

while n <= Nt:
    t = n * dt

    # Plot pada waktu t
    if n % plot_every == 0 or n == Nt:
        plt.plot(x, u, label=f"t = {t:.2f} s")

    if n == Nt:
        break

    # Batas kiri (Dirichlet)
    u[0] = s(t + dt)

    # Titik interior
    for i in range(1, Nx - 1):
        u[i] = (u_old[i]
                + r * (u_old[i + 1] - 2 * u_old[i] + u_old[i - 1])
                + g(t) * dt)

    # Batas kanan (Neumann / adiabatik)
    u[Nx - 1] = (u_old[Nx - 1]
                 + 2 * r * (u_old[Nx - 2] - u_old[Nx - 1])
                 + g(t) * dt)

    # Perbarui u_old dengan salinan u
    u_old = u.copy()

    # Perbarui penghitung langkah
    n += 1

plt.xlabel("Posisi x (m)")
plt.ylabel("Temperatur u (K)")
plt.title("Simulasi Difusi Panas 1D")
plt.legend()
plt.grid(True)
plt.show()
