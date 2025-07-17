import streamlit as st

# 🌅 Background dari GitHub 
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/ziyausername/streamlit-air-index/main/background.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #ffffff;
    }
    .block-container {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎯 Judul dan Deskripsi
st.title("🌊 Indeks Pencemaran Air")
st.subheader("Menilai kualitas air berdasarkan parameter fisik dan kimia")

st.markdown("""
Indeks Pencemaran Air (IPA) adalah indikator komposit yang digunakan untuk menilai tingkat pencemaran suatu badan air. IPA dihitung berdasarkan beberapa parameter kualitas air, dan hasilnya dikategorikan menjadi status air: **baik, sedang, buruk, atau sangat tercemar**.

""")

st.markdown("---")

# 📋 Penjelasan Parameter
with st.expander("📘 Penjelasan Setiap Parameter"):
    st.markdown("""
- **pH**: Menunjukkan tingkat keasaman atau kebasaan air. Ideal: 6.5 – 8.5  
- **Suhu**: Berpengaruh pada kelarutan oksigen dan reaksi biologis  
- **DO (Oksigen Terlarut)**: Kunci kehidupan akuatik. Standar minimal: >4 mg/L  
- **BOD (Biological Oxygen Demand)**: Kebutuhan oksigen mikroba untuk mengurai bahan organik  
- **COD (Chemical Oxygen Demand)**: Kebutuhan oksigen kimiawi untuk oksidasi zat organik dan anorganik  
- **TSS (Total Suspended Solid)**: Padatan tersuspensi dalam air. Tinggi TSS bisa menurunkan kualitas air  
- **Logam Berat**: Toksik jika melebihi ambang batas (misalnya Hg, Pb, Cd)  
- **E-Coli**: Indikator pencemaran biologis (mikroorganisme patogen)  
    """)

# 📏 SNI Acuan
with st.expander("📌 Acuan SNI (Standar Nasional Indonesia)"):
    st.markdown("""
- **SNI 6989.65:2009** → Parameter pH  
- **SNI 6989.57:2008** → BOD  
- **SNI 6989.2:2009** → COD  
- **SNI 6989.1:2019** → Suhu  
- **SNI 6989.14:2009** → DO  
- **SNI 6989.3:2009** → TSS  
- **SNI 6989.54:2008** → Logam Berat (sesuai jenis)  
- **SNI 2897:2008** → E-Coli dan mikrobiologi air  
    """)

st.markdown("---")

# 🧮 Input Parameter
st.markdown("📝 Masukkan parameter kualitas air berikut:")

ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
temp = st.number_input("Suhu (°C)", min_value=-10.0, max_value=50.0, step=0.1)
do = st.number_input("Oksigen Terlarut (DO, mg/L)", min_value=0.0, max_value=20.0, step=0.1)
bod = st.number_input("BOD (mg/L)", min_value=0.0, max_value=100.0, step=0.1)
cod = st.number_input("COD (mg/L)", min_value=0.0, max_value=100.0, step=0.1)
tss = st.number_input("TSS (mg/L)", min_value=0.0, max_value=1000.0, step=0.1)
logam = st.number_input("Logam Berat (mg/L)", min_value=0.0, max_value=10.0, step=0.1)
ecoli = st.number_input("E-Coli (CFU/100mL)", min_value=0, max_value=10000, step=1)

# 🧠 Hitung Indeks
def calculate_index(*args):
    valid_values = [val for val in args if val != 0]
    if valid_values:
        return sum(valid_values) / len(valid_values)
    return None

index = calculate_index(ph, temp, do, bod, cod, tss, logam, ecoli)
if index is not None:
    st.success(f"💧 Indeks Pencemaran Air: {index:.2f}")
else:
    st.warning("⚠️ Isi minimal satu parameter untuk menghitung indeks.")
