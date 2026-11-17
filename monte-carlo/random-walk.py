import numpy as np
import matplotlib.pyplot as plt

# Parameter
N = 100     #Jumlah partikel
Nt = 1000   #Jumlah langkah waktu
dt = 1.0    #Selang waktu per langkah

# Posisi awal semua partikel di (0, 0)
x = np.zeros((Nt, N))
y = np.zeros((Nt, N))

# Simulasi random walk 2D
for i in range(1, Nt):
    x[i] = x[i-1] + np.random.randn(N)
    y[i] = y[i-1] + np.random.randn(N)

# Waktu
t = np.arange(Nt) * dt

# Hitung MSD tiap waktu
msd = np.mean(x**2 + y**2, axis=1)

# Hitung koefisien difusi dari MSD = 4Dt

a, b = np.polyfit(t, msd, 1)
D = a / 4
print("Koefisien difusi D =", D)

# Plot jejak partikel
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
for j in range(N):
    plt.plot(x[:, j], y[:, j], linewidth=0.5)
plt.title("Jejak 100 Partikel (Random Walk 2D)")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")

# Plot MSD terhadap waktu
plt.subplot(1, 2, 2)
plt.plot(t, msd, label="MSD simulasi")
plt.plot(t, a*t + b, "r--", label="Fit linear, D = " + str(round(D, 3)))
plt.title("Mean Square Displacement")
plt.xlabel("Waktu")
plt.ylabel("MSD")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
