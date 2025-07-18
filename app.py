import streamlit as st
import base64

# === Fungsi untuk mengatur background ===
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css_code = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)

# === Tambahkan CSS untuk lapisan transparan ("glass") ===
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

# === Atur gambar latar belakang ===
set_background("background.jpg")

# === Judul utama (di luar glass biar tetap polos) ===
st.markdown("<h1 style='text-align:center; color:white;'>💧 Indeks Pencemaran Air</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# === Mulai kontainer transparan ===
st.markdown("<div class='glass'>", unsafe_allow_html=True)

# === Penjelasan & Parameter ===
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
    <li><b>pH</b>: Keseimbangan asam-basa air. 💡 Baku mutu: 6.5 – 8.5</li>
    <li><b>Suhu</b>: Mempengaruhi kelarutan oksigen. 💡 Baku mutu: Maks. naik 3°C dari suhu alami</li>
    <li><b>DO</b>: Oksigen terlarut, dibutuhkan biota air. 💡 Baku mutu: > 5 mg/L</li>
    <li><b>BOD</b>: Kebutuhan oksigen mikroorganisme. 💡 Baku mutu: < 3 mg/L</li>
    <li><b>COD</b>: Jumlah oksigen untuk oksidasi bahan organik/anorganik. 💡 Baku mutu: < 10 mg/L</li>
    <li><b>TSS</b>: Padatan tersuspensi. 💡 Baku mutu: < 50 mg/L</li>
    <li><b>Logam Berat</b>: (Pb, Hg, Cr, Cd) 💡 Contoh batas: Pb < 0.03 mg/L, Hg < 0.002 mg/L, Cr⁶⁺ < 0.05 mg/L</li>
    <li><b>E. coli</b>: Bakteri indikator pencemaran tinja.  
        <br>💡 Baku mutu: 0 JML/100 mL  
        <br><i>Jumlah tinggi bisa sebabkan diare dan infeksi lainnya</i>
    </li>
</ul>
""", unsafe_allow_html=True)

# === Form input ===
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
        logam = st.number_input("Logam Berat (mg/L)", step=0.01, format="%.2f")
        ecoli = st.number_input("E-Coli (Jumlah/100 mL)", step=1.0, format="%.0f")

    submitted = st.form_submit_button("🔍 Analisis Sekarang")

# === Hasil analisis indeks pencemaran ===
if submitted:
    values = [
        ph if ph else None,
        suhu if suhu else None,
        do if do else None,
        bod if bod else None,
        cod if cod else None,
        tss if tss else None,
        logam if logam else None,
        ecoli if ecoli else None
    ]
    nilai_terisi = [v for v in values if v is not None and v != 0]

    if nilai_terisi:
        indeks = sum(nilai_terisi) / len(nilai_terisi)

        if indeks < 20:
            status, color = "💚 Baik", "#2ecc71"
        elif indeks < 50:
            status, color = "🟡 Sedang", "#f1c40f"
        elif indeks < 80:
            status, color = "🟠 Tercemar", "#e67e22"
        else:
            status, color = "🔴 Sangat Tercemar", "#e74c3c"

        st.markdown(f"""
            <div style="padding:20px; background-color:{color}; border-radius:10px;">
                <h4 style="color:white;">Indeks Pencemaran: {indeks:.2f}</h4>
                <h5 style="color:white;">Status Mutu Air: {status}</h5>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Harap isi minimal satu parameter untuk melakukan analisis.")

# === Tutup lapisan transparan ===
st.markdown("</div>", unsafe_allow_html=True)

# === Footer ===
st.markdown("""
<hr style="border:0.5px solid white">
<p style="text-align:center; color:lightgrey;">
    © 2025 | Aplikasi Indeks Pencemaran Air - Streamlit
</p>
""", unsafe_allow_html=True)
