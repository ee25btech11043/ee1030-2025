import numpy as np
import matplotlib.pyplot as plt

def find_intersection_of_tangents_at_latus_rectum_ends(a_param):
    #the ends of the latus rectum are:
    # L1 = (a, 2a)
    # L2 = (a, -2a)

    # 2. Determine the equations of the tangents at these points
    # The general equation of a tangent to y^2 = 4ax at a point (x1, y1) is:
    # y * y1 = 2a * (x + x1)

    # Tangent at L1 (a, 2a):
    # y * (2a) = 2a * (x + a)
    # y = x + a  (Equation for Tangent 1)

    # Tangent at L2 (a, -2a):
    # y * (-2a) = 2a * (x + a)
    # y = -x - a (Equation for Tangent 2)
    # x + a = -x - a
    # x = -a

    # Substitute x = -a
    # y = (-a) + a
    # y = 0

    x_intersect = -a_param
    y_intersect = 0.0

    return x_intersect, y_intersect

# --- Main execution and plotting ---
# Given parabola: y^2 = 4x
# 4a = 4  => a = 1
a_value = 1.0

# Calculate the intersection point using the Python function
intersection_x, intersection_y = find_intersection_of_tangents_at_latus_rectum_ends(a_value)

print(f"For the parabola y^2 = 4x (where a = {a_value}):")
print(f"The point of intersection of the tangents at the ends of the latus rectum is ({intersection_x:.2f}, {intersection_y:.2f})")

# --- Plotting Section ---

plt.figure(figsize=(10, 8))

# 1. Plot the parabola y^2 = 4x
y_parabola = np.linspace(-4, 4, 400)
x_parabola = (y_parabola**2) / (4 * a_value)
plt.plot(x_parabola, y_parabola, 'b-', label=f'Parabola $y^2 = 4x$')

# 2. Plot the focus
focus_x, focus_y = a_value, 0
plt.scatter(focus_x, focus_y, color='orange', s=100, zorder=5, label=f'Focus ({focus_x}, {focus_y})')
plt.annotate(f'F({focus_x},{focus_y})', (focus_x, focus_y), textcoords="offset points", xytext=(5,5), ha='left')

# 3. Plot the latus rectum line
latus_rectum_x_val = a_value
latus_rectum_y_min, latus_rectum_y_max = -2 * a_value, 2 * a_value
plt.plot([latus_rectum_x_val, latus_rectum_x_val], [latus_rectum_y_min, latus_rectum_y_max], 'k-', label='Latus Rectum (x=1)')

# 4. Plot the ends of the latus rectum
latus_rectum_end1 = (a_value, 2 * a_value)
latus_rectum_end2 = (a_value, -2 * a_value)
plt.scatter(latus_rectum_end1[0], latus_rectum_end1[1], color='red', s=100, zorder=5, label=f'End L ({latus_rectum_end1[0]},{latus_rectum_end1[1]})')
plt.annotate(f'L({latus_rectum_end1[0]},{latus_rectum_end1[1]})', latus_rectum_end1, textcoords="offset points", xytext=(5,5), ha='left')
plt.scatter(latus_rectum_end2[0], latus_rectum_end2[1], color='red', s=100, zorder=5, label=f'End L\' ({latus_rectum_end2[0]},{latus_rectum_end2[1]})')
plt.annotate(f'L\'({latus_rectum_end2[0]},{latus_rectum_end2[1]})', latus_rectum_end2, textcoords="offset points", xytext=(5,-5), ha='right') # Adjusted xytext for better label placement

# 5. Plot the tangents
x_tangent_range = np.linspace(-3, 3, 100) # Define a range for x for tangent lines
y_tangent1 = x_tangent_range + a_value  # y = x + a
y_tangent2 = -x_tangent_range - a_value # y = -x - a

plt.plot(x_tangent_range, y_tangent1, 'g-', label=f'Tangent at L (y=x+{a_value})')
plt.plot(x_tangent_range, y_tangent2, 'm-', label=f'Tangent at L\' (y=-x-{a_value})')

# 6. Plot the intersection point
plt.scatter(intersection_x, intersection_y, color='purple', s=100, zorder=6, label=f'Intersection ({intersection_x:.2f},{intersection_y:.2f})')
plt.annotate(f'P({intersection_x:.2f},{intersection_y:.2f})', (intersection_x, intersection_y), textcoords="offset points", xytext=(10, -15), ha='left', color='purple', fontsize=12)

# --- Plot Aesthetics ---
plt.xlim(-3, 6)
plt.ylim(-4, 4)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Parabola, Latus Rectum, Tangents, and Intersection Point')
plt.grid(True)
plt.legend()
plt.axhline(0, color='gray', linewidth=0.5) # X-axis
plt.axvline(0, color='gray', linewidth=0.5) # Y-axis
plt.show()