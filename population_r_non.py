# for nonconstant r
# Model logistik : r = r0(1-N/M)
# Model linier: r = r0(1/(1+N))
# Model dengan ancaman: r = r0 bla bla bla
import numpy as np
import matplotlib.pyplot as plt
# timestep
h= 0.01 # dalam bulan
r0 = 1
M = 20

# waktu
t = np.arange(0,12,h)

#Nilai awal
N0 = 10
#Nh = N0 +  N0/(1+N0)*h/2
Nh = N0 + r0*(1-N0/M)*N0*h/2

N = [N0]
Nhalf = [Nh]

for i in range(len(t)-1):
    #N.append(N[i] + h*Nhalf[i]/(1+Nhalf[i]))
    #Nhalf.append(Nhalf[i] + h*N[i+1]/(1+N[i+1]))
    N.append(N[i] + h*r0*(1-N[i]/M)*Nhalf[i])
    Nhalf.append(Nhalf[i] + h*r0*(1-Nhalf[i]/M)*N[i+1])

plt.plot(t,N, label='logistik')
plt.xlim([0,12])
plt.ylim([0,25])
plt.legend()
plt.xlabel('Time (months)')
plt.ylabel('Population')
plt.show()