import itertools
import csv

# Generar combinaciones
caras = range(1, 21)
combinaciones = itertools.product(caras, repeat=3)

# Guardar en archivo CSV
with open("dados_20_caras.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Dado 1", "Dado 2", "Dado 3"])
    writer.writerows(combinaciones)
