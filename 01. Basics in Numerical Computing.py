import numpy as np

# Solving a simple matrix equation Ax = B

A = np.array([[3, 2], [1, 4]])  # Coefficient matrix
B = np.array([8, 10])           # Result vector

# Solve for x
x = np.linalg.solve(A, B)
print("Solution x:", x)
