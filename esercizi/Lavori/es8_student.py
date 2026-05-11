Anni = int(input("Inserisci l'anno:"))

if (Anni % 4 == 0 and Anni % 100 != 0) or (Anni % 400 == 0):
    print(f"L'anno {Anni} è bisestile.")
else:
    print(f"L'anno {Anni} non è bisestile.")