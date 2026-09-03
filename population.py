import numpy as np
import matplotlib.pyplot as plt

#konstanta
r = 0.2
#

# timestep
h= 0.2 # dalam bulan

# waktu-> grid
t = np.arange(0,12,h)


#Nilai awal
N0 = 10
Nh = N0 + N0*r*h/2  # beda maju

# daftar N dan N 1/2
N = [N0]
Nhalf = [Nh]

for i in range(len(t)-1):
    N.append(N[i] + h*r*Nhalf[i])
    Nhalf.append(Nhalf[i] + h*r*N[i+1])

Nexact = N0*np.exp(r*t)

#perhitungan error:
error = np.sqrt(np.mean(np.square(Nexact-N)))
print("Error = ", error)

plt.plot(t,N, label='FD')
plt.plot(t,Nexact, label = 'Exact')
plt.legend()
plt.xlim([0,12])
plt.ylim([0,25])
plt.xlabel('Time (months)')
plt.ylabel('Population')
plt.show()