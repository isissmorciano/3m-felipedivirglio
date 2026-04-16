from streaming import video, playlist

def main():
    playlist_personale = playlist.crea_playlist("Corso Python Base")

    video1 = video.crea_video("Introduzione a Python", 930, "1080p", 5000)
    video2 = video.crea_video("Variabili e Tipi", 1335, "720p", 3000)
    video3 = video.crea_video("Funzioni e Moduli", 1080, "1080p", 5000)
    video4 = video.crea_video("Liste e Dizionari", 1560, "480p", 2000)

    playlist.aggiungi_video(playlist_personale, video1)
    playlist.aggiungi_video(playlist_personale, video2)
    playlist.aggiungi_video(playlist_personale, video3)
    playlist.aggiungi_video(playlist_personale, video4)

    print(playlist.mostra_playlist(playlist_personale))


main()