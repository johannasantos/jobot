# Bibliotecas varias
import logging, sys

if __name__ == '__main__':

    # Set logs
    from src.base.logs import set_logs
    set_logs()
    
    # Start bot
    from src.base.jobot import jobot   
    from src.modules import *

    jobot.start_bot()
