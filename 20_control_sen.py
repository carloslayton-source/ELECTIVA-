import serial # Importa la libreria serial para poder comunicarse con el puerto serial del ESP32.
from time import sleep # Importa la funcion sleep para poder pausar la ejecucion del programa por un tiempo determinado.

puerto = serial.Serial("COM3", 115200, timeout=3) # Configura el puerto serial con la velocidad de comunicacion y el tiempo de espera para recibir datos.

sleep(3) # Pausa el programa por 2 segundos para permitir que el puerto serial se inicialice correctamente.
puerto.reset_input_buffer() # Limpia el buffer de entrada del puerto serial para evitar que se reciban datos antiguos.

while True:
    dato = puerto.readline().decode('utf-8').strip() # Lee una linea de datos del puerto serial, la decodifica a UTF-8 y elimina los espacios en blanco al inicio y al final.
    
    try: 
        distancia = float(dato) # Intenta convertir el dato recibido a un numero flotante.
        print("Distancia: ", distancia, " cm") # Muestra la distancia en centimetros.
        
        if distancia < 10: # Si la distancia es menor a 10 cm
            puerto.write(b'ENCENDER\n') # Envia el mensaje "ENCENDER" al ESP32 para encender el LED.
        else: # Si la distancia es mayor o igual a 10 cm
            puerto.write(b'APAGAR\n') # Envia el mensaje "APAGAR" al ESP32 para apagar el LED.
    except ValueError: # Si ocurre un error al convertir el dato a float (por ejemplo, si el dato no es un numero valido)
        pass # Ignora el error y continua con la siguiente iteracion del bucle.
        
        