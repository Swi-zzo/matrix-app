import streamlit as st
from tabs import mul, det

st.title("Matrix Calculator")

tab1, tab2 = st.tabs(["Multiplication", "Determinant"])

with tab1:
    mul.show()

with tab2:
    det.show()
