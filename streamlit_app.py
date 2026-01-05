import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. KONFIGURASI KEAMANAN (MENGAMBIL DARI SECRETS)
# Pastikan GOOGLE_API_KEY sudah diisi di Settings > Secrets Streamlit Cloud
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("❌ API Key tidak ditemukan! Masukkan di menu Settings > Secrets.")
    st.stop()

# 2. PENGATURAN HALAMAN
st.set_page_config(page_title="PetCare AI - Mr. Bambang", page_icon="🐾")
st.title("🐾 PetCare AI: Deteksi & Perawatan")
st.write("Selamat datang, Mr. Bambang. Gunakan AI ini untuk menganalisis kesehatan hewan Anda.")

# 3. MENU NAVIGASI
pilihan = st.sidebar.selectbox("Pilih Menu", ["Deteksi AI", "Jadwal Perawatan"])

if pilihan == "Deteksi AI":
    st.write("### 📸 Deteksi Kesehatan via Foto")
    hewan = st.radio("Target Analisis:", ["Burung Kicau", "Kucing", "Tanaman Hias"])
    
    file_upload = st.file_uploader("Unggah Foto", type=["jpg", "jpeg", "png"])

    if file_upload is not None:
        image = Image.open(file_upload)
        st.image(image, caption="Foto yang diunggah", use_container_width=True)
        
        if st.button("Mulai Analisis AI"):
            with st.spinner("Sedang memproses..."):
                try:
                    # MENGGUNAKAN NAMA MODEL PALING STABIL UNTUK MENGHINDARI ERROR 404
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    prompt = f"Anda adalah pakar kesehatan {hewan}. Analisis foto ini dan berikan saran perawatan atau pengobatan jika hewan/tanaman terlihat sakit."
                    
                    response = model.generate_content([prompt, image])
                    st.success("✅ Analisis Selesai!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"⚠️ Terjadi kendala: {e}")
                    st.info("Saran Pakar: Pastikan file requirements.txt sudah berisi 'google-generativeai>=0.8.3'")

elif pilihan == "Jadwal Perawatan":
    st.write("### 📅 Jadwal Perawatan Rutin")
    st.info("Fitur jadwal ini sedang dalam pengembangan oleh Mr. Bambang.")
