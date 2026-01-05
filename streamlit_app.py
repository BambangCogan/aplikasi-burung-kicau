import streamlit as st

# Tampilan Judul
st.set_page_config(page_title="PetCare AI - Mr. Bambang", page_icon="🐦")
st.title("🐾 PetCare AI: Deteksi & Perawatan")
st.subheader("Solusi Pakar untuk Burung Kicau & Kucing")

# Menu Navigasi
pilihan = st.sidebar.selectbox("Pilih Kategori", ["Beranda", "Deteksi Kesehatan", "Jadwal Perawatan"])

if pilihan == "Beranda":
    st.write("Selamat datang di aplikasi perawatan hewan Mr. Bambang.")
    st.info("Gunakan menu di samping untuk mulai mendeteksi kesehatan hewan Anda.")

elif pilihan == "Deteksi Kesehatan":
    st.write("### Unggah Foto atau Rekaman Suara")
    hewan = st.radio("Jenis Hewan:", ["Burung Kicau", "Kucing"])
    file_upload = st.file_uploader("Pilih file (Gambar/Audio)", type=["jpg", "png", "mp3", "wav"])
    
    if file_upload is not None:
        st.success("File berhasil diunggah! AI sedang menganalisis...")
        # Simulasi Logika AI
        if hewan == "Burung Kicau":
            st.warning("Hasil: Burung terdeteksi kurang jemur dan nutrisi. Disarankan beri jangkrik ekstra.")
        else:
            st.warning("Hasil: Ada gejala jamur ringan pada telinga. Gunakan salep antijamur.")

elif pilihan == "Jadwal Perawatan":
    st.write("### Kalender Perawatan")
    st.checkbox("Pemberian Vitamin (Pagi)")
    st.checkbox("Pembersihan Kandang")
    st.checkbox("Latihan Kicau (Sore)")
