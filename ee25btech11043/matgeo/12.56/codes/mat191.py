import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib_area = ctypes.CDLL("/Users/nishidkhandagre/matgeo/venv/bin/code19.so")

# Define the argument types and return type for the C function
lib_area.calculateEnclosedArea.argtypes = []
lib_area.calculateEnclosedArea.restype = ctypes.c_double

# Call the C function to get the enclosed area
area_result = lib_area.calculateEnclosedArea()

print(f"The area enclosed between the curves y^2 = 4x and x^2 = 4y is: {area_result:.4f}")

# Generate points for plotting the curves
# x values for y^2=4x must be non-negative
x_parabola = np.linspace(0, 5, 400) 
x_other_curve = np.linspace(0, 5, 400) # x values for x^2=4y

# --- CHANGE STARTS HERE ---
# Curve 1: y^2 = 4x  =>  y = +/- 2*sqrt(x)
y_upper_parabola = 2 * np.sqrt(x_parabola)
y_lower_parabola = -2 * np.sqrt(x_parabola)

# Curve 2: x^2 = 4y  =>  y = x^2 / 4
y_other_curve = x_other_curve**2 / 4

# Plotting
plt.figure(figsize=(8, 8))

# Plot y^2 = 4x as a complete parabola
plt.plot(x_parabola, y_upper_parabola, 'b-', label=r'$y^2 = 4x$') # Plot upper half
plt.plot(x_parabola, y_lower_parabola, 'b-') # Plot lower half with the same style, no new label

# Plot x^2 = 4y
plt.plot(x_other_curve, y_other_curve, 'r-', label=r'$x^2 = 4y$')
# --- CHANGE ENDS HERE ---


# Fill the enclosed area (this part remains the same as it correctly identifies the bounds)
x_fill = np.linspace(0, 4, 100)
y_upper_fill = 2 * np.sqrt(x_fill)  # This is y from y^2=4x for filling
y_lower_fill = x_fill**2 / 4       # This is y from x^2=4y for filling
plt.fill_between(x_fill, y_lower_fill, y_upper_fill, color='lightgray', alpha=0.5, label='Enclosed Area')

# Intersection points
plt.scatter([0, 4], [0, 4], color='green', s=100, zorder=5, label='Intersection Points')
plt.annotate('(0,0)', (0, 0), textcoords="offset points", xytext=(5,5), ha='left')
plt.annotate('(4,4)', (4, 4), textcoords="offset points", xytext=(5,5), ha='left')

plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(f'Area Enclosed Between $y^2=4x$ and $x^2=4y')
plt.grid(True)
plt.legend()
plt.ylim(-5, 5) # Adjusted y-limits to better show the full parabola
plt.xlim(-0.5, 5.5) # Adjust x-limits for better view
plt.show()