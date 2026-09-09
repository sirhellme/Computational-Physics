# Model osilasi teredam
# mx+bx+kx=0
import numpy as np
import matplotlib.pyplot as plt

# parameter
m = 1.0  # massa (kg)
b = 0.2  # koefisien redaman (kg/s)
k = 0.5  # konstanta pegas (N/m)

osq = k / m  # frekuensi alami kuadrat (rad^2/s^2)
gamma = b / m  # koefisien redaman (1/s)

h = 0.01  # langkah waktu (s)
t = np.arange(0, 100, h)  # vektor waktu (s)

# kondisi awal
x0 = 3.0  # posisi awal (m)
v0 = 0.0  # kecepatan awal (m/s)

# mencari v1
a0 = -gamma * v0 - osq * x0  # percepatan awal (m/s^2)

v1 = v0 + a0 * h  # kecepatan pada langkah pertama (m/s)

# mencari x1
x1 = x0 + v0 * h  # posisi pada langkah pertama (m)

# daftar posisi
x = [x0, x1]

# finite difference method
for i in range(2, len(t)):
    a = -gamma * v1 - osq * x1  # percepatan (m/s^2)
    xi = x[i - 1] + v1 * h  # posisi (m)
    xim1 = x[i - 2] + v1 * h  # posisi sebelumnya (m)
    vi = (xi - xim1) / h  # kecepatan (m/s)
    
    # finite difference formula
    xbaru = 2 * xi - xim1 - gamma * vi * h**2 - osq * xi * h**2 # posisi baru (m)

    x.append(xbaru)  # menambahkan posisi baru ke daftar

# plot hasil
plt.plot(t, x)

plt.title('Osilasi Teredam')
plt.xlabel('Waktu (s)')
plt.ylabel('Posisi (m)')
plt.grid()
plt.show()