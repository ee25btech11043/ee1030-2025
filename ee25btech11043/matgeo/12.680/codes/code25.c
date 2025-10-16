#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to swap two rows in a matrix
void swapRows(int *matrix, int r1, int r2, int cols) {
    for (int j = 0; j < cols; j++) {
        int temp = *(matrix + r1 * cols + j);
        *(matrix + r1 * cols + j) = *(matrix + r2 * cols + j);
        *(matrix + r2 * cols + j) = temp;
    }
}

// Function to calculate the rank of a matrix
int calculate_rank(int *matrix, int rows, int cols) {
    int rank = 0;
    int lead = 0; // Current column to process

    for (int r = 0; r < rows && lead < cols; r++) {
        int i = r;
        // Find a row with a non-zero element in the current column 'lead'
        while (i < rows && *(matrix + i * cols + lead) == 0) {
            i++;
        }

        if (i == rows) {
            // No pivot found in this column, move to the next column
            lead++;
            r--; // Re-process the current row with the new lead column
            continue;
        }

        // Swap the current row with the pivot row
        swapRows(matrix, r, i, cols);

        // Make the pivot element 1 (not strictly necessary for rank, but good for visualization)
        // For integer matrices, it's better to avoid division and use LCM/GCD for elimination.
        // However, for just rank, we can proceed with elimination directly.

        // Eliminate other rows
        for (i = 0; i < rows; i++) {
            if (i != r) {
                int factor = *(matrix + i * cols + lead);
                int pivot_val = *(matrix + r * cols + lead);

                // If the pivot value is 0, we've already handled it or it's not a pivot for this row
                if (pivot_val == 0) continue;

                // Perform row operation: R_i = R_i - (factor / pivot_val) * R_r
                // To avoid floating point, multiply row r by 'factor' and row i by 'pivot_val'
                // Then subtract: (pivot_val * R_i) - (factor * R_r)
                for (int j = lead; j < cols; j++) {
                    *(matrix + i * cols + j) = (pivot_val * *(matrix + i * cols + j)) - (factor * *(matrix + r * cols + j));
                }
            }
        }
        lead++;
    }

    // Count non-zero rows (each non-zero row indicates a pivot)
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (*(matrix + i * cols + j) != 0) {
                rank++;
                break; // Found a non-zero element in this row, move to the next row
            }
        }
    }

    return rank;
}