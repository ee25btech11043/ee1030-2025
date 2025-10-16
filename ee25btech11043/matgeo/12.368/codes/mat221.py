import ctypes
import numpy as np

# Load the shared library
lib_matrix = ctypes.CDLL("/Users/nishidkhandagre/matgeo/venv/bin/code22.so")


# Define the argument types and return type for the C function
# Our C function `calculate_determinant` takes a pointer to a double (for the flat array)
# and returns a double.
lib_matrix.calculate_determinant.argtypes = [
    ctypes.POINTER(ctypes.c_double) # matrix_elements (flat array of 9 doubles)
]
lib_matrix.calculate_determinant.restype = ctypes.c_double

def get_determinant_from_c(k_value):
    """
    Constructs the matrix for a given k_value, flattens it,
    and calls the C function to get its determinant.
    """
    # The matrix is:
    # [ k  1  2 ]
    # [ 1 -1 -2 ]
    # [ 1  1  4 ]

    # Prepare the matrix elements as a flat array for the C function
    # Order: a11, a12, a13, a21, a22, a23, a31, a32, a33
    matrix_elements_flat = (ctypes.c_double * 9)(
        k_value, 1.0, 2.0,
        1.0, -1.0, -2.0,
        1.0, 1.0, 4.0
    )

    # Call the C function
    determinant = lib_matrix.calculate_determinant(matrix_elements_flat)
    return determinant

def solve_for_k_with_c_determinant():
    """
    Finds the value of k such that the nullity of the matrix is 1.
    This implies the determinant of the matrix is 0.
    """
    print("Solving for 'k' in the matrix problem where nullity is 1 (determinant = 0).\n")

    # The problem implies we need to find k such that the determinant is 0.
    # We derived the determinant as: det = -2k - 2

    # Option 1: Direct algebraic solution (most efficient for this problem)
    # -2k - 2 = 0
    # -2k = 2
    # k = -1
    k_solution_algebraic = -1.0
    print(f"1. Algebraic Solution: From det = -2k - 2 = 0, we find k = {k_solution_algebraic:.0f}")

    # Option 2: Using the C function to verify or approximate (if det wasn't linear)
    print("\n2. Verification using the C function for k = -1:")
    verified_determinant = get_determinant_from_c(k_solution_algebraic)
    print(f"   For k = {k_solution_algebraic:.0f}, the determinant (from C code) is: {verified_determinant:.6f}")

    if abs(verified_determinant) < 1e-9: # Check if close to zero
        print("   The determinant is approximately zero, confirming k = -1 is correct.")
    else:
        print("   The determinant is not zero. There might be an issue with calculation or assumption.")

    print(f"\nTherefore, the value of k for which the nullity of the matrix is 1 is: {k_solution_algebraic:.0f}")

    # For visual context, here's what the matrix looks like with k = -1:
    print("\n--- Visualizing the matrix with k = -1 ---")
    final_matrix_k = -1
    final_matrix = np.array([
        [final_matrix_k, 1, 2],
        [1, -1, -2],
        [1, 1, 4]
    ])
    print(final_matrix)
    print(f"Numpy's determinant for this matrix: {np.linalg.det(final_matrix):.6f}")
    print(f"Numpy's rank for this matrix: {np.linalg.matrix_rank(final_matrix)}")
    print(f"Numpy's nullity (columns - rank): {final_matrix.shape[1] - np.linalg.matrix_rank(final_matrix)}")

# Run the solver
solve_for_k_with_c_determinant()