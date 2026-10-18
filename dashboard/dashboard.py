import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

# 1. Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded",
)

sns.set_theme(style="whitegrid", palette="muted")


# 2. Fungsi Memuat Data Bersih
@st.cache_data
def load_data():
    current_dir = os.path.dirname(__file__) if "__file__" in locals() else "."
    file_candidates = [
        os.path.join(current_dir, "main_data.csv"),
        os.path.join(current_dir, "dashboard", "main_data.csv"),
        "main_data.csv",
        os.path.join("dashboard", "main_data.csv"),
    ]
    for fpath in file_candidates:
        if os.path.exists(fpath):
            df = pd.read_csv(fpath)
            df["dteday"] = pd.to_datetime(df["dteday"])
            return df
    raise FileNotFoundError("Berkas main_data.csv tidak ditemukan di direktori!")


df = load_data()

# 3. Sidebar Filter Interaktif
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2972/2972185.png", width=80
)
st.sidebar.title("🚲 Filter Analisis")

# Filter Rentang Tanggal
min_date = df["dteday"].min().date()
max_date = df["dteday"].max().date()

date_range = st.sidebar.date_input(
    label="Pilih Rentang Tanggal",
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date],
)

if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

# Filter Musim
all_seasons = ["Spring", "Summer", "Fall", "Winter"]
selected_seasons = st.sidebar.multiselect(
    label="Pilih Musim (Season)",
    options=all_seasons,
    default=all_seasons,
)

# Filter Kondisi Cuaca
all_weathers = df["weather_label"].unique().tolist()
selected_weathers = st.sidebar.multiselect(
    label="Pilih Kondisi Cuaca",
    options=all_weathers,
    default=all_weathers,
)

# Filter Hari Kerja vs Libur
day_type = st.sidebar.radio(
    label="Tipe Hari",
    options=["Semua Hari", "Hari Kerja (Working Day)", "Akhir Pekan / Libur"],
)

# Terapkan Filter
filtered_df = df[
    (df["dteday"].dt.date >= start_date)
    & (df["dteday"].dt.date <= end_date)
    & (df["season_label"].isin(selected_seasons))
    & (df["weather_label"].isin(selected_weathers))
]

if day_type == "Hari Kerja (Working Day)":
    filtered_df = filtered_df[
        filtered_df["workingday_label"] == "Working Day"
    ]
elif day_type == "Akhir Pekan / Libur":
    filtered_df = filtered_df[
        filtered_df["workingday_label"] == "Weekend/Holiday"
    ]

# 4. Header & KPI Cards
st.title("🚲 Dashboard Analisis Penyewaan Sepeda (Capital Bikeshare)")
st.markdown(
    "Dashboard interaktif untuk memonitor volume penyewaan armada sepeda, perilaku pengguna komuter vs kasual, serta pengaruh musim dan cuaca."
)
st.markdown("---")

total_rentals = filtered_df["cnt"].sum()
total_registered = filtered_df["registered"].sum()
total_casual = filtered_df["casual"].sum()
avg_hourly = (
    filtered_df["cnt"].mean() if not np.isnan(filtered_df["cnt"].mean()) else 0
)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Penyewaan Sepeda", f"{total_rentals:,} unit")
with col2:
    pct_reg = (
        (total_registered / total_rentals * 100) if total_rentals > 0 else 0
    )
    st.metric("Pengguna Terdaftar", f"{total_registered:,}", f"{pct_reg:.1f}%")
with col3:
    pct_cas = (total_casual / total_rentals * 100) if total_rentals > 0 else 0
    st.metric("Pengguna Kasual", f"{total_casual:,}", f"{pct_cas:.1f}%")
with col4:
    st.metric("Rata-rata Sewa per Jam", f"{avg_hourly:.1f} unit/jam")

st.markdown("---")

# 5. Tab Visualisasi Data
tab1, tab2, tab3, tab4 = st.tabs([
    "🌤️ Pengaruh Musim & Cuaca",
    "⏰ Pola Jam Sibuk Pengguna",
    "📈 Pertumbuhan Bulanan (YoY)",
    "🔍 Analisis Lanjutan (Clustering)",
])

with tab1:
    st.subheader("Dinamika Permintaan Berdasarkan Musim dan Cuaca")
    c1, c2 = st.columns(2)

    with c1:
        fig1, ax1 = plt.subplots(figsize=(7, 4.5))
        season_mean = (
            filtered_df.groupby("season_label")["cnt"]
            .mean()
            .reindex(selected_seasons)
            .dropna()
        )
        if not season_mean.empty:
            sns.barplot(
                x=season_mean.index,
                y=season_mean.values,
                hue=season_mean.index,
                palette=["#95a5a6", "#3498db", "#e67e22", "#2ecc71"],
                legend=False,
                ax=ax1,
            )
            ax1.set_title(
                "Rata-rata Sewa per Musim", fontsize=12, fontweight="bold"
            )
            ax1.set_xlabel("Musim")
            ax1.set_ylabel("Rata-rata Unit/Hari")
            for i, v in enumerate(season_mean.values):
                ax1.text(
                    i,
                    v + (max(season_mean.values) * 0.02),
                    f"{v:,.0f}",
                    ha="center",
                    fontweight="bold",
                )
        st.pyplot(fig1)

    with c2:
        fig2, ax2 = plt.subplots(figsize=(7, 4.5))
        weather_mean = (
            filtered_df.groupby("weather_label")["cnt"]
            .mean()
            .sort_values(ascending=False)
        )
        if not weather_mean.empty:
            sns.barplot(
                x=weather_mean.index,
                y=weather_mean.values,
                hue=weather_mean.index,
                palette=["#2ecc71", "#f39c12", "#e74c3c"],
                legend=False,
                ax=ax2,
            )
            ax2.set_title(
                "Rata-rata Sewa per Kondisi Cuaca",
                fontsize=12,
                fontweight="bold",
            )
            ax2.set_xlabel("Kondisi Cuaca")
            ax2.set_ylabel("Rata-rata Unit/Hari")
            plt.xticks(rotation=15)
            for i, v in enumerate(weather_mean.values):
                ax2.text(
                    i,
                    v + (max(weather_mean.values) * 0.02),
                    f"{v:,.0f}",
                    ha="center",
                    fontweight="bold",
                )
        st.pyplot(fig2)

    st.info(
        "Insight: Permintaan sewa memuncak pada Musim Gugur (Fall) dan Musim Panas (Summer). Cuaca buruk (Light Snow/Rain) menurunkan drastis utilitas sepeda hingga lebih dari 60%."
    )

with tab2:
    st.subheader(
        "Pola Jam Sibuk Komuter vs Rekreasi (Hari Kerja vs Akhir Pekan)"
    )
    hourly_df = (
        filtered_df.groupby(["workingday_label", "hr"])[
            ["casual", "registered"]
        ]
        .mean()
        .reset_index()
    )

    fig3, axes = plt.subplots(1, 2, figsize=(15, 4.5), sharey=True)

    # Hari Kerja
    wk_df = hourly_df[hourly_df["workingday_label"] == "Working Day"]
    if not wk_df.empty:
        sns.lineplot(
            data=wk_df,
            x="hr",
            y="registered",
            ax=axes[0],
            label="Registered",
            color="#2980b9",
            linewidth=2.5,
            marker="o",
        )
        sns.lineplot(
            data=wk_df,
            x="hr",
            y="casual",
            ax=axes[0],
            label="Casual",
            color="#e74c3c",
            linewidth=2.5,
            marker="s",
        )
    axes[0].set_title(
        "Hari Kerja (Working Day)", fontsize=12, fontweight="bold"
    )
    axes[0].set_xlabel("Jam (00:00 - 23:00)")
    axes[0].set_ylabel("Rata-rata Sewa (Unit/Jam)")
    axes[0].set_xticks(range(0, 24, 2))
    axes[0].grid(True, linestyle="--", alpha=0.5)

    # Akhir Pekan
    wkd_df = hourly_df[hourly_df["workingday_label"] == "Weekend/Holiday"]
    if not wkd_df.empty:
        sns.lineplot(
            data=wkd_df,
            x="hr",
            y="registered",
            ax=axes[1],
            label="Registered",
            color="#2980b9",
            linewidth=2.5,
            marker="o",
        )
        sns.lineplot(
            data=wkd_df,
            x="hr",
            y="casual",
            ax=axes[1],
            label="Casual",
            color="#e74c3c",
            linewidth=2.5,
            marker="s",
        )
    axes[1].set_title(
        "Akhir Pekan / Hari Libur (Weekend/Holiday)",
        fontsize=12,
        fontweight="bold",
    )
    axes[1].set_xlabel("Jam (00:00 - 23:00)")
    axes[1].set_xticks(range(0, 24, 2))
    axes[1].grid(True, linestyle="--", alpha=0.5)

    st.pyplot(fig3)
    st.info(
        "Insight: Pengguna Registered mendominasi lonjakan jam berangkat kerja (08:00) dan pulang kantor (17:00–18:00). Pengguna Casual lebih aktif pada siang hingga sore akhir pekan untuk rekreasi."
    )

with tab3:
    st.subheader("Tren Volume Penyewaan Bulanan (Year-over-Year: 2011 vs 2012)")
    month_order = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    monthly_data = (
        filtered_df.groupby(["year_label", "month_label"], observed=False)[
            "cnt"
        ]
        .sum()
        .reset_index()
    )

    fig4, ax4 = plt.subplots(figsize=(13, 4.5))
    sns.barplot(
        data=monthly_data,
        x="month_label",
        y="cnt",
        hue="year_label",
        palette=["#3498db", "#2ecc71"],
        ax=ax4,
    )
    ax4.set_title(
        "Perbandingan Total Sewa Bulanan (2011 vs 2012)",
        fontsize=13,
        fontweight="bold",
    )
    ax4.set_xlabel("Bulan")
    ax4.set_ylabel("Total Penyewaan (Unit)")
    ax4.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, pos: f"{int(x*1e-3):,}k")
    )
    ax4.legend(title="Tahun")
    st.pyplot(fig4)
    st.info(
        "Insight: Tahun 2012 mencatatkan peningkatan sewa sebesar 64,88% YoY dibandingkan 2011 dengan pertumbuhan bulanan tertinggi di awal tahun (Q1)."
    )

with tab4:
    st.subheader(
        "Manual Clustering via Binning (Waktu Operasional & Kenyamanan Suhu)"
    )
    tc1, tc2 = st.columns(2)

    with tc1:
        fig5, ax5 = plt.subplots(figsize=(7, 4.5))
        if "time_cluster" in filtered_df.columns:
            time_cl_mean = (
                filtered_df.groupby("time_cluster")["cnt"]
                .mean()
                .sort_values(ascending=False)
            )
            sns.barplot(
                x=time_cl_mean.values,
                y=time_cl_mean.index,
                hue=time_cl_mean.index,
                palette="Blues_r",
                legend=False,
                ax=ax5,
            )
            ax5.set_title(
                "Rata-rata Sewa per Klaster Jam", fontsize=12, fontweight="bold"
            )
            ax5.set_xlabel("Rata-rata Unit/Jam")
            for i, v in enumerate(time_cl_mean.values):
                ax5.text(
                    v + (max(time_cl_mean.values) * 0.02),
                    i,
                    f"{v:,.1f}",
                    va="center",
                    fontweight="bold",
                )
            st.pyplot(fig5)

    with tc2:
        fig6, ax6 = plt.subplots(figsize=(7, 4.5))
        # Binning suhu langsung
        temp_bins = [0, 15, 25, 45]
        temp_labels = [
            "Cold (<15°C)",
            "Comfortable (15-25°C)",
            "Warm/Hot (>25°C)",
        ]
        filtered_df["temp_cluster"] = pd.cut(
            filtered_df["temp_c"], bins=temp_bins, labels=temp_labels
        )
        temp_cl_mean = filtered_df.groupby("temp_cluster", observed=False)[
            "cnt"
        ].mean()

        sns.barplot(
            x=temp_cl_mean.index,
            y=temp_cl_mean.values,
            hue=temp_cl_mean.index,
            palette="YlOrRd",
            legend=False,
            ax=ax6,
        )
        ax6.set_title(
            "Rata-rata Sewa per Klaster Suhu", fontsize=12, fontweight="bold"
        )
        ax6.set_ylabel("Rata-rata Unit/Hari")
        for i, v in enumerate(temp_cl_mean.values):
            ax6.text(
                i,
                v + (max(temp_cl_mean.values) * 0.02),
                f"{v:,.0f}",
                ha="center",
                fontweight="bold",
            )
        st.pyplot(fig6)

    st.info(
        "Insight: Klaster 'Evening Commute' (16:00–19:59) memiliki intensitas sewa tertinggi per jam (377,6 unit/jam). Suhu nyaman dan hangat di atas 15°C menggandakan minat pengguna dibanding hari dingin (<15°C)."
    )

# 6. Footer Penulis
st.markdown("---")
st.markdown(
    "**Author:** Dimas Raditya Putra Handoko | **Dicoding ID:** `ds012b6y0460` | **Email:** `dimxshan916@gmail.com`"
)