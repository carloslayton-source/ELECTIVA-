# r = read leer El archivo debe existir 
# w = write escribir crea o remplaza
# a =  append agregar conserva y suma al final 


# Abrir archivo
# archivo = open("Saludo.txt")
# contenido = archivo.read()
# print(contenido)
# archivo.close() 

# with open("Saludo.txt","r") as archivo: 
#     texto = archivo.read()
# print(texto)

# with open("datos.txt","w") as archivo: 
#      archivo.write("Ana")

# with open("datos.txt","r") as archivo:
#     texto = archivo.read()
# print(texto)

# # Agregar con append o con la a. 
# with open("registro.txt","w") as archivo:
#     archivo.write("Ana\n")

# with open("registro.txt","a") as archivo:
#     archivo.write("Luis\n")
#     archivo.write("Carlos\n")
    
# with open("registro.txt","r") as archivo:
#     leer = archivo.read()
# print(leer)

# with open("registro.txt", "r") as archivo:
#     for linea in archivo:
#         print(linea.strip()) #elimina saltos de linea y espacios

# with open("edades.txt","w") as archivo:
#     archivo.write("20\n")
#     archivo.write("25\n")
#     archivo.write("30\n")
# with open("edades.txt","r") as archivo:
#     for linea in archivo:
#         edad = int(linea.strip())
#         print(edad + 5)

# with open("registro.txt", "r") as archivo:
#     datos = archivo.readlines()
# print (datos[1].strip())

# #Listas de archivos
# productos = ["Mouese", "Teclado", "Monitor"]
# with open("productos.txt", "w") as archivo:
#     for  producto in productos:
#         archivo.write(producto + "\n")

# #Otro para escribir 
# nombres = ["Ana\n", "Luis\n", "Carlos\n"]

# with open("nombre.txt", "w")as archivo:
#     archivo.writelines(nombres)


#Guardar registros separados por comas

# productos = [
#     {"nombre": "Mouse", "Precio": 50000, "cantidad":5},
#     {"nombre": "Teclado", "Precio": 80000, "cantidad":3}
# ]

# with open("productos.txt", "w") as archivo:
#     for producto in productos:
#         archivo.write(producto["nombre"] + "," + str(producto["Precio"]) + "," + str(producto["cantidad"]) + "\n")
        
# Leer un registro con split
 # split() divide un texto segun separador
 
linea = "Teclado,80000,3"
datos = linea.strip().split(",")

nombres = datos [0]
precio = int(datos[1])
cantidad = int(datos[2])
total = precio * cantidad
print(datos)
print(total)