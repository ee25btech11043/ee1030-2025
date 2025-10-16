import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D

# --- Pure Python Determinant Calculation for a 3x3 matrix ---
def calculate_determinant_3x3_python(matrix):
    """
    Calculates the determinant of a 3x3 matrix.
    Matrix should be a 3x3 NumPy array.
    """
    if matrix.shape != (3, 3):
        raise ValueError("Input matrix must be 3x3.")

    a, b, c = matrix[0, 0], matrix[0, 1], matrix[0, 2]
    d, e, f = matrix[1, 0], matrix[1, 1], matrix[1, 2]
    g, h, i = matrix[2, 0], matrix[2, 1], matrix[2, 2]

    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return det

# --- Define the system of equations ---
# 2x1 + x2 + x3 = 0   (Plane 1)
# 0x1 + x2 - x3 = 0   (Plane 2)
# x1 + x2 + 0x3 = 0   (Plane 3)

# Coefficient matrix A:
# [2  1  1]
# [0  1 -1]
# [1  1  0]

coefficient_matrix_np = np.array([
    [2.0, 1.0, 1.0],
    [0.0, 1.0, -1.0],
    [1.0, 1.0, 0.0]
], dtype=np.float64)

print("Coefficient Matrix:")
print(coefficient_matrix_np)

# Calculate the determinant using the pure Python function
determinant = calculate_determinant_3x3_python(coefficient_matrix_np)

print(f"\nCalculated Determinant (Pure Python): {determinant:.4f}")

# Determine the nature of the solutions based on the determinant
if abs(determinant) > 1e-9: # Using a small epsilon for floating point comparison
    solution_type = "a) a unique solution (the trivial solution: x1=0, x2=0, x3=0)"
    plot_title_suffix = "Unique Solution (Intersection at Origin)"
    has_intersection_line = False
else:
    solution_type = "c) infinite number of solutions"
    plot_title_suffix = "Infinite Solutions (Intersection along a Line)"
    has_intersection_line = True

print(f"\nFor this homogeneous system, the conclusion is:\n{solution_type}")

# --- 3D Plotting of Planes ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Define a range for x, y, z for plotting
r_range = 3 # Range for plotting, adjust as needed
x_vals = np.linspace(-r_range, r_range, 10)
y_vals = np.linspace(-r_range, r_range, 10)
X, Y = np.meshgrid(x_vals, y_vals)

# Equation 1: 2x1 + x2 + x3 = 0  => x3 = -2x1 - x2
Z1 = -2*X - Y
ax.plot_surface(X, Y, Z1, alpha=0.5, color='cyan', label='2x1 + x2 + x3 = 0')

# Equation 2: x2 - x3 = 0  => x3 = x2
Z2 = Y
ax.plot_surface(X, Y, Z2, alpha=0.5, color='magenta', label='x2 - x3 = 0')

# Equation 3: x1 + x2 = 0  => x2 = -x1
# For plotting, we need to handle this vertical plane.
# We can express it as (X, -X, Z_varying)
X3_plot, Z3_plot = np.meshgrid(x_vals, np.linspace(-r_range, r_range, 10))
Y3_plot = -X3_plot # The Y coordinate for the third plane
ax.plot_surface(X3_plot, Y3_plot, Z3_plot, alpha=0.5, color='yellow', label='x1 + x2 = 0')


# Plot the intersection line (if infinite solutions)
if has_intersection_line:
    # From eq2: x2 = x3
    # Substitute into eq3: x1 + x2 = 0 => x1 = -x2
    # So, x1 = -x2 and x3 = x2
    # Let x2 = t. Then x1 = -t, x3 = t.
    # This gives the line: (-t, t, t)
    t = np.linspace(-r_range, r_range, 100)
    intersection_line_x = -t
    intersection_line_y = t
    intersection_line_z = t
    ax.plot(intersection_line_x, intersection_line_y, intersection_line_z,
            color='red', linewidth=3, label='Intersection Line (-t, t, t)')

# Add a point at the origin (trivial solution, always exists for homogeneous systems)
ax.scatter(0, 0, 0, color='red', s=100, label='Origin (0,0,0)', zorder=5)

# Set labels and title
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')
ax.set_title(f"Planes for System of Equations")

# Add a legend using custom line objects for surfaces
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