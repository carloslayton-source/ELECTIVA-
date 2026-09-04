# # # 1A Tipos de Datos
# # # El siguiente programa     pretende determinar si una persoan es mayor de edad, pero presenta un problema de error al ejecutarse

# # edad = int(input("Ingrese su edad"))

# # if edad >  18:
# #     print("Mayor de Edad")
# # else:
# #     print("Menor de edad")

# # #Faltaba agregar la funcion int para que se pudiera leer la variable de edad. 
# # #Corrija el programa para que funcione correctamente al final del codigo escriba un comentario breve explicando el problema 


# # B ESTRCUTURA DEL CONDICIONAL

# # El siguiente programa pude mostar mas de un resultado en la misma nota: 


# # B ESTRUCTURA DEL CONDICIONAL

# # nota = float(input("Ingrese la nota: "))

# # if nota >= 4.5:
# #     print("Desempeño Superior")
# # elif nota >= 3.0:
# #     print("Aprobado")
# # else:
# #     print("No aprobado")
    
# # # Modifique el codigo para que se muestre una sola claisificacion
# # # Rango de nota     Resultado 
# # # Menor de 3.0      No aprobado
# # # Desde 3.0 hasta antes de 4.5      Aprobado
# # # desde 4.5  a 5.0  Desemepeño Superior




# # Punto 2 Clasificacion y Validacion 
# # Construye un programa que solicite al usuario una nota. La nota validandebe encontrase entre 0.0 y 5.0
# #Condicion                      Resultado 
# # Menor que 0 y mayor que 5     Nota Inavalida 
# # Menor que 3.0                 No apropado 
# #Desde 3.0 hasta 4.0            DEsempeño Basico 
# # Desde 4.0 hasta 4.6           Desempeño alto
# # Desde 4.6 hasta 5.0           Desemepeño Superior

# # Ejemplos de salida
# # Ingrese la nota de: 5.5 
# # Nota Invalida

# # Ingrese la nota de 3.7:
# # Desempeño Basico
# # Ingrese la nota de 4.8:
# # Desempeño superior

# nota = float(input("Ingrese la nota: "))

# if nota < 0.0 or nota > 5.0:
#     print("Nota Invalida")
# elif nota < 3.0:
#     print("No aprobado")
# elif nota < 4.0:
#     print("Desempeño Basico")
# elif nota < 4.6:
#     print("Desempeño Alto")
# else:
#     print("Desempeño superior")
    
    
    
# # Punto 3   Programa con While 
# Una tienda necesita registrar sus ventas durante el dia
# El programa debe iniciar con

# Debe mantenerse funcionando mediante un while hasta que el usuario seleccione la opcion 3

# 1. Registar venta 
# 2. Consultar resumen 
# 3. Finalizar

# Opcion 1 
# Solicite el valor de la venta. Si el valor es menor o igual a 0, muestre "Valor Invalido" y no lo contabilice
# Si es valido
# sumele el total de ventas 
# aumente la cantidad_ventas en 1 
# muestre "Venta Registrada"

# Opcion 2 Consultar el resumen 
# cantidad de ventas: x
# total vendido: x 

# Opcion 3 Finalizar
# Registro finalizado 
# Cantidad de ventas totales: x 
# total vendido: x

# Al seleccionar esta opcion el ciclo debe terminar. Cualquier opcion diferente de 1, 2 o 3 debe mostar opcion invalida


total_ventas = 0 
cantidad_ventas = 0
opcion = 0

while opcion != 3:
    print("1. Registrar venta")
    print("2. Consultar resumen")
    print("3. Finalizar")
    
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        venta = float(input("Ingrese el valor de la venta: "))
        if venta <= 0:
            print("Valor Invalido")
        else:
            total_ventas = total_ventas + venta
            cantidad_ventas = cantidad_ventas + 1
            print("Venta Registrada")
            
    elif opcion == 2:
        print("cantidad de ventas:", cantidad_ventas)
        print("total vendido:", total_ventas)
        
    elif opcion == 3:
        print("Registro finalizado")
        print("Cantidad de ventas totales:", cantidad_ventas)
        print("total vendido:", total_ventas)
        
    else:
        print("opcion invalida")