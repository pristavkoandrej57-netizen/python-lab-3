
import numpy as np


A = np.array([[4, -1.5, 2, 0.5],
              [1, 5, -2, 1.2],
              [-2, 1, 6, -1],
              [0.5, 2, -1, 7]])

B = np.array([[11.05],
              [-6.82],
              [11.5],
              [-0.5]])


det_A = np.linalg.det(A)
print("det(A) =", det_A)
print("cond(A) =", np.linalg.cond(A))

if np.isclose(det_A, 0):
    print("Определитель равен нулю, система не имеет единственного решения")
else:

    X1 = np.linalg.inv(A) @ B


    X2 = np.linalg.solve(A, B)


    print("\nНорма разности решений ||X1 - X2|| =", np.linalg.norm(X1 - X2))


    print("Невязка ||A*X1 - B|| =", np.linalg.norm(A @ X1 - B))
    print("Невязка ||A*X2 - B|| =", np.linalg.norm(A @ X2 - B))


    print("\nРешение X (округлено до 0.1):")
    print(np.round(X2.flatten(), 1))