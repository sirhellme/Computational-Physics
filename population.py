import math
import matplotlib.pyplot as plt

# Parameter Populasi (dengan nilai konstan)
N_0 = 1000  # Jumlah populasi awal
b = 0.03    # Laju kelahiran
d = 0.01    # Laju kematian

# Menghitung laju pertumbuhan populasi 
r = b - d  

# Waktu
t = 10      

# Model eksponensial untuk pertumbuhan populasi
N_t = N_0 * math.exp(r * t)

# Data untuk grafik
waktu = range(0, t + 1)
populasi = [N_0 * math.exp(r * tahun) for tahun in waktu]

# Membuat grafik pertumbuhan populasi
plt.plot(waktu, populasi, marker='o')
plt.title('Pertumbuhan Populasi Eksponensial')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Populasi')
plt.grid()
plt.show()

plt.savefig("pertumbuhan_populasi.png", dpi=300, bbox_inches="tight")  # Menyimpan grafik sebagai file PNG

print("pertumbuhan_populasi.png")

print(N_t,'Warga di tahun ke-',t)