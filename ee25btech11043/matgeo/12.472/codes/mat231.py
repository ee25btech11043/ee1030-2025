import ctypes

# Load the shared library
lib_code = ctypes.CDLL("/Users/nishidkhandagre/matgeo/venv/bin/code23.so")

# Define the argument types and return type for the C function
lib_code.calculate_horizontal_force.argtypes = [
    ctypes.c_double,  # weight
    ctypes.c_double   # angle_degrees
]
lib_code.calculate_horizontal_force.restype = ctypes.c_double

# Given values from the problem
weight = 100.0  # N
angle_degrees = 30.0 # degrees

# Call the C function
force_F = lib_code.calculate_horizontal_force(weight, angle_degrees)

print(f"The magnitude of force F is (in N): {force_F:.3f}")