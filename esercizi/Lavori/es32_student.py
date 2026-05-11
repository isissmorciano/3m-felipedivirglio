# 1.Implementa un dizionario di città e popolazioni (es. {"Roma": 2870000, "Milano": 1350000, "Napoli": 975000}). 
# 2.Usa il metodo .items() (che restituisce una vista di coppie (chiave, valore) del dizionario) 
# per stampare ogni città con la sua popolazione in formato "Città: Popolazione abitanti".


citta_pop: dict[str, str | int] = {"Roma": 2870000, "Milano": 1350000, "Napoli": 975000}

for nome, pop in citta_pop.items():
    print(f"{nome}: {pop} abitanti")