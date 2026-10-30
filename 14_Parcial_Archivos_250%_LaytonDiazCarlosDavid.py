#Una tienda necesita registar informacion basica de 3 productos.Desarrolle un programa en pythonque cumpla con los siguientes requerimientos.

# 1.Solicite al usuario la informacion de 3 productos:nombre, cantidad, precio unitario. 
# 2.Guarde los productos en un archivo productos.txt dejando cada producto en una linea con el formato nombre,cantidad,precio.
# 3.Despues de guardar los 3 productos, abara nuevamente productos.txt y lea su contenido.
# 4. Separe correctamente los datos de cada linea y convierta los valores numericos al tipo de dato correspondiente. 
# 5. Calcule y muestre el valor total de cada producto mediante la operacion cantidad x precio unitario.
# 6. Muestre unicamente los productos cuyo valor sea superior a $200.000
# 7. Calcule y muestre el valor total de todos los productos registrados.

# with open("productos.txt", "w") as archivo:
#     for i in range(3):
#         print(f"\nRegistro del producto {i+1}")
#         nombre = input("Nombre del producto: ")
#         cantidad = input("Cantidad: ")
#         precio = input("Precio unitario: ")
        
#         archivo.write(f"{nombre},{cantidad},{precio}\n")

# gran_total= 0
# producto_superior = []

# with open("productos.txt", "r") as archivo:
#     for linea in archivo:
#         datos = linea.strip().split(",")
#         nombre = datos[0]
#         cantidad = int(datos[1])
#         precio = float(datos[2])
        
#         valor_total = cantidad * precio
#         gran_total += valor_total
        
#         print(f"{nombre}: Valor total = ${valor_total:,.2f}")
        
#         if valor_total > 200000:
#             producto_superior.append((nombre, valor_total))

# print("\nProductos con valor a $200.000")

# if producto_superior:
#     for nombre, valor in producto_superior:
#         print(f"{nombre}: ${valor:,.2f}")
# else:
#     ("No hay productos con valor a $200.000")


# print("\nValor total del inventario")
# print(f"Gran total: ${gran_total:,.2f}")   


#PARTE C POO

# Una institucion necesita representar mediante POO los sensores utilizados en el proyecto. 
# 1. Clase Dispositivo
# - Cree una clase llamada Dispositivo con los atributos de nombre, marca y precio
# - La clase debe permitir mostrar la informacion del dispositivo.
# - La clase debe permitir calcular el precio final despues de aplicar un porcentaje de descuento. 

# 2. Clase sensor
# - Cree una clase llamada Sensor que herede de Dispositivo y agregue los atributos tipo, unidad y estado.
# - El atributo estado debe estar encapsulado
# - Permite consulatar el estado actual del sensor.
# - Permite Modificar el estado unicamnete si el nuevo valor es "Activo" o "Inactivo"
# - Permite mostar toda la informacion del sensor, incluyendo la informacion heredada.
# - Cree un metodo que reciba una lectura y un limite y determine si la lectura supera dicho limite.

# 3. Uso de los objetos
# - Cree dos objeto tipo Sensor
# - Muestre la informacion de ambos. 
# - Cambie correctamente el estado a uno de ellos
# - Intente asignar un estado diferente de "Activo" o "Inactivo" y compruebe el comportamiento del programa.
# - Aplique un descuento al precio de uno de los sensores y muestre el resultado. 
# - Utilice el metodo de lectura para comprobar si un valor supera el limite. 


class Dispositivo:
    def __init__(self, nombre,marca,precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre} - Marca: {self.marca} - Precio: ${self.precio:,.2f}"
    
    def calcular_descuento(self,porcentaje):
        descuento = self.precio * porcentaje
        return self.precio - descuento
    
class Sensor(Dispositivo):
    def __init__(self, nombre, marca, precio, tipo, unidad, estado_inicial):
        super().__init__(nombre,marca,precio)
        self.tipo = tipo
        self.unidad = unidad 
        self.__estado = "Inactivo"
        self.cambiar_estado(estado_inicial)
        
    def consultar_estado(self):
        return self.__estado
    
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado == "Activo" or nuevo_estado == "Inactivo":
            self.__estado = nuevo_estado 
        else:
            print(f"Error: '{nuevo_estado}' no es un estado válido. Solo se acepta 'Activo' o 'Inactivo'.")
    
    def mostrar_info_sensor(self):
        info_basica = self.mostrar_informacion()
        return f"{info_basica} - Tipo: {self.tipo} - Unidad: {self.unidad} - Estado: {self.__estado}"
    
    def verificar_lectura(self, lectura, limite):
        if lectura > limite:
            "Alerta: La lectura de {lectura}{self.unidad} supera el límite establecido de {limite}{self.unidad}."
        else:
            return f"Normal: La lectura de {lectura}{self.unidad} está dentro del límite de {limite}{self.unidad}."


sensor1 = Sensor("TempMaster V5", "Pajarito", 120000, "Temperatura", "C°", "Activo")
sensor2 = Sensor("Humid", "Unit", 85000, "Humedad", "%", "Inactivo")


print(sensor1.mostrar_info_sensor())
print(sensor2.mostrar_info_sensor())

sensor2.cambiar_estado("Activo")
print(f" El nuevo estado de {sensor2.nombre} es: {sensor2.consultar_estado()}")

sensor1.cambiar_estado("Dañado")
print(f" El estado de {sensor1.nombre} se mantuvo como: {sensor1.consultar_estado()}")

porcentaje_descuento = 0.15
precio_final = sensor1.calcular_descuento(porcentaje_descuento)
print (f"Precio orginal del {sensor1.nombre} ${sensor1.precio:,.2f}")
print (f"Precio con descuento del 15%: ${precio_final:,.2f}")

print(sensor1.verificar_lectura(35, 30))
print(sensor2.verificar_lectura(45, 90))


