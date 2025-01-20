# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

# Initialize the given utility matrix M with blank entries as NaN
M = np.array([
    [5, 2, 4, 4, 3],
    [3, 1, 2, 4, 1],
    [2, np.nan, 3, 1, 4],
    [2, 5, 4, 3, 5],
    [4, 4, 5, 4, np.nan]
])

# Initialize U and V with all ones
n, m = M.shape  # Number of users (rows) and items (columns)
d = 2  # Number of latent dimensions
U = np.ones((n, d))
V = np.ones((d, m))

# Function to compute RMSE
def compute_rmse(M, U, V):
    P = np.dot(U, V)
    errors = []
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if not np.isnan(M[i, j]):  # Only consider non-blank entries
                errors.append((M[i, j] - P[i, j]) ** 2)
    return np.sqrt(np.mean(errors))

# Optimize a specific entry in U
def optimize_u(M, U, V, row, col):
    numerator, denominator = 0, 0
    for j in range(M.shape[1]):
        if not np.isnan(M[row, j]):  # Only consider non-blank entries
            predicted = sum(U[row, k] * V[k, j] for k in range(d) if k != col)
            numerator += V[col, j] * (M[row, j] - predicted)
            denominator += V[col, j] ** 2
    U[row, col] = numerator / denominator

# Optimize a specific entry in V
def optimize_v(M, U, V, row, col):
    numerator, denominator = 0, 0
    for i in range(M.shape[0]):
        if not np.isnan(M[i, col]):  # Only consider non-blank entries
            predicted = sum(U[i, k] * V[k, col] for k in range(d) if k != row)
            numerator += U[i, row] * (M[i, col] - predicted)
            denominator += U[i, row] ** 2
    V[row, col] = numerator / denominator


rmse1 = compute_rmse(M, U, V)
print(f"RMSE before optimization: {rmse1}")


# Optimize u32 (row 2, column 1 in 0-based indexing)
optimize_u(M, U, V, 2, 1)

# Optimize v41 (row 0, column 3 in 0-based indexing)
optimize_v(M, U, V, 0, 3)

# Compute and display the new RMSE
rmse = compute_rmse(M, U, V)
print(f"Updated U matrix:\n{U}")
print(f"Updated V matrix:\n{V}")
<<<<<<< HEAD
<<<<<<< HEAD
print(f"RMSE after optimization: {rmse}")


def functionality(x):
    x = 12
    return x
=======
print(f"RMSE after optimization: {rmse}")
>>>>>>> main
=======
print(f"RMSE after optimization: {rmse}")
>>>>>>> parent of 0c56a38 (updated code)
