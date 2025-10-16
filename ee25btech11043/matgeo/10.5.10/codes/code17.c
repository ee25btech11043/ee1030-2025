// tangent_calculator.c
#include <math.h> // For sqrt

// Function to calculate the length of the tangent
// radius: radius of the circle
// distance_from_center: distance of the external point from the center
// tangent_length: pointer to a double where the result will be stored
void calculateTangentLength(double radius, double distance_from_center, double *tangent_length) {
    if (distance_from_center <= radius) {
        // If the point is inside or on the circle, no tangent can be drawn from the outside
        *tangent_length = 0.0; // Or handle as an error, for now set to 0
    } else {
        *tangent_length = sqrt(distance_from_center * distance_from_center - radius * radius);
    }
}