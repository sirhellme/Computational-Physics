# Simulasi difusi panas 1D pada kawat aluminium alloy
# Panjang 50 cm, k = 200 W/(m K), rho = 2.7e3 kg/m^3, c = 900 J/(kg K)
#
# Versi "centered heat":
#   Berbeda dari heat-rod.py, panas awal dipusatkan di TENGAH kawat,
#   dan KEDUA ujung bersifat adiabatik (Neumann), sehingga total panas
#   di dalam kawat tetap kekal selama simulasi.
#
# Persamaan:  u_t = beta * u_xx + g(t),   beta = k / (rho c)
# Skema:      FTCS eksplisit

import numpy as np
import matplotlib.pyplot as plt

# Parameter material
k = 200.0          # konduktivitas termal [W/(m K)]
rho = 2.7e3        # densitas [kg/m^3]
c = 900.0          # kapasitas panas spesifik [J/(kg K)]

# Parameter ruang dan waktu
L = 0.5            # panjang kawat [m]
dx = 0.01          # jarak antar grid [m]
tf = 3000.0        # waktu akhir simulasi [s]

# Parameter fisika
beta = k / (rho * c)                  # difusivitas termal [m^2/s]
Nx = int(round(L / dx)) + 1           # jumlah titik grid
x = np.linspace(0.0, L, Nx)

# Langkah waktu dipilih dari angka difusi target r = beta*dt/dx^2.
# Skema eksplisit stabil untuk r <= 0.5.
r_target = 0.25
Nt = int(round(tf / (r_target * dx**2 / beta)))
dt = tf / Nt                          # agar waktu akhir tepat sama dengan tf
r = beta * dt / dx**2
assert r <= 0.5, f"Skema tidak stabil: r = {r:.3f} > 0.5"

# Kondisi awal: hotspot Gaussian di tengah kawat
T_ambient = 300.15    # 27 C
T_hot = 373.15        # 100 C, puncak di tengah kawat
w = 0.08              # lebar hotspot [m]

def g(t):
    """Suku sumber panas internal [K/s] (0 = tidak ada sumber)."""
    return 0.0

u = T_ambient + (T_hot - T_ambient) * np.exp(-((x - L / 2.0) / w) ** 2)
u_old = u.copy()

# Simpan beberapa snapshot agar grafik mudah dibaca
n_snapshots = 10
snapshot_steps = set(np.linspace(0, Nt, n_snapshots).astype(int))
snapshots = []

# Iterasi waktu
for n in range(Nt + 1):
    t = n * dt

    if n in snapshot_steps:
        snapshots.append((t, u_old.copy()))

    if n == Nt:
        break

    u_new = np.empty_like(u_old)

    # Batas kiri (Neumann / adiabatik) dengan ghost node
    u_new[0] = (u_old[0]
                + 2.0 * r * (u_old[1] - u_old[0])
                + g(t) * dt)

    # Titik interior (FTCS)
    for i in range(1, Nx - 1):
        u_new[i] = (u_old[i]
                    + r * (u_old[i + 1] - 2.0 * u_old[i] + u_old[i - 1])
                    + g(t) * dt)

    # Batas kanan (Neumann / adiabatik) dengan ghost node
    u_new[Nx - 1] = (u_old[Nx - 1]
                     + 2.0 * r * (u_old[Nx - 2] - u_old[Nx - 1])
                     + g(t) * dt)

    u_old = u_new

# Cek kekekalan panas. Gunakan rata-rata berbobot (aturan trapesium),
# karena titik batas mewakili setengah volume kontrol.
def mean_temperature(profile):
    # dx/L = 1/(Nx - 1) untuk grid seragam
    return (0.5 * profile[0] + profile[1:-1].sum() + 0.5 * profile[-1]) / (Nx - 1)

print(f"Rata-rata suhu awal  : {mean_temperature(u):.3f} K")
print(f"Rata-rata suhu akhir : {mean_temperature(u_old):.3f} K")
print(f"Selisih              : {abs(mean_temperature(u_old) - mean_temperature(u)):.3e} K")

# Plot snapshot dengan warna yang berbeda
colors = plt.cm.viridis(np.linspace(0.0, 1.0, len(snapshots)))
fig, ax = plt.subplots(figsize=(9, 5))
for (t, profile), color in zip(snapshots, colors):
    ax.plot(x, profile, color=color, label=f"t = {t:.0f} s")

ax.set_xlabel("Position x (m)")
ax.set_ylabel("Temperature u (K)")
ax.set_title("1D Heat Diffusion — heat concentrated at the center")
ax.grid(True)
ax.legend()
fig.tight_layout()
plt.show()
