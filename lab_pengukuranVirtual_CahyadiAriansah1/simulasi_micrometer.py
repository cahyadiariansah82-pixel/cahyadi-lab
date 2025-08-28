import streamlit as st

def show():
    st.header("⚙️ Simulasi Micometer - Cahyadi Ariansah")
    st.write("Masukkan pembacaan skala utama dan skala nonius:")

    skala_utama = st.number_input("Skala Utama (mm)", 0.0, 25.0, 10.0, 0.01)
    nonius = st.number_input("Skala Nonius (mm)", 0.0, 0.49, 0.0, 0.01)

    hasil = skala_utama + nonius
    ketelitian = 0.01

    st.latex(r"\text{Hasil pengukuran} = \text{skala utama} + \text{skala nonius}")
    st.success(f"Hasil: {hasil:.2f} ± {ketelitian} mm")

    st.caption("Simulasi ini dibuat oleh Cahyadi Ariansah")