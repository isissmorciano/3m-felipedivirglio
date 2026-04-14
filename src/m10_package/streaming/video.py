def crea_video(titolo: str, durata: float, risoluzione: int, bitrate: int) -> dict:
    return {
        "titolo": titolo,
        "durata": durata,
        "risoluzione": risoluzione,
        "bitrate": bitrate
    }


def dimensione_video(video: dict) -> float:
    return (video["bitrate"] * video["durata"]) / (8 * 1024)


def info_video(video: dict):
    minuti = video["durata"] // 60
    secondi = video["durata"] % 60
    return f"{video['titolo']} - ({minuti}:{secondi:02d}) - {video['risoluzione']} - ({video['bitrate']} kbps)"