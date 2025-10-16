import ctypes
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the shared library
lib_solver = ctypes.CDLL("/Users/nishidkhandagre/matgeo/venv/bin/code21.so")

# Define the argument types and return type for the C function
lib_solver.calculate_determinant_3x3.argtypes = [
    ctypes.POINTER(ctypes.c_double)
]
lib_solver.calculate_determinant_3x3.restype = ctypes.c_double

# Define the coefficient matrix for the system of equations:
# 2x1 + x2 + x3 = 0   (Plane 1)
# 0x1 + x2 - x3 = 0   (Plane 2)
# x1 + x2 + 0x3 = 0   (Plane 3)

# Coefficient matrix A:
# [2  1  1]
# [0  1 -1]
# [1  1  0]

coefficient_matrix_np = np.array([
    2.0, 1.0, 1.0,
    0.0, 1.0, -1.0,
    1.0, 1.0, 0.0
], dtype=np.float64)
matrix_reshaped = coefficient_matrix_np.reshape(3,3)

print("Coefficient Matrix:")
print(matrix_reshaped)

# Create a ctypes array from the numpy array for the C function
matrix_c = (ctypes.c_double * len(coefficient_matrix_np))(*coefficient_matrix_np)

# Call the C function to calculate the determinant
determinant = lib_solver.calculate_determinant_3x3(matrix_c)

print(f"\nCalculated Determinant: {determinant:.4f}")

# Determine the nature of the solutions based on the determinant
if abs(determinant) > 1e-9: # Using a small epsilon for floating point comparison
    solution_type = "a) a unique solution (the trivial solution: x1=0, x2=0, x3=0)"
    plot_title_suffix = "Unique Solution (Intersection at Origin)"
else:
    solution_type = "c) infinite number of solutions"
    plot_title_suffix = "Infinite Solutions (Intersection along a Line)"

print(f"\nFor this homogeneous system, the conclusion is:\n{solution_type}")

# --- 3D Plotting of Planes ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define a range for x, y, z
r = 3 # Range for plotting, adjust as needed
x = np.linspace(-r, r, 10)
y = np.linspace(-r, r, 10)
X, Y = np.meshgrid(x, y)

# Equation 1: 2x1 + x2 + x3 = 0  => x3 = -2x1 - x2
Z1 = -2*X - Y

# Equation 2: x2 - x3 = 0  => x3 = x2
Z2 = Y

# Equation 3: x1 + x2 = 0  => x2 = -x1. This plane is parallel to the x3-axis.
# For plotting, we need Z values. Since x3 can be any value, we express x1 in terms of x2 (or vice-versa).
# Or, more directly, if x2 = -x1, then this equation does not constrain x3.
# We can represent it by picking points (x, -x, z)
# For the plot, let's fix X and Z and solve for Y for this plane
# Since X and Y are meshgrid, we need to solve for one in terms of the other, or parameterize.
# Let's consider points (x, -x, z) for plane 3.
# To plot as a surface (X, Y, Z), we need Y as a function of X, and Z as independent.
# So, for the third plane, Y = -X, and Z can be any value (from -r to r).
Y3 = -X
Z3_values = np.linspace(-r, r, 10) # X, Y are 10x10, so Z needs to be 10x10 or implicitly defined.
# A plane where one variable is free can be visualized by defining two variables and letting the third vary
# For x1 + x2 = 0, points are (x, -x, z). Let's use different meshing for this to avoid conflicts
X3_plot, Z3_plot = np.meshgrid(x, Z3_values)
Y3_plot = -X3_plot # This is the X2 (Y) coordinate for plane 3


# Plot the planes
ax.plot_surface(X, Y, Z1, alpha=0.5, color='cyan', label='2x1 + x2 + x3 = 0')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='magenta', label='x2 - x3 = 0')
# For plane 3, we need to swap axes or plot carefully
# One way to plot x1 + x2 = 0 is to create points (x, -x, z) where z varies
ax.plot_surface(X3_plot, Y3_plot, Z3_plot, alpha=0.5, color='yellow', label='x1 + x2 = 0')


# Find the intersection line
# From eq2: x2 = x3
# Substitute into eq3: x1 + x2 = 0 => x1 = -x2
# So, x1 = -x2 and x3 = x2
# Let x2 = t. Then x1 = -t, x3 = t.
# This gives the line: (-t, t, t)
t = np.linspace(-r, r, 100)
intersection_line_x = -t
intersection_line_y = t
intersection_line_z = t
ax.plot(intersection_line_x, intersection_line_y, intersection_line_z,
        color='red', linewidth=3, label='Intersection Line (-t, t, t)')

# Add a point at the origin (trivial solution)
ax.scatter(0, 0, 0, color='red', s=100, label='Origin (0,0,0)', zorder=5)


# Set labels and title
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')
ax.set_title(f"Planes for System of Equations: {plot_title_suffix}\n(Det = {determinant:.0f})")

# Add a legend
# Due to a bug/feature in older matplotlib, surfaces don't appear in legend easily.
# We'll use custom patches for the legend.
from matplotlib.lines import Line2D
custom_lines = [
    Line2D([0], [0], color='cyan', lw=4, alpha=0.5),
    Line2D([0], [0], color='magenta', lw=4, alpha=0.5),
    Line2D([0], [0], color='yellow', lw=4, alpha=0.5),
    Line2D([0], [0], color='red', lw=3)
]
ax.legend(custom_lines,
          ['2x1 + x2 + x3 = 0', 'x2 - x3 = 0', 'x1 + x2 = 0', 'Intersection Line'],
          loc='upper left', bbox_to_anchor=(0.8, 0.95))

plt.tight_layout()
plt.show()