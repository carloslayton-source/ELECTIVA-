# def saludar (): # Define 
#     print("Hola")
# saludar() # Ejecuta 

# def presentar(nombre, edad):
#     print("Nombre:", nombre)
#     print("Edad:", edad)
# presentar("Laura", 22)

# def sumar(a,b):
#     print(a+b)
# resultado = sumar (5,3)
# print(resultado)

# def sumar(a,b):
#     return a + b
# resultado = sumar (5,3)
# print(resultado)

# def multiplicar(a,b):
#     return a * b
# resultado = multiplicar(4,5) +10
# print (resultado)

# def calcular_promedio(notas):
#      suma = 0 
#      for nota in notas:
#          suma += nota
#      return suma / len(notas)

# notas_ana = [4.0,3.5,5.0]
# promedio = calcular_promedio(notas_ana)
# print(round(promedio,2))

# def calcular():
#     resultado = 20
#     print(resultado)

# calcular()
# print(resultado)    

# nombre = "Laura"

# def saludar():
#     print(nombre)
# saludar()

# contador = 10 

# def aumentar():
#     contador = contador + 1
#     print(contador)

# aumentar()

# def aumentar(numero):
#     return numero +1

# contador = 10
# contador = aumentar(contador) # contador es un argumento
# print(contador)


# EJERCICIO INTEGRADOR: FUNCION + DICCIONARIO
# def calcular_total(precio,cantidad):
#     return precio * cantidad

# producto = {
#     "nombre": "Teclado",
#     "precio":80000,
#     "cantidad":3
# }

# producto["total"] = calcular_total(
#     producto["precio"],
#     producto["cantidad"]
# )
# print(producto)

# CORREGIR CODIGO 
# puntos = 5 
# def sumar_puntos():
#     puntos = puntos + 10
#     print(puntos)
# sumar_puntos()


# PUNTO CORREGIDO 

# def sumar_puntos(puntos_actuales):
#     return puntos_actuales + 10
# puntos = 5 
# puntos = sumar_puntos(puntos) # puntos es un argumento y se actualiza con el return
# print(puntos)



# Taller De Clase
# Construir una solucion pequeña pero completa
# Crear una funcion calcular_promedio(notas) que devuelva el proemdio en una lista
#Luego recorre esta lista de estudiantes y agrega dos claves nuevas: promedio y estado


def calcular_promedio(notas):
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas) 

estudiantes = [
    {"nombre":"Ana", "notas":[4.0,3.5,5.0]},
    {"nombre":"Luis", "notas":[2.5,3.0,2.8]},
    {"nombre":"Carlos", "notas":[4.5,4.0,4.8]}
] 

for estudiante in estudiantes: 
    promedio_calculado = calcular_promedio(estudiante["notas"])
    estudiante["promedio"] = round(promedio_calculado,2)
    
    if estudiante["promedio"] >= 3.0:
        estudiante["estado"] = "aprobo"
    else:
        estudiante["estado"] = " No aprobo" 

#print("Luis")
#print(estudiantes[1])

print ("Resultados Finales:")
for estudiante in estudiantes:
    print(estudiante)