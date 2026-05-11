squadre: list[str] = ["Milan","Juventus","Inter"]
punteggi: list[int] = [75, 80, 70]

print(f"{squadre[0]} ha totalizzato {punteggi[0]} punti")

somma_dei_punteggi: int = 0
for punteggio in punteggi:
    somma_dei_punteggi += punteggio

media_dei_punteggi: float = somma_dei_punteggi / len(punteggi)

print(f"La somma dei {len(punteggi)} punteggio delle squadre vale: {media_dei_punteggi:.2f}")

massimo_dei_punteggi: int = max(punteggi)
print(f"Il punteggio massimo é: {massimo_dei_punteggi}")

minimo_dei_punteggi: int = 100
for punteggio in punteggi:
    if punteggio < minimo_dei_punteggi:
        minimo_dei_punteggi = punteggio
print(f"Il punteggio minimo é: {minimo_dei_punteggi}")

for squadra in squadre:
    print(squadra)
    for punteggio in punteggi:
        print(punteggio)

n = 0 
for squadra in squadre:
    print(f"{squadre[n]} hanno un punteggio di {punteggi[n]}")
    n += 1

lunghezza_lista = len(squadre)
for i in range(lunghezza_lista):
    print(f"{squadre[i]} hanno un punteggio di: {punteggi[i]}")
