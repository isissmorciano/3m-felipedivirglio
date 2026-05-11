giocatori = {
    "Mario": 85,
    "Luca": 92,
    "Anna": 78,
    "Giulia": 95 
}

giocatori_max = ""
punteggio_max = 0

for punteggio in giocatori:
    if punteggio[giocatori] > punteggio_max:
        punteggio_max = punteggio[giocatori]
        giocatori_max = giocatori

