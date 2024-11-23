# Program, który wypełnia 'lewy' trójkąt macierzy kwadratowej o wymiarach NxN
# kolejnymi liczbami naturalnymi (reszta elementów = 0). Wartość N podawana przez
# użytkownika na wejściu.
# Np. N = 3
# macierz:
# 1 2 3
# 4 5 0
# 6 0 0

import numpy as np

N = int(input("Podaj N: "))
macierz = np.zeros((N, N)) # Tworzy macierz NxN wypełnioną zerami

licznik = 1

for i in range(macierz.shape[0]): # Przechodzimy po wierszach
    for j in range(macierz.shape[1] - i): # Przechodzimy po kolumnach (tylko lewy trójkąt). Wartość kolumny zależy od wiersza, dzięki czemu wypełniamy tylko lewy trójkąt
        macierz[i][j] = licznik # Wstawiamy licznik
        licznik += 1 # Zwiększamy liczniks

# Jest to tylko jedno z wielu możliwych rozwiązań. Można to zrobić na wiele innych sposobów. :-)

print(macierz)