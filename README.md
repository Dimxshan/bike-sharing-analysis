# Proyek Analisis Data: Bike Sharing Dataset 🚲

Submission proyek akhir kelas **Belajar Analisis Data dengan Python** dari Dicoding Indonesia.

## 👤 Identitas Pengembang
- **Nama:** Dimas Raditya Putra Handoko
- **Email:** dimxshan916@gmail.com
- **ID Dicoding:** ds012b6y0460
- **Tautan Dashboard:** [Streamlit Community Cloud](https://bike-sharing-analysis-dimas.streamlit.app)

## 📌 Ringkasan Proyek
Proyek ini melakukan analisis data eksploratori dan visualisasi terhadap **Capital Bikeshare Dataset (2011–2012)** untuk menjawab:
1. **Pengaruh Musim & Cuaca:** Menilai dampak perubahan musim (`season`) dan kondisi cuaca (`weathersit`) terhadap rata-rata serta total penyewaan sepeda harian (`cnt`).
2. **Karakteristik Pengguna & Jam Sibuk:** Mengidentifikasi perbedaan pola jam sibuk (*peak hours*, `hr`) antara pengguna komuter (*registered*) dan pengguna rekreasi (*casual*) pada hari kerja vs hari libur.
3. **Pertumbuhan Tahunan (YoY):** Menganalisis lonjakan volume sewa antar-tahun (2011 vs 2012) di setiap bulan serta kontribusi masing-masing segmen pengguna.
4. **Analisis Lanjutan (Manual Clustering via Binning):** Mengelompokkan jam operasional ke dalam 4 klaster waktu aktivitas (*Morning Commute*, *Midday Activity*, *Evening Commute*, *Night/Off-Peak*) dan mengelompokkan temperatur ke dalam 3 klaster kenyamanan (*Cold*, *Comfortable*, *Warm/Hot*).

## 📁 Struktur Direktori Proyek
| Nama Berkas / Folder | Deskripsi |
| :--- | :--- |
| `dashboard/dashboard.py` | Skrip utama aplikasi dashboard interaktif berbasis Streamlit |
| `dashboard/main_data.csv` | Dataset bersih tingkat jam yang telah melalui tahap *Cleaning* & *Feature Engineering* |
| `data/day.csv` | Dataset mentah agregasi penyewaan harian (731 baris) |
| `data/hour.csv` | Dataset mentah agregasi penyewaan per jam (17.379 baris) |
| `data/Readme.txt` | Dokumentasi asli dan lisensi dataset dari peneliti |
| `notebook.ipynb` | Jupyter Notebook berisi tahapan lengkap *Data Wrangling*, *EDA*, *Visualization*, dan *Conclusion* |
| `README.md` | Dokumentasi proyek dan panduan instalasi |
| `requirements.txt` | Daftar pustaka Python untuk environment lokal dan deployment Streamlit Cloud |
| `url.txt` | Tautan aplikasi dashboard publik di Streamlit Community Cloud |

## 💻 Panduan Menjalankan Dashboard Secara Lokal
1. **Instalasi Dependensi:**
   ````bash
   python -m pip install -r requirements.txt