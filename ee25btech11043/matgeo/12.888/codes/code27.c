#include <math.h>
#include <stdio.h>

// Function to find eigenvalues of a 2x2 matrix
// mat = [[a, b], [c, d]]
// Returns 0 if real eigenvalues are found, -1 if complex
int findEigenvalues(double a, double b, double c, double d, double *lambda1, double *lambda2) {
    double trace = a + d;
    double det = a * d - b * c;

    // Characteristic equation: lambda^2 - (trace)lambda + (det) = 0
    // Using quadratic formula: lambda = (-B ± sqrt(B^2 - 4AC)) / 2A
    // Here A=1, B=-trace, C=det
    double discriminant = trace * trace - 4 * det;

    if (discriminant >= 0) {
        *lambda1 = (trace + sqrt(discriminant)) / 2.0;
        *lambda2 = (trace - sqrt(discriminant)) / 2.0;
        return 0; // Real eigenvalues
    } else {
        // Complex eigenvalues (not relevant for this problem, but good to handle)
        // You might want to return complex numbers or just indicate failure
        return -1; // Complex eigenvalues
    }
}