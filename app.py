import streamlit as st
import base64

# 🔧 Fungsi background
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    background = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(background, unsafe_allow_html=True)

# 🔧 Pasang background
set_background("background.jpg")

# ========================== TAMPILAN ==========================
st.markdown("<h1 style='text-align:center; color:#ffffff;'>💧 Indeks Pencemaran Air</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#eeeeee;'>Cintai Bumi, Lindungi Air Kita 🌍</h4>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ✅ Panel edukasi
with st.expander("📘 Apa itu Indeks Pencemaran Air?"):
    st.markdown("""
        Indeks Pencemaran Air digunakan untuk mengetahui sejauh mana kualitas air telah tercemar oleh berbagai parameter 
        seperti pH, suhu, BOD, COD, TSS, dan mikroorganisme. Website ini membantu menilai kondisi air berdasarkan parameter yang Anda masukkan.
    """)

st.markdown("<br>", unsafe_allow_html=True)

# ========================== FORM INPUT ==========================
with st.form("form_input"):
    col1, col2 = st.columns(2)

    with col1:
        ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1, format="%.2f")
        suhu = st.number_input("Suhu (°C)", step=0.1, format="%.2f")
        do = st.number_input("Oksigen Terlarut / DO (mg/L)", step=0.1, format="%.2f")
        bod = st.number_input("BOD (mg/L)", step=0.1, format="%.2f")

    with col2:
        cod = st.number_input("COD (mg/L)", step=0.1, format="%.2f")
        tss = st.number_input("TSS (mg/L)", step=0.1, format="%.2f")
        logam_berat = st.number_input("Logam Berat (mg/L)", step=0.01, format="%.2f")
        ecoli = st.number_input("E-Coli (Jumlah/100mL)", step=1.0, format="%.0f")

    submitted = st.form_submit_button("🔍 Analisis Sekarang")

# ========================== OUTPUT ==========================
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

    nilai_terisi = [v for v in data.values() if v is not None]

    if nilai_terisi:
        indeks = sum(nilai_terisi) / len(nilai_terisi)
        if indeks < 20:
            status, color = "💚 Baik", "#3CB371"
        elif indeks < 50:
            status, color = "🟡 Sedang", "#F4D03F"
        elif indeks < 80:
            status, color = "🟠 Tercemar", "#E67E22"
        else:
            status, color = "🔴 Sangat Tercemar", "#E74C3C"

        st.markdown(f"""
            <div style="padding:20px; background-color:{color}; border-radius:10px;">
                <h3 style="color:white;">Hasil Indeks: {indeks:.2f}</h3>
                <h4 style="color:white;">Status: {status}</h4>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Masukkan minimal satu parameter untuk analisis.")

# ========================== FOOTER ==========================
st.markdown("""
<hr style="border:0.5px solid white">
<p style="text-align:center; color:lightgrey;">
    © 2025 | Dibuat dengan ❤️ oleh Kamu yang peduli lingkungan
</p>
""", unsafe_allow_html=True)
