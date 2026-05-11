
velocita = float(input("Inserisci velocità:"))
limite_di_velocita = float(input("Inserisci il limite di velocità:"))



differenza_tra = velocita - limite_di_velocita

if differenza_tra <= 10:
    sanzione = 36
elif 10 < differenza_tra <= 40:
    sanzione = 148
elif 40 < differenza_tra <= 60:
    sanzione = 370
elif differenza_tra > 60:
    sanzione = 500
else:
    sanzione = 0


if velocita < limite_di_velocita:
    print("La velocità è inferiore al limite: Nessuna Sanzione")
else:
    sanzione 
    print(f"La sanzione è di €{sanzione}")


