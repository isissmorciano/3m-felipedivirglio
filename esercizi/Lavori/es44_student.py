# template: ripeti finché la condizione non è soddisfatta
while True:
    valore:int = int(input("Inserisci un valore: "))  # leggi input
    # controlla se l'input soddisfa la condizione desiderata
    if valore >= 0:
        print(f"Numero valido: {valore}")        # azione quando l'input è valido
        break
    else: 
        print("Numero non valido scriverne uno nuovo!")
    # azione quando l'input non è valido (messaggio, nuovo tentativo, ...)