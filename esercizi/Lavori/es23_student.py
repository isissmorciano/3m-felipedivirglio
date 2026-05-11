nomi: list[str] = ["Roma", "Milano", "Napoli"]
popolazione: list[int] = [2800000, 1400000, 1000000]
area: list[float] = [1285.0, 181.0, 117.0]

if len(nomi) == len(popolazione) == len(area):
    print("Le liste hanno la stessa lunghezza.")
else:
    print("Le liste non hanno la stessa lunghezza.")

for i in range(len(nomi)):
    densita = popolazione[i] / area[i]
    print(f"La densità di popolazione di {nomi[i]} è di {densita:.2f} abitanti per km².")

densita_massima: float = max(popolazione[i] / area[i] for i in range(len(nomi)))
print(f"La densità di popolazione massima è di {densita_massima:.2f} abitanti per km².")

contatore: int = 0
for i in range(len(nomi)):
    densita = popolazione[i] / area[i]
    if densita > 3000:
        contatore += 1
print(f"Ci sono {contatore} città con una densità di popolazione superiore a 3000 abitanti per km².")
