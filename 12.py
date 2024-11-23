# Napisz program, który wyświetla wszystkie potęgi liczby 2 nie większe niż podana przez
# użytkownika liczba naturalna N.

N = int(input("Podaj liczbę naturalną: "))

liczba = 1
while liczba < N:
    print(liczba)
    liczba = liczba * 2