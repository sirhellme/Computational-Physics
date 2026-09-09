# model osilasi harmonik sederhana
# x_i = 2*x_(i-1) - x_(i-2) - omega^2*x_(i-1)*h^2
# x_1 = x_0 + v_0*h
# v_1 = v_0 - omega^2*x_0*h

import numpy as np
import matplotlib.pyplot as plt

# parameter
x0 = 3.0 # posisi awal (m)
v0 = 0.0 # kecepatan awal (m/s)
Osq = 0.5 # omega^2 (rad/s)^2
h = 0.2 # langkah waktu (s)

# waktu
t = np.arange(0, 100, h)

# posisi awal
x1 = x0 + v0*h

# kecepatan awal
v1 = v0 - Osq*x0*h

# daftar posisi
x = [x0, x1]

for i in range(2, len(t)):
    x.append(2*x[i-1] - x[i-2] - Osq*x[i-1]*h**2)

print(len(t))
print(len(x))

plt.plot(t,x)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.show()
