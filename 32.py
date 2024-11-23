# Napisz program, który tworzy nową macierz poprzez przepisanie kolumn macierzy
# wejściowej w odwrotnej kolejności.
# Np.
# macierz zdefiniowana w programie:
# 3 1 0 6
# 5 5 3 2
# 1 1 0 1
# macierz wyjściowa:
# 6 0 1 3
# 2 3 5 5
# 1 0 1 1

import numpy as np
import json

A = np.array(json.loads(input("Podaj macierz: "))) # [[1, 2, 3], [4, 5, 6]]
B = np.zeros(A.shape) # Tworzy macierz B o wymiarach odwrotnych do A

for i in range(A.shape[0]): # Przechodzimy po wierszach
    for j in range(A.shape[1]): # Przechodzimy po kolumnach
        B[i][B.shape[1] - j - 1] = A[i][j] # Przepisujemy wartości z macierzy A do macierzy B w odwrotnej kolejności

print(B)