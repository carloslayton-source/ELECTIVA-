import pandas as pd
import matplotlib.pyplot as plt

tabla_datos = pd.read_csv("distancias.csv") # Lee el archivo CSV "distancias.csv" y lo carga en un DataFrame

#plt.plot(tabla_datos["Medicion"], tabla_datos["Distancia"]) # Crea un gráfico de línea con los datos de "Medicion" y "Distancia"
#plt.scatter(tabla_datos["Medicion"], tabla_datos["Distancia"], color='red') # Agrega puntos rojos en el gráfico para cada medición      
#plt.bar(tabla_datos["Medicion"], tabla_datos["Distancia"], alpha=0.5) # Agrega un gráfico de barras con transparencia del 50%
plt.hist(tabla_datos["Distancia"], bins=5, alpha=0.7, color='blue') # Crea un histograma de las distancias con 5 bins y color azul  
#plt.grid(axis='y', alpha=0.75) # Agrega una cuadrícula al eje y con transparencia del 75%
#plt.xticks(range(0, 25, 5)) # Establece los ticks del eje x en incrementos de 5
plt.xlabel("Medición") # Etiqueta el eje x
plt.ylabel("Distancia") # Etiqueta el eje y
plt.title("Distancias medidas por el HC - SR04") # Establece el título del gráfico

plt.show() # Muestra el gráfico  