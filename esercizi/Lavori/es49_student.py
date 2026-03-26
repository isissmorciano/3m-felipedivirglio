import random

def genera_numeri() -> int:
    return random.randint(1, 100)

def chiedi_tentetativo() -> int:
    while True:
        tentetativo = input("Inserisci un numero tra 1 e 100: ")
        if tentetativo.isdigit():
            tentetativo = int(tentetativo)
            if 1 <= tentetativo <= 100:
                return tentetativo
        print("Numero non valido.")

def verifica_tentetativo(tentetativo: int, numero_segreto: int) -> bool:
    if tentetativo < numero_segreto:
        print("Troppo basso!")
        return False
    elif tentetativo > numero_segreto:
        print("Troppo alto!")
        return False
    else:
        print("\nHai indovinato!")
        return True

def aggiorna_contatore(tentativi: int) -> int:
    return tentativi + 1

def stampa_fine(tentativi: int):
    print(f"\nHai indovinato il numero in {tentativi} tentativi!\n")

def main():
    numero_segreto = genera_numeri()
    tentativi = 0

    while True:
        tentetativo = chiedi_tentetativo()
        tentativi = aggiorna_contatore(tentativi)
        if verifica_tentetativo(tentetativo, numero_segreto):
            break

    stampa_fine(tentativi)

main()