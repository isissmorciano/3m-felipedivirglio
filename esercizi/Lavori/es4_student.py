# Scrivere un programma che risolve  un' equazione di primo grado ax+b=0.

a = float(input("Inserisci il numero a:"))
b = float(input("Inserisci il numero b:"))

if a != 0: 
    x = -b / a
    print(f"La soluzione dell'equazione è x = {x}")
elif b == 0:
    print("L'equazione ha infinite soluzioni.")
else:
    print("L'equazione non ha soluzione")