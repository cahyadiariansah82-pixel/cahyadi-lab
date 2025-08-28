import streamlit as st

import home
import teori_dan_konsep
import simulasi_jangka_sorong
import simulasi_micrometer
import kuis_angka_penting
import analisis_kesalahan

st.set_page_config(page_title="Lab Pengukuran Virtual - Cahyadi Ariansah", page_icon="⚙️",layout="wide")

# Sidebar menu
menu = st.sidebar.radio("📌 Menu Utama", [
    "🏠 Home",
    "📏 Teori dan Konsep",
    "📐 Simulasi jangka sorong",
    "📐 Simulasi micrometer",
    "🔢 Kuis angka penting",
    "📊 Analisis kesalahan"
])

if st.button("refresh!"):
    st.cache_data.clear()

# Halaman utama
if menu == "🏠 Home":
    home.show()

elif menu == "📏 Teori dan Konsep":
    teori_dan_konsep.tampil()

elif menu == "📐 Simulasi jangka sorong":
    simulasi_jangka_sorong.show()

elif menu == "📐 Simulasi micrometer":
    simulasi_micrometer.show()

elif menu == "🔢 Kuis angka penting":
    kuis_angka_penting.tampil2()

elif menu == "📊 Analisis kesalahan":
    analisis_kesalahan.show()