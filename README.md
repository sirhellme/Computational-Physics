# Computational Physics

Kumpulan implementasi metode numerik dan simulasi fisika dalam Python
untuk mata kuliah Fisika Komputasi.

## 📌 Daftar Isi

- [Tentang Project](#tentang-project)
- [Struktur Project](#struktur-project)
- [Daftar Project](#daftar-project)
- [Metode yang Digunakan](#metode-yang-digunakan)
- [Instalasi](#instalasi)
- [Cara Menjalankan](#cara-menjalankan)
- [Output Charts](#output-charts)
- [Author](#author)

---

## Tentang Project

Project ini berisi implementasi berbagai metode numerik yang
digunakan dalam pembelajaran Fisika Komputasi.

Tujuan project ini adalah memahami bagaimana konsep matematika
dan fisika dapat diterapkan menggunakan pemrograman Python.

## Struktur Project

```text
computational-physics/
├── heat-equation/
│   ├── heat-rod.py
│   ├── heat-rod-centered.py
│   └── references.py
├── monte-carlo/
│   ├── integral-mc.py
│   ├── pi-estimate.py
│   ├── random-walk.py
│   ├── random-walk-2D.py
│   └── random-walk-project.py
├── oscillation/
│   ├── simple-oscillation-harmonic.py
│   └── damped-oscillation.py
├── people-growth/
│   ├── pg-r-constant.py
│   └── pg-r-non-constant.py
└── media/
    ├── heat-equation/
    ├── monte-carlo/
    ├── oscillation/
    └── population-growth/
```

## Daftar Project

| Project | Deskripsi | File |
| --- | --- | --- |
| **Heat Equation** | Simulasi difusi panas 1D pada kawat aluminium alloy menggunakan skema FTCS eksplisit, dengan variasi waktu simulasi, time step, dan kondisi awal panas terpusat di tengah. | `heat-equation/` |
| **Monte Carlo** | Estimasi nilai π, integrasi numerik dengan metode Monte Carlo, dan simulasi random walk 2D beserta perhitungan koefisien difusi dari MSD. | `monte-carlo/` |
| **Oscillation** | Simulasi osilasi harmonik sederhana dan osilasi teredam menggunakan metode beda hingga. | `oscillation/` |
| **People Growth** | Model pertumbuhan populasi eksponensial dengan laju konstan dan model logistik dengan ancaman serta skenario bencana. | `people-growth/` |

## Metode yang Digunakan

Beberapa metode yang terdapat dalam repository ini:

- Metode beda hingga (finite difference) untuk persamaan panas dan osilasi
- Skema FTCS (Forward Time Centered Space) eksplisit
- Kondisi batas Dirichlet dan Neumann (adiabatik)
- Integrasi Monte Carlo dan estimasi π
- Simulasi random walk 2D dan analisis Mean Square Displacement (MSD)
- Model pertumbuhan populasi eksponensial dan logistik

## Instalasi

Clone Repository:

```bash
git clone https://github.com/username/Computational-Physics.git
cd Computational-Physics
```

Install Dependencies:

```bash
pip install numpy matplotlib
```

`pi-estimate.py` menggunakan backend `QtAgg`, sehingga PyQt6 mungkin diperlukan
jika ingin menampilkan grafiknya secara interaktif:

```bash
pip install PyQt6
```

## Cara Menjalankan

Jalankan salah satu script, misalnya:

```bash
python heat-equation/heat-rod.py
python monte-carlo/pi-estimate.py
python oscillation/damped-oscillation.py
python people-growth/pg-r-non-constant.py
```

## Output Charts

### Heat Equation

#### Variasi Waktu Simulasi

<p align="center">
  <img src="media/heat-equation/heat-equation-T-var.png" width="600">
</p>

#### Variasi Time Step

<p align="center">
  <img src="media/heat-equation/heat-equation-dt-var.png" width="600">
</p>

#### Panas Dipusatkan di Tengah Kawat

<p align="center">
  <img src="media/heat-equation/heat-rod-centered.png" width="600">
</p>

### Monte Carlo

#### Estimasi π

<p align="center">
  <img src="media/monte-carlo/pi-estimation.png" width="600">
</p>

#### Integrasi Monte Carlo

<p align="center">
  <img src="media/monte-carlo/integral-monte-carlo.png" width="600">
</p>

#### Random Walk

<p align="center">
  <img src="media/monte-carlo/random-walk-diffusion.png" width="600">
</p>

### Oscillation

#### Osilasi Harmonik Sederhana

<p align="center">
  <img src="media/oscillation/simple-harmonic-oscillation.png" width="600">
</p>

#### Osilasi Teredam

<p align="center">
  <img src="media/oscillation/damped-oscillation.png" width="600">
</p>

### People Growth

#### Pertumbuhan Populasi r Konstan

<p align="center">
  <img src="media/population-growth/population-r-constant.png" width="600">
</p>

#### Pertumbuhan Populasi r Tidak Konstan (Logistik)

<p align="center">
  <img src="media/population-growth/population-r-non-constant.png" width="600">
</p>

## Author

**Helmi Saputra Bratama**

**NIM: H1021241015**

Physics Student  
Universitas Tanjungpura  
Pontianak, Indonesia

📚 Physics | 💻 Computational Physics