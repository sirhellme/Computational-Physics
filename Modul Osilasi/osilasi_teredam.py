# Model osilasi teredam
# mx+bx+kx=0
import numpy as np
import matplotlib.pyplot as plt

# Parameter
m = 1.0
b = 0.2
k = 0.5

h = 0.2
t = np.arange(0, 100, h)

# Kondisi awal
x0 = 3.0
v0 = 0.0

# Array
x = [x0]
v = [v0]

# Iterasi
for i in range(len(t) - 1):

    # percepatan
    a = -(b/m)*v[i] - (k/m)*x[i]

    # kecepatan baru
    v_new = v[i] + a*h

    # posisi baru
    x_new = x[i] + v_new*h

    # simpan
    v.append(v_new)
    x.append(x_new)

# Plot
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Osilasi Teredam')
plt.grid()
plt.show()