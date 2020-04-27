# Comando /help
import globales


def ayuda(update, context):

    # Tomo descripciones
    descripciones = globales.descripciones

    # Aviso que voy a mandar un mensajillo
    context.bot.send_chat_action(chat_id=update.message.chat_id, action='typing')

    # En texto voy a ir guardando los comandos descriptos
    texto = ["Comandos del bot:\n"]

    # Itero sobre descripciones para irlas obteniendo
    for comando, desc in descripciones.items():
        # La oración es "/comando descripción"
        oracion = "/" + comando + " " + desc
        # Lo agergo al texto que va a pasar el botazo
        texto.append(oracion)

    # "texto" es una lista y lo tengo que transformar en un lindo string
    texto = "\n".join(texto)

    # Finalmente mando le mensaje
    context.bot.send_message(chat_id=update.message.chat_id, text=texto)