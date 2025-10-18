#include <math.h>

// Function to calculate the horizontal force F
// weight: the weight of the ball (in N)
// angle_degrees: the angle the string makes with the vertical (in degrees)
// Returns the magnitude of the horizontal force F (in N)
double calculate_horizontal_force(double weight, double angle_degrees) {
    // Convert angle from degrees to radians for trigonometric functions
    double angle_radians = angle_degrees * M_PI / 180.0;

   // In equilibrium, summing forces in the vertical direction:
    // T * cos(angle_radians) = weight
    // So, Tension T = weight / cos(angle_radians)

    // Summing forces in the horizontal direction:
    // F = T * sin(angle_radians)

    // Substitute T into the equation for F:
    // F = (weight / cos(angle_radians)) * sin(angle_radians)
    // F = weight * tan(angle_radians)
    
    // F = W * tan(angle)
    double force_F = weight * tan(angle_radians);

    return force_F;
}
