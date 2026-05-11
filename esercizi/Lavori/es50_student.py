def aggiungi_elemento():
    nome_elemento = str(input("Inserisci il nome dell'elemento: "))
    prezzo_elemento = float(input("Inserisci il prezzo dell'elemento: "))
    return [nome_elemento, prezzo_elemento]

def rimuovi_elemento(lista_spesa):
    nome_elemento = str(input("Inserisci il nome dell'elemento da rimuovere: "))
    prezzo_elemento = float(input("Inserisci il prezzo dell'elemento da rimuovere: "))
    lista_spesa.remove(nome_elemento)
    lista_spesa.remove(prezzo_elemento)

def visualizza_lista(lista_spesa):
    print(lista_spesa)

def calcola_totale(lista_spesa):
    totale = 0
    for i in range(1, len(lista_spesa), 2):
        totale += lista_spesa[i]
    return totale

def main():
    lista_spesa: list[str | float] = []
    while True:
        print("Menu:")
        print("1. Aggiungi elemento")
        print("2. Rimuovi elemento")
        print("3. Visualizza lista")
        print("4. Calcola totale")
        print("5. Esci")
        scelta = input("Scegli un'opzione: ")
        
        if scelta == '1':
            elemento = aggiungi_elemento()
            lista_spesa.extend(elemento)
        elif scelta == '2':
            rimuovi_elemento(lista_spesa)
        elif scelta == '3':
            visualizza_lista(lista_spesa)
        elif scelta == '4':
            totale = calcola_totale(lista_spesa)
            print(f"Totale: {totale}")
        elif scelta == '5':
            break
        else:
            print("Scelta non valida, riprova.")

main()