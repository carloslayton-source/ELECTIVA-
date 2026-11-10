# #Velocidad de comunicacion
# #Los extremos deben utilizar la misma velocidad de comunicacion

# #Esp32 = 115200

# # Que es el py serial
# # Es la libreria que permite a ýthon utilizar eñl puerto serial del computador
# # import serial

# # Abrir el puerto desde python 
# # Primero indocamos por donde y a que velocidad nos comunicaremos

# # import serial
# # puerto = serial.Serial("COM10", 115200)

# # Python -> ESP32: Enviar informacion 
# # (mrite solo envia)
# # puerto.write(...)


# # PORQUE USAMO ENCODE?
# # PySerial envia bytes, por eso convertimos el texto antes de enviarlo
# # puerto.write((mensaje + "\n")).encode())

# # El salto de linea \n: Nos ayuda a marcar donde termina cada mensaje.

# # "ENCENDER\n" # Envia el mensaje "ENCENDER" al ESP32, seguido de un salto de linea para indicar el final del

# # ESP32 -> PYTHON:Recibir informacion

# # redline() espera y lee una linea recibida por el puerto serial. 

# dato = puerto.readline() # Espera a recibir una linea de texto y la guarde en la variable dato. 

# #¿Porque usamos decode()?
# # Convierte los bytes recibiendos en texto que Python puede manejar con facilidad.

# dato.puerto.readline().decode() # Convierte los bytes recibidos en texto. 

# # Preparar el dato para utulizarlo
# # Despues de recibirlo limpiamos el textp y reconstruimos el tipo de dato que necesitamos. 
 
#  dato = puerto.readline().decode().strip() # Elimina los espacios en blanco al inicio y al final del texto.
#  temperatura = float(dato) # Convierte el texto en un numero decimal (Float)
 
 
from machine import Pin
from time import sleep

led = Pin(18, Pin.OUT)

while True:
    led.value(1)
    sleep(1)
    
    led.value(0)
    sleep(1)