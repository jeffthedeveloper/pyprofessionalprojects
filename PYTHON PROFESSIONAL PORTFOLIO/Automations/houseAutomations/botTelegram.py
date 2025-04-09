import telegram
import time

bot = telegram.Bot(token="SEU_TOKEN_TELEGRAM")

def enviar_mensagem(chat_id, mensagem):
    bot.send_message(chat_id=chat_id, text=mensagem)

chat_id = "SEU_CHAT_ID"
enviar_mensagem(chat_id, "Hora de tomar água!")