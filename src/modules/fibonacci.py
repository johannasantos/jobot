from ..base.jobot import jobot

def fibonacci(update, context):
    
    # Typing...
    context.bot.send_chat_action(chat_id=update.message.chat_id, action='typing')

    # Take args
    args = context.args 

    # Empty list (no args)
    if not args:
        error = "Tenés que pasarme un número"
        context.bot.send_message(chat_id=update.message.chat_id, 
                                 text=error,
                                 reply_to_message_id=update.message.message_id)
    
    # More than a word
    elif len(args) > 1:
        error = "Tenés que pasarme UN SOLO número"
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=error,
                                 reply_to_message_id=update.message.message_id)

    # Check positive number or 0
    elif not args[0].isdigit():
        error = "Dale che dame un número natural"
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=error,
                                 reply_to_message_id=update.message.message_id)

    # Only one word, check if it is a number
    else:
        # This is a number, take it 
        number = int(args[0])

        if number <= 0:
            error = "Tiene que ser positivo"
            context.bot.send_message(chat_id=update.message.chat_id,
                                    text=error,
                                    reply_to_message_id=update.message.message_id)
        elif number > 19500:
            error = "Disculpame pero puedo calcular hasta el 19500 número de fibonacci :("
            context.bot.send_message(chat_id=update.message.chat_id,
                                    text=error,
                                    reply_to_message_id=update.message.message_id)
        else:
            context.bot.send_message(chat_id=update.message.chat_id,
                                    text=str(fib(number)),
                                    reply_to_message_id=update.message.message_id)


def fib(num):
    # First two fibonacci numbers 1
    if 1 <= num <= 2:
        return 1
    
    # Else, calculate using the formula
    else:
        # Last two values
        last = 1
        penult = 1

        # Every iteration is sum
        for i in range(3, num+1):
            # Next value is the sum between last and penult
            next_fib = last + penult

            # Actualizate penult and last
            penult = last
            last = next_fib

        return last

jobot.add_command("fibonacci", fibonacci,
                  description="Manda el n-ésimo número de fibonacci")
