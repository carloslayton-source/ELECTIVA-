# # # # edad = int(input("Digite su edad porfavor: "))

# # # # if edad >=18:
# # # #     print("Mayor De Edad")
# # # # else:
# # # #     print("Menor de Edad")
    
# # # # nota = int(input("Digite la Nota: "))

# # # # if nota >= 3.0:
# # # #     print("Aprobado")
# # # # else:
# # # #     print("No ha Aprobado")

# # # nota = float(input("Digite la Nota: "))
# # # if nota < 3.0:
# # #     print("Insuficiente")
# # # elif nota < 4.0:
# # #     print("Basico")
# # # elif nota < 4.6:
# # #     print("Alto")
# # # else:
# # #     print("Superior")

# # nota = float(input("Digite la Nota: "))
# # if nota >= 3.0:
# #     print("Aprobado")
# # elif nota >= 4.5:
# #      print("Excelente")

# # nota = float(input("Digite la Nota: "))
# # if nota < 0 or nota > 5:
# #     print ("Nota no valida")
# # elif nota < 3:
# #     print ("Insuficiente")
# # elif nota < 4:
# #     print("Basico")
# # elif nota < 4.6:
# #     print("Alto")
# # else: 
# #     print("Superior")


# nota = float(input("Digite la Nota: "))
# edad = 25
# matricula = "Si"
# contraseña = "azul121"

# if edad < 18: 
#     print("Acceso Restringido")
# else:
    
# #  usuario= input("usuario: ")   
# #  nombre =input("nombre: ")
# #  edad= input("edad: ")
# #  temperaturacorporal=float(input("temperaturacorporal: "))
# #  nota=float(input("NOTA DE 0.0 A 5.0 "))
# #  carnet = input ("¿tiene carnet? si o no : ")

# #  mayor_edad=edad>=18
# #  temp_adecuada=temperaturacorporal==37.5
# #  notafinal=nota>=0.0 and nota<=5.0
# #  requisito=carnet=="si"
# #  cumple_requisitos=mayor_edad and temp_adecuada and requisito

# #  print ("cumple requisitos de ingreso ",    cumple_requisitos)
# #  print ("es mayor de edad",   mayor_edad)
# #  print("tiene carnet" ,requisito)
# #  print("tiene temperatura normal",temp_adecuada )


# # nota=float(input("Nota: "))
# # if nota<0 or nota >5:
# #   print("nota no valida")
# # elif nota <3
# #      print (insufuciente)
# # elif nota<4.6:
# #      print (alto)


# # edad = 25
# # matricula = "si"
# # contraseña = "azul21"

# # if edad < 18:
# #     print("Acceso retringido")
# # else :
# #     if matricula == "si" :
# #         if contraseña =="azul21" :
# #              print("Bienvenido")
# #         else:
# #              print("Contraseña incorrecta ")    
# #     else:
# #          print("No matriculado")   

# # nombre =input("nombre: ")
# # edad=  int(input("edad: "))
# # invitacion = input ("¿tiene invitacion ? si o no:")
# # invitacion = invitacion.lower()
# # if edad >= 18 and invitacion == "si" :
# #     print("Autorizado ", nombre)
# # elif edad>=18 and invitacion== "no":
# #      print("Necesita invitacion ", nombre)
# # else:          
# #      print("Acceso retringido", nombre)

# # numero = 1
# # while numero <=5:
# #     print(numero)
# #     numero=numero + 1

# # contador = 1
# # while contador <=3:
# #     print(contador)
# #     contador = contador + 1


# # numero = 1
# # while numero <=3:
# #     print(numero)

# #contraseña = ""
# #intentos = 0

# while contraseña != "python" and intentos < 3:
#      contraseña = input("contraseña: ")
#      intentos = intentos + 1

# if contraseña =="python":
#   print ("Acceso autorizado")     
# else:
#   print ("Acceso bloqueado")


pin_correcto = "1012"
pin_ingresado = ""
intentos = 0

while intentos < 3 and pin_ingresado != pin_correcto:
    pin_ingresado = input("Ingrese su PIN: ")
    intentos += 1 

if pin_ingresado == pin_correcto:
    print("Acceso a la cuenta")   
else:
    print("Tarjeta bloqueada")