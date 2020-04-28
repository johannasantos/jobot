# Comando /help
from ..base.jobot import jobot

def help_func(update, context):

    context.bot.send_chat_action(chat_id=update.message.chat_id, action='typing')

    text = []
    for command, description in jobot.command_descriptions.items():
        text.append(f'/{command} - {description}')
    text.sort()

    title = f'@{jobot.user.username}\nVersión {jobot.version}\n\nTodo esto puedo hacer:\n'

    context.bot.send_message(chat_id=update.message.chat_id,
                             text=title + "\n".join(text))

jobot.add_command("help", help_func, args=False)
jobot.add_command("ayuda", help_func, args=False,
                  description="Manda los comandos del bot")
