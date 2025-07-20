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

# Pasang background
set_background("kurakura.png")

# === Judul Aplikasi ===
st.markdown("<h1 style='text-align:center; color:white;'>💧 Indeks Pencemaran Air</h1>", unsafe_allow_html=True)

# === Penjelasan ===
with st.expander("📘 Penjelasan Parameter Kualitas Air"):
    st.markdown("""
    <div style='color:white'>
    <b>Indeks Pencemaran Air (IPA)</b> digunakan untuk mengetahui tingkat pencemaran air berdasarkan parameter kualitas air:
    - <b>pH</b>: 6.5 - 8.5
    - <b>Suhu</b>: Maksimal kenaikan 3°C
    - <b>DO</b>: &gt; 5 mg/L
    - <b>BOD</b>: &lt; 3 mg/L
    - <b>COD</b>: &lt; 10 mg/L
    - <b>TSS</b>: &lt; 50 mg/L
    - <b>TDS</b>: ≤ 500 mg/L
    - <b>E-Coli</b>: 0 JML/100 mL
    - <b>Logam Berat</b>: (opsional, tergantung jenis)
    </div>
    """, unsafe_allow_html=True)

# === Ambang batas logam berat ===
ambang_logam = {
    "Arsen (As)": 0.01, "Kadmium (Cd)": 0.003, "Kromium (Cr)": 0.05, "Raksa (Hg)": 0.001,
    "Timbal (Pb)": 0.01, "Selenium (Se)": 0.02, "Antimon (Sb)": 0.02, "Barium (Ba)": 0.7,
    "Boron (B)": 0.5, "Besi (Fe)": 0.3, "Mangan (Mn)": 0.1, "Nikel (Ni)": 0.07,
    "Tembaga (Cu)": 2.0, "Seng (Zn)": 3.0, "Aluminium (Al)": 0.2
}

# === Input Form ===
with st.form("form_input"):
    col1, col2 = st.columns(2)
    with col1:
        ph = st.number_input("pH", 0.0, 14.0, step=0.1)
        suhu = st.number_input("Suhu (°C)", step=0.1)
        do = st.number_input("Oksigen Terlarut / DO (mg/L)", step=0.1)
        bod = st.number_input("BOD (mg/L)", step=0.1)
        tds = st.number_input("TDS (mg/L)", step=1.0)
    with col2:
        cod = st.number_input("COD (mg/L)", step=0.1)
        tss = st.number_input("TSS (mg/L)", step=0.1)
        ecoli = st.number_input("E-Coli (Jumlah/100mL)", step=1.0)

    selected_logam = st.multiselect("Pilih Jenis Logam Berat yang Terdeteksi (Opsional)", list(ambang_logam.keys()))

    kadar_logam_input = {}
    for logam in selected_logam:
        kadar = st.number_input(f"Kadar {logam} (mg/L)", step=0.001, format="%.3f", key=logam)
        kadar_logam_input[logam] = (kadar, ambang_logam[logam])

    submitted = st.form_submit_button("Tampilkan Hasil Analisis")

# Simpan status analisis lanjut
if submitted:
    if selected_logam:
        st.markdown("### 💡 Nilai Kadar Logam Berat:")
        for logam, (nilai, ambang) in kadar_logam_input.items():
            st.markdown(f"- **{logam}**: {nilai} mg/L (Ambang batas: {ambang} mg/L)")
    
    # === Analisis Keseluruhan ===
    pelanggaran = 0
    catatan = []

    if ph < 6.5 or ph > 8.5:
        pelanggaran += 1
        catatan.append("pH di luar rentang aman (6.5 - 8.5)")
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
            catatan.append(f"{logam} melebihi ambang batas ({nilai} > {ambang})")

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
