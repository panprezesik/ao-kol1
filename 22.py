# Napisz program, który wyświetli na ekranie wektor, który jest wektorem utworzonym w
# odwrotnej kolejności do wektora zdefiniowanego w programie. Np. wektor w = (2, 5, 7,8) 
# to wyświetlony zostanie w_odwrotny = (8, 7, 5, 2).

import numpy as np
import json

A = np.array(json.loads(input("Podaj wektor: "))) # [1, 2, 3, 4, 5]
B = np.zeros(A.shape) # Tworzy wektor B o takim samym rozmiarze jak A

for i in range(A.shape[0]):
    B[B.shape[0] - i - 1] = A[i]

print(B)