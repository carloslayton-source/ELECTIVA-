import pandas as pd # Importa la librería pandas y le asigna el alias pd
datos ={ # Diccionario de datos con dos listas: "Medicion" y "Distancia"
    "Medicion": [1, 2, 3, 4, 5],
    "Distancia": [12.5, 15.0, 9.8, 20.1, 18.3], 
}
tabla_datos = pd.DataFrame(datos) # Crea un DataFrame a partir del diccionario de datos
# print(tabla_datos) # Muestra la tabla completa de datos

print(tabla_datos["Distancia"]) # Muestra la columna de distancias

promedio = tabla_datos["Distancia"].mean() # Calcula el promedio de la columna "Distancia"
print("Promedio de distancias:", promedio) # Muestra el promedio de distancias

dis_max = tabla_datos["Distancia"].max() # Encuentra la distancia máxima en la columna "Distancia"
print("Distancia máxima:", dis_max) # Muestra la distancia máxima

dis_min = tabla_datos["Distancia"].min() # Encuentra la distancia mínima en la columna "Distancia"
print("Distancia mínima:", dis_min) # Muestra la distancia mínima

tem_altas = tabla_datos[tabla_datos["Distancia"] > 15] # Filtra las filas donde la distancia es mayor a 15
print("Distancias mayores a 15:", tem_altas) # Muestra las filas filtradas

tabla_datos["Distancia Doble"] = tabla_datos["Distancia"] * 2 # Crea una nueva columna "Distancia Doble" multiplicando la columna "Distancia" por 2
print(tabla_datos) # Muestra la tabla completa de datos con la nueva columna

tabla_datos.to_csv("distancias.csv", index=False) # Guarda la tabla de datos en un archivo CSV llamado "distancias.csv" sin incluir el índice 
