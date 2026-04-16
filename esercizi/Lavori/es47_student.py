def chiedi_numeri() -> list[float]:
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero:"))
    return [num1, num2]


def scegli_operazione() -> str:
    print("Scegli un'operazione: ")
    print("Addizione (+)")
    print("Sottrazione (-)")
    print("Moltiplicazione (*)")
    print("Divisione (/)")
    scelta = input("Scegli il simbolo dell'operazione: ")
    if scelta == "+":
        return "+"
    elif scelta == "-":
        return "-"
    elif scelta == "*":
        return "*"
    elif scelta == "/":
        return "/"
    else:
        return ""
    
def calcola(num1: float, num2: float, operazione: str) -> float:
    if operazione == "+":
        return num1 + num2
    elif operazione == "-":
        return num1 - num2
    elif operazione == "*":
        return num1 * num2
    elif operazione == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Errore divisione per zero.")
            return None
    else:
        return None

def main():
    print("benvenuto nella Calcolatrice")
    numeri = chiedi_numeri()
    operazione = scegli_operazione()
    risultato = calcola(numeri[0], numeri[1], operazione)

    if risultato is not None:
        print(f"Il risultato è: {risultato}")
    else:
        print("Operazione non valida.")

main()
