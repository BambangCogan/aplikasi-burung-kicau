import streamlit as st
import google.generativeai as genai

st.title("🛠️ Tes Koneksi AI Mr. Bambang")

# Mengambil kunci dari brankas Secrets
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    st.success("✅ API Key ditemukan di Secrets!")
else:
    st.error("❌ API Key TIDAK ditemukan di Secrets. Silakan isi di menu Settings.")
    st.stop()

if st.button("Klik untuk Tes Respons AI"):
    try:
        # Menggunakan versi -latest untuk menghindari error NotFound
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content("Halo Gemini, apakah koneksi ini berhasil?")
        
        st.balloons()
        st.write("### 🤖 Respons dari AI:")
        st.success(response.text)
        st.info("Koneksi Sempurna! Anda bisa kembali menggunakan kode utama PetCare AI.")
        
    except Exception as e:
        st.error(f"⚠️ Masih ada kendala teknis: {e}")
        st.warning("Jika errornya 'NotFound', pastikan Anda sudah menggunakan 'gemini-1.5-flash-latest'.")
