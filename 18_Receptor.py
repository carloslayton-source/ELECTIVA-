import serial 
from time import sleep

puerto = serial.Serial("COM3", 115200, timeout=3) # Configura el puerto serial con la velocidad de comunicacion y el tiempo de espera para recibir datos.
sleep(3) # Pausa el programa por 3 segundos para dar tiempo a que se establezca la conexion con el ESP32.

puerto.reset_input_buffer() # Limpia el buffer de entrada del puerto serial para eliminar cualquier dato que pueda haber quedado de una conexion anterior.

while True:
    dato = puerto.readline().decode().strip() # Lee una linea de texto recibida por el puerto serial, la decodifica y elimina los espacios en blanco al inicio y al final del texto.
    
    if dato: # Si se recibe un dato valido
        distancia = float(dato) # Convierte el texto recibido en un numero decimal (Float)
        print("Distancia recibida: ", distancia, "cm") # Muestra la distancia recibida en la consola de Python
        