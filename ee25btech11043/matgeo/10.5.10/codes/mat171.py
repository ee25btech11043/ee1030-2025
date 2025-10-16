import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library

lib_tangent = ctypes.CDLL("/Users/nishidkhandagre/matgeo/venv/bin/code17.so")

# Define the argument types and return type for the C function
lib_tangent.calculateTangentLength.argtypes = [
    ctypes.c_double,  # radius
    ctypes.c_double,  # distance_from_center
    ctypes.POINTER(ctypes.c_double) # tangent_length (output)
]
lib_tangent.calculateTangentLength.restype = None

# Given values
radius_given = 4.0  # cm
distance_given = 6.0  # cm (distance of the external point from the center)

# Create a ctypes double to hold the result
tangent_length_result = ctypes.c_double()

# Call the C function to calculate the tangent length
lib_tangent.calculateTangentLength(
    radius_given,
    distance_given,
    ctypes.byref(tangent_length_result)
)

tangent_length = tangent_length_result.value

print(f"The length of the tangent calculated by C function is: {tangent_length:.2f} cm")

# --- Plotting the construction (mostly the same as before) ---

# Assuming the center of the circle is at (0,0)
center_x, center_y = 0, 0

# The external point can be placed on the x-axis for simplicity
point_x, point_y = distance_given, 0

plt.figure(figsize=(8, 8))

# 1. Draw the circle
theta = np.linspace(0, 2 * np.pi, 200)
circle_x = center_x + radius_given * np.cos(theta)
circle_y = center_y + radius_given * np.sin(theta)
plt.plot(circle_x, circle_y, 'b-', label=f'Circle (Radius = {radius_given} cm)')

# 2. Plot the center of the circle
plt.scatter(center_x, center_y, color='green', s=100, zorder=5, label='Center (C)')
plt.annotate('C (0,0)', (center_x, center_y), textcoords="offset points", xytext=(5,5), ha='left')

# 3. Plot the external point
plt.scatter(point_x, point_y, color='red', s=100, zorder=5, label=f'External Point (P) - {distance_given} cm from C')
plt.annotate(f'P ({point_x},{point_y})', (point_x, point_y), textcoords="offset points", xytext=(5,5), ha='left')

# 4. Draw the line segment from the center to the external point (CP)
plt.plot([center_x, point_x], [center_y, point_y], 'g--', label=f'CP (Distance = {distance_given} cm)')

# 5. Find the tangent points (T1, T2) using trigonometry
angle_CP = np.arctan2(point_y - center_y, point_x - center_x)

# Angle between CP and CT (tangent point)
# This uses asin(opposite/hypotenuse) where opposite is radius and hypotenuse is distance_from_center
angle_CT_offset = np.arcsin(radius_given / distance_given)

# Coordinates of tangent points T1 and T2
T1_angle = angle_CP + angle_CT_offset
T2_angle = angle_CP - angle_CT_offset

T1_x = center_x + radius_given * np.cos(T1_angle)
T1_y = center_y + radius_given * np.sin(T1_angle)

T2_x = center_x + radius_given * np.cos(T2_angle)
T2_y = center_y + radius_given * np.sin(T2_angle)

# Plot tangent points
plt.scatter(T1_x, T1_y, color='orange', s=100, zorder=5, label='Tangent Point (T1)')
plt.annotate(f'T1 ({T1_x:.2f},{T1_y:.2f})', (T1_x, T1_y), textcoords="offset points", xytext=(5,5), ha='left')

plt.scatter(T2_x, T2_y, color='orange', s=100, zorder=5, label='Tangent Point (T2)')
plt.annotate(f'T2 ({T2_x:.2f},{T2_y:.2f})', (T2_x, T2_y), textcoords="offset points", xytext=(5,5), ha='left')


# 6. Draw the tangents PT1 and PT2
plt.plot([point_x, T1_x], [point_y, T1_y], 'm-', label=f'Tangent PT1 (Length = {tangent_length:.2f} cm)')
plt.plot([point_x, T2_x], [point_y, T2_y], 'm-', label=f'Tangent PT2 (Length = {tangent_length:.2f} cm)')

# 7. Draw the radii to the tangent points (CT1 and CT2)
plt.plot([center_x, T1_x], [center_y, T1_y], 'c:', label='Radius CT1 (Perpendicular to Tangent)')
plt.plot([center_x, T2_x], [center_y, T2_y], 'c:', label='Radius CT2 (Perpendicular to Tangent)')


plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Construction of Tangents to a Circle (C function for length)')
plt.grid(True, linestyle='--')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()