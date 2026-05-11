n: int = int(input("Inserisci un numero di righe: "))
m: int = int(input("Inserisci un numero di colonne: "))

matrice: list[list[int]] = [[1 for _ in range(m)] for _ in range(n)]
for riga in matrice:
    print(riga)