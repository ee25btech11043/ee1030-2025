import numpy as np

def check_eigenvalues(matrix, target_eigenvalues):
    """
    Calculates the eigenvalues of a 2x2 matrix and checks if they match
    the target eigenvalues.

    Args:
        matrix (np.array): A 2x2 NumPy array representing the matrix.
        target_eigenvalues (set): A set of the target eigenvalues (e.g., {1, 6}).

    Returns:
        bool: True if the calculated eigenvalues match the target, False otherwise.
        set: The calculated eigenvalues (rounded for comparison).
    """
    # Calculate eigenvalues using numpy's eig function
    # eig returns two arrays: eigenvalues and eigenvectors. We only need eigenvalues.
    eigenvalues, _ = np.linalg.eig(matrix)

    # Convert complex eigenvalues to real if they are essentially real (i.e., imaginary part is negligible)
    # And round them to a few decimal places
    calculated_eigenvalues = set(round(val.real, 6) for val in eigenvalues)

    return calculated_eigenvalues == target_eigenvalues, calculated_eigenvalues

# Define the target eigenvalues
target_eigenvalues = {1.0, 6.0}

# Define the matrices as NumPy arrays
matrices = {
    "a": np.array([[5, -2], [-2, 2]]),
    "b": np.array([[3, -1], [-2, 2]]),
    "c": np.array([[3, -1], [-1, 2]]),
    "d": np.array([[2, -1], [-1, 3]])
}

print(f"Searching for a matrix with eigenvalues: {target_eigenvalues}\n")

# Iterate through each matrix and check its eigenvalues
for label, matrix in matrices.items():
    print(f"Checking Matrix {label}:\n{matrix}")
    match, calculated_eigs = check_eigenvalues(matrix, target_eigenvalues)

    if match:
        print(f"  Result: This matrix hs the target eigenvalues {calculated_eigs}!\n")
    else:
        print(f"  Result: Calculated eigenvalues are {calculated_eigs}, which do NOT match the target.\n")