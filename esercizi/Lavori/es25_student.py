n: int = int(input("Inserisci un numero di righe: "))
m: int = int(input("Inserisci un numero di colonne: "))

matrice: list[list[int]] = [[i + j for j in range(m)] for i in range(n)]
for riga in matrice:
    print(riga)