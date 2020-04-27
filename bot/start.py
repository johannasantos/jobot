# Comando /start

def start(update, context):
    # Aviso que voy a mandar un mensajillo
    context.bot.send_chat_action(chat_id=update.message.chat_id, action='typing')
    # Mando el mensaje jeje
    texto = "OLA, soy la mismísima JOBOT\nMandá /help para saber qué hago!"
    context.bot.send_message(chat_id=update.message.chat_id, text=texto)