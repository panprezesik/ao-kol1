# Napisz program, który wczytuje liczby podawane przez użytkownika do momentu, kiedy
# poda liczbę 0. Następnie program wyświetla największą i najmniejszą wartość z
# podanych wcześniej liczb (nie licząc zera).

# 1 krok (MAX i MIN jest równe pierwszej liczbie podanej przez użytkownika)
i = int(input("Podaj liczbę: "))
min = i
max = i

# 2 krok (pętla)
while i != 0:
    i = int(input("Podaj liczbę: "))
    if i != 0:
        if i > max:
            max = i
        if i < min:
            min = i

print(f"MAX: {max}, MIN: {min}") # Alternatywnie można użyć np. print("MAX", max, "MIN", min)