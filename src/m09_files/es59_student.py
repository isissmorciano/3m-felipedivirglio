import json


def salva_inventario(prodotti: list[dict], nome_file: str) -> None:
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            json.dump(prodotti, file, indent=4)
        print(f"File '{nome_file}' salvato con successo.")
    except IOError as e:
        print(f"Errore durante il salvataggio del file: {e}")


def carica_inventario(nome_file: str) -> list[dict]:
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            prodotti = json.load(file)
        return prodotti
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non è stato trovato.")
        return []
    except json.JSONDecodeError as e:
        print(f"Errore nel parsing JSON: {e}")
        return []


def filtra_per_categoria(prodotti: list[dict], categoria: str) -> list[dict]:
    filtrati = []
    for prodotto in prodotti:
        if prodotto["categoria"] == categoria:
            filtrati.append(prodotto)
    return filtrati


def calcola_totale_categoria(prodotti: list[dict], categoria: str) -> float:
    totale = 0.0
    for prodotto in prodotti:
        if prodotto["categoria"] == categoria:
            totale += prodotto["prezzo"] * prodotto["quantita"]
    return totale


def main() -> None:
    prodotti = [
        {"nome": "Mela", "categoria": "Frutta", "prezzo": 2.5, "quantita": 10},
        {"nome": "Pane", "categoria": "Pane", "prezzo": 1.0, "quantita": 5},
        {"nome": "Banana", "categoria": "Frutta", "prezzo": 1.8, "quantita": 8}
    ]
    
    nome_file = "inventario.json"
    salva_inventario(prodotti, nome_file)
    
    prodotti_caricati = carica_inventario(nome_file)
    if prodotti_caricati:
        frutta = filtra_per_categoria(prodotti_caricati, "Frutta")
        totale_frutta = calcola_totale_categoria(prodotti_caricati, "Frutta")
        print(f"Prodotti Frutta: {frutta}")
        print(f"Totale valore Frutta: {totale_frutta:.1f}")


main()