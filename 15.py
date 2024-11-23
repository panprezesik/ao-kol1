# Napisz program, który pobiera dwie liczby A i B (A musi być < od B). Następnie
# wyświetla wszystkie wartości od A do B, czyli wartości A, A+1, A+2, ..., B.

A = int(input("Podaj A: "))
B = int(input("Podaj B: "))

if A < B:
    for i in range(A, B + 1):
        print(i)