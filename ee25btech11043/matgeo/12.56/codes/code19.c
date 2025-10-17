#include <math.h>

// Function to calculate the area between y^2 = 4x and x^2 = 4y
double calculateEnclosedArea() {
    // The intersection points are (0,0) and (4,4)
    // The upper curve is y = 2*sqrt(x)
    // The lower curve is y = x*x / 4
    // Integral of (2*sqrt(x) - x*x / 4) from 0 to 4
    // Integral of 2*x^(1/2) is 2 * (x^(3/2) / (3/2)) = (4/3)*x^(3/2)
    // Integral of x^2 / 4 is (1/4) * (x^3 / 3) = x^3 / 12

    // Evaluate at x=4:
    double upper_at_4 = (4.0/3.0) * pow(4.0, 1.5); // (4/3) * 8 = 32/3
    double lower_at_4 = pow(4.0, 3.0) / 12.0;       // 64 / 12 = 16/3

    // Evaluate at x=0 (both are 0)

    return upper_at_4 - lower_at_4; // 32/3 - 16/3 = 16/3
}