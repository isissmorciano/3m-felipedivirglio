import matplotlib.pyplot as plt
import numpy as np  

# Esercizio 1: Linea semplice
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])    
plt.figure(figsize=(8, 5))
plt.plot(xpoints, ypoints)
plt.savefig('linea_semplice.png')

# Esercizio 2: Linea punteggiata
ypoints = np.array([3, 8, 1, 10])
plt.figure(figsize=(8, 5))
plt.plot(ypoints, linestyle='dotted')
plt.savefig('linea_punteggiata.png')

# Esercizio 3: Grafico a barre
categorie = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile']
valori = [10, 15, 7, 12]
plt.figure(figsize=(8, 5))
plt.bar(categorie, valori, color='skyblue')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig('grafico_a_barre.png')

# Esercizio 4: Grafici con subplot
xpoints = np.array([0, 6])
ypoints1 = np.array([0, 250])
categorie = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile']
valori = [10, 15, 7, 12]
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(xpoints, ypoints1)
plt.subplot(1, 2, 2)
plt.bar(categorie, valori, color='skyblue')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig('grafici_con_subplot.png')
