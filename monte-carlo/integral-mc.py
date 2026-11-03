import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Definisikan fungsi yang ingin diintegralkan, misalnya f(x) = x^2
    return x**2

def monte_carlo_integral(f, a, b, N):
    # Cari nilai maksimum fungsi pada selang [a, b] untuk menentukan tinggi kotak
    # Kita gunakan sampel linear untuk mengestimasi nilai maksimum f(x)
    x_vals = np.linspace(a, b, 1000)
    y_vals = f(x_vals)
    y_max = np.max(y_vals)
    y_min = min(0, np.min(y_vals)) # Mengakomodasi jika ada nilai negatif

    # Generate N titik acak
    x_rand = np.random.uniform(a, b, N)
    y_rand = np.random.uniform(y_min, y_max, N)

    # Evaluasi fungsi pada titik x_rand
    f_val = f(x_rand)

    # Tentukan titik mana saja yang berada di bawah kurva
    # Untuk fungsi positif:
    under_curve = (y_rand >= 0) & (y_rand <= f_val)
    # Untuk fungsi negatif:
    above_curve = (y_rand < 0) & (y_rand >= f_val)

    inside = under_curve | above_curve

    # Hitung luas area kotak
    area_box = (b - a) * (y_max - y_min)

    # Estimasi integral (luas di bawah kurva)
    # Titik di atas kurva negatif bernilai mengurangi hasil integral
    integral_est = area_box * (np.sum(under_curve) - np.sum(above_curve)) / N

    # Visualisasi
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, color='black', linewidth=2, label='f(x) = x^2')
    plt.scatter(x_rand[inside], y_rand[inside], color='blue', s=4, label='Inside')
    plt.scatter(x_rand[~inside], y_rand[~inside], color='red', s=4, label='Outside')
    plt.axhline(0, color='black', linestyle='--')
    plt.legend()
    plt.title(f'Monte Carlo Integration (N = {N})\nEstimated Value = {integral_est:.4f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    return integral_est

# Parameter
a = 0
b = 2
N = 100

hasil = monte_carlo_integral(f, a, b, N)
print(f"Hasil Estimasi Integral: {hasil}")
# Nilai eksak integral x^2 dari 0 ke 2 adalah 8/3 = 2.6667
print(f"Nilai Eksak: {8/3:.4f}")