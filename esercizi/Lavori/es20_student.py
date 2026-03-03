try:
    N = int(input("Inserisci il numero di valori: "))
    if N <= 0:
        print("Errore N deve essere un intero positivo.")
        exit()

    K = int(input("Inserisci il valore di K: "))
    if K <= 0:
        print("Errore K deve essere un intero positivo.")
        exit()

    A = int(input("Inserisci il valore di A: "))
    B = int(input("Inserisci il valore di B: "))
    if A >= B:
        print("Errore A deve essere minore di B.")
        exit()

    numeri = [int(input(f"Inserisci il numero {i+1}: ")) for i in range(N)]

    filtrati = [num for num in numeri if num % K == 0 and A <= num <= B]

    print("Numeri filtrati:", filtrati)
    print("Numero di elementi:", len(filtrati))

    if filtrati:
        media = sum(filtrati) / len(filtrati)
        print("Media dei numeri filtrati:", media)
    else:
        print("Nessun numero soddisfa i criteri.")

except ValueError:
    print("Errore: N, K, A e B devono essere numeri interi.")
