import os
import json

class Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

class NoConfigDataException(Exception):
    def __init__(self, msg):
        super.__init__(msg)

getch = Getch()

def config(args: dict=None) -> dict:
    """Load or save a config file

    Args:
        args (dict, optional): The config data to save. Key is in-program name, value is user prompt. Defaults to None.

    Returns:
        dict: Parsed JSON output
    """
    
    if os.path.exists(r".\config.ini"):  return __load()
    else:                                return __create(args)

def deleteConfig():
    """Deletes the config
    """

    os.remove(r".\config.ini")

def updateConfig(args):
    print("-----                 UPDATING CONFIG                 -----")
    print("----- [N]ext | [P]revious | [ENTER] Change | [F]inish -----")

    conf = __load()
    selectionIdx = 0
    while True:
        print(f"\033[2K\r  {list(args.values())[selectionIdx]} >>>{list(conf.values())[selectionIdx]}", end="\r")

        char = getch()
        
        if char.lower() == b"n":
            if selectionIdx < len(conf.values()) - 1:  selectionIdx += 1
            else:                                  selectionIdx = 0

        elif char.lower() == b"p":
            if selectionIdx > 0:  selectionIdx -= 1
            else:                 selectionIdx = len(conf.values()) - 1

        elif char == b"\r" or char == b"\n":
            option = input(f"\033[2K\r{list(args.values())[selectionIdx]} >>>")
            print(end="\033[1A") # Move cursor up
            conf[list(conf.keys())[selectionIdx]] = option

        elif char == b"f":
            __save(conf)
            break

def __load():
    with open(r".\config.ini", "r") as file:
        data = file.readlines()

    data = json.loads("".join(data).replace("'", '"'))
    return data

def __save(conf):
    with open(r".\config.ini", "w") as file:
        file.write(str(conf))

def __create(args):
    if args == None: raise NoConfigDataException("No config file was found and no config arguments were passed")

    with open(r".\config.ini", "w") as file:
        print("----- FIRST RUN CONFIG -----")
        data = {}
        
        for key, value in args.items():
            data[key] = input(value + " >>>")

        file.write(str(data))

    return data
