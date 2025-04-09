import RPi.GPIO as GPIO
import time
from twilio.rest import Client

# Configurações do Twilio
account_sid = "SEU_SID"
auth_token = "SEU_TOKEN"
client = Client(account_sid, auth_token)

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Sensor de porta
GPIO.setup(23, GPIO.OUT) # Relay da porta.

def enviar_sms(mensagem):
    client.messages.create(body=mensagem, from_="SEU_NUMERO_TWILIO", to="NUMERO_DESTINO")

try:
    while True:
        porta_aberta = GPIO.input(18)
        if porta_aberta:
            enviar_sms("Porta da garagem aberta!")
            GPIO.output(23, GPIO.HIGH) # liga a porta
            time.sleep(2)
            GPIO.output(23, GPIO.LOW) # Desliga a porta
            time.sleep(60) # Intervalo para evitar spam.
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()