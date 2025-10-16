import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib_code = ctypes.CDLL("/Users/nishidkhandagre/matgeo/venv/bin/code18.so")

# Define the argument types and return type for the C function
lib_code.findIntersectionOfTangents.argtypes = [
    ctypes.c_double,             # a_param
    ctypes.POINTER(ctypes.c_double), # intersect_x
    ctypes.POINTER(ctypes.c_double)  # intersect_y
]
lib_code.findIntersectionOfTangents.restype = None

# Given parabola: y^2 = 4x
# Comparing with y^2 = 4ax, we get 4a = 4, so a = 1
a_value = 1.0

# Create ctypes doubles to hold the results
intersect_x_result = ctypes.c_double()
intersect_y_result = ctypes.c_double()

# Call the C function to find the point of intersection
lib_code.findIntersectionOfTangents(
    a_value,
    ctypes.byref(intersect_x_result),
    ctypes.byref(intersect_y_result)
)

intersection_x = intersect_x_result.value
intersection_y = intersect_y_result.value

print(f"For the parabola y^2 = 4x (where a = {a_value}):")
print(f"The point of intersection of the tangents at the ends of the latus rectum is ({intersection_x:.2f}, {intersection_y:.2f})")

# --- Plotting Section ---

# Generate points for the parabola y^2 = 4x
y_parabola = np.linspace(-4, 4, 400)
x_parabola = (y_parabola**2) / 4

# Ends of the latus rectum
latus_rectum_end1_x, latus_rectum_end1_y = a_value, 2 * a_value
latus_rectum_end2_x, latus_rectum_end2_y = a_value, -2 * a_value

# Tangent equations derived from the problem (y = x + a and y = -x - a)
# For y = x + a (tangent at (a, 2a))
x_tangent1 = np.linspace(-3, 3, 100)
y_tangent1 = x_tangent1 + a_value

# For y = -x - a (tangent at (a, -2a))
x_tangent2 = np.linspace(-3, 3, 100)
y_tangent2 = -x_tangent2 - a_value


plt.figure(figsize=(10, 8))

# Plot the parabola
plt.plot(x_parabola, y_parabola, 'b-', label='Parabola $y^2 = 4x$')

# Plot the focus
plt.scatter(a_value, 0, color='orange', s=100, zorder=5, label=f'Focus ({a_value}, 0)')
plt.annotate(f'F({a_value},0)', (a_value, 0), textcoords="offset points", xytext=(5,5), ha='left')

# Plot the latus rectum line
plt.plot([a_value, a_value], [-2*a_value, 2*a_value], 'k-', label='Latus Rectum (x=1)')

# Plot the ends of the latus rectum
plt.scatter(latus_rectum_end1_x, latus_rectum_end1_y, color='red', s=100, zorder=5, label=f'End L ({latus_rectum_end1_x},{latus_rectum_end1_y})')
plt.annotate(f'L({latus_rectum_end1_x},{latus_rectum_end1_y})', (latus_rectum_end1_x, latus_rectum_end1_y), textcoords="offset points", xytext=(5,5), ha='left')
plt.scatter(latus_rectum_end2_x, latus_rectum_end2_y, color='red', s=100, zorder=5, label=f'End L\' ({latus_rectum_end2_x},{latus_rectum_end2_y})')
plt.annotate(f'L\'({latus_rectum_end2_x},{latus_rectum_end2_y})', (latus_rectum_end2_x, latus_rectum_end2_y), textcoords="offset points", xytext=(5,5), ha='right')


# Plot the tangents
plt.plot(x_tangent1, y_tangent1, 'g-', label=f'Tangent at L (y=x+{a_value})')
plt.plot(x_tangent2, y_tangent2, 'm-', label=f'Tangent at L\' (y=-x-{a_value})')

# Plot the intersection point
plt.scatter(intersection_x, intersection_y, color='purple', s=100, zorder=6, label=f'Intersection ({intersection_x:.2f},{intersection_y:.2f})')
plt.annotate(f'P({intersection_x:.2f},{intersection_y:.2f})', (intersection_x, intersection_y), textcoords="offset points", xytext=(10, -15), ha='left', color='purple', fontsize=12)


plt.xlim(-3, 6)
plt.ylim(-4, 4)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Parabola, Latus Rectum, Tangents, and Intersection Point')
plt.grid(True)
plt.legend()
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.show()