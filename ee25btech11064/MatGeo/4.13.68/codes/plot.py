import numpy as np
import matplotlib.pyplot as plt

# Define the points
points = np.array([
    [3, 1],     # A
    [12, -2],   # B
    [0, 2]      # C
])

# Extract x and y coordinates
x = points[:, 0]
y = points[:, 1]

# Plot the points
plt.figure(figsize=(6, 6))
plt.plot(x, y, 'ro', label='Points')           # Red dots
plt.plot(x, y, 'b--', label='Connecting Line') # Dashed blue line

# Annotate each point
labels = ['A (3,1)', 'B (12,-2)', 'C (0,2)']
for i in range(len(labels)):
    plt.text(x[i] + 0.5, y[i] + 0.5, labels[i], fontsize=10)

# Add plot details
plt.title('Plot of Three Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.tight_layout()
plt.show()