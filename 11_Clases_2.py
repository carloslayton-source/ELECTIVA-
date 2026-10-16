# class Producto:
#     def __init__(self, nombre, precio, cantidad=0):
#         self.nombre = nombre
#         self.precio = precio 
#         self.cantidad = cantidad
        
#     def agregar_stock(self, unidades):
#         self.cantidad += unidades
        
#     def calcular_total(self, unidades_a_comprar):
#         return self.precio * unidades_a_comprar

# celular = Producto("Celular", 20000)
# # celular.agregar_stock(5)

# teclado = Producto("Teclado", 35000)
# mouse = Producto("Mouse", 23000)
# monitor = Producto("Monitor", 5000)
# # mouse.agregar_stock(4)

# print(mouse.calcular_total(3))

#DICCIONARIOS VS OBJETOS
#Ambos organizan datos, pero los objetos tambien pueden tener comportamientos

# producto = {
#     "nombre": "Mouse",
#     "precio": 50000
# }

# # print(producto["precio"])

# class Producto:
#     def __init__(self,nombre,precio,cantidad): #PARAMETROS
#         self.nombre = nombre # PARAMETROS 
#         self.precio = precio #PARAMETROS
#         self.cantidad = cantidad #PARAMETROS 
        
#         # SELF.NOMBRE, SELF.PRECIO, SELF.CANTIDAD ESTOS SON ATRIBUTOS
#     def mostrar_datos(self): #METODOS
#         return f"{self.nombre} - {self.precio} - {self.cantidad}"
    
#     def calcular_total(self):
#         return self.precio * self.cantidad 
    
# #AHORA VAMOS A CREAR LOS OBJETOS 

# celular = Producto("Celular", 2300000, 5)
# cerveza = Producto("Aguila_Light", 3500, 5)
# monitor = Producto("Monitor", 700000, 1)

# print(celular.mostrar_datos())
# print(cerveza.calcular_total())


#RETO FINAL: SISTEMA BANCARIO 
#Creuna clase llamada CuentaBancaria que permita administrar el dinero de los diferentes clientes.
# Requisitos del programa
# El constructor debe recibir titular y saldo. 
#El metodo retirar(cantidad) debe verificar que la cantidad sea positiva y que existe fondos suficientes.
#El metodo consultar_saldo()        debe devolver el saldo utilizando return
#El metodo mostrar_datos() debe devolver una cadena con el nombre del titular y su saldo actual
#El metodo depositar (cantidad) debe aumentar el saldo, siempre que la cantidad sea positiva.


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def retirar(self,cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
        elif cantidad > self.saldo:
            print("Fondos Insuficientes")
        else:
            print("La cantidad debe ser positiva")
    
    def consultar_saldo(self):
        return self.saldo
    
    def mostrar_datos(self):
        return f"Titular: {self.titular} - Saldo actual: ${self.saldo}"
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            print("El depósito debe ser un valor positivo.")
            
cuenta1 = CuentaBancaria("Carlos", 100000)
cuenta2 = CuentaBancaria("Ana", 50000)
cuenta1.depositar(50000)
cuenta1.retirar(30000)
cuenta2.retirar(60000)
print(cuenta1.mostrar_datos())
print(cuenta2.mostrar_datos())   
    