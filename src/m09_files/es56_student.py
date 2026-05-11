def scrivi_file(frasi, nome_file):
    with open (nome_file, 'w') as f:
        for frase in frasi:
            f.write(frase + "\n")

def leggi_file(nome_file):
    contenuto = ""
    with open (nome_file, 'r') as frasi:
        for line in frasi:
            contenuto += line.strip() + "\n"
    return contenuto

def main():
    frasi = ["Ciao mondo", "Python è divertente", "File handling"]
    nome_file = "frasi.txt"

    scrivi = scrivi_file(frasi, nome_file)    
    leggi = leggi_file(nome_file)
    
    print("---Contenuto del file:")
    print(leggi)

main()