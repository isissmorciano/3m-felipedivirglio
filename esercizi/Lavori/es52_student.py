def chiedi_dati() -> float:
    peso = float(input("Inserisci il tuo peso: "))
    altezza = float(input("Inserisci la tua altezza: "))
    if peso < 0:
        print("ERRORE inserisci un numero positivo.")
    if altezza < 0:
        print("ERRORE inserisci un numero positivo.")
    return peso, altezza

def calcolare(peso, altezza) -> float:
    BMI = peso / altezza**2
    return BMI

def colore_categoria(BMI) -> str:
    if BMI < 18.5:
        return "🔵 Sottopeso"
    elif 18.5 <= BMI < 24.9:
        return "🟢 Normopeso"
    elif 25 <= BMI < 29.9:
        return "🟡 Sovrappeso"
    else:
        return "🔴 Obeso"
    return colore_categoria


def stampa_risultato(peso, altezza, BMI, categoria):
   peso = print(f"Il tuo peso: {peso}")
   altezza = print(f"La tua altezza. {altezza}")
   BMI = print(f"Il tuo BMI: {BMI}")
   categoria = print(f"La tua categoria: {categoria}")


def main():
    while True:
        print("Menu:")
        print("1. Calcola BMI")
        print("2. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == '1':
            peso, altezza = chiedi_dati()
            BMI = calcolare(peso, altezza)
            categoria = colore_categoria(BMI)
            stampa_risultato(peso, altezza, BMI, categoria)
        elif scelta == '2':
            break
        else:
            print("Scelta non valida, riprova.")
    
main()

