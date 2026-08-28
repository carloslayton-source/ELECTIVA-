# nombre = input ("DIGITE SU NOMBRE POR FAVOR")
# edad = int (input("DIGITE SU EDAD POR FAVOR"))
# temperatura = float (input("INGRESE LA TEMPERATURA CORPORAL"))
# nota = float (input("INGRESE LA NOTA OBTENIDA EN LA CAPACOITACION DE 0.0 A 5.0:"))
# carnet = (input("TIENES CARNET(ESCRIBA SI O NO)"))

# mayor_edad = edad >= 18
# tem_adecuada = temperatura < 37.5
# capacitacion_aprobada = nota > 3.0 
# tiene_carnet = carnet == "SI"

# cumple_requisitos = mayor_edad and tem_adecuada and capacitacion_aprobada and tiene_carnet

# print("mayor_edad:", mayor_edad)
# print("temp_adecuada:", tem_adecuada)
# print("cap_aprobada:", capacitacion_aprobada)
# print("tiene_carnet:", tiene_carnet)
# print("cumple_requisitos:", cumple_requisitos)


nombre = input("INGRESE EL NOMBRE DEL CLIENTE: ")
producto = input("INGRESE EL PRODUCTO:  ")
precio_unitario = float (input("INGRESE EL PRECIO UNITARIO:  "))
cantidad = int (input("INGRESE LA CANTIDAD: "))

total = precio_unitario * cantidad

print ("Nombre", nombre)
print ("Producto", producto)
print ("Cantidad ", cantidad)
print ("Precio Unidad", precio_unitario)
print ("Total Compra", total)

