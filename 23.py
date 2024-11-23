# Napisz program, który oblicza średnią z elementów wektora, które znajdują się na
# pozycjach o parzystych indeksach.

import numpy as np
import json
wektor = np.array(json.loads(input("Podaj wektor: "))) # [1, 2, 3, 4, 5]

suma = 0
ilosc = 0

for i in range(wektor.shape[0]):
    if i % 2 == 0: # Sprawdzamy czy indeks (pozycja) jest parzysty
        suma += wektor[i] # Dodajemy element wektora do sumy
        ilosc += 1 # Zwiększamy ilość elementów

print("Średnia z elementów wektora, które znajdują się na pozycjach o parzystych indeksach wynosi:", suma/ilosc)