import streamlit as st
import base64
import pandas as pd

# Fungsi untuk mengatur gambar latar belakang
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    background = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(background, unsafe_allow_html=True)

# Atur gambar latar
set_background("background.jpg")  # Ganti nama sesuai gambar Anda

# Judul dan deskripsi
st.markdown("<h1 style='color:white;'>Indeks Pencemaran Air</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:white;'>Masukkan parameter kualitas air yang tersedia di bawah ini:</p>", unsafe_allow_html=True)

# Form input parameter
with st.form("form_input"):
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1, format="%.2f")
    suhu = st.number_input("Suhu (°C)", step=0.1, format="%.2f")
    do = st.number_input("Oksigen Terlarut / DO (mg/L)", step=0.1, format="%.2f")
    bod = st.number_input("BOD (mg/L)", step=0.1, format="%.2f")
    cod = st.number_input("COD (mg/L)", step=0.1, format="%.2f")
    tss = st.number_input("TSS (mg/L)", step=0.1, format="%.2f")
    logam_berat = st.number_input("Logam Berat (mg/L)", step=0.01, format="%.2f")
    ecoli = st.number_input("E-Coli (JML/100mL)", step=1.0, format="%.0f")

    submitted = st.form_submit_button("Hitung Indeks Pencemaran")

if submitted:
    data = {
        "pH": ph if ph != 0.0 else None,
        "Suhu": suhu if suhu != 0.0 else None,
        "DO": do if do != 0.0 else None,
        "BOD": bod if bod != 0.0 else None,
        "COD": cod if cod != 0.0 else None,
        "TSS": tss if tss != 0.0 else None,
        "Logam Berat": logam_berat if logam_berat != 0.0 else None,
        "E-Coli": ecoli if ecoli != 0.0 else None,
    }

    # Filter nilai yang diisi
    nilai_terisi = [v for v in data.values() if v is not None]
    
    if nilai_terisi:
        # Perhitungan sederhana: rata-rata nilai terisi
        indeks = sum(nilai_terisi) / len(nilai_terisi)
        status = ""
        if indeks < 20:
            status = "Baik"
        elif indeks < 50:
            status = "Sedang"
        elif indeks < 80:
            status = "Tercemar"
        else:
            status = "Sangat Tercemar"

        st.markdown(f"<h3 style='color:white;'>Hasil Indeks Pencemaran: {indeks:.2f} ({status})</h3>", unsafe_allow_html=True)
    else:
        st.warning("Silakan isi minimal satu parameter untuk menghitung indeks.")
1
