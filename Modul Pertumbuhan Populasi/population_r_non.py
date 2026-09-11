# for nonconstant r

# Model logistik : r = r0(1-N/M)
# Model linier   : r = r0(1/(1+N))
# Model dengan ancaman : r = r0(1-N/M) - d

import numpy as np
import matplotlib.pyplot as plt

# parameter
h= 0.01 # dalam bulan
r0 = 1 # laju pertumbuhan maksimum
M = 20 # kapasitas lingkungan
d = 0.05 # kematian akibat ancaman 

# parameter bencana
p_bencana = 0.1 # probabilitas bencana
D = 0.2 # dampak bencana (misal 20% populasi hilang)

# waktu
t = np.arange(0,12,h)

# Nilai awal
N0 = 10

# N pada half step
Nh = N0 + (r0*(1-N0/M)-d)*N0*h/2

# Inisialisasi array untuk menyimpan nilai populasi
N = [N0] 
Nhalf = [Nh]

# Loop untuk menghitung populasi pada setiap timestep
for i in range(len(t)-1):
    # laju pertumbuhan pada N[i]
    r = r0*(1-N0/M)-d

    # N(i+1)
    N.append(N[i] + h*r*Nhalf[i])

    # cek apakah terjadi bencana
    if np.random.random() < p_bencana:
        N[i+1] *= (1-D)  # populasi berkurang akibat bencana

    # laju pertumbuhan pada Nhalf[i]
    r_half = r0*(1-Nhalf[i]/M) - d

    # Nhalf(i+1)
    Nhalf.append(Nhalf[i] + h*r_half*N[i+1])

# Plotting
plt.plot(t,N, label='dengan ancaman')
plt.xlim([0,12])
plt.ylim([0,25])
plt.legend()
plt.xlabel('Time (months)')
plt.ylabel('Population')
plt.show()