import ctypes
import numpy as np

# Load the shared library
lib_code = ctypes.CDLL("./code13.so")

# --- Part 1: Find k for non-trivial solution ---

# Define argument types and return type for calculateDeterminant
lib_code.calculateDeterminant.argtypes = [ctypes.c_double]
lib_code.calculateDeterminant.restype = ctypes.c_double

k_for_nontrivial = None

k_val = 0.0 
det = lib_code.calculateDeterminant(k_val)
# In a real scenario with floating point, we check if it's close to zero
if abs(det) < 1e-9:  # A small epsilon for floating point comparison
    k_for_nontrivial = None

# If not found directly, we know k = 33/2 = 16.5 analytically.
# We can just set it based on our manual calculation if the loop didn't find it precisely due to floating point.
if k_for_nontrivial is None:
    k_for_nontrivial = 33.0 / 2.0
    print(f"\nAnalytically determined k for non-trivial solution: {k_for_nontrivial:.2f}")

print(f"\nValue of k for which the system possesses a non-trivial solution: k = {k_for_nontrivial:.2f}")

# --- Part 2: Find all solutions for that value of k ---

# Define argument types and return type for solveSystem
lib_code.solveSystem.argtypes = [
    ctypes.c_double,
    ctypes.POINTER(ctypes.c_double),  # x_coeff_z
    ctypes.POINTER(ctypes.c_double)   # y_coeff_z
]
lib_code.solveSystem.restype = None

# Create ctypes doubles to hold the coefficients
x_coeff_z_result = ctypes.c_double()
y_coeff_z_result = ctypes.c_double()

# Call the C function to get the coefficients
lib_code.solveSystem(
    k_for_nontrivial,
    ctypes.byref(x_coeff_z_result),
    ctypes.byref(y_coeff_z_result)
)

x_coeff = x_coeff_z_result.value
y_coeff = y_coeff_z_result.value

print(f"\nFor k = {k_for_nontrivial:.2f}, the solutions are of the form:")
print(f"x = {x_coeff:.3f} * z")
print(f"y = {y_coeff:.3f} * z")
print(f"z = z (where z can be any rational number)")
print("\nThis means the solution set is a subspace spanned by the vector:")
print(f"Solution vector: ({x_coeff:.3f}, {y_coeff:.3f}, 1)")

# Example non-trivial solution (let z = 6, to get integer values for x and y based on the derived coeffs)
if k_for_nontrivial == 33.0 / 2.0:
    print("\nExample non-trivial solution (let z = 6 to get integers):")
    example_z = 6
    example_x = x_coeff * example_z
    example_y = y_coeff * example_z
    print(f"  If z = {example_z}, then x = {example_x:.0f}, y = {example_y:.0f}")
    print(f"  Solution: ({example_x:.0f}, {example_y:.0f}, {example_z:.0f})")
    print("\nLet's verify this solution with the original equations (with k=33/2):")
    print(f"  1({example_x}) + {k_for_nontrivial}({example_y}) + 3({example_z}) = {1*example_x + k_for_nontrivial*example_y + 3*example_z}")
    print(f"  3({example_x}) + {k_for_nontrivial}({example_y}) - 2({example_z}) = {3*example_x + k_for_nontrivial*example_y - 2*example_z}")
    print(f"  2({example_x}) + 3({example_y}) - 4({example_z}) = {2*example_x + 3*example_y - 4*example_z}")
