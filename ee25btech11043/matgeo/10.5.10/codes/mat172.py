import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# --- Helper Functions (from your example, adapted slightly if needed) ---

def line_gen_num(A, B, num_points):
    """
    Generates points for a line segment between two points A and B.
    A, B: numpy arrays representing 2D points (e.g., [x, y] or [[x],[y]])
    num_points: number of points to generate along the line
    Returns: a 2xnum_points array of (x,y) coordinates
    """
    A = A.flatten()
    B = B.flatten()
    t = np.linspace(0, 1, num_points)
    # Ensure points are generated correctly for 2D
    points = np.array([A[i]*(1-t) + B[i]*t for i in range(len(A))])
    return points


def circ_gen(center, radius, num_points=100):
    """
    Generates points for a circle.
    center: numpy array representing the center of the circle (e.g., [x, y] or [[x],[y]])
    radius: radius of the circle
    num_points: number of points to generate for the circle
    Returns: a 2xnum_points array of (x,y) coordinates
    """
    center = center.flatten()
    theta = np.linspace(0, 2 * np.pi, num_points)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return np.array([x, y])

# --- Main Program for Tangent Construction ---

# Given values
radius = 4  # cm
distance_from_center = 6  # cm (distance of the external point from the center)

# Define the center of the circle (C) and the external point (P)
# For simplicity, place the center at (0,0) and P on the positive x-axis
C = np.array([0, 0]).reshape(-1, 1)
P_ext = np.array([distance_from_center, 0]).reshape(-1, 1)

# 1. Calculate the length of the tangent (PT)
# Using Pythagorean theorem: PT^2 + CT^2 = CP^2
# PT = sqrt(CP^2 - CT^2) = sqrt(distance_from_center^2 - radius^2)
if distance_from_center <= radius:
    print("Error: The external point is inside or on the circle. No external tangents can be drawn.")
    tangent_length = 0
else:
    tangent_length = np.sqrt(distance_from_center**2 - radius**2)
    print(f"The length of the tangent is: {tangent_length:.2f} cm")

# 2. Find the coordinates of the tangent points (T1, T2)
# The tangent points T1 and T2 form right-angled triangles with C and P_ext.
# Angle of rotation for tangent points relative to CP line
# In triangle CTP_ext, sin(angle_PCT) = CT / CP_ext = radius / distance_from_center
angle_PCT = np.arcsin(radius / distance_from_center) # This is the angle between CP and CT

# Vector CP_ext
vec_CP = P_ext - C
# Magnitude of CP_ext (which is distance_from_center, but good to reconfirm)
mag_CP = LA.norm(vec_CP)

# Unit vector along CP
unit_vec_CP = vec_CP / mag_CP

# Rotate the unit vector CP by +/- angle_PCT and scale by radius to get CT1 and CT2
# Rotation matrix for an angle 'a': [[cos(a), -sin(a)], [sin(a), cos(a)]]

# For T1 (positive rotation)
rot_matrix_pos = np.array([
    [np.cos(angle_PCT), -np.sin(angle_PCT)],
    [np.sin(angle_PCT),  np.cos(angle_PCT)]
])
vec_CT1_unit = rot_matrix_pos @ unit_vec_CP
T1 = C + radius * vec_CT1_unit

# For T2 (negative rotation)
rot_matrix_neg = np.array([
    [np.cos(-angle_PCT), -np.sin(-angle_PCT)],
    [np.sin(-angle_PCT),  np.cos(-angle_PCT)]
])
vec_CT2_unit = rot_matrix_neg @ unit_vec_CP
T2 = C + radius * vec_CT2_unit

# --- Plotting ---

plt.figure(figsize=(9, 9))

# Generate points for the circle
x_circ = circ_gen(C, radius)
plt.plot(x_circ[0,:], x_circ[1,:], "b-", label=f"Circle (Radius={radius} cm)")

# Plot the center C and external point P
plt.scatter(C[0], C[1], color='green', s=100, zorder=5, label='Center C')
plt.annotate(f'C({C[0,0]:.0f},{C[1,0]:.0f})', (C[0,0], C[1,0]), textcoords="offset points", xytext=(5,5), ha='left')

plt.scatter(P_ext[0], P_ext[1], color='red', s=100, zorder=5, label=f'External Point P ({distance_from_center} cm from C)')
plt.annotate(f'P({P_ext[0,0]:.0f},{P_ext[1,0]:.0f})', (P_ext[0,0], P_ext[1,0]), textcoords="offset points", xytext=(5,5), ha='left')

# Plot the line segment CP
x_CP = line_gen_num(C, P_ext, 20)
plt.plot(x_CP[0,:], x_CP[1,:], "g--", label=f"Line CP (Length={distance_from_center} cm)")

# Plot the tangent points T1 and T2
plt.scatter(T1[0], T1[1], color='orange', s=100, zorder=5, label='Tangent Point T1')
plt.annotate(f'T1({T1[0,0]:.2f},{T1[1,0]:.2f})', (T1[0,0], T1[1,0]), textcoords="offset points", xytext=(5,5), ha='left')

plt.scatter(T2[0], T2[1], color='orange', s=100, zorder=5, label='Tangent Point T2')
plt.annotate(f'T2({T2[0,0]:.2f},{T2[1,0]:.2f})', (T2[0,0], T2[1,0]), textcoords="offset points", xytext=(5,5), ha='left')

# Plot the tangents PT1 and PT2
x_PT1 = line_gen_num(P_ext, T1, 20)
plt.plot(x_PT1[0,:], x_PT1[1,:], "m-", label=f"Tangent PT1 (Length={tangent_length:.2f} cm)")

x_PT2 = line_gen_num(P_ext, T2, 20)
plt.plot(x_PT2[0,:], x_PT2[1,:], "m-", label=f"Tangent PT2 (Length={tangent_length:.2f} cm)")

# Plot the radii CT1 and CT2 (which are perpendicular to tangents)
x_CT1 = line_gen_num(C, T1, 20)
plt.plot(x_CT1[0,:], x_CT1[1,:], "c:", label="Radius CT1")

x_CT2 = line_gen_num(C, T2, 20)
plt.plot(x_CT2[0,:], x_CT2[1,:], "c:", label="Radius CT2")


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True, linestyle='--')
plt.title("Construction of Tangents to a Circle")
plt.axis('equal') # Ensures the circle looks circular
plt.tight_layout() # Adjust layout to prevent labels from being cut off
plt.show()