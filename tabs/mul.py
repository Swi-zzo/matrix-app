import streamlit as st
from utils.mat_ops import parse_matrix, matrix_to_latex, multiply_matrices

def show():
    st.subheader("Matrix Multiplication")
    text_A = st.text_area("Matrix A", "1,2\n3,4", key="A_mul")
    text_B = st.text_area("Matrix B", "5,6\n7,8", key="B_mul")

    A = parse_matrix(text_A)
    B = parse_matrix(text_B)

    if st.button("Multiply Matrices", key="multiply_button"):
        if A is None or B is None:
            st.error("❌ Could not parse matrices.")
        elif A.shape[1] != B.shape[0]:
            st.warning("⚠️ Columns of A must equal rows of B.")
        else:
            result = multiply_matrices(A, B)
            st.subheader("✅ Result Matrix")
            st.latex(matrix_to_latex(result))
