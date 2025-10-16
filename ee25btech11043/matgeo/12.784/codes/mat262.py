import numpy as np

def solve_matrix_problem_pure_python():
    """
    Solves the given matrix problem using pure Python and NumPy.
    Calculates a11 + a21 + a31 + m.
    """

    # 1. Analyze the given information to find eigenvalues and eigenvectors
    # A * v1 = 2 * v1
    v1 = np.array([1, 2, 1])
    lambda1 = 2

    # A * v2 = 2 * v2
    v2 = np.array([0, 1, 1])
    lambda2 = 2

    # A * v3 = 4 * v3
    v3 = np.array([-1, 1, 0])
    lambda3 = 4

    print("--- Problem Analysis ---")
    print(f"Eigenvector v1: {v1}, Eigenvalue: {lambda1}")
    print(f"Eigenvector v2: {v2}, Eigenvalue: {lambda2}")
    print(f"Eigenvector v3: {v3}, Eigenvalue: {lambda3}")

    # Check for linear independence of eigenvectors
    # Transpose to make eigenvectors columns for matrix P
    P_check = np.array([v1, v2, v3]).T
    det_P = np.linalg.det(P_check)
    print(f"Determinant of eigenvector matrix P: {det_P:.2f}")
    if np.isclose(det_P, 0):
        print("Warning: Eigenvectors are linearly dependent. Matrix might not be diagonalizable.")
    else:
        print("Eigenvectors are linearly independent, so matrix A is diagonalizable.")

    # 2. Determine the degree of the minimal polynomial (m)
    # The distinct eigenvalues are 2 and 4.
    # For a diagonalizable matrix, the minimal polynomial is (x - distinct_lambda_1)(x - distinct_lambda_2)...
    distinct_eigenvalues = {lambda1, lambda2, lambda3} # Set automatically handles uniqueness
    m = len(distinct_eigenvalues) # The degree is the count of distinct eigenvalues
    print(f"\nDistinct Eigenvalues: {distinct_eigenvalues}")
    print(f"Degree of the minimal polynomial (m): {m}")

    # 3. Find the first column of matrix A (a11, a21, a31)
    # This is equivalent to finding A * e1, where e1 = [1, 0, 0]^T.

    # First, express e1 as a linear combination of the eigenvectors:
    # e1 = c1 * v1 + c2 * v2 + c3 * v3
    # In matrix form: P * [c1, c2, c3]^T = e1
    # So, [c1, c2, c3]^T = P_inv * e1

    P_matrix = np.array([v1, v2, v3]).T # Matrix P where columns are eigenvectors
    e1_vector = np.array([1, 0, 0])

    # Calculate P_inverse
    P_inverse = np.linalg.inv(P_matrix)
    print(f"\nMatrix P (eigenvectors as columns):\n{P_matrix}")
    print(f"Inverse of P:\n{P_inverse}")

    # Calculate the coefficients [c1, c2, c3]^T
    c_coefficients = np.dot(P_inverse, e1_vector)
    c1, c2, c3 = c_coefficients
    print(f"Coefficients (c1, c2, c3): c1={c1:.4f}, c2={c2:.4f}, c3={c3:.4f}")

    # Now calculate A * e1 using the property A*v = lambda*v
    # A * e1 = c1*(A*v1) + c2*(A*v2) + c3*(A*v3)
    # A * e1 = c1*(lambda1*v1) + c2*(lambda2*v2) + c3*(lambda3*v3)

    first_column_of_A = (c1 * lambda1 * v1) + \
                        (c2 * lambda2 * v2) + \
                        (c3 * lambda3 * v3)

    a11 = first_column_of_A[0]
    a21 = first_column_of_A[1]
    a31 = first_column_of_A[2]

    print(f"\nCalculated first column of A (a11, a21, a31): {first_column_of_A}")
    print(f"a11: {a11:.4f}")
    print(f"a21: {a21:.4f}")
    print(f"a31: {a31:.4f}")

    # 4. Calculate the final sum: a11 + a21 + a31 + m
    final_sum = a11 + a21 + a31 + m

    print(f"\n--- Final Result ---")
    print(f"a11 + a21 + a31 + m = {final_sum:.2f}")
    return final_sum

if __name__ == "__main__":
    solve_matrix_problem_pure_python()