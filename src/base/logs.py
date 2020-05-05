import sys, logging

def check_args():
    # Take args
    args = sys.argv[1:]
    loglevel, logfile = None, None
    valid_levels = ["DEBUG", "WARNING", "INFO", "CRITICAL", "ERROR", "NOTSET"]

    for arg in args:
        arg = arg.lower()
            
        # Set loglevel
        if arg.startswith("--loglevel="):
            if loglevel is not None:
                print(f'loglevel parameter passed more than one time, '
                        f'{arg[11:]} will be ignored.')
            else:
                arg_level = arg[11:].upper()
                if not arg_level in valid_levels:
                    print(f'loglevel parameter ({arg_level}) is not valid, '
                          f'it will be ignored')
                else:
                    loglevel = arg_level
                    print(f'loglevel input: {loglevel}')

        # Set logfile
        elif arg.startswith("--logfile="):
            if logfile is not None:
                print(f'logfile parameter passed more than one time, '
                      f'{arg[7:]} will be ignored.')
            elif arg.endswith(".log"):
                    logfile = arg[10:]
            else:
                print(f'logfile parameter ({logfile}) not taken, '
                      f'must finish with .log and must have not got spaces.')
            
        # Set logfile with default name
        elif arg == "-lf":
            if logfile is None:
                logfile = "bot_logs.log"
            else:
                print(f'logfile alredy setted as {logfile}')
        # Wrong input
        else:
            print(f'{arg} not recognized as a parameter, it will be ignored.\n'
                  "\nUse --loglevel= to pass the level of the logger. Levels allowed "
                  "are 'notset', 'debug', 'info', 'warning', 'error' and 'critical'\n"
                  "Use --logfile= to pass the file were the logs will be write. "
                  "Any file that ended with '.log' is valid.\n"
                  "Use -lf to set 'bot_logs.log' as a logfile.\n")

    return loglevel, logfile


def set_logs():
    # Call the script with no args
    if len(sys.argv) == 1:
        loglevel, logfile = None, None
    
    # Call the script with args
    else:
        loglevel, logfile = check_args()

    if loglevel is None: loglevel = "INFO"
    print(f'Logger seted on {loglevel}')

    # This handler bullshit is for both see on console write the logs on logfile
    handlers = [logging.StreamHandler()]
    
    if logfile is None:
        print("No logfile")
    else:
        handlers.append(logging.FileHandler(logfile))
        print(f'Logs will be append on: {logfile}')

    logging.basicConfig(format=("%(asctime)s - %(name)s - "
                                "%(levelname)s - %(message)s"),
                        level=loglevel, handlers=handlers)
