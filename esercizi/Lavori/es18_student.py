# INPUT
n = int(input("Inserisci il valore n: "))
x = int(input("Inserisci il valore x: "))

# CHECK
if n < 0:
    print("Errore n deve essere positivo.")
    exit(1) # esci dal programma con codice di errore 1
if x < 0:
    print("Errore x deve essere positivo.")
    exit(1)

# ELABORAZIONE
lista_delle_stringhe_lunghe: list[str] = []
for _ in range(n):
    stringa_utente = input("Inserisci una stringa: ")
    # controlla se la stringa ha lunghezza maggiore di x
    if len(stringa_utente) > x:
        # se si, aggiungerla a una lista
        lista_delle_stringhe_lunghe.append(stringa_utente)

print(lista_delle_stringhe_lunghe)
# contare il numero di elementi nella lista (srinche più lunga di x)
print(f"Numero di stringhe più lunghe di {x} : {len(lista_delle_stringhe_lunghe)}")

# Gestire il caso in cui nessuna stringa sia più lunga di x, stanpando un messaggio appropriato
if len(lista_delle_stringhe_lunghe) == 0:
    print(f"Nessuna stringa è più lunga di {x}.")
    exit(1)

# Se la lista non è vuota, calcolare la lunghezza media delle stringhe nella lista (somme delle lunghezze diviso il numero di stringhe)
somma_lunghezze: int = 0
for stringa in lista_delle_stringhe_lunghe:
    print(stringa)
    somma_lunghezze = somma_lunghezze + len(stringa) 

lunghezza_lista: int = len(lista_delle_stringhe_lunghe)
media_lunghezza_stringhe: float = somma_lunghezze / lunghezza_lista

# OUTPUT
