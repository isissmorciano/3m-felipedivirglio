Numeri = int(input("Quanti numeri interi vuoi inserire? "))

somma = 0 

for i in range(Numeri):
    numero = int(input(f"Inserisci il numero {i+1}:"))
    if numero > 0:
       somma += numero


print(f"La somma totale dei numeri inseriti è {somma}")

