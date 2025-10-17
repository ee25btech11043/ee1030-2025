import numpy as np
import matplotlib.pyplot as plt

# Define the functions for the two curves
def curve1_y_positive(x):
    return 2 * np.sqrt(x)  # For y^2 = 4x, y = +2*sqrt(x)

def curve1_y_negative(x):
    return -2 * np.sqrt(x) # For y^2 = 4x, y = -2*sqrt(x)

def curve2_y(x):
    return x**2 / 4  # For x^2 = 4y, y = x^2 / 4

# Define the range for x
# For y^2 = 4x, x must be non-negative.
x_parabola1 = np.linspace(0, 10, 400) # Extend range to show more of the parabola opening right

# For x^2 = 4y, x can be any real number.
x_parabola2 = np.linspace(-6, 6, 400) # Extend range to show more of the parabola opening up

# Calculate y values for each curve
y1_positive = curve1_y_positive(x_parabola1)
y1_negative = curve1_y_negative(x_parabola1)
y2 = curve2_y(x_parabola2)

# Plotting the curves
plt.figure(figsize=(9, 7))

# Plot y^2 = 4x (full parabola)
plt.plot(x_parabola1, y1_positive, color='blue', label='$y^2 = 4x$ (upper part)')
plt.plot(x_parabola1, y1_negative, color='blue', linestyle='--', label='$y^2 = 4x$ (lower part)')

# Plot x^2 = 4y (full parabola)
plt.plot(x_parabola2, y2, color='green', label='$x^2 = 4y$')

# Shade the enclosed area between (0,0) and (4,4)
x_fill = np.linspace(0, 4, 100)
y_upper_bound = 2 * np.sqrt(x_fill)
y_lower_bound = x_fill**2 / 4
plt.fill_between(x_fill, y_upper_bound, y_lower_bound, color='lightgray', alpha=0.5, label='Enclosed Area')

# Add intersection points
intersection_x = [0, 4]
intersection_y = [0, 4]
plt.scatter(intersection_x, intersection_y, color='red', zorder=5, label='Intersection Points')
plt.text(0.1, 0.1, '(0,0)', fontsize=10, verticalalignment='bottom')
plt.text(4.2, 4.2, '(4,4)', fontsize=10, verticalalignment='bottom')

# Add labels and title
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Full Parabolas and Enclosed Area')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(-2, 11) # Adjusted x-limit to show more of y^2=4x
plt.ylim(-7, 7)  # Adjusted y-limit to show more of both parabolas
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.savefig("full_parabolas_enclosed_area.png")
plt.show()

print("Figure saved as full_parabolas_enclosed_area.png")
print(f"The calculated enclosed area is: {16/3:.2f} square units")