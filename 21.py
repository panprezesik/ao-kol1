# Napisz program, który wyznacza średnią z elementów wektora i wyznacza ile elementów
# jest mniejszych i ile większych od średniej.
import numpy as np
import json

wektor = np.array(json.loads(input("Podaj wektor: "))) # [1, 2, 3, 4, 5]

suma = 0
# Obliczanie średniej
for i in wektor: # Bierze każdy element z wektora i dodaje go do sumy
    suma += i

srednia = suma / wektor.shape[0]
print(srednia)

# Wyznaczanie mniejszych i większych od średniej
wieksze = 0
mniejsze = 0

for i in wektor: # Bierze każdy element z wektora i sprawdza czy jest większy, czy mniejszy od średniej
    if i > srednia:
        wieksze += 1
    elif i < srednia:
        mniejsze += 1
print(f"Mniejszych od średniej: {mniejsze}, większych od średniej: {wieksze}")