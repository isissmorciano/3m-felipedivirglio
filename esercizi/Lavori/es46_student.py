def calcola_area_triangolo(base, altezza) -> float:
    risultato = (base * altezza)/2
    return risultato


base:float = float(input("Inserisci base del triangolo: "))
altezza:float = float(input("Inserisci altezza del triangolo: "))
area = calcola_area_triangolo(base, altezza)
print(f"L'area del triangolo è: {area}")
