from machine import Pin
import sys

led = Pin(18, Pin.OUT)

while True: 
    mensaje = sys.stdin.readline().strip() # Lee el mensaje enviado desde Python y lo guarda en la variable mensaje.
    
    if mensaje == "ENCENDER": # Si el mensaje recibido es "ENCENDER"
        led.value(1) # Enciende el LED
        
    if mensaje == "APAGAR": # Si el mensaje recibido es "APAGAR"
        led.value(0) # Apaga el LED
        
        
# python -m mpremote connect COM10 fs ls 16_contro_Led.py :main.py
