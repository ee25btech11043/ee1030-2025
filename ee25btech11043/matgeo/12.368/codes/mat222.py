import numpy as np

def calculate_determinant_pure_python(k_val):
    """
    Calculates the determinant of the given 3x3 matrix using NumPy.
    The matrix structure is:
    [ k  1  2 ]
    [ 1 -1 -2 ]
    [ 1  1  4 ]
    """
    matrix = np.array([
        [k_val, 1, 2],
        [1, -1, -2],
        [1, 1, 4]
    ])
    return np.linalg.det(matrix)

def solve_matrix_problem_pure_python():
    """
    For a 3x3 matrix, nullity 1 means rank is 2.
    For rank to be 2 (and not 3), the determinant must be 0.
    """
    print("Solving the matrix nullity problem using pure Python (NumPy).\n")

    # The condition for nullity = 1 in a 3x3 matrix means rank = 2.
    # This implies that the determinant of the matrix must be 0.
    # Let's derive the determinant formula in terms of k:
    # Determinant = -2k - 2
    # We need to find k such that Determinant = 0
    # k = -1

    k_solution = -1.0

    print(f"1. Manual Algebraic Derivation:")
    print(f"   The determinant of the matrix is -2k - 2.")
    print(f"   For nullity to be 1, the determinant must be 0.")
    print(f"   Setting -2k - 2 = 0 gives k = {k_solution:.0f}.\n")

    print(f"2. Verification using NumPy's determinant function:")
    # Create the matrix with the derived k value
    matrix_with_k = np.array([
        [k_solution, 1, 2],
        [1, -1, -2],
        [1, 1, 4]
    ])

    print("   Matrix with k = -1:")
    print(matrix_with_k)

    det_verified = np.linalg.det(matrix_with_k)
    print(f"   Determinant (calculated by NumPy): {det_verified:.6f}")

    if abs(det_verified) < 1e-9: # Check if determinant is close to zero
        print("   The determinant is approximately zero, confirming k = -1 is correct for rank < 3.")
    else:
        print("   Error: Determinant is not zero as expected.")

    # Also verify the rank and nullity directly with NumPy
    rank = np.linalg.matrix_rank(matrix_with_k)
    # Nullity = number of columns - rank
    nullity = matrix_with_k.shape[1] - rank

    print(f"   Rank of the matrix: {rank}")
    print(f"   Nullity of the matrix (columns - rank): {nullity}\n")

    if nullity == 1:
        print(f"Conclusion: The value of k that results in a nullity of 1 is: {k_solution:.0f}")
    else:
        print("Conclusion: The calculated k did not result in a nullity of 1.")

# Run the solver
solve_matrix_problem_pure_python()