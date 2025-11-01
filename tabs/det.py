import streamlit as st
from utils.mat_ops import parse_matrix, determinant

def show():
    st.subheader("Determinant Calculator")
    text_matrix = st.text_area("Matrix", "1,2\n3,4", key="det_matrix")
    A = parse_matrix(text_matrix)

    if st.button("Calculate Determinant", key="det_button"):
        if A is None:
            st.error("❌ Could not parse the matrix.")
        else:
            det = determinant(A)
            if det is None:
                st.warning("⚠️ Determinant only defined for square matrices.")
            else:
                st.subheader("✅ Determinant")
                st.latex(f"\\det(A) = {det:.2f}")
