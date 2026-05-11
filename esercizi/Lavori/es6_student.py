
import math

voto: float = float(input("Inserire il voto:"))

if voto > 10 or voto < 0:
     print("Il voto non esiste")
elif voto <= 5:
     print("Giudizio insufficente")
elif voto <= 6.5:
     print("Giudizio sufficente")
elif voto > 7.5:
     print("Giudizio ottimo")

     