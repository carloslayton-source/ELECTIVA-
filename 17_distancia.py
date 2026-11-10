from machine import Pin, time_pulse_us
from time import sleep_us  # sleep_us: Permite pausar la ejecucion del programa por un tiempo determinado. El tiempo se indica en microsegundos (1 segundo = 1,000,000 microsegundos)

trig = Pin(18, Pin.OUT) # Pin de salida para el trigger del sensor
echo = Pin(19, Pin.IN) # Pin de entrada para el echo del sensor

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
        
    else: 
        print("Sin medicion valida") # Muestra un mensaje de error si no se recibe el pulso de retorno en el tiempo maximo de espera.
        
    sleep_us(1) # Pausa el programa por 1 segundo antes de realizar la siguiente medicion
    