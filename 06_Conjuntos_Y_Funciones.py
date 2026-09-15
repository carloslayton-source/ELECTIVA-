#Crear un lista vacia
# Diccionario es estudiante
# Nombre es la clave con variable nombre
# Notas es la clave con la variable notas
# Nombre de la lista.pend para agregar cosas

# Solicitar al usuiario la cantidad de estudiantes que desea registrar.
#Pedir 3 notas del estudiante
# Guardar cada estudiante como diccionario
# Utilizaremos o un for para hacer el reccorido del promedio y del resultado
# Al final debe aparecer nombre, promedio, y si aprobo o no


# lista_estudiantes = []
# cantidad = int(input("¿Cuántos estudiantes deseas registrar? "))

# for i in range(cantidad):
#     print(f"\n Estudiante {i+1}")
#     nombre = input("Ingresa el nombre del estudiante: ") 
#     nota1 = float(input("Ingresa la nota de cada estudiante"))
#     nota2 = float(input("Ingresa la nota de cada estudiante"))
#     nota3 = float(input("Ingresa la nota de cada estudiante"))
    
#     notas = [nota1, nota2, nota3]
    
#     estudiante = {
#         "Nombre": nombre,
#         "Notas": notas
#     }
#     lista_estudiantes.append(estudiante)
    
# print("RESULTADOS FINALES")

# for estudiante in lista_estudiantes:
#     nombre_actual = estudiante["Nombre"]
#     nota_actuales = estudiante["Notas"]
    
#     promedio = sum(nota_actuales) / len(nota_actuales)
    
#     if promedio >= 3.0: 
#         estado = "Aprobo"
#     else: 
#         estado = "No Apobo"
    
#     print(f"Nombre: {nombre_actual} | Promedio: {promedio:.2f} | Estado: {estado}")
    

 # CONJUNTOS
# datos = set () # Cuando esta vacio el
# numeros = {10, 20, 30, 30, 40}

# numeros.add(50)  
# numeros.remove(20) 

# print(numeros)

# UNION, INTERSECCION, DIFERENCIA

#UNION
# numeros = {10, 20, 30, 30, 40}
# numb = {10, 25, 30, 45}
# union = numeros | numb
# print("Unión:", union)

# INTERSECCION
# numeros = {10, 20, 30, 30, 40}
# numb = {10, 25, 30, 45}
# interseccion = numeros & numb
# print("Interseccion:", interseccion)

#DIFERENCIA
# numeros = {10, 20, 30, 30, 40}
# numb = {10, 25, 30, 45}
# # diferencia = numeros - numb
# diferencia = numb - numeros
# print("diferencia:", diferencia)




  
    
    