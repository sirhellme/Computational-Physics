
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. PARAMETER SIMULASI
# ==========================================

N = 100              # Jumlah partikel
steps = 1000         # Jumlah langkah waktu
dt = 0.01            # Interval waktu
step_length = 1.0    # Skala perpindahan

time = np.arange(steps + 1) * dt

# ==========================================
# 2. RANDOM WALK 2D
# ==========================================

# Posisi awal seluruh partikel
x = np.zeros((N, steps + 1))
y = np.zeros((N, steps + 1))

# Bilangan acak untuk perpindahan
dx = np.random.normal(
    0, step_length, (N, steps)
)

dy = np.random.normal(
    0, step_length, (N, steps)
)

# Menghitung posisi kumulatif
x[:, 1:] = np.cumsum(dx, axis=1)
y[:, 1:] = np.cumsum(dy, axis=1)

# ==========================================
# 3. MEAN SQUARE DISPLACEMENT (MSD)
# ==========================================

# Kuadrat perpindahan setiap partikel
squared_displacement = (
    (x - x[:, [0]])**2 +
    (y - y[:, [0]])**2
)

# Rata-rata seluruh partikel
MSD = np.mean(squared_displacement, axis=0)

# ==========================================
# 4. MENGHITUNG KOEFISIEN DIFUSI
# ==========================================

# Regresi linear MSD = 4Dt
slope, intercept = np.polyfit(time, MSD, 1)

D = slope / 4

print(f"Koefisien difusi D = {D:.4f}")
print(f"Slope MSD = {slope:.4f}")
print(f"Intercept = {intercept:.4f}")

# ==========================================
# 5. VISUALISASI RANDOM WALK 2D
# ==========================================

plt.figure(figsize=(10, 7))

for i in range(N):
    plt.plot(x[i], y[i], alpha=0.5, linewidth=0.8)

plt.scatter(0, 0, color="red", label="Posisi awal", zorder=3)

plt.title("Random Walk 2D - 100 Partikel")
plt.xlabel("Posisi X")
plt.ylabel("Posisi Y")
plt.axis("equal")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

# ==========================================
# 6. VISUALISASI MSD TERHADAP WAKTU
# ==========================================

plt.figure(figsize=(10, 7))

plt.plot(time, MSD, label="MSD Simulasi")

# Garis regresi linear
plt.plot(
    time,
    slope * time + intercept,
    "--",
    label=f"Linear Fit (D = {D:.4f})"
)

plt.title("Mean Square Displacement vs Time")
plt.xlabel("Waktu")
plt.ylabel("MSD")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

plt.show()

