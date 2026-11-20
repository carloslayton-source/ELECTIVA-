import pandas as pd
tabla_datos = pd.read_csv("distancias.csv", index = False) # Lee el archivo CSV "distancias.csv" y lo carga en un DataFrame
print(tabla_datos) # Muestra la tabla completa de datos cargada desde el archivo