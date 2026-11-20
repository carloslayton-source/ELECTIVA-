import numpy as np # Importa la biblioteca NumPy para trabajar con arrays y realizar cálculos numéricos

# temperaturas = np.array([22.5, 23.0, 21.8, 24.1, 22.9]) # Array de temperaturas en grados Celsius

# temp_aumentadas = temperaturas + 2.0 # Aumenta cada temperatura en 2 grados
# promedio = np.mean(temperaturas) # Calcula el promedio de las temperaturas aumentadas
# temp_maxima = np.max(temperaturas) # Encuentra la temperatura máxima
# temp_minima = np.min(temperaturas) # Encuentra la temperatura mínima

# print("Temperaturas aumentadas:", temp_aumentadas) # Muestra las temperaturas aumentadas
# print("Promedio de temperaturas:", promedio) # Muestra el promedio de las temperaturas
# print("Temperatura máxima:", temp_maxima) # Muestra la temperatura máxima
# print("Temperatura mínima:", temp_minima) # Muestra la temperatura mínima

# print(temperaturas[0]) # Muestra la primera temperatura del array
# print(temperaturas[4]) # Muestra la última temperatura del array

# tem_bajas = temperaturas[temperaturas < 28] # Filtra las temperaturas menores a 28 grados
# print("Temperaturas menores a 28 grados:", tem_bajas) # Muestra las temperaturas filtradas

# tem_altas = temperaturas[temperaturas > 28] # Filtra las temperaturas mayores a 28 grados
# print("Temperaturas mayores a 28 grados:", tem_altas) # Muestra las temperaturas filtradas    

temperaturas = np.array([22.5, 23.0, 21.8, 24.1, 22.9]) # Array de temperaturas en grados Celsius
suma_temperaturas = np.sum(temperaturas) # Suma todas las temperaturas
print("Suma de temperaturas:", suma_temperaturas) # Muestra la suma de las temperaturas

promedio_temperaturas = np.mean(temperaturas) # Calcula el promedio de las temperaturas
print("Promedio de temperaturas:", promedio_temperaturas) # Muestra el promedio de las

media_std = np.std(temperaturas) # Calcula la desviación estándar de las temperaturas
print("Desviación estándar de temperaturas:", media_std) # Muestra la desviación estándar de las temperaturas

print(round(promedio_temperaturas,2)) # Muestra la primera temperatura del array redondeada a 2 decimales
print(round(media_std,2)) # Muestra la desviación estándar redondeada a 2 decimales

print(round(media_std,2)) # Muestra la desviación estándar redondeada a 2 decimales
print(round(promedio_temperaturas,2)) # Muestra la primera temperatura del array redondeada a 2 decimales

