GEN = 1 
FEB = 2
MAR = 3
APR = 4
MAG = 5
GIU = 6
LUG = 7
AGO = 8
SET = 9 
OTT = 10 
NOV = 11
DIC = 12


sigla = input("inserisci la sigla del mese:")

if sigla in ["MAR", "APR", "MAG"]:
    stagione = "primavera"
elif sigla in ["GIU", "LUG", "AGO"]:
    stagione = "estate"
elif sigla in ["SET", "OTT", "NOV"]:
    stagione = "autunno"
elif sigla in ["GEN", "FEB", "DIC"]:
    stagione = "inverno"

print(f"La stagione del mese {sigla} è {stagione}:")