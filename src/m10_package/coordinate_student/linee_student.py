from .punti_student import distanza_tra_punti


def crea_linea(p1: dict, p2: dict) -> dict:
    linea = {"p1": p1, "p2": p2}
    return linea

def lungezza_linea(linea: dict) -> float:
    p1 = linea["p1"]
    p2 = linea["p2"]
    distanza = distanza_tra_punti(p1, p2)
    return distanza


def punto_medio(linea: dict):
    p1 = linea["p1"]
    p2 = linea["p2"]
    medio_di_x = (p1["x"] + p2["x"]) / 2
    medio_di_y = (p1["y"] + p2["y"]) / 2
    return {'x': medio_di_x, 'y': medio_di_y}

def info_linea(linea: dict) -> str:
    return f"Linea da {linea['p1']} a {linea['p2']}"