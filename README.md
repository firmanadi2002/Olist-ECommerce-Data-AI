# End-to-End E-Commerce Data Pipeline: From Analytics to AI Inference 🚀

Proyek ini mendemonstrasikan siklus hidup data end-to-end menggunakan **Brazilian E-Commerce Public Dataset by Olist**. Proyek ini dibagi menjadi tiga peran utama dalam ekosistem data: **Data Analyst** (eksplorasi & SQL), **Data Scientist** (Segmentasi Machine Learning), dan **AI Engineer** (Simulasi API Inferensi).

---

## 📌 A. Latar Belakang Bisnis (Business Context)
Di industri *e-commerce*, mendatangkan pelanggan baru itu penting, tetapi **mempertahankan pelanggan yang sudah ada (retensi)** jauh lebih hemat biaya. Tim *Marketing* sering kali membuang-buang anggaran dengan memberikan promo diskon ke semua orang tanpa pandang bulu.

**Tujuan Proyek:**
Membangun sistem cerdas yang mampu menganalisis tren pendapatan, mengelompokkan pelanggan berdasarkan perilaku belanja (RFM), dan secara otomatis memberikan rekomendasi tindakan *marketing* (*actionable insights*) melalui sebuah API.

---

## 📊 B. Tahap 1: Data Analyst (Exploratory Data Analysis)
Pada tahap ini, saya merancang miniatur *database* relasional menggunakan **SQLite** dan menulis *query* SQL kompleks (dengan operasi `JOIN` dan agregasi) untuk mengekstrak *insight* bisnis.

### 1. Tren Pendapatan Bulanan
[MASUKKAN SCREENSHOT GRAFIK GARIS TREN PENDAPATAN DI SINI]
> **Insight Bisnis:** Terjadi lonjakan pendapatan yang sangat tajam pada bulan November 2017, yang berkorelasi kuat dengan musim belanja liburan dan *Black Friday*. Secara keseluruhan, tren pendapatan dari tahun ke tahun menunjukkan pertumbuhan yang positif.

### 2. Top 10 Kategori Produk Penyumbang Pendapatan
[MASUKKAN SCREENSHOT GRAFIK BATANG KATEGORI PRODUK DI SINI]
> **Insight Bisnis:** Kategori `beleza_saude` (Kesehatan & Kecantikan) merupakan tulang punggung pendapatan perusahaan. Ini mengindikasikan bahwa kampanye promosi masa depan harus sangat difokuskan pada produk *skincare* dan kosmetik untuk memaksimalkan ROI (Return on Investment).

---

## 🧠 C. Tahap 2: Data Scientist (RFM & Machine Learning)
Mengetahui produk yang laris saja tidak cukup; kita harus mengenali pelanggannya. Saya melakukan rekayasa fitur (*Feature Engineering*) untuk mengekstrak metrik **RFM (Recency, Frequency, Monetary)** dari riwayat transaksi, kemudian melatih model *Unsupervised Learning* menggunakan **K-Means Clustering**.

### Segmentasi Pelanggan 3D
[MASUKKAN SCREENSHOT GRAFIK 3D K-MEANS DI SINI]
[MASUKKAN SCREENSHOT TABEL KARAKTERISTIK RATA-RATA KLASTER DI SINI]

> **Hasil Segmentasi:**
> * **Cluster 2 (Sultan/VIP):** Pelanggan dengan pembelanjaan tertinggi, sering berbelanja, dan transaksi terakhirnya baru-baru ini.
> * **Cluster 0 (Churn/Berisiko):** Pelanggan yang dulu berbelanja namun sudah berbulan-bulan tidak kembali.

---

## ⚙️ D. Tahap 3: AI Engineer (API Deployment Simulation)
Agar model *Machine Learning* tidak sekadar menjadi *notebook* statis, saya mengembangkannya menjadi sebuah *Inference Pipeline* menggunakan Python. Fungsi ini mensimulasikan *backend* REST API yang mengotomatisasi keputusan *marketing* secara *real-time*.

### Cuplikan Output JSON (Simulasi API)
[MASUKKAN SCREENSHOT OUTPUT JSON DARI GOOGLE COLAB DI SINI]

> **Cara Kerja Sistem:** Ketika ID pelanggan (misal: pelanggan dari Cluster VIP) masuk ke dalam sistem, AI langsung memproses data RFM terkini, melakukan standarisasi (*scaling*), dan mengembalikan instruksi otomatis ke *frontend* (misal: *"Tampilkan Banner Khusus VIP & Berikan Akses Awal Produk Baru"*).

---

## 💡 E. Kesimpulan & Dampak Bisnis
Melalui *pipeline* terintegrasi ini, perusahaan dapat:
1. **Meningkatkan Efisiensi Anggaran Promosi:** Diskon besar (50%) kini hanya dikirimkan secara otomatis kepada pelanggan di *Cluster Churn* untuk re-aktivasi.
2. **Meningkatkan Pengalaman Pengguna (UX):** Pelanggan VIP secara otomatis disuguhi antarmuka premium di *website* tanpa intervensi manual dari tim *Marketing*.
3. **Memonitor Kesehatan Bisnis:** Visualisasi tren yang jelas membantu manajemen mengambil keputusan strategis di waktu yang tepat.

---
**Tech Stack:** `Python` | `SQLite` | `Pandas` | `Scikit-Learn` | `Plotly`
