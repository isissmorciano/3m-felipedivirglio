# # Esercizio 35: Conteggio di frequenze in una lista

# ## Obiettivo
# Creare un dizionario per contare la frequenza di ogni elemento in una lista data.

# ## Istruzioni
# 1. Definisci una lista di parole (es. ["rosso", "blu", "rosso", "verde", "blu"]).
# 2. Inizializza un dizionario vuoto per le frequenze.
# 3. Usa un ciclo per scorrere la lista: per ogni parola, incrementa il conteggio nel dizionario (usa `get()` per gestire chiavi nuove).
# 4. Stampa le frequenze usando `.items()` in formato "Parola: Conteggio".

# ## Nota
# Il metodo `get(chiave, default)` restituisce il valore se la chiave esiste, altrimenti il default (utile per inizializzare a 0).

# ## Esempio
# Per la lista ["rosso", "blu", "rosso"], output:
# rosso: 2
# blu: 1

# colori = ["rosso", "blu", "rosso", "verde", "blu"],
colori = ["rosso", "blu", "rosso", "verde", "blu"]
frequenze_dict = {}

# codice...

print(f"Per la lista: {colori}")
for colore in colori:
    print(colore)
    # frequenze_dict[colore] = frequenze_dict.get(colore, 0) + 1
    if not colore in frequenze_dict:
        frequenze_dict[colore] = 1
    else:
        frequenze_dict[colore] = frequenze_dict[colore] + 1
for colore, frequenza in frequenze_dict.items():
    print(f"{colore}: {frequenza}")
