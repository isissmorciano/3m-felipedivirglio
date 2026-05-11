try:
    N = int(input("Inserisci il numero di stringhe: "))
    if N <= 0:
        print("Errore N deve essere un intero positivo.")
        exit()

    C = input("Inserisci una lettera: ")
    if len(C) != 1 or not C.isalpha():
        print("Errore C deve essere una singola lettera.")
        exit()

    X = int(input("Inserisci la lunghezza minima: "))
    if X <= 0:
        print("Errore X deve essere un intero positivo.")
        exit()

   
    stringhe = [input(f"Inserisci la stringa {i+1}: ") for i in range(N)]

    
    filtrate = [s for s in stringhe if C in s and len(s) > X]

   
    print("Stringhe filtrate:", filtrate)
    print("Numero di stringhe filtrate:", len(filtrate))

    if filtrate:
        lunghezza_minima = min(len(s) for s in filtrate)
        print("Lunghezza minima tra le stringhe filtrate:", lunghezza_minima)
    else:
        print("Nessuna stringa soddisfa i criteri.")

except ValueError:
    print("Errore: N e X devono essere numeri interi.")
