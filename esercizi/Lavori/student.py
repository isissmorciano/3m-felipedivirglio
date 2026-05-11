a = float(input("inserisci il numero a:"))
b = float(input("inserisci il numero b:"))
c = float(input("inserisci il numero c:"))

if a !=0:
    x = -b / c
    print(f"La soluzione dell'equazione è x = {x}")
elif b == 0:
    print("L'equazione ha infinite soluzioni.")
else:
    print("L'equazione non ha soluzione.")