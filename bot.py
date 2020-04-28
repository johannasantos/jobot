# Bibliotecas varias
import logging, sys

if __name__ == '__main__':

    if len(sys.argv) == 1:
        level = logging.INFO
        logging.info("Logger seted on INFO")
    elif len(sys.argv) == 2 and sys.argv[1].lower() == "--debug":
        level = logging.DEBUG
#       logging.debug("Logger seted on DEBUG")
    else:
        level = logging.INFO
#        logging.info(f'Error on the arguments, only valid argument is --debug\', '
#                     f'you have passed \'{" ".join(sys.argv)}\'')

    logging.basicConfig(format=("%(asctime)s - %(name)s - "
                                "%(levelname)s - %(message)s"),
                        level=level)
    # Inicio bot
    from src.base.jobot import jobot   
    from src.modules import *

    jobot.start_bot()
