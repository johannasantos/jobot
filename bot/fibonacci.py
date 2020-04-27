def fibonacci(update, context):
    
    # Aviso que voy a mandar un mensajillo
    context.bot.send_chat_action(chat_id=update.message.chat_id, action='typing')

    # Tomo argumentos que acompañan al comando
    args = context.args 

    # Si la lista está vacía (no pasaron argumentos)
    if not args:
        error = "Tenés que pasarme un número"
        context.bot.send_message(chat_id=update.message.chat_id, 
                                 text=error,
                                 reply_to_message_id=update.message.message_id)
    
    # Si pasan más de una palabra
    elif len(args) > 1:
        error = "Tenés que pasarme UN SOLO número"
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=error,
                                 reply_to_message_id=update.message.message_id)

    # Me fijo que sea un número positivo o 0, si es cualquier otra cosa tiro error
    elif not args[0].isdigit():
        error = "Dale che dame un número natural"
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=error,
                                 reply_to_message_id=update.message.message_id)

    # Si entro acá es porque pasaron una sola palabra, tengo que ver que sea un número
    else:
        # Ya se que es un número, lo tomo entonces
        numero = int(args[0])

        if numero <= 0:
            error = "Tiene que ser positivo"
            context.bot.send_message(chat_id=update.message.chat_id,
                                    text=error,
                                    reply_to_message_id=update.message.message_id)
        elif numero > 19500:
            error = "Disculpame pero puedo calcular hasta el 19500 número de fibonacci :("
            context.bot.send_message(chat_id=update.message.chat_id,
                                    text=error,
                                    reply_to_message_id=update.message.message_id)
        else:
            context.bot.send_message(chat_id=update.message.chat_id,
                                    text=str(fib(numero)),
                                    reply_to_message_id=update.message.message_id)


def fib(num):
    # Los primeros dos números de fibonacci son 1
    if 1 <= num <= 2:
        return 1
    
    # Si no, lo calculo usando la fórmula
    else:
        # Tomo los dos últimos valores
        ultimo = 1
        ante_ultimo = 1

        # Cada iteración es una suma
        for i in range(3, num+1):
            # El próximo valor de la sucesión es la suma de los dos anteriores
            proximo = ultimo + ante_ultimo

            # El anteúltimo pasa a ser el que antes fue el último
            ante_ultimo = ultimo
            # Y el último es justamente el último valor calculado
            ultimo = proximo

        return ultimo
