import streamlit as st
import base64

# === Background Gambar ===
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("kurakura.png")

# === Judul Aplikasi ===
st.markdown("<h1 style='text-align:center; color:white;'>💧 Indeks Pencemaran Air</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# === Penjelasan IPA ===
with st.expander("📘 Penjelasan Indeks Pencemaran Air & Parameter"):
    st.markdown("""
    <div style='color:white'>
    **Indeks Pencemaran Air (IPA)** digunakan untuk menilai kualitas air berdasarkan parameter fisik, kimia, dan biologi.  

    **Baku Mutu Parameter:**
    - pH: 6.5 – 8.5
    - Suhu: Max 3°C lebih tinggi dari alami
    - DO: > 5 mg/L
    - BOD: < 3 mg/L
    - COD: < 10 mg/L
    - TSS: < 50 mg/L
    - TDS: ≤ 500 mg/L
    - E-Coli: 0 JML/100 mL
    - Logam Berat: batas tergantung jenis
    </div>
    """, unsafe_allow_html=True)

# === Ambang Batas Logam Berat ===
ambang_logam = {
    "Arsen (As)": 0.01,
    "Kadmium (Cd)": 0.003,
    "Kromium (Cr)": 0.05,
    "Raksa (Hg)": 0.001,
    "Timbal (Pb)": 0.01,
    "Selenium (Se)": 0.02,
    "Antimon (Sb)": 0.02,
    "Barium (Ba)": 0.7,
    "Boron (B)": 0.5,
    "Besi (Fe)": 0.3,
    "Mangan (Mn)": 0.1,
    "Nikel (Ni)": 0.07,
    "Tembaga (Cu)": 2.0,
    "Seng (Zn)": 3.0,
    "Aluminium (Al)": 0.2
}

# === Input Parameter Air ===
with st.form("form_input"):
    col1, col2 = st.columns(2)
    with col1:
        ph = st.number_input("pH", 0.0, 14.0, step=0.1)
        suhu = st.number_input("Suhu (°C)", step=0.1)
        do = st.number_input("DO (mg/L)", step=0.1)
        bod = st.number_input("BOD (mg/L)", step=0.1)
        tds = st.number_input("TDS (mg/L)", step=1.0)
    with col2:
        cod = st.number_input("COD (mg/L)", step=0.1)
        tss = st.number_input("TSS (mg/L)", step=0.1)
        ecoli = st.number_input("E-Coli (Jumlah/100mL)", step=1.0)

    selected_logam = st.multiselect("Pilih Logam Berat (opsional)", list(ambang_logam.keys()))
    kadar_logam_input = {}
    for logam in selected_logam:
        kadar = st.number_input(f"Kadar {logam} (mg/L)", step=0.001, format="%.3f", key=logam)
        kadar_logam_input[logam] = (kadar, ambang_logam[logam])

    lanjutkan = st.form_submit_button("🔬 Lanjutkan Analisis")

# === ANALISIS DIMULAI ===
if lanjutkan:
    pelanggaran = 0
    catatan = []

    if ph < 6.5 or ph > 8.5:
        pelanggaran += 1
        catatan.append("pH di luar rentang aman (6.5–8.5)")
    if suhu > 30:
        pelanggaran += 1
        catatan.append("Suhu naik > 3°C dari alami")
    if do < 5:
        pelanggaran += 1
        catatan.append("DO < 5 mg/L")
    if bod > 3:
        pelanggaran += 1
        catatan.append("BOD > 3 mg/L")
    if cod > 10:
        pelanggaran += 1
        catatan.append("COD > 10 mg/L")
    if tss > 50:
        pelanggaran += 1
        catatan.append("TSS > 50 mg/L")
    if tds > 500:
        pelanggaran += 1
        catatan.append("TDS > 500 mg/L")
    if ecoli > 0:
        pelanggaran += 1
        catatan.append("E-Coli terdeteksi")

    for logam, (nilai, ambang) in kadar_logam_input.items():
        if nilai > ambang:
            pelanggaran += 1
            catatan.append(f"{logam} melebihi ambang batas ({nilai} > {ambang} mg/L)")

    # === Status Air
    if pelanggaran == 0:
        status, color = "💚 Baik", "rgba(46, 204, 113, 0.75)"
    elif pelanggaran <= 2:
        status, color = "🟡 Sedang", "rgba(244, 208, 63, 0.75)"
    elif pelanggaran <= 4:
        status, color = "🟠 Tercemar", "rgba(230, 126, 34, 0.75)"
    else:
        status, color = "🔴 Sangat Tercemar", "rgba(231, 76, 60, 0.75)"

    st.markdown(f"""
    <div style="padding:20px; background-color:{color}; border-radius:12px;">
        <h3 style="color:white;">Status Kualitas Air: {status}</h3>
        <ul style="color:white;">
            {''.join(f"<li>{c}</li>" for c in catatan)}
        </ul>
    </div>
    """, unsafe_allow_html=True)

# === Footer ===
st.markdown("""
<hr style="border:0.5px solid white">
<p style="text-align:center; color:lightgrey;">
    Disusun oleh Kelompok 11 Logika dan Pemrograman Komputer 
</p>
""", unsafe_allow_html=True)
