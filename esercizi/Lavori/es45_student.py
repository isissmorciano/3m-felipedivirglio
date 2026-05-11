import random


personaggio = {"nome": "Eroe", "livello": 1, "hp": 100, "attacco": 10}
inventario = []

oggetti_possibili = [
    {"nome": "Spada", "tipo": "arma", "valore": 20, "usato": False},
    {"nome": "Pozione", "tipo": "cura", "valore": 30, "usato": False},
    {"nome": "Arco", "tipo": "arma", "valore": 15, "usato": False},
    {"nome": "Scudo", "tipo": "difesa", "valore": 10, "usato": False},
    {"nome": "Anello", "tipo": "magia", "valore": 25, "usato": False},
]


while True:
    print("\n--- MENU ---")
    print("1. Esplora")
    print("2. Combatti")
    print("3. Inventario")
    print("4. Statistiche")
    print("5. Esci")

    scelta = input("Scegli un'opzione: ")

    if not scelta.isdigit():
        print("Errore: inserisci un numero valido.")
        continue

    scelta = int(scelta)

    
    if scelta == 1:
        oggetto = random.choice(oggetti_possibili)
        inventario.append(oggetto.copy())
        print(f"Hai trovato: {oggetto['nome']} ({oggetto['tipo']}, valore: {oggetto['valore']})")

  
    elif scelta == 2:
        if len(inventario) == 0:    
            print("Non hai oggetti per combattere. Esplora prima!")
            continue

        print("\n--- INVENTARIO PER COMBATTERE ---")
        for i in range(len(inventario)):
            oggetto = inventario[i]
            print(f"{i+1}. {oggetto['nome']} ({oggetto['tipo']}, valore: {oggetto['valore']}, usato: {oggetto['usato']})")

        scelta_ogg = input("Scegli un oggetto per combattere: ")

        if not scelta_ogg.isdigit():
            print("Input non valido.")
            continue

        scelta_ogg = int(scelta_ogg)

        if scelta_ogg < 1 or scelta_ogg > len(inventario):
            print("Oggetto inesistente.")
            continue

        oggetto = inventario[scelta_ogg - 1]

        if oggetto["usato"]:
            print("Questo oggetto è già stato usato!")
            continue

    
        hp_mostro = random.randint(50, 100)
        attacco_mostro = random.randint(5, 15)

        print(f"\nUn mostro appare! HP mostro: {hp_mostro}, Attacco: {attacco_mostro}")

      
        danno_giocatore = personaggio["attacco"] + oggetto["valore"]
        print(f"Attacchi con {oggetto['nome']} e infliggi {danno_giocatore} danni!")

        if danno_giocatore >= hp_mostro:
            print("Hai sconfitto il mostro!")
            personaggio["livello"] += 1
            print("Sali di livello!")
        else:
            danno_subito = attacco_mostro
            personaggio["hp"] -= danno_subito
            print(f"Il mostro ti colpisce! Perdi {danno_subito} HP.")

            if personaggio["hp"] <= 0:
                print("Sei morto! Game Over.")
                break

        oggetto["usato"] = True


    elif scelta == 3:
        if len(inventario) == 0:
            print("Inventario vuoto.")
        else:
            print("\n--- INVENTARIO ---")
            for oggetto in inventario:
                print(f"- Nome: {oggetto['nome']}, Tipo: {oggetto['tipo']}, Valore: {oggetto['valore']}, Usato: {oggetto['usato']}")


    elif scelta == 4:
        print("\n--- STATISTICHE ---")
        print(f"Nome: {personaggio['nome']}")
        print(f"Livello: {personaggio['livello']}")
        print(f"HP: {personaggio['hp']}")
        print(f"Attacco: {personaggio['attacco']}")
        print(f"Totale oggetti: {len(inventario)}")

    elif scelta == 5:
        print("Hai scelto di uscire dal gioco.")
        break

    else:
        print("Scelta non valida.")
