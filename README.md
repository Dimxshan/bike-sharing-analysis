# Bike Sharing Analytics Dashboard 🚲✨

Submission proyek akhir kelas **Belajar Analisis Data dengan Python** dari Dicoding Indonesia.

## 👤 Identitas Pengembang
- **Nama:** Dimas Raditya Putra Handoko
- **Email:** dimxshan916@gmail.com
- **ID Dicoding:** dimxshan

## 📌 Deskripsi Proyek
Proyek ini menganalisis dan memvisualisasikan data historis **Capital Bikeshare Dataset (2011–2012)** untuk mengevaluasi pengaruh faktor musim dan kondisi cuaca terhadap penyewaan sepeda, membandingkan pola jam sibuk pengguna *registered* vs *casual* pada hari kerja dan hari libur, mengukur pertumbuhan bulanan *Year-over-Year* (YoY), serta menerapkan analisis lanjutan berupa **Manual Clustering via Binning** berdasarkan waktu operasional dan kenyamanan suhu.

## 📁 Struktur Direktori Proyek
```text
submission/
├── dashboard/
│   ├── dashboard.py        # Skrip utama aplikasi dashboard Streamlit
│   └── main_data.csv       # Dataset bersih hasil Data Wrangling & Clustering
├── data/
│   ├── day.csv             # Dataset mentah agregasi harian (731 baris)
│   ├── hour.csv            # Dataset mentah agregasi per jam (17.379 baris)
│   └── Readme.txt          # Dokumentasi asli dataset
├── notebook.ipynb          # Berkas Jupyter Notebook analisis data lengkap
├── README.md               # Dokumentasi panduan setup dan eksekusi proyek
├── requirements.txt        # Daftar library Python yang dibutuhkan
└── url.txt                 # Tautan live dashboard di Streamlit Community Cloud
```

## 🛠️ Setup Environment - Anaconda
Pastikan Anaconda atau Miniconda telah terinstal di komputer Anda, lalu jalankan perintah berikut pada terminal/Anaconda Prompt:
```bash
conda create --name bike-sharing-ds python=3.11
conda activate bike-sharing-ds
pip install -r requirements.txt
```

## 💻 Setup Environment - Shell/Terminal (venv / Pipenv)
Jika Anda menggunakan terminal standar (PowerShell, Command Prompt, atau Bash), pilih salah satu metode *virtual environment* berikut:

**Opsi 1: Menggunakan `venv` (Bawaan Python)**
```bash
# Membuat virtual environment
python -m venv .venv

# Mengaktifkan virtual environment (Windows)
.venv\Scripts\activate

# Mengaktifkan virtual environment (macOS/Linux)
source .venv/bin/activate

# Menginstal library dari requirements.txt
pip install -r requirements.txt
```

**Opsi 2: Menggunakan `pipenv`**
```bash
mkdir bike_sharing_analysis
cd bike_sharing_analysis
pipenv install
pipenv shell
pip install -r requirements.txt
```

## 🚀 Run Streamlit App
Setelah *virtual environment* aktif dan seluruh library pada `requirements.txt` terinstal, jalankan perintah berikut dari direktori utama proyek (sesuai struktur folder `dashboard/dashboard.py`):
```bash
streamlit run dashboard/dashboard.py
```

Jika Anda berada di dalam sub-direktori `dashboard/`, Anda juga dapat menjalankannya dengan:
```bash
cd dashboard
streamlit run dashboard.py
```

Aplikasi dashboard akan otomatis terbuka di browser Anda pada alamat `http://localhost:8501`.
