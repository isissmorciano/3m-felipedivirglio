from .canzoni_student import info_canzone


def crea_playlist(nome: str) -> dict:
    return {
        "nome": nome,
        "canzoni": []
    }

def aggiungi_canzone(playlist: dict, canzone: dict) -> None:
    playlist["canzoni"].append(canzone)


def rimuovi_canzone(playlist: dict, indice: dict) -> None:
    if 0 <= indice < len(playlist["canzoni"]):
        playlist["canzoni"].pop(indice)
    else:
        print(f"Indice {indice} non valido.")


def durata_totale(playlist: dict) -> int:
    return sum(canzone["durata"]for canzone in playlist["canzoni"])



def mostra_playlist(playlist: dict) -> str:
    if not playlist:
        return print(f"La playlist {playlist} è vuota.")
    
    nome_playlist = [f"Playlist: {playlist['nome']}"]
    for i, canzone in enumerate(playlist["canzoni"], 1):
        nome_playlist.append(f"{i}. {info_canzone(canzone)}")


    durata = durata_totale(playlist)
    minuti = durata // 60
    secondi = durata % 60
    return print(f"Durata della playlist: {minuti}:{secondi:02d}")
    