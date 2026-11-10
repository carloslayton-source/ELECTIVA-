from machine import Pin, time_pulse_us
from time import sleep, sleep_us  # sleep_us: Permite pausar la ejecucion del programa por un tiempo determinado. El tiempo se indica en microsegundos (1 segundo = 1,000,000 microsegundos)
import sys
import select

trig = Pin(18, Pin.OUT) # Pin de salida para el trigger del sensor
echo = Pin(19, Pin.IN) # Pin de entrada para el echo del sensor
led = Pin(22, Pin.OUT) # Pin de salida para el led

led.value(0) # Apaga el LED al inicio del programa

while True:
    trig.value(0) # Envia un pulso de 1 al pin de salida del trigger
    sleep_us(2) # Pausa el programa por 2 microsegundos
    
    trig.value(1) # Envia un pulso de 1 al pin de salida del trigger
    sleep_us(10) # Pausa el programa por 10 microsegundos
    trig.value(0) # Envia un pulso de 0 al pin de salida del trigger
    
    tiempo = time_pulse_us(echo, 1, 30000) # Mide el tiempo que tarda en recibir el pulso de retorno del echo. El tiempo se mide en microsegundos. El tercer parametro es el tiempo maximo de espera para recibir el pulso de retorno. Si no recibe el pulso de retorno en ese tiempo, devuelve un valor negativo.
    
    if tiempo > 0:
        distancia = tiempo / 58 # Convierte el tiempo en distancia en centimetros. La formula es: distancia = tiempo / 58
        print(round(distancia, 1)) # Muestra la distancia en centimetros con 1 decimales
        
    if select.select([sys.stdin], [], [], 0.0)[0]: # Verifica si hay datos disponibles en la entrada estandar (stdin) sin bloquear la ejecucion del programa.
        mensaje = sys.stdin.readline().strip() # Lee el mensaje enviado desde Python y lo guarda en la variable mensaje.
        
        if mensaje == "ENCENDER": # Si el mensaje recibido es "ENCENDER"
            led.value(1) # Enciende el LED
            
        if mensaje == "APAGAR": # Si el mensaje recibido es "APAGAR"
            led.value(0) # Apaga el LED
    sleep(0.5) # Pausa el programa por 0.1 segundos para evitar que se ejecute demasiado rapido y se saturen los recursos del microcontrolador.