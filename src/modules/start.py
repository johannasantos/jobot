# Comando /start
from ..base.jobot import jobot

def start(update, context):
    # Aviso que voy a mandar un mensajillo
    context.bot.send_chat_action(chat_id=update.message.chat_id, action='typing')
    # Mando el mensaje jeje
    text = "OLA, soy la mismísima JOBOT\nMandá /help para saber qué hago!"
    context.bot.send_message(chat_id=update.message.chat_id, text=text)

jobot.add_command("start", start, args=False,
                  description="Inicia el bot")
jobot.add_command("inicio", start, args=False)
