# # Esercizio 37: Lista di Dizionari - Età Massima

# Scrivi un programma Python che:

# 1. Crea una lista di dizionari, dove ogni dizionario rappresenta una persona con chiavi "nome: "età: "città".
# 2. Aggiungi almeno 5 persone alla lista.
# 3. Trova l'età massima tra tutte le persone.
# 4. Trova e stampa le informazioni della persona con l'età massima.

# Esempio di output:
# ```
# Nome: Mario, Età: 30, Città: Milano
# Nome: Luca, Età: 25, Città: Roma
# Nome: Anna, Età: 35, Città: Milano
# Nome: Giovanni, Età: 28, Città: Napoli
# Nome: Sofia, Età: 22, Città: Milano
# Età massima: 35
# Persona con età massima: Nome: Anna, Età: 35, Città: Milano
# ```




lista_di_persone: list[str, any] = [
    {
        "Nome": "Mario",
        "Età": 30,
        "Città": "Milano",
    },
    {
        "Nome": "Luca",
        "Età": 25,
        "Città": "Roma",
    },
    {
        "Nome": "Anna",
        "Età": 35,
        "Città": "Milano",
    },
    {
        "Nome": "Giovanni",
        "Età": 28,
        "Città": "Napoli",
    },
    {
        "Nome": "Sofia",
        "Età": 22,
        "Città": "Milano"
    }

]

eta_massima = 0
for persona in lista_di_persone:
    if persona["Età"] > eta_massima:
        eta_massima = persona["Età"]

persona_massima = None
for persona in lista_di_persone:
    if persona["Età"] == eta_massima:
        persona_massima = persona


print(f"Età massima: {eta_massima}")
if persona_massima:
    print(f"Persona con età massima: Nome: {persona_massima['Nome']}, Età: {persona_massima['Età']}, Città: {persona_massima['Città']}")


for persona in lista_di_persone:
    print(f"Nome: {persona['Nome']}, Età: {persona['Età']}, Città: {persona['Città']}")