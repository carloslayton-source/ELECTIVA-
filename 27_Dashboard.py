import streamlit as st

st.title("Dashboard de Distancias") # Establece el título del dashboard
st.write("Este dashboard muestra las distancias medidas por el sensor HC-SR04.") # Muestra un texto descriptivo en el dashboard     

# uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"]) # Permite al usuario subir un archivo CSV

distancias = st.slider("Selecciona un rango de distancias", min_value=0.0, max_value=30.0, value=(0.0, 30.0)) # Crea un slider para seleccionar un rango de distancias
st.write("Rango seleccionado:", distancias) # Muestra el rango de distancias seleccionado por el usuario  
  

if distancias < 20:
    st.write("La distancia es menor a 20 cm") # Muestra un mensaje de éxito si la distancia es menor a 20 cm
    
else: 
    st.write("La distancia es mayor o igual a 20 cm") # Muestra un mensaje de advertencia si la distancia es mayor o igual a 20 cm
    
import pandas as pd

datos = {
    "Medicion": [1, 2, 3, 4, 5],
    "Distancia": [12.5, 15.0, 9.8, 20.1, 18.3],
}   

tabla_datos = pd.DataFrame(datos) # Crea un DataFrame a partir del diccionario de datos
st.subheader("Tabla de Distancias") # Muestra un subtítulo en el dashboard
st.dataframe(tabla_datos) # Muestra la tabla de datos en el dashboard

st.subheader("Estadísticas de Distancias") # Muestra un subtítulo en el dashboard
promedio = tabla_datos["Distancia"].mean() # Calcula el promedio de la  columna "Distancia"     

st.line_chart(tabla_datos["Distancia"]) # Muestra un gráfico de línea con los datos de la columna "Distancia"   
tabla_datos["Distancia Ajustada"] = tabla_datos["Distancia"] + 2.0 # Crea una nueva columna "Distancia Ajustada" sumando 2 a la columna "Distancia"|    
tabla_datos["Distancia Doble"] = tabla_datos["Distancia"] * 2 # Crea una nueva columna "Distancia Doble" multiplicando la columna "Distancia" por 2 

st.line_chart(tabla_datos, x="Medicion", y=["Distancia", "Distancia Ajustada", "Distancia Doble"]) # Muestra un gráfico de línea con las columnas "Distancia", "Distancia Ajustada" y "Distancia Doble" en función de la columna "Medicion"     

opcion = st.selectbox("Selecciona una opción", ["Promedio", "Máximo", "Mínimo"]) # Crea un menú desplegable para seleccionar una opción 

st.line_chart(tabla_datos["Distancia"]) # Muestra un gráfico de línea con los datos de la columna "Distancia"   

cantidad = st.number_input("Ingresa un valor numérico", min_value=0.0, max_value=30.0, value=15.0) # Crea un campo de entrada para ingresar un valor numérico   

