import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # GPIO 17 controla a luz

def ligar_luz():
    GPIO.output(17, GPIO.HIGH)

def desligar_luz():
    GPIO.output(17, GPIO.LOW)

try:
    ligar_luz()
    time.sleep(5)  # Liga por 5 segundos
    desligar_luz()
except KeyboardInterrupt:
    GPIO.cleanup()