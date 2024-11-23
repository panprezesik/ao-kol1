# Napisz program, który wczytuje rozmiar wektora podany przez użytkownika i następnie
# tworzy wektor dwukrotnie dłuższy poprzez wpisywanie do elementów wektora o
# nieparzystych indeksach wartości podanych przez użytkownika, a w parzystych wpisuje
# wartość 0.
# Np. dlugosc_wektora = 3: wektor = (3, 0, 8, 0, 2, 0) <= To jest błąd w przykładzie, powinno być (0, 3, 0, 8, 0, 2)
# Liczenie indeksów zaczynamy od 0.

import numpy as np
import json

n = int(input("Podaj rozmiar wektora: ")) # Zapytanie o rozmiar wektora
wektor = np.zeros(n * 2) # Tworzy wektor zer o rozmiarze 2*n

for i in range(n):
    wektor[i * 2 + 1] = int(input("Podaj wartość: ")) # Zapytanie o wartość i zapisanie jej w danej nieparzystej pozycji wektora

print(wektor)