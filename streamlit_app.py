import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- KONFIGURASI AI ---
# MASUKKAN API KEY ANDA DI SINI
# Ganti baris 7-8 yang lama dengan ini:
API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.set_page_config(page_title="PetCare AI - Mr. Bambang", page_icon="🐦")
st.title("🐾 PetCare AI: Deteksi & Perawatan")

pilihan = st.sidebar.selectbox("Pilih Menu", ["Deteksi AI", "Jadwal Perawatan"])

if pilihan == "Deteksi AI":
    st.write("### 📸 Deteksi Kesehatan via Foto")
    hewan = st.radio("Target Analisis:", ["Burung Kicau", "Kucing", "Tanaman Hias"])
    
    file_upload = st.file_uploader("Unggah Foto", type=["jpg", "jpeg", "png"])
    
    if file_upload is not None:
        image = Image.open(file_upload)
        st.image(image, caption="Foto yang diunggah", use_container_width=True)
        
        if st.button("Mulai Analisis AI"):
            with st.spinner("Sedang berpikir..."):
                # Instruksi khusus untuk AI
                prompt = f"Anda adalah pakar kesehatan {hewan}. Analisis foto ini dan berikan saran kesehatan atau identifikasi jenisnya secara singkat dan mudah dipahami dalam bahasa Indonesia."
                response = model.generate_content([prompt, image])
                st.success("Analisis Selesai!")
                st.write(response.text)

elif pilihan == "Jadwal Perawatan":
    st.write("### 📅 Catatan Harian")
    st.text_input("Nama Hewan/Tanaman:")
    st.date_input("Tanggal Perawatan:")
    st.checkbox("Pemberian Vitamin/Pupuk")
    st.button("Simpan Jadwal")
