# Direct Method

import numpy as np

# Gaussian elimination using NumPy
A = np.array([[3, 2], [1, 4]])
B = np.array([8, 10])
x = np.linalg.solve(A, B)  # Direct method
print("Solution using Direct Method:", x)
