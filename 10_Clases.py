# #Archivos Segunda Parte
# productos = []
# with open ("productos.txt","r") as archivo:
#     for linea in archivo:
#         datos = linea.strip().split(",")
        
#         producto ={
#             "nombre": datos[0],
#             "precio": int(datos[1]),
#             "cantidad": int(datos[2])
#         }
                
#         productos.append(producto)
        
# print(productos)


# Ejercicio Guiado: Registro de estudiantes
#Primero guardar nombre y edad en un archivo

# Meta del ejercicio
# 1. pedir 3 estudiantes
# 2. guardarlos en estudiantes.txt
# 3. Verifique el archivo

# with open("estudiantes.txt", "w") as archivo:
#     for i in range(3):
#         print(f"\nEstudiante {i+1}")
#         nombre = input("Ingrese el nombre del estudiante: ")
#         edad = input("Ingrese la edad del estudiante: ")
        
#         archivo.write(nombre + "," + str(edad) + "\n")

# estudiantes = []
# with open ("estudiantes.txt","r") as archivo:
#     for linea in archivo:
#         datos = linea.strip().split(",")
        
#         estudiante ={
#             "nombre": datos[0],
#              "edad": int(datos[1])
#          }        
#         estudiantes.append(estudiante)
        
# print(estudiantes)

# PORGRAMACION ORIENTADA A OBJETOS POO
# clases Y Objeto

# Clase: es un molde las especificaciones generales:
# Clase:
#Producto

#Objeto 1
#Mouse
#Nombre: Mouse
#Precio: 50000

#Objeto 2
#teclado
#Nombre:Teclado
#Precio:80000

#Crear la primera clase 
# pass permite crear una clase valida aunque todavia no tenga contenido propio
# class Producto:
#     pass
# mouse = Producto()
# teclado = Producto()
# print(type(mouse))

#El constructor _init_
#_init_ se ejecuta automaticamente cuando creamos el objeto

# class Producto:
#     def __init__(self,nombre,precio):
#         self.nombre = nombre
#         self.precio = precio
# mouse = Producto("Mouse", 50000)

#self.variable sirve para guardar datos
#Self: Representa el objeto que se esta usando el metodo en ese momento

#Atributos del objeto: Un atributo es informacion que pertenece al objeto. 

# class Producto: 
#     pass
#     def __init__(self, nombre, precio, cantidad):
#         self.nombre = nombre
#         self.precio = precio
#         self.cantidad = cantidad
        
# teclado = Producto("Teclado", 80000, 3)
# print(teclado.nombre)
# print(teclado.precio)
# print(teclado.cantidad)

# self.atributo guarda datos dentro del objeto actual

#METODOS: Funciones dentro de una clase 
#Un metodo representa una accion que puede realizar el objeto

# class Producto: 
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio
#     def mostrar_precio(self):
#         print(self.nombre, self.precio, self.mostrar_precio)
# mouse = Producto("Mouse", 50000)
# mouse.mostrar_precio()