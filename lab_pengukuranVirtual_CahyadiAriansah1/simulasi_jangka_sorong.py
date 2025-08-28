import streamlit as st

def show():
    st.header("📐 Simulasi Jangka Sorong - Cahyadi Ariansah")
    st.write("Atur panjang benda yang akan diukur:")

    panjang = st.slider("Panjang (mm)", 0.0, 150.0, 50.0, 0.1)
    ketelitian = 0.05
    st.latex(r"\text{Hasil pengukuran} = \text{nilai} \pm \text{ketelitian}")
    st.success(f"Hasil: {panjang} ± {ketelitian} mm")

    st.caption("Simulasi ini dibuat oleh Cahyadi Ariansah")