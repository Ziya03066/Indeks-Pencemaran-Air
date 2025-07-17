import streamlit as st
import base64
import os

# === Fungsi background dari gambar ===
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

# === CSS transparan untuk konten utama ===
st.markdown("""
    <style>
    .main-container {
        background-color: rgba(0, 0, 0, 0.55);
        padding: 25px;
        border-radius: 15px;
        color: white;
        margin-top: 20px;
    }
    .main-container h2, .main-container h3, .main-container h4,
    .main-container p, .main-container li {
        color: white !important;
    }
    .stApp h1 {
        background-color: transparent;
    }
    </style>
""", unsafe_allow_html=True)

# === Pasang background ===
set_background("turtle.jpg")

# === Judul utama (di luar lapisan transparan) ===
st.markdown("<h1 style='text-align:center; color:white;'>💧 Indeks Pencemaran Air</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# === Buka container transparan ===
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
with st.container():
    st.markdown("""
    <div class='main-container'>
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
            <li><b>pH (Keasaman)</b>  
                <ul>
                    <li>Mengukur keseimbangan asam-basa air</li>
                    <li>💡 Baku mutu: <b>6.5 - 8.5</b></li>
                </ul>
            </li>
            <li><b>Suhu</b>  
                <ul>
                    <li>Mempengaruhi kelarutan oksigen</li>
                    <li>💡 Baku mutu: Maks. kenaikan 3°C dari suhu alami</li>
                </ul>
            </li>
            <li><b>DO (Oksigen Terlarut)</b>  
                <ul>
                    <li>Dibutuhkan makhluk hidup air</li>
                    <li>💡 Baku mutu: > 5 mg/L</li>
                </ul>
            </li>
            <li><b>BOD</b>  
                <ul>
                    <li>Mengukur kebutuhan oksigen oleh mikroba</li>
                    <li>💡 Baku mutu: < 3 mg/L</li>
                </ul>
            </li>
            <li><b>COD</b>  
                <ul>
                    <li>Jumlah oksigen yang dibutuhkan untuk oksidasi bahan organik/anorganik</li>
                    <li>💡 Baku mutu: < 10 mg/L</li>
                </ul>
            </li>
            <li><b>TSS</b>  
                <ul>
                    <li>Padatan tersuspensi seperti lumpur, pasir</li>
                    <li>💡 Baku mutu: < 50 mg/L</li>
                </ul>
            </li>
            <li><b>Logam Berat</b>  
                <ul>
                    <li>Logam berbahaya (Pb, Hg, Cr, Cd)</li>
                    <li>💡 Contoh ambang batas: Pb < 0.03 mg/L, Hg < 0.002 mg/L, Cr⁶⁺ < 0.05 mg/L</li>
                </ul>
            </li>
            <li><b>E. coli</b>  
                <ul>
                    <li>Parameter E. coli mengacu pada uji keberadaan dan jumlah bakteri <i>Escherichia coli</i> dalam suatu sampel air atau makanan.</li>
                    <li>E. coli adalah bakteri indikator yang menunjukkan adanya pencemaran oleh limbah tinja, dan bisa menjadi penyebab penyakit seperti diare jika terdapat dalam jumlah tinggi.</li>
                    <li>💡 Baku mutu: <b>0 JML/100 mL</b></li>
                </ul>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# === Panel penjelasan ===
with st.expander("📘 Penjelasan Indeks Pencemaran Air & Parameter Kualitas (PP No. 22/2021, PP No. 20/1990, SNI)"):
    st.markdown("""
    ### 🧠 Apa itu Indeks Pencemaran Air?
    Indeks Pencemaran Air (IPA) adalah indikator untuk mengetahui tingkat pencemaran suatu badan air berdasarkan parameter fisik, kimia, dan biologi. IPA digunakan untuk menentukan status mutu air: **Baik**, **Sedang**, **Tercemar**, atau **Sangat Tercemar**.

    #### 📌 Referensi:
    - **PP No. 22 Tahun 2021** tentang Perlindungan & Pengelolaan Lingkungan
    - **PP No. 20 Tahun 1990** tentang Pengendalian Pencemaran Air
    - **SNI 6989 series** untuk pengujian kualitas air

    ---

    ### 📊 Parameter Kualitas Air & Baku Mutunya:

    **1. pH (Keasaman)**  
    - Mengukur keseimbangan asam-basa air  
    - 💡 Baku mutu: **6.5 - 8.5**

    **2. Suhu**  
    - Mempengaruhi kelarutan oksigen  
    - 💡 Baku mutu: Maks. kenaikan 3°C dari suhu alami

    **3. DO (Oksigen Terlarut)**  
    - Dibutuhkan makhluk hidup air  
    - 💡 Baku mutu: **> 5 mg/L**

    **4. BOD (Biochemical Oxygen Demand)**  
    - Mengukur kebutuhan oksigen oleh mikroba  
    - 💡 Baku mutu: **< 3 mg/L**

    **5. COD (Chemical Oxygen Demand)**  
    - Jumlah oksigen yang dibutuhkan untuk oksidasi bahan organik/anorganik  
    - 💡 Baku mutu: **< 10 mg/L**

    **6. TSS (Total Suspended Solid)**  
    - Padatan tersuspensi seperti lumpur, pasir  
    - 💡 Baku mutu: **< 50 mg/L**

    **7. Logam Berat (Pb, Hg, Cr, Cd)**  
    - Zat beracun berbahaya bahkan pada dosis kecil  
    - 💡 Contoh ambang batas:
        - Pb: < 0.03 mg/L  
        - Hg: < 0.002 mg/L  
        - Cr⁶⁺: < 0.05 mg/L

    **8. E-Coli**  
    - E. coli mengacu pada uji keberadaan dan jumlah bakteri *Escherichia coli* dalam suatu sampel air atau makanan.  
    - E. coli adalah bakteri indikator yang menunjukkan adanya pencemaran oleh limbah tinja, dan bisa menjadi penyebab penyakit seperti diare jika terdapat dalam jumlah tinggi.  
    - 💡 Baku mutu: **0 JML/100 mL**
    """)

# === Form Input Parameter ===
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

# === Perhitungan Indeks ===
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
            status, color = "💚 Baik", "#2ECC71"
        elif indeks < 50:
            status, color = "🟡 Sedang", "#F4D03F"
        elif indeks < 80:
            status, color = "🟠 Tercemar", "#E67E22"
        else:
            status, color = "🔴 Sangat Tercemar", "#E74C3C"

        st.markdown(f"""
            <div style="padding:20px; background-color:{color}; border-radius:10px;">
                <h3 style="color:white;">Hasil Indeks Pencemaran: {indeks:.2f}</h3>
                <h4 style="color:white;">Status: {status}</h4>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Masukkan minimal satu parameter untuk analisis.")

# === Footer ===
st.markdown("""
<hr style="border:0.5px solid white">
<p style="text-align:center; color:lightgrey;">
    © 2025 | Dibuat oleh Mahasiswa Kelompok 11 Logika dan Pemrograman Komputer 💧
</p>
""", unsafe_allow_html=True)

# === Tutup div lapisan transparan ===
st.markdown("</div>", unsafe_allow_html=True)
