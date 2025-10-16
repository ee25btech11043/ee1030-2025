#include <stdio.h>

// Function to find the point of intersection of tangents at the ends of the latus rectum
// For y^2 = 4ax, the ends of the latus rectum are (a, 2a) and (a, -2a)
// The tangents are:
// at (a, 2a): y(2a) = 2a(x + a)  => 2ay = 2ax + 2a^2 => y = x + a
// at (a, -2a): y(-2a) = 2a(x + a) => -2ay = 2ax + 2a^2 => -y = x + a => y = -x - a
//  x + a = -x - a => 2x = -2a => x = -a
// Substitute x = -a into y = x + a => y = -a + a => y = 0
void findIntersectionOfTangents(double a_param, double *intersect_x, double *intersect_y) {
    *intersect_x = -a_param;
    *intersect_y = 0.0;
}