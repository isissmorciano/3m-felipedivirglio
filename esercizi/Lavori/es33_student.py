# 1.Inizia con un dizionario vuoto. Aggiungi coppie chiave-valore per colori e codici RGB (es. "rosso": "#FF0000"). 
# 2.Poi, usa .keys() per verificare se un colore specifico (inserito dall'utente) 
# è presente nel dizionario, stampando un messaggio appropriato (es. "Colore presente" o "Colore non trovato").

colori = {}
colori["rosso"] = "#FF0000"
colori["blu"] = "#0000FF"
colori["verde"] = "#00FF00"


colore_da_cercare = input("Inserisci un colore da verificare: ")
if colore_da_cercare in colori.keys():
    print("Colore presente")
else:
    print("Colore non trovato")