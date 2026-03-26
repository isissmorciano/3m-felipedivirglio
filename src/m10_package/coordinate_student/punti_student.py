import math

def crea_punto(x: float, y: float) -> list:
    x = float(input("Inserisci la coordinata x: "))
    y = float(input("Inserisci la coordinata y: "))
    punto = [x, y]
    return punto

def distanza_tra_punti(p1: list, p2: list) -> float:
    distanza_di_x = p2[0] - p1[0]
    distanza_di_y = p2[1] - p1[1]
    distanza = math.sqrt(distanza_di_x**2 + distanza_di_y**2) 
    return distanza

def info_punto(punto: list) -> str:
    return f"Le tuo coordinate sono ({punto[0]}, {punto[1]})"