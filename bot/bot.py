# Bibliotecas varias
import yaml
import logging
import os

# Nos traemos bellas funciones de la biblioteca de bots para python
from telegram.ext import Updater, CommandHandler, PrefixHandler


def main():
    # Inicializamos el botazo
    try:
        # Levanto los datos de inicialización
        datos = datos_config()

        # Tomo la token de los datos (datos es un diccionario)
        token = datos['tg_token']
        # Creo el actualizador que leerá los mensajes que vayan llegando
        updater = Updater(token=token, use_context=True)

        # Seteo el logger
        logging.basicConfig(format='''%(asctime)s - %(name)s - 
                                    %(levelname)s - %(message)s''',
                            level=logging.INFO)

        # Guardo el despachador de mensajes acá
        dispatcher = updater.dispatcher
        # Inicializo los comandos
        agregar_comandos(dispatcher)

        # Empezamos a recibir los mensajes de telegram con esto
        updater.start_polling()
        # Si en algún momento muere, entonces nos quedamos haciendo nada
        updater.idle()

    # EL HORROR
    except Exception as e:
        logging.critical('OH POR DIOS EL BOT HA MUERTO')
        raise e


def datos_config():
    # Obtengo el archivo config, está así medio turbina porque
    # depende de donde se ejecute el bot, puede cambiar
    directorio = os.path.dirname(__file__)
    archivo = os.path.join(directorio, "datos/config.yml")

    # Lo abro y hago la magia
    with open(archivo, 'r') as datos:
        # Por si aparece un error salvaje
        try:
            # Devuelvo los datos en buen formato
            return yaml.safe_load(datos)
        except yaml.YAMLError as exc:
            logging.critical('NO SE PUDIERON CARGAR LOS DATOS DEL BOT')
            raise exc

# Habría que buscar una forma de hacer esto de forma más linda porque va a
# escalar violentamente en el futuro


def agregar_comandos(dispatcher):

    # Llamo a ayuia para ir guardando las descripciones de cada comando
    import globales
    descripciones = globales.descripciones

    # Armo los prefijos para los comandos
    prefijos = ["!", "$", ".", ">"]

    # Comando /start
    from start import start
    agregar(dispatcher, prefijos, "start", start,
            descripciones, "Inicia el bot")
    agregar(dispatcher, prefijos, "inicio", start)

    # Comando /help
    from ayuda import ayuda
    desc_help = "Manda los comandos disponibles del bot"
    agregar(dispatcher, prefijos, "help", ayuda, descripciones, desc_help)
    agregar(dispatcher, prefijos, "ayuda", ayuda)

    # Comando /fibonacci
    from fibonacci import fibonacci
    desc_fib = "Calcula el n-ésimo número de fibonacci"
    agregar(dispatcher, prefijos, "fibonacci",
            fibonacci, descripciones, desc_fib, True)

    # Comando /vanzazo
    from randomVanzazo import image_random_generator
    desc_van = "Envia una foto random de van"
    agregar(dispatcher, prefijos, "vanzazo", image_random_generator, descripciones, desc_van)


def agregar(dispatcher, prefijos, comando, funcion,
            descripciones=None, desc_comando=None,
            args=False):
    dispatcher.add_handler(CommandHandler(comando, funcion, pass_args=args))
    dispatcher.add_handler(PrefixHandler(
        prefijos, comando, funcion, pass_args=args))

    if not (descripciones is None or desc_comando is None):
        descripciones[comando] = desc_comando


# Llamamos al método main para ejecutarlo
if __name__ == '__main__':
    main()
