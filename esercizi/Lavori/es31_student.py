# 1.Crea un dizionario di libri e autori (es. {"1984": "Orwell", "Il Signore degli Anelli": "Tolkien", "Harry Potter": "Rowling"}). 
# 2.Usa il metodo .keys() (che restituisce una vista di tutte le chiavi del dizionario) per stampare un elenco di tutti i titoli dei libri, 
# uno per riga.

libri: dict[str, str] = {"1984": "Orwell", "Il Signore degli Anelli": "Tolkien", "Harry Potter": "Rowling"}

print("Titoli dei libri:")
for titolo in libri.keys():
    print(titolo)