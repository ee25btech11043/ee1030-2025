import ctypes
import numpy as np

# Load the shared library
lib_eigen = ctypes.CDLL("/Users/nishidkhandagre/matgeo/venv/bin/code27.so")

# Define the argument types and return type for the C function
lib_eigen.findEigenvalues.argtypes = [
    ctypes.c_double, # a
    ctypes.c_double, # b
    ctypes.c_double, # c
    ctypes.c_double, # d
    ctypes.POINTER(ctypes.c_double), # lambda1
    ctypes.POINTER(ctypes.c_double)  # lambda2
]
lib_eigen.findEigenvalues.restype = ctypes.c_int # Returns 0 for real, -1 for complex

# Given target eigenvalues
target_eigenvalues = {1.0, 6.0}

matrices = {
    "a": np.array([[5, -2], [-2, 2]], dtype=float),
    "b": np.array([[3, -1], [-2, 2]], dtype=float),
    "c": np.array([[3, -1], [-1, 2]], dtype=float),
    "d": np.array([[2, -1], [-1, 3]], dtype=float)
}

print("Checking matrices for eigenvalues 1 and 6:\n")

for label, mat in matrices.items():
    a, b = mat[0, 0], mat[0, 1]
    c, d = mat[1, 0], mat[1, 1]

    lambda1_result = ctypes.c_double()
    lambda2_result = ctypes.c_double()

    # Call the C function
    status = lib_eigen.findEigenvalues(
        a, b, c, d,
        ctypes.byref(lambda1_result),
        ctypes.byref(lambda2_result)
    )

    if status == 0:
        found_eigenvalues = {round(lambda1_result.value, 6), round(lambda2_result.value, 6)}
        print(f"Matrix {label}:\n{mat}")
        print(f"  Calculated eigenvalues: {found_eigenvalues}")
        if found_eigenvalues == target_eigenvalues:
            print("  This matrix has eigenvalues 1 and 6!\n")
        else:
            print("  Eigenvalues do not match 1 and 6.\n")
    else:
        print(f"Matrix {label}:\n{mat}")
        print("  Could not find real eigenvalues (they might be complex).\n")