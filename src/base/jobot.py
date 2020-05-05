# Bibliotecas varias
import yaml, logging, os

# Nos traemos bellas funciones de la biblioteca de bots para python
from telegram.ext import Updater, CommandHandler, PrefixHandler, Filters

class group_level():
    
    def __init__(self):
        self.URGENT = 0
        self.IMPORTANT = 1
        self.NORMAL = 2
        self.BASIC = 3
        self.LOW = 4

    def OTHER(level):
        return level

LEVEL = group_level()

class Jobot():

    def __init__(self):
        # Set the data 
        directory = os.path.dirname(__file__)
        file = os.path.join(directory, "../../data/config.yml")
        with open(file, 'r') as data_file:
            data = yaml.safe_load(data_file)

        # Create glorious and magnificent updater, and also save some variables
        updater = Updater(token=data['tg_token'], use_context=True)

        self.bot = updater.bot
        # Remember, if the username
        # is changed when the bot stills running, the user
        # will contain the old username 
        self.user = updater.bot.get_me()
        self.updater = updater
        self.dispatcher = updater.dispatcher
        self.command_descriptions = {}
        self.version = "0.1"

    def start_bot(self):
        try:
            logging.log(msg="JOBOT STARTED", level=99)
            # Start polling messages from telegram
            self.updater.start_polling()
            
            self.updater.idle()

        # THE DEVL
        except Exception as e:
            logging.critical("THE BOT IS FUCKING DEAD")
            raise e

    def add_command(self, command, function, description=None,
                    args=True, edited=False, group_level=LEVEL.NORMAL):
        
        filters = None if edited is True else ~Filters.update.edited_message
    
        # Good old commands
        command_handler = CommandHandler(command, function,
                                         filters=filters, pass_args=args)
        self.dispatcher.add_handler(command_handler, group=group_level)
    
        # Prefix commands
        prefixes = ["!", "$", ".", ">"]
        prefix_handler = PrefixHandler(prefixes, command, function,
                                        filters=filters, pass_args=args)
        self.dispatcher.add_handler(prefix_handler, group=group_level)
    
        # TODO: add "alias command args"
    
        if description is not None:
            self.command_descriptions[command] = description


jobot = Jobot()
