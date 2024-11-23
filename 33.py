# Napisz program, który oblicza średnie osobno z każdego wiersza macierzy wejściowej.

import numpy as np
import json

macierz = np.array(json.loads(input("Podaj macierz: "))) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(macierz.shape[0]):
    suma = 0
    ilosc = 0
    for j in range(macierz.shape[1]): # Przechodzimy po każdym elemencie w wierszu
        suma += macierz[i][j] # Dodajemy element do sumy
        ilosc += 1 # Zwiększamy ilość elementów
    print("Średnia z wiersza", i, "wynosi:", suma/ilosc)