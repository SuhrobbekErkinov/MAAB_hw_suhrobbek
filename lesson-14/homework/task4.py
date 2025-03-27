import numpy as np

A = np.array([
    [10, -2, 3],
    [-2, 8, 1],
    [3, -1, 6]
])

B = np.array([12, -5, 15])

solution = np.linalg.solve(A, B)

if __name__ == "__main__":
    print(solution)