import streamlit as st

def tampil(): 
    st.header("📏 Teori dan Konsep Pengukuran - Cahyadi Ariansah")

    st.subheader("1. Pengertian Pengukuran")
    st.write("proses penentuan kuantitas atau nilai numerik suatu besaran fisik (seperti panjang, massa, atau suhu) dengan cara membandingkannya terhadap besaran sejenis yang sudah ditetapkan sebagai satuan standar menggunakan alat ukur yang sesuai")

    st.subheader("2. Satuan dan Standar")
    st.write("""
    Sistem Internasional (SI) digunakan untuk menyamakan acuan satuan di seluruh dunia.
    Contoh:
    - Panjang: meter (m)
    - Massa: kilogram (kg)
    - Waktu: sekon (s)
    - suhu : kelvin (K)
    - Intensitas cahaya : candela (cd)
    - Kuat arus : Ampere (A)
    - Jumlah zat : Mol (mol)
    """)
    st.write("""
    Besaran turunan adalah besaran fisika yang diperoleh dari kombinasi, perkalian, atau pembagian beberapa besaran pokok,
    dan memiliki satuan yang merupakan gabungan dari satuan-satuan besaran pokok.
    contoh besaran turunan.
    Contoh besaran turunan :
    luas (m^2), 
    volume (m^3), 
    kecepatan (m/s), 
    massa jenis (kg/m^3),
    gaya (N).
    """)
    st.subheader("3. Angka Penting")
    st.latex(r"\text{Ketelitian} = \pm \frac{\text{Skala terkecil}}{2}")

    st.write("""
    **Aturan angka penting:**
    1. Semua angka bukan nol adalah penting.
    2. Nol di antara angka bukan nol adalah penting.
    3. Nol di awal bilangan tidak penting.
    4. Nol di akhir bilangan desimal adalah penting.
    """)

    st.subheader("4. Rumus Dasar Fisika Terkait Pengukuran")
    st.latex(r"\text{Kecepatan} \ (v) = \frac{\text{jarak} \ (s)}{\text{waktu} \ (t)}")
    st.latex(r"\text{Volume balok} = p \times l \times t")
    st.latex(r"\text{Volume silinder} = \pi r^2 t")