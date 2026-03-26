from .punti_student import distanza_tra_punti


def crea_linea(p1: dict, p2: dict) -> dict:
    p1 = input("Inserisci p1: ")
    p2 = input("Inserisci p2: ")
    linea = [p1,p2]
    return linea

def lungezza_linea(linea: dict) -> float:
    p1 = linea
    p2 = linea
    distanza = distanza_tra_punti(p1, p2)
    return distanza


def punto_medio(linea: dict):
    p1 = linea
    p2 = linea
    medio_di_x = (p1[0] + p2[0]) / 2
    medio_di_y = (p1[1] + p2[1]) / 2
    return {'x': medio_di_x, 'y': medio_di_y}

def info_linea(linea: dict) -> str:
    return f"Linea da {linea[0]} a {linea[1]}"