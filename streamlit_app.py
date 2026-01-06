import streamlit as st
import google.generativeai as genai
from PIL import Image

# ===============================
# 1. KONFIGURASI API (WAJIB)
# ===============================
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("❌ GOOGLE_API_KEY tidak ditemukan di Streamlit Secrets")
    st.stop()

# ===============================
# 2. PENGATURAN HALAMAN
# ===============================
st.set_page_config(
    page_title="PetCare AI - Mr. Bambang",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PetCare AI")
st.caption("Deteksi & Rekomendasi Perawatan Berbasis AI")

# ===============================
# 3. MENU SIDEBAR
# ===============================
menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Deteksi AI", "Jadwal Perawatan"]
)

# ===============================
# 4. FITUR DETEKSI AI
# ===============================
if menu == "Deteksi AI":
    st.subheader("📸 Deteksi Kesehatan via Foto")

    hewan = st.radio(
        "Target Analisis:",
        ["Burung Kicau", "Kucing", "Tanaman Hias"]
    )

    file_upload = st.file_uploader(
        "Unggah Foto",
        type=["jpg", "jpeg", "png"]
    )

    if file_upload:
        image = Image.open(file_upload)
        st.image(image, caption="Foto yang diunggah", use_container_width=True)

        if st.button("🔍 Mulai Analisis AI"):
            with st.spinner("AI sedang menganalisis gambar..."):
                try:
                    # ===============================
                    # MODEL YANG BENAR & STABIL (VISION)
                    # ===============================
                    model = genai.GenerativeModel(
                        model_name="models/gemini-1.0-pro-vision"
                    )

                    prompt = f"""
                    Anda adalah pakar kesehatan {hewan}.
                    Analisis kondisi pada foto ini secara profesional.

                    Berikan:
                    1. Diagnosis awal (jika ada indikasi masalah)
                    2. Kemungkinan penyebab
                    3. Saran perawatan praktis
                    4. Kapan harus ke dokter/hewan/pakar

                    Gunakan bahasa yang mudah dipahami orang awam.
                    """

                    response = model.generate_content([prompt, image])

                    st.success("✅ Analisis Berhasil")
                    st.markdown(response.text)

                except Exception as e:
                    st.error("⚠️ Gagal memproses analisis AI")
                    st.code(str(e), language="text")

# ===============================
# 5. FITUR JADWAL PERAWATAN
# ===============================
elif menu == "Jadwal Perawatan":
    st.subheader("📅 Jadwal Perawatan Rutin")
    st.info("Fitur ini sedang dikembangkan oleh Mr. Bambang.")
