def Fibonacci(n):
    '''Calcola il numero di Fibonacci'''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)
    
def main():
    try:
        n = int(input("Inserisci un numero intero: "))

        if n < 0:
            print("ERRORE il numero deve essere maggiore o uguale a 0.")
        else:
            risultato = Fibonacci(n)
            print(f"Fibonacci({n}) = {risultato}")

    except ValueError:
        print("ERRORE devi inserire un numero intero valido.")


main()
