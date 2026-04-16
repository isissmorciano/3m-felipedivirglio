def conta_parole(nome_file: str) -> dict[str, int]:
    conteggio = {}
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            contenuto = file.read().lower()
            contenuto = contenuto.replace(".", "").replace(",", "")
            parole = contenuto.split()
            for parola in parole:
                if parola in conteggio:
                    conteggio[parola] += 1
                else:
                    conteggio[parola] = 1
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non è stato trovato.")
    except IOError as e:
        print(f"Errore durante la lettura del file: {e}")
    return conteggio


def stampa_conteggio(dizionario: dict[str, int]) -> None:
    print("Conteggio parole:")
    for parola, numero in sorted(dizionario.items()):
        print(f"{parola}: {numero}")

    

def main() -> None:
    testo = "Python è un linguaggio di programmazione. Python è semplice e potente."
    nome_testo = "esercizio57.txt"

    nome_file = "esercizio57.txt"
    try:
        with open(nome_file, "w") as file:
            file.write(testo)
        print(f"File '{nome_file}' creato con successo.")
    except IOError as e:
        print(f"Errore durante la scrittura del file: {e}")
        return

main()