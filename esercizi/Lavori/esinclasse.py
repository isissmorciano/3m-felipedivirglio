nomi: list[str] = ["Alice","Bob","Charlie"]
voti: list[int] = [8, 7, 9]

# print("Alice ha preso 8")
print(f"{nomi[0]} ha preso {voti[0]}")


# somma tutti i voti
somma_dei_voti: int = 0
for voto in voti:
    somma_dei_voti +=  voto
# media dei voti
media_dei_voti: float = somma_dei_voti / len(voti)

print(f"La somma dei {len(voti)} voti degli studenti vale:  {media_dei_voti:.2f}")

massimo_dei_voti: int = max(voti)
print(f"Il voro massimo è: {massimo_dei_voti}")

minimo_dei_voti: int = 10
for voto in voti:
    if voto < minimo_dei_voti:
        minimo_dei_voti = voto
print(f"Il voto minimo è: {minimo_dei_voti}")

# stampare lista studenti
for nome in nomi:
    print(nome)
    for voto in voti:
        print(voto)

n = 0
for nome in nomi:
    print(f"{nomi[n]} ha preso {voti[n]}")
    n += 1

lunghezza_lista = len(nomi) # len(voti)
for i in range(lunghezza_lista):
    print(f"{nomi[i]} ha preso {voti[i]}")
