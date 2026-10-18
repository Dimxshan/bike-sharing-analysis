# Proyek Analisis Data: Bike Sharing Dataset

Submission proyek akhir kelas **Belajar Analisis Data dengan Python** dari Dicoding Indonesia.

## Identitas Pengembang
- **Nama:** Dimas Raditya Putra Handoko
- **Email:** dimxshan916@gmail.com
- **ID Dicoding:** ds012b6y0460

## Ringkasan Proyek
Proyek ini mengeksplorasi dan memvisualisasikan **Capital Bikeshare Dataset (2011–2012)** untuk menjawab tiga pertanyaan bisnis utama serta menerapkan analisis lanjutan tanpa *Machine Learning*:
1. **Pengaruh Musim & Kondisi Cuaca:** Mengukur dampak perubahan musim (`season`) dan cuaca (`weathersit`) terhadap rata-rata serta total penyewaan sepeda harian (`cnt`).
2. **Perilaku Jam Operasional Segmen Pengguna:** Membandingkan pola jam sibuk (*peak hours*, `hr`) antara pengguna terdaftar (`registered`) dan pengguna kasual (`casual`) pada hari kerja (`workingday = 1`) vs akhir pekan/libur (`workingday = 0`).
3. **Pertumbuhan Tahunan (YoY) & Kontribusi Segmen:** Menghitung persentase pertumbuhan penyewaan sepeda bulanan dari tahun 2011 ke 2012 serta rasio kontribusi masing-masing segmen pengguna.
4. **Analisis Lanjutan (Manual Clustering via Binning):** Mengelompokkan jam operasional ke dalam 4 klaster waktu aktivitas (*Morning Commute*, *Midday Activity*, *Evening Commute*, *Night/Off-Peak*) dan mengelompokkan suhu aktual ke dalam 3 klaster kenyamanan (*Cold*, *Comfortable*, *Warm/Hot*).

## Struktur Direktori Proyek
| Nama Berkas / Folder | Deskripsi |
| :--- | :--- |
| `dashboard/dashboard.py` | Skrip utama aplikasi dashboard interaktif berbasis Streamlit |
| `dashboard/main_data.csv` | Dataset bersih tingkat jam yang telah melalui tahap *Data Wrangling* & *Clustering* |
| `data/day.csv` | Dataset mentah agregasi penyewaan harian (731 baris) |
| `data/hour.csv` | Dataset mentah agregasi penyewaan per jam (17.379 baris) |
| `notebook.ipynb` | Jupyter Notebook berisi tahapan lengkap *Data Wrangling*, *EDA*, *Visualization*, dan *Conclusion* |
| `requirements.txt` | Daftar pustaka Python untuk instalasi lokal dan deployment Streamlit Cloud |
| `url.txt` | Tautan aplikasi dashboard publik yang telah di-deploy di Streamlit Community Cloud |

## Cara Menjalankan Dashboard Secara Lokal

### 1. Persiapan Environment & Instalasi Dependensi
Pastikan terminal berada di direktori utama proyek (`ASAH`), lalu jalankan perintah berikut:

```bash
python -m pip install -r requirements.txt
```

### 2. Menjalankan Aplikasi Streamlit
Gunakan perintah `python -m streamlit` agar tidak terkendala konfigurasi `PATH` di Windows:

```bash
python -m streamlit run dashboard/dashboard.py
```

Aplikasi akan otomatis terbuka di browser pada alamat `http://localhost:8501`.
