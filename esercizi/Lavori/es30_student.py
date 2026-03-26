# 1.Scrivi un programma che crea un dizionario di prodotti e prezzi (es. {"mela": 1.5, "banana": 2.0, "arancia": 1.8}). 
# 2.Usa il metodo .values() (che restituisce una vista di tutti i valori del dizionario) 
# per contare quanti prodotti costano più di 1.7 euro. 
# 3.Stampa il conteggio.

prodotti: dict[str, float | str] = {"mela": 1.5, "banana": 2.0, "arancia": 1.8}

conteggio = 0
for prezzo in prodotti.values():
    if prezzo > 1.7:
        conteggio += 1

print(f"Numero di prodotti che costano più di 1.7 euro: {conteggio}")