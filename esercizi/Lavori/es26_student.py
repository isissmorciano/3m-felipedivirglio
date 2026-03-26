n: int = int(input("Quanti numeri interi positivi vuoi inserire?: "))
if n <= 0:
    print("Errore n deve essere un intero positivo.")
    
numeri: list[int] = []

for i in range(n):
    numero_inserito = int(input(f"Inserisci il numero {i+1}: "))
    numeri.append(numero_inserito)

print("Lista numeri:", numeri)


for i in range(len(numeri)):
    for j in range(i + 1, len(numeri)):
        if numeri[i] > numeri[j]:
            numeri[i], numeri[j] = numeri[j], numeri[i]


if len(numeri) == 0:
    print("Errore: la lista è vuota.")
else:
    print("Lista ordinata:", numeri)

print("Lista originale:", numeri)