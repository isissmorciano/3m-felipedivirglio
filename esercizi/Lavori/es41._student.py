# Scrivi un programma che legga un testo dall'utente e lo analizzi utilizzando cicli e dizionari. Utilizza metodi delle stringhe per contare i caratteri totali, le parole e le frasi. Formatta l'output utilizzando sequenze di escape (come tab e newline).

# **Esempio di input/output:**

# - Input: "Inserisci un testo: Ciao mondo. Python è fantastico."
# - Output:
# ```
# Analisi testo:
# 	Caratteri: 30
# 	Parole: 5
# 	Frasi: 2
# ```


testo = input("Inserisci un testo: ").strip()
if not testo:
    print("Errore: testo vuoto.")
    exit()

# Metodi e analisi
num_caratteri = len(testo)
parole = testo.split()
num_parole = len(parole)
frasi = testo.split(".")
num_frasi = len(frasi)


# Output formattato
print(
    f"Analisi testo:\n\tCaratteri: {num_caratteri}\n\tParole: {num_parole}\n\tFrasi: {num_frasi}\n\t"
)