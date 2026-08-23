import math
import matplotlib.pyplot as plt

# Parameter Populasi (dengan nilai konstan)
N_0 = 290125073         # Jumlah populasi indonesia pada tahun 2026
birth = 4440000     # Laju kelahiran di indonesia
death = 1800000     # Laju kematian di indonesia
t = 10                  # Periode waktu dalam tahun

# Menghitung laju pertumbuhan populasi
b = birth/N_0
d = death/N_0
r = b - d 

# Model eksponensial
def pertumbuhan_populasi(N_awal, laju, waktu):
    """
    Menghitung populasi pada waktu tertentu menggunakan model eksponensial.
    
    Rumus:
        N(t) = N_0 * e^(r * t)
    """
    return N_awal * math.exp(laju * waktu)

# Menghitung populasi pada waktu t
N_t = N_0 * math.exp(r * t)

# Data untuk grafik
waktu = list(range(0, t + 1))

populasi = [
    pertumbuhan_populasi(N_0, r, tahun) 
    for tahun in waktu]

# Membuat grafik pertumbuhan populasi
# Membuat grafik bantuan AI 
plt.figure(figsize=(10, 6))

plt.plot(
    waktu,
    populasi, 
    marker='o',
    linewidth=2.5,
    markersize=6,
    color='blue',
    label="Populasi"
)

plt.annotate(
    f"{N_0:,.0f}".replace(",", "."),
    (waktu[0], populasi[0]),
    textcoords="offset points",
    xytext=(0,10),
    ha='center'
)

plt.annotate(
    f"{N_t:,.0f}".replace(",", "."),
    (waktu[-1], populasi[-1]),
    textcoords="offset points",
    xytext=(0,10),
    ha='center'
)

plt.title(
    "Prediksi Pertumbuhan Populasi",
    fontsize=16,
    fontweight='bold'
)

plt.xlabel("Waktu (tahun)", fontsize=12)
plt.ylabel("Populasi", fontsize=12)
plt.grid(
    True,
    linestyle='--',
    alpha=0.5
)

plt.legend()
plt.tight_layout()
plt.savefig("pertumbuhan_populasi.png", dpi=300, bbox_inches="tight")  # Menyimpan grafik sebagai file PNG
plt.show()

print("pertumbuhan_populasi.png")

print(f"{N_t},Warga di tahun ke-,{t}")
