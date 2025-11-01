import numpy as np

def parse_matrix(text, sep=","):
    try:
        matrix = [list(map(float, row.strip().split(sep))) for row in text.strip().split("\n")]
        return np.array(matrix)
    except:
        return None

def matrix_to_latex(matrix):
    latex_str = "\\begin{bmatrix}"
    rows = [" & ".join(map(str, row)) for row in matrix]
    latex_str += " \\\\ ".join(rows)
    latex_str += "\\end{bmatrix}"
    return latex_str

def multiply_matrices(A, B):
    return np.matmul(A, B)

def determinant(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        return None
    return np.linalg.det(matrix)
