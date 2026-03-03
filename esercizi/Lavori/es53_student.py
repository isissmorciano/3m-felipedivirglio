voti = [
    {"nome": "Alice", "voti": [8.5, 7.8, 9.0, 8.2]},
    {"nome": "Bob", "voti": [6.5, 7.0, 6.8, 7.2]},
    {"nome": "Charlie", "voti": [9.5, 9.2, 9.8, 9.0]},
    {"nome": "Diana", "voti": [7.0, 8.5, 7.5, 8.0]},
    {"nome": "Eve", "voti": [5.5, 6.0, 5.8, 6.2]},
]


def calcola_media(voti) -> float:
    return sum(voti) / len(voti)


def analizza_studente(nome, voti) -> dict:
    max_voto = max(voti)
    min_voto = min(voti)
    media = calcola_media(voti)

    return {
        "nome": nome,
        "media": media,
        "max": max_voto,
        "min": min_voto
    }

def stampa_intestazione():
    print(f"{'Nome':<10} {'Media':<10} {'Max':<10} {'Min':<10}")


def stampa_stundenti(analizza_studente):
    for studente in analizza_studente:
        print(f"{studente['nome']} Media: {studente['media']:.2f} Max: {studente['max']} Min: {studente['min']}")
    
def media_classe(risultati) -> float:
    totale = sum(studente['media'] for studente in risultati)
    return totale / len(risultati)

def main():
    risultati = []
    for studente in voti:
        risultato = analizza_studente(studente["nome"], studente["voti"])
        risultati.append(risultato)
        
    stampa_intestazione()
    stampa_stundenti(risultati)
    media = media_classe(risultati)
    print(f"\nMedia della classe: {media:.2f}")
main()