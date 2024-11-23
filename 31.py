# Napisz program, który tworzy nową macierz poprzez przepisanie wierszy macierzy
# wejściowej w odwrotnej kolejności.
# Np.
# macierz zdefiniowana w programie:
# 3 1 0 6
# 5 5 3 2
# 1 1 0 1
# macierz wyjściowa:
# 1 1 0 1
# 5 5 3 2
# 3 1 0 6

import numpy as np
import json

A = np.array(json.loads(input("Podaj macierz: "))) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = np.zeros(A.shape) # Tworzy macierz B o takim samym rozmiarze jak A

for i in range(A.shape[0]):
    B[B.shape[0] - i - 1] = A[i]

print(B)