import streamlit as st
import pandas as pd
import joblib

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Prediksi Segmen Pelanggan", layout="centered")

st.title("🛍️ AI Customer Segmentation")
st.write("Masukkan metrik perilaku belanja pelanggan (RFM) untuk mengetahui segmen dan rekomendasi strategi marketing secara otomatis.")

# 2. Memuat Model (Pastikan file .pkl berada di folder yang sama)
@st.cache_resource
def load_models():
    kmeans_model = joblib.load('kmeans_clustering_model.pkl')
    scaler_model = joblib.load('rfm_scaler.pkl')
    return kmeans_model, scaler_model

kmeans, scaler = load_models()

# 3. Form Input dari Pengguna (3 Parameter Wajib)
col1, col2, col3 = st.columns(3)

with col1:
    recency = st.number_input("Recency (Hari sejak belanja terakhir)", min_value=0, value=15)
with col2:
    frequency = st.number_input("Frequency (Jumlah transaksi)", min_value=1, value=2)
with col3:
    monetary = st.number_input("Monetary (Total belanja BRL)", min_value=0.0, value=250.0)

# 4. Tombol Prediksi
if st.button("Analisis Segmen Pelanggan"):
    # Memasukkan input ke dalam DataFrame sesuai format saat latihan
    input_data = pd.DataFrame([[recency, frequency, monetary]], columns=['recency', 'frequency', 'monetary'])
    
    # Standarisasi skala
    scaled_data = scaler.transform(input_data)
    
    # Prediksi Klaster
    klaster = kmeans.predict(scaled_data)[0]
    
    # Menampilkan Hasil (Logika Bisnis)
    st.markdown("---")
    if klaster == 2:
        st.success("🌟 **Segmen: VIP / Champions**")
        st.info("💡 **Aksi Marketing:** Kirimkan akses eksklusif untuk peluncuran produk baru dan tawarkan program loyalitas premium.")
    elif klaster == 0:
        st.error("⚠️ **Segmen: Churn / Hibernating**")
        st.info("💡 **Aksi Marketing:** Kirimkan email re-aktivasi dengan voucher diskon besar (misal: 50% Off) untuk memancing mereka kembali.")
    else:
        st.warning("🤝 **Segmen: Reguler / Loyal**")
        st.info("💡 **Aksi Marketing:** Tampilkan rekomendasi produk pelengkap (Cross-selling) di halaman beranda mereka.")