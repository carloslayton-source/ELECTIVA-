# # #HERENCIA Y ENCAPSULAMIENTO 

# # #Pass Permite ejecutar sin necesidad de tener codigo dentro de esa clase

# # # class Persona:
# # #     def __init__(self,nombre):
# # #         self.nombre = nombre
        
# # #     def saludar(self):
# # #         return f"Hola, soy{self.nombre}"

# # # class Estudiante(Persona):# En esta clase la clase padre debe estar en parentesis
# # #     estudiante1 = Estudiante("Pepito")
# # #     print(estudiante1.saludar())
# # # pass

# # #Persona tiene constructor y tiene el metodo saludar()
# # # Estudiante no agrega nada nuevo, Pero Hereda lo de la persona. 


# # # Para que sirve super()

# # #super() permite ejecutar el constructor o los metodos de la clase padre 

# # class Persona: # ESTA CLASE PADRE INICIALIZA NOMBRE Y EDAD 
# #     def __init__(self,nombre, edad):
# #         self.nombre = nombre
# #         self.edad = edad
        
# # # class Estudiante(Persona): #ESTA CLASE HIJA REUTILIZA LO ANTERIOR Y AGREGA CARRERA
# # #     def __init__(self, nombre, edad, carrera):
# # #         super().__init__(nombre, edad)
# # #         self.carrera = carrera 
# # # estudiante1 = Estudiante("Pepito", "12", "Licenciatura en matematicas")     
# # # print(estudiante1.saludar())       
# # # #super() evita repetir self.nombre = nombre y self.edad = edad. 


# # #ATRIBUTOS HEREDADOS Y PROPIOS
# # # La clase hija puede conservar lo heredado y agregar informacion nueva

# # class Estudiante(Persona):
# #     def __init__(self, nombre, edad, carrera, nota):
# #         super().__init__(nombre, edad)
# #         self.carrera = carrera 
# #         self.__nota = nota
# # estudiante1 = Estudiante("Luis", 34, "  Lic. Tecnologia, 4.5")
# # print(estudiante1.saludar)


# # # HERERDAR METODOS HEREDADOS Y METODOS PROPIOS
# # # Un objeto de clase hija puede usar metodos heredados y metodos definidos en la hija 

# # estudiante1.presentarse() # Presentarse viene de la clase padre
# # #Metodo heredado de Persona

# # estudiante1.mostrar_nota()
# # #Metodo propio de Estudiante 

# # estudiante1.obtener_estado()
# # # Metodo Propio de Estudiante 


# # # SOBRE ESCRITURA DE METODOS. 
# # # La clase Hija puede redifinir un metodo heredado para tener un comportamiento propio 

# # class Persona: # Persona presentarse() version general 
# #     def presentarse(self):
# #         return " Soy una persona"
    
# # class Estudiante(Persona):
# #     def presesentarse(self): # Estudiante presentarse() Version Propia
# #         return "Soy un estudiante"
    
    
# # #Python usa primero el metodo que esta definido en la clase objeto 

# # # ENCAPSULAMIENTO 
# # # Encapsular es controlar como se accede y como se modifica el estado interno del objeto

# # class Estudiante: # Publico self.nota Acceso directo 
# #     def __init__(self, nota):
# #         self.__nota = nota
    
# #     def mostrar_nota(self): # Privado self.__nota Acceso controlado
# #         return self.__nota
    
    
# # # _atributo y __atributo 
# # # No son exactamente lo mismo. Representa niveles diferentes de proteccion e intencion

# # # _ atributo = Uso interno por convencion 
# # # __ atributo = Acceso mas restringido Python aplica un name mangling 

# # # Regla rapido 
# # # Unguin bajo advierte 
# # #Dos guiones restringen mas 


# # class Sensor:
# #     def __init__(self):
# #         self._ubicacion = "Sala"
# #         self.__temperatura = 25
        
# # # _Ubicacion de interno con convencion
# # # __temperatura es restringido 

# # # Getter y setter 
# # # Son metodos para consultar o modificar un atributo de manera controlada 

# class Estudiante:
#     def __init__(self, nota):
#         self.__nota = nota
    
#     def mostrar_nota(self): #Getter mostar_nota() = Consulta un datpo
#         return self.__nota
    
#     def cambiar_nota(self, nueva_nota): # SETTER cambiar_nota() = Modifica con validacion
#         if 0 <= nueva_nota <= 5:
#             self.__nota = nueva_nota
    
#     def obtener_estado(self):
#         if self.__nota >= 3:
#             return f"Aprobado con: {self.__nota}"
#         else:
#             return f"Reprobado con: {self.__nota}"       
# # Validar antes de modificar 
# # El setter protege el atributo y evita datos incoherentes 

# estudiante1 = Estudiante(4.5)
# print(estudiante1.mostrar_nota())

# estudiante1.cambiar_nota(3.8) # Dato valido 3.8 Se actualiza la nota
# print(estudiante1.mostrar_nota()) # La validacion mantiene coherente el estado del objeto 
# estudiante1.cambiar_nota(7)
# print(estudiante1.cambiar_nota) # Dato invalido 
# print(estudiante1.obtener_estado())
# # Metodo de obtener_estado()
# # El objeto puede decidir si estado suaando su propia nota nota encapsulado
# # Dos objetos, estados diferentes
# # Ambos objetos son Estudiante pero cada uno conserva su propia informacion 
# estudiante1 = Estudiante ("Luis", 34, "Lic. Tecnologia", 4.5)
# estudiante2 = Estudiante("Pedro", 25, "Lic. Tecnologia", 2.8)
# print(estudiante1.obtener_estado()) # Estudiante 1 nota:4.5 Aprobado
# print(estudiante2.obtener_estado()) # Estudiante 2 nota:2.8 Reprobado

# # PORQUE DEBEMOS ENCAPSULAR DATOS 
# # Encpasulamos los datos que no deberian modificarse libremente desde cualquier parte del programa 

# class Cuenta: 
#     def __init__(self, titular, saldo): #Sin control cualquier valor podria entrar
#         self.titular = titular 
#         self.__saldo = saldo 
    
#     def consultar_saldo(self):
#         return self.__saldo
    
#     def depositar(self, cantidad): # Con control el metodo valida antes de modificar
#         if cantidad > 0:
#           self.__saldo += cantidad  
          
# # Actividasd 
# #Construye el sistema Persona ----> Estudiante y prueba dos objetos

# class Persona: 
#     #nombre, edad, presentarse()

# class Estudiante(Persona):
#     #carrera, __ nota
#     #mostar_nota()
#     #cambiar_nota()
#     #obtener_estado()

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera, nota):
        super().__init__(nombre, edad)
        self.carrera = carrera 
        self.__nota = nota
        
    def mostrar_nota(self):
        return self.__nota
    
    def cambiar_nota(self, nueva_nota):
        if 0 <= nueva_nota <= 5:
            self.__nota = nueva_nota
        else: 
            print(f"Error: {nueva_nota} es un dato inválido. No se actualizó la nota.")
        
    def obtener_estado(self):
        if self.__nota >= 3:
            return f"Aprobado con: {self.__nota}"
        else:
            return f"Reprobado con: {self.__nota}"
        
estudiante1 = Estudiante("Sebastian", 26, "Lic. Tecnologia", 4.8)
estudiante2 = Estudiante("Zair", 22, "Lic. Matematicas", 2.8)

print(estudiante1.mostrar_nota())
estudiante1.cambiar_nota(4.6)
print(estudiante1.obtener_estado())

print(estudiante2.mostrar_nota())
estudiante2.cambiar_nota(2.0)
print(estudiante2.obtener_estado())

print(estudiante2.mostrar_nota())
estudiante2.cambiar_nota(9)
print(estudiante2.obtener_estado())