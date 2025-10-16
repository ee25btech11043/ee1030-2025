import math

def calculate_horizontal_force_pure_python(weight, angle_degrees):

#Calculates the horizontal force F required to pull a ball

    # Convert angle from degrees to radians for trigonometric functions
    angle_radians = math.radians(angle_degrees)

    # In equilibrium, summing forces in the vertical direction:
    # T * cos(angle_radians) = weight
    # So, Tension T = weight / cos(angle_radians)

    # Summing forces in the horizontal direction:
    # F = T * sin(angle_radians)

    # Substitute T into the equation for F:
    # F = (weight / cos(angle_radians)) * sin(angle_radians)
    # F = weight * tan(angle_radians)

    force_F = weight * math.tan(angle_radians)

    return force_F

# Given values from the problem
weight_ball = 100.0  # N
angle_string_vertical = 30.0 # degrees

# Calculate the force using the pure Python function
force_F_magnitude = calculate_horizontal_force_pure_python(weight_ball, angle_string_vertical)

print(f"The magnitude of force F is (in N): {force_F_magnitude:.3f}")