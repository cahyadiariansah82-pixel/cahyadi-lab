import streamlit as st
import pandas as pd

def show():
    st.header("📊 Analisis Kesalahan Pengukuran - Cahyadi Ariansah")
    st.write("Masukkan data pengukuran, pisahkan dengan koma:")

    nilai = st.text_area("Contoh: 10.1, 10.2, 10.0, 10.3", "10.1, 10.2, 10.0, 10.3")

    if nilai:
        data = [float(x) for x in nilai.split(",")]
        df = pd.DataFrame(data, columns=["Pengukuran"])
        rata2 = df["Pengukuran"].mean()
        simpangan = df["Pengukuran"].std()

        st.subheader("Hasil Perhitungan")
        st.write(f"Rata-rata: {rata2}")
        st.write(f"Simpangan baku: {simpangan}")

        st.subheader("Rumus")
        st.latex(r"\text{Rata-rata} = \frac{\Sigma x_i}{n}")
        st.latex(r"\sigma = \sqrt{\frac{\Sigma (x_i - \bar{x})^2}{n-1}}")

    st.caption("Analisis ini dibuat oleh Cahyadi Ariansah")