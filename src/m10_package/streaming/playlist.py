from .video import info_video

def crea_playlist(nome: str) -> dict:
    return {
        "nome": nome,
        "video": []
    }

def aggiungi_video(playlist: dict, video: dict) -> None:
    playlist["video"].append(video)

def rimuovi_video(playlist: dict, indice: int) -> None:
    if 0 <= indice < len(playlist["video"]):
        playlist["video"].pop(indice)
    else: 
        print(f"Errore indice {indice} non valido.")

def durata_totale(playlist: dict) -> int:
    return sum(video["durata"] for video in playlist["video"])

def dimensione_totale(playlist: dict) -> int:
    return sum(video["bitrate"] for video in playlist ["video"])

def mostra_playlist(playlist: dict) -> str:
    if not playlist["video"]:
        return f"=== Playlist: {playlist['nome']} ===\n(Vuota )"

    linee = [f"=== Playlist: {playlist['nome']} ==="]
    for i, video in enumerate(playlist["video"], 1):
        linee.append(f"{i}. {info_video(video)}") 

    total = durata_totale(playlist)
    minuti = total // 60
    secondi = total % 60
    linee.append(f"\nDurata totale: {minuti}:{secondi:02d}")
    
    return "\n".join(linee)

def ordina_per_durata(playlist: dict) -> None:
    playlist["video"].sort(key=lambda v: v["durata"])
    
    