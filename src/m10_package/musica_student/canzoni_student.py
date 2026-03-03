def crea_canzone(titolo: str, artista: str, durata: int) -> dict:
    return {
        "titolo": titolo,
        "artista": artista,
        "durata": durata   
    }

def info_canzone(canzone: dict) -> str:
    
    minuti = canzone["durata"] // 60
    secondi = canzone["durata"] % 60
    return print(f"{canzone['titolo']} - {canzone['artista']} ({minuti}:{secondi:02d})")