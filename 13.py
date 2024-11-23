# Napisz program, który wczytuje liczby podawane przez użytkownika do momentu, kiedy
# poda liczbę 0. Następnie program wyświetla średnią arytmetyczną wszystkich
# dotychczasowo podanych liczb.

i = 1
suma = 0
ilosc = 0
while i != 0:
    i = int(input("Podaj liczbę: "))
    if i != 0: # == != >= <= > <
        suma += i
        ilosc += 1

print("Średnia: ", suma / ilosc)