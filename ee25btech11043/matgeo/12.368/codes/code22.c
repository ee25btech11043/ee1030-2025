#include <stdio.h>

// Function to calculate the determinant of a 3x3 matrix
// matrix(array): [a11, a12, a13, a21, a22, a23, a31, a32, a33]
double calculate_determinant(double* matrix_elements) {
    double a = matrix_elements[0]; double b = matrix_elements[1]; double c = matrix_elements[2];
    double d = matrix_elements[3]; double e = matrix_elements[4]; double f = matrix_elements[5];
    double g = matrix_elements[6]; double h = matrix_elements[7]; double i = matrix_elements[8];

    // Formula for 3x3 determinant:
    // a(ei - fh) - b(di - fg) + c(dh - eg)
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e 
