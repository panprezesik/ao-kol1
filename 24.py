# Napisz program, który wczytuje rozmiar wektora. Tworzy wektor samych zer o podanej
# długości, następnie uzupełnia ten wektor wartościami podanymi przez użytkownika
# zaczynając od ostatniego elementu, tj. uzupełnia wektor w odwrotnej kolejności.

import numpy as np
import json

n = int(input("Podaj rozmiar wektora: ")) # Zapytanie o rozmiar wektora
wektor = np.zeros(n) # Tworzy wektor zer o rozmiarze n

for i in range(n):
    wektor[n - i - 1] = int(input("Podaj wartość: ")) # Zapytanie o wartość i zapisanie jej w danej pozycji wektora

print(wektor)