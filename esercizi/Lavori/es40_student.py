# Scrivi un programma che utilizzi il seguente dizionario per memorizzare dati di prodotti:

# prodotti = {
#     "prodotto1": {"nome": "Mela", "prezzo": 1.50, "quantita": 10},
#     "prodotto2": {"nome": "Banana", "prezzo": 2.00, "quantita": 5},
#     "prodotto3": {"nome": "Arancia", "prezzo": 1.20, "quantita": 8}
# }
# Per ciascun prodotto, esegui le seguenti operazioni usando cicli:

# Metodi stringa: Verifica se il nome inizia con 'M' e conta le occorrenze di 'a'.
# Formattazione: Calcola il totale con possibile sconto (10% se totale > 10 €) e formatta con 2 decimali.
# Stampa i risultati per ogni prodotto.

# Esempio di output: Prodotto: Mela, Totale: 13.50 € (sconto 10%), Inizia con 'M': True, Conteggio 'a': 1


prodotti = {
    "prodotto1": {"nome": "Mela", "prezzo": 1.50, "quantita": 10},
    "prodotto2": {"nome": "Banana", "prezzo": 2.00, "quantita": 5},
    "prodotto3": {"nome": "Arancia", "prezzo": 1.20, "quantita": 8}
}

for chiave, dati in prodotti.items():
    nome = dati["nome"]
    totale = dati["prezzo"] * dati["quantita"]
    sconto = 0.1 if totale > 10 else 0
    totale_scontato = totale * (1 - sconto)


    inizia_con_m = nome.startswith("M")
    conteggio_a = nome.count("a")

    print(
        f"Prodotto: {nome}, Totale: {totale_scontato:.2f} € (sconto {sconto * 100:.0f}%), Inizia con 'M': {inizia_con_m}, Conteggio 'a': {conteggio_a}"
    )