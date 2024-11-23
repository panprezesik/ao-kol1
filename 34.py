# Napisz program, który znajduje minimalną wartość i maksymalną wartość osobno w
# każdej kolumnie macierzy wejściowej.

import numpy as np
import json

macierz = np.array(json.loads(input("Podaj macierz: "))) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(macierz.shape[1]):
    min = macierz[0][i] # Przypisujemy pierwszy element z kolumny
    max = macierz[0][i] # Przypisujemy pierwszy element z kolumny
    for j in range(macierz.shape[0]): # Przechodzimy po każdym elemencie w kolumnie
        if macierz[j][i] < min: # Jeśli element jest mniejszy od aktualnego minimum dla kolumny
            min = macierz[j][i]
        if macierz[j][i] > max: # Jeśli element jest większy od aktualnego maksimum dla kolumny
            max = macierz[j][i]
    print("Minimalna wartość w kolumnie", i, "wynosi:", min, "Maksymalna wartość w kolumnie", i, "wynosi:", max) # Wyświetlamy minimum i maksimum dla kolumny