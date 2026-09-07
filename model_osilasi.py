# import numpy as np
# import matplotlib.pyplot as plt
# # omega^2
# Osq = 0.5
# #langkah
# h = 0.2
# # grid
# t = np.arange(0,100,h)
# # nilai awal
# x0 = 3.
# v0 = 0.
# # kecepatan v1
# v1 = v0 - Osq*x0*h
# # posisi x1
# x1 = x0 + v1*h

# # daftar posisi
# x = [x0,x1]

# for i in range(2, len(t)):
#   x.append(2*x[i-1] - x[i-2] - Osq*h*h*x[i-1])

# print(len(t))
# print(len(x))

# plt.plot(t,x)
# plt.xlabel('Time (s)')
# plt.ylabel('Position (m)')
# plt.show()

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