from musica_student import canzoni_student, playlist_student

def main():
    playlist_personale = playlist_student.crea_playlist("Le mie canzoni")
    # Crea le canzoni
    canzone1 = canzoni_student.crea_canzone("Bohemian Rhapsody", "Queen", 355)
    canzone2 = canzoni_student.crea_canzone("Stairway to Heaven", "Led Zeppelin", 482)
    canzone3 = canzoni_student.crea_canzone("Hotel California", "Eagles", 390)
    
    # Aggiungi le canzoni alla playlist

    playlist_student.aggiungi_canzone(playlist_personale, canzone1)
    playlist_student.aggiungi_canzone(playlist_personale, canzone2)
    playlist_student.aggiungi_canzone(playlist_personale, canzone3)

    print(playlist_student.mostra_playlist(playlist_personale))


main()