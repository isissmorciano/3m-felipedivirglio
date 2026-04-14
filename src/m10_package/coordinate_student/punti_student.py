import math

def crea_punto(x: float, y: float) -> dict:
    #x = float(input("Inserisci la coordinata x: "))
    #y = float(input("Inserisci la coordinata y: "))
    punto = {"x": x, "y": y}
    return punto

def distanza_tra_punti(p1: dict, p2: dict) -> float:
    distanza_di_x = p2["x"] - p1["x"]
    distanza_di_y = p2["y"] - p1["y"]
    distanza = math.sqrt(distanza_di_x**2 + distanza_di_y**2) 
    return distanza

def info_punto(punto: dict) -> str:
    return f"Le tuo coordinate sono ({punto['x']}, {punto['y']})"