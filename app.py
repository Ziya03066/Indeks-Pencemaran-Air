import streamlit as st
import base64

# === Fungsi untuk background gambar ===
def set_background(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(bg_img, unsafe_allow_html=True)

# === Fungsi utama background & CSS ===
set_background("background.jpg")

st.markdown("""
    <style>
    .glass {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 30px;
        border-radius: 15px;
        margin-top: 20px;
        color: white;
    }
    .glass h3, .glass h4, .glass ul, .glass p, .glass li {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# === Judul utama ===
st.markdown("<h1 style='text-align:center; color:white;'>💧 Indeks Pencemaran Air</h1><br>", unsafe_allow_html=True)

# === Kontainer transparan utama ===
st.markdown("<div class='glass'>", unsafe_allow_html=True)

st.markdown("""
<h3>🧠 Apa itu Indeks Pencemaran Air?</h3>
<p>Indeks Pencemaran Air (IPA) adalah indikator untuk mengetahui tingkat pencemaran suatu badan air berdasarkan parameter fisik, kimia, dan biologi. IPA digunakan untuk menentukan status mutu air: <b>Baik</b>, <b>Sedang</b>, <b>Tercemar</b>, atau <b>Sangat Tercemar</b>.</p>

<h4>📌 Referensi:</h4>
<ul>
    <li><b>PP No. 22 Tahun 2021</b> tentang Perlindungan & Pengelolaan Lingkungan</li>
    <li><b>PP No. 20 Tahun 1990</b> tentang Pengendalian Pencemaran Air</li>
    <li><b>SNI 6989 series</b> untuk pengujian kualitas air</li>
</ul>

<h3>📊 Parameter Kualitas Air & Baku Mutunya:</h3>
<ul>
    <li><b>pH (Keasaman)</b>: Mengukur keseimbangan asam-basa air. 💡 Baku mutu: 6.5 - 8.5</li>
    <li><b>Suhu</b>: Mempengaruhi kelarutan oksigen. 💡 Maks. kenaikan: 3°C dari suhu alami</li>
    <li><b>DO</b>: Oksigen terlarut yang dibutuhkan biota air. 💡 Baku mutu: > 5 mg/L</li>
    <li><b>BOD</b>: Jumlah oksigen yang dibutuhkan mikroorganisme. 💡 Baku mutu: < 3 mg/L</li>
    <li><b>COD</b>: Jumlah oksigen untuk oksidasi bahan kimia. 💡 Baku mutu: < 10 mg/L</li>
    <li><b>TSS</b>: Padatan tersuspensi seperti lumpur. 💡 Baku mutu: < 50 mg/L</li>
    <li><b>Logam Berat</b>: Seperti Pb, Hg, Cr. 💡 Contoh: Pb < 0.03 mg/L</li>
    <li><b>E. coli</b>: Indikator pencemaran tinja. 💡 Baku mutu: 0/100 mL<br>
        <i>Parameter ini menunjukkan potensi kontaminasi limbah domestik dan dapat menyebabkan penyakit seperti diare</i>
    </li>
</ul>
""", unsafe_allow_html=True)

# === Form input nilai parameter ===
with st.form("form_input"):
    col1, col2 = st.columns(2)
    with col1:
        ph = st.number_input("pH", step=0.1, format="%.2f")
        suhu = st.number_input("Suhu (°C)", step=0.1, format="%.2f")
        do = st.number_input("Oksigen Terlarut (DO)", step=0.1, format="%.2f")
        bod = st.number_input("BOD (mg/L)", step=0.1, format="%.2f")
    with col2:
        cod = st.number_input("COD (mg/L)", step=0.1, format="%.2f")
        tss = st.number_input("TSS (mg/L)", step=0.1, format="%.2f")
        logam = st.number_input("Logam Berat (mg/L)", step=0.01, format="%.2f")
        ecoli = st.number_input("E-Coli (Jumlah/100mL)", step=1.0, format="%.0f")
    submit = st.form_submit_button("🔍 Analisis Sekarang")

# === Analisis hasil ===
if submit:
    data = [
        ph if ph else None,
        suhu if suhu else None,
        do if do else None,
        bod if bod else None,
        cod if cod else None,
        tss if tss else None,
        logam if logam else None,
        ecoli if ecoli else None
    ]

    nilai_valid = [v for v in data if v is not None and v != 0]

    if nilai_valid:
        indeks = sum(nilai_valid) / len(nilai_valid)

        if indeks < 20:
            status = "💚 Baik"
            bg_color = "rgba(46, 204, 113, 0.7)"  # hijau transparan
        elif indeks < 50:
            status = "🟡 Sedang"
            bg_color = "rgba(241, 196, 15, 0.7)"
        elif indeks < 80:
            status = "🟠 Tercemar"
            bg_color = "rgba(230, 126, 34, 0.7)"
        else:
            status = "🔴 Sangat Tercemar"
            bg_color = "rgba(231, 76, 60, 0.7)"

        st.markdown(f"""
            <div style="padding:20px; background-color:{bg_color}; border-radius:12px;">
                <h4 style="color:white;">Hasil Indeks Pencemaran: {indeks:.2f}</h4>
                <h5 style="color:white;">Status: {status}</h5>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Masukkan minimal satu parameter untuk dianalisis.")

# === Tutup div transparan utama ===
st.markdown("</div>", unsafe_allow_html=True)

# === Footer ===
st.markdown("""
<hr style="border:0.5px solid white">
<p style="text-align:center; color:lightgrey;">
    © 2025 | Dibuat oleh Mahasiswa Kelompok 11 Logika dan Pemrograman Komputer 🧠
</p>
""", unsafe_allow_html=True)
