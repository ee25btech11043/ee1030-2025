// determinant_solver.c
#include <stdio.h>

// Function to calculate the determinant of a 3x3 matrix
// The matrix is passed as a 1D array in row-major order:
// [a11, a12, a13, a21, a22, a23, a31, a32, a33]
double calculate_determinant_3x3(double* matrix) {
    double det = 0.0;

    det = matrix[0] * (matrix[4] * matrix[8] - matrix[5] * matrix[7])
        - matrix[1] * (matrix[3] * matrix[8] - matrix[5] * matrix[6])
        + matrix[2] * (matrix[3] * matrix[7] - matrix[4] * matrix[6]);

    return det;
}