import ctypes
import numpy as np

# Load the shared library

lib_matrix = ctypes.CDLL("/Users/nishidkhandagre/matgeo/venv/bin/code26.so")

# Define the argument types and return type for the C function
# The function name has changed to reflect the simplified version
lib_matrix.solve_matrix_problem_simplified.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # result_sum
    ctypes.POINTER(ctypes.c_int)       # minimal_poly_degree
]
lib_matrix.solve_matrix_problem_simplified.restype = None

# Create ctypes variables to hold the results
result_sum = ctypes.c_double()
minimal_poly_degree = ctypes.c_int()

# Call the C function to solve the problem
lib_matrix.solve_matrix_problem_simplified(
    ctypes.byref(result_sum),
    ctypes.byref(minimal_poly_degree)
)

# Extract the values from the ctypes variables
final_sum = result_sum.value
degree_m = minimal_poly_degree.value

print(f"The degree of the minimal polynomial (m) is: {degree_m}")
print(f"The value of a11 + a21 + a31 + m is: {final_sum:.2f}")