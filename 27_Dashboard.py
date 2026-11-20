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
