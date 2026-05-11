# 1. Crea una lista di dizionari, dove ogni dizionario rappresenta 
# un'azienda con chiavi "nome", "settore", e "dipendenti". La chiave "dipendenti" è una lista di dizionari, 
# ciascuno rappresentante un dipendente con chiavi "nome", "età", "ruolo".
# 2. Aggiungi almeno 2 aziende con i loro dipendenti.
# 3. Per ogni azienda, stampa il nome dell'azienda, il settore, e i nomi e ruoli dei suoi dipendenti.


aziende = [
        {
            "nome": "TechCorp",
            "settore": "Tecnologia",
            "dipendenti": [
                {"nome": "Mario", "età": 30, "ruolo": "Sviluppatore"},
                {"nome": "Luca", "età": 25, "ruolo": "Designer"},
            ],
        },
        {
            "nome": "FoodInc",
            "settore": "Alimentare",
            "dipendenti": [
                {"nome": "Anna", "età": 35, "ruolo": "Manager"},
                {"nome": "Giovanni", "età": 28, "ruolo": "Cuoco"},
            ],
        },
    ]


for azienda in aziende:
    nome_azienda = azienda["nome"]
    settore = azienda["settore"]
    dipendenti = azienda["dipendenti"]
    print(f"Azienda: {nome_azienda}, Settore: {settore}")
    dipendenti_str = ""
    for dip in dipendenti:
        dipendenti_str += f"{dip['nome']} ({dip['ruolo']}), "
        dipendenti_str = dipendenti_str.rstrip(", ")
        print(f"Dipendenti: {dipendenti_str}")