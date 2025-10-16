import ctypes
import numpy as np

# Load the shared library
lib_code = ctypes.CDLL("/Users/nishidkhandagre/matgeo/venv/bin/code25.so")

# Define the argument types and return type for the C function
# The C function still expects a pointer to an int array for input,
# but performs calculations using doubles internally.
lib_code.calculate_rank.argtypes = [
    ctypes.POINTER(ctypes.c_int), # matrix_ptr (flattened 2D array)
    ctypes.c_int,                  # rows
    ctypes.c_int                   # cols
]
lib_code.calculate_rank.restype = ctypes.c_int

# The matrix from the image
matrix_data = [
    [1, 2, 2, 3],
    [3, 4, 2, 5],
    [5, 6, 2, 7],
    [7, 8, 2, 9]
]

rows = len(matrix_data)
cols = len(matrix_data[0])

# Flatten the matrix into a 1D list for C compatibility
flattened_matrix = [item for sublist in matrix_data for item in sublist]

# Convert the flattened list to a C-compatible array
C_int_array = ctypes.c_int * (rows * cols)
c_matrix = C_int_array(*flattened_matrix)

# Call the C function to calculate the rank
rank = lib_code.calculate_rank(c_matrix, rows, cols)

print(f"The rank of the matrix is: {rank}")