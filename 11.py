# Napisz program, który wyświetla wszystkie dodatnie liczby nieparzyste mniejsze od
# podanej przez użytkownika liczby naturalnej N.

N = int(input("Podaj liczbę naturalną: "))

for i in range(N):
    if i % 2 == 1:
        print(i)