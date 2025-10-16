#include <stdio.h>
#include <math.h> // For fabs() for determinant calculation tolerance

// Function to calculate the determinant of a 3x3 matrix
double determinant_3x3(double m[3][3]) {
    return m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
           m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
           m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]);
}

// Function to calculate the inverse of a 3x3 matrix
// Returns 1 on success, 0 on failure (singular matrix)
int inverse_3x3(double m[3][3], double inv[3][3]) {
    double det = determinant_3x3(m);
    if (fabs(det) < 1e-9) { // Check for singularity (determinant close to zero)
        return 0; // Singular matrix, inverse does not exist
    }

    double invDet = 1.0 / det;

    inv[0][0] = (m[1][1] * m[2][2] - m[1][2] * m[2][1]) * invDet;
    inv[0][1] = (m[0][2] * m[2][1] - m[0][1] * m[2][2]) * invDet;
    inv[0][2] = (m[0][1] * m[1][2] - m[0][2] * m[1][1]) * invDet;

    inv[1][0] = (m[1][2] * m[2][0] - m[1][0] * m[2][2]) * invDet;
    inv[1][1] = (m[0][0] * m[2][2] - m[0][2] * m[2][0]) * invDet;
    inv[1][2] = (m[0][2] * m[1][0] - m[0][0] * m[1][2]) * invDet;

    inv[2][0] = (m[1][0] * m[2][1] - m[1][1] * m[2][0]) * invDet;
    inv[2][1] = (m[0][1] * m[2][0] - m[0][0] * m[2][1]) * invDet;
    inv[2][2] = (m[0][0] * m[1][1] - m[0][1] * m[1][0]) * invDet;

    return 1; // Success
}

// Function to multiply a 3x3 matrix by a 3x1 vector
void multiply_mat_vec_3x3(double mat[3][3], double vec[3], double result[3]) {
    result[0] = mat[0][0] * vec[0] + mat[0][1] * vec[1] + mat[0][2] * vec[2];
    result[1] = mat[1][0] * vec[0] + mat[1][1] * vec[1] + mat[1][2] * vec[2];
    result[2] = mat[2][0] * vec[0] + mat[2][1] * vec[1] + mat[2][2] * vec[2];
}


// Main function to solve the problem
// It takes pointers to return the calculated sum and minimal polynomial degree
void solve_matrix_problem_simplified(double *result_sum, int *minimal_poly_degree) {
    // 1. Determine minimal polynomial degree (m)
    // Distinct eigenvalues are 2 and 4.
    // Minimal polynomial m(x) = (x - 2)(x - 4), degree = 2.
    *minimal_poly_degree = 2;

    // 2. Find coefficients c1, c2, c3 for e1 = c1*v1 + c2*v2 + c3*v3
    // v1 = [1, 2, 1]^T
    // v2 = [0, 1, 1]^T
    // v3 = [-1, 1, 0]^T
    // Equation: P * [c1, c2, c3]^T = [1, 0, 0]^T, where P = [v1 | v2 | v3]
    double P_matrix[3][3] = {
        {1.0, 0.0, -1.0},
        {2.0, 1.0, 1.0},
        {1.0, 1.0, 0.0}
    };
    double e1_vec[3] = {1.0, 0.0, 0.0};
    double P_inverse[3][3];
    double c_vec[3]; // To store [c1, c2, c3]^T

    // [c1, c2, c3]^T = P_inverse * e1_vec
    multiply_mat_vec_3x3(P_inverse, e1_vec, c_vec);

    double c1 = c_vec[0];
    double c2 = c_vec[1];
    double c3 = c_vec[2];

    // 3. Calculate A*e1 = a11, a21, a31
    // A*e1 = c1*(A*v1) + c2*(A*v2) + c3*(A*v3)
    // A*e1 = c1*(lambda1*v1) + c2*(lambda2*v2) + c3*(lambda3*v3)
    // A*e1 = c1*(2*v1) + c2*(2*v2) + c3*(4*v3)

    double v1_arr[3] = {1.0, 2.0, 1.0};
    double v2_arr[3] = {0.0, 1.0, 1.0};
    double v3_arr[3] = {-1.0, 1.0, 0.0};

    double a11_a21_a31_vec[3] = {0.0, 0.0, 0.0};

    // Add c1 * 2 * v1
    a11_a21_a31_vec[0] += c1 * 2.0 * v1_arr[0];
    a11_a21_a31_vec[1] += c1 * 2.0 * v1_arr[1];
    a11_a21_a31_vec[2] += c1 * 2.0 * v1_arr[2];

    // Add c2 * 2 * v2
    a11_a21_a31_vec[0] += c2 * 2.0 * v2_arr[0];
    a11_a21_a31_vec[1] += c2 * 2.0 * v2_arr[1];
    a11_a21_a31_vec[2] += c2 * 2.0 * v2_arr[2];

    // Add c3 * 4 * v3
    a11_a21_a31_vec[0] += c3 * 4.0 * v3_arr[0];
    a11_a21_a31_vec[1] += c3 * 4.0 * v3_arr[1];
    a11_a21_a31_vec[2] += c3 * 4.0 * v3_arr[2];

    double a11 = a11_a21_a31_vec[0];
    double a21 = a11_a21_a31_vec[1];
    double a31 = a11_a21_a31_vec[2];

    // 4. Calculate the final sum
    *result_sum = a11 + a21 + a31 + (*minimal_poly_degree);
}