import math

a: float = float(input("inserisci la variabile a:"))
b: float = float(input("inserisci la variabile b:"))
c: float = float(input("inserisci la variabile c:"))

discriminante: float = b**2 - 4*a*c

if discriminante > 0:
    x1: float = (-b + math.sqrt(discriminante)) / (2*a)
    x2: float = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"La soluzione x1 = {x1} x2 e = {x2}")
elif discriminante == 0:
    x: float = -b / (2*a)
    print(f"la doppia soluzione e x = {x}")
else:
    print(f"non ci sono soluzioni.")
