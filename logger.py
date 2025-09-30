import datetime
import sys

class LoggingTypes:
    Prefix = 0
    Plain = 1

class AnsiColorCodes:
    Reset = "\033[0m"
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    White = "\033[37m"
    Gray = "\033[2m"

    EscapeSequence = "\033["
    
    TypeNormal = "0;"
    TypeBold = "1;"
    TypeItalic = "3;"
    TypeUnderline = "4;"
    TypeShiftHue = "5;"
    
    ColorBlack = "30;"
    ColorRed = "31;"
    ColorGreen = "32;"
    ColorYellow = "33;"
    ColorBlue = "34;"
    ColorPink = "35;"
    ColorWhite = "37;"
    ColorDefault = "49;"
    
    BackBlack = "40"
    BackRed = "41"
    BackGreen = "42"
    BackYellow = "43"
    BackBlue = "44"
    BackPurple = "45"
    BackWhite = "47"
    BackDefault = "49"
    
    Finish = "m"
    
    FullReset = "\033[0;0;0m"

class FunctionLogger:
    def __init__(self, timestamps: bool = False, stdout = sys.stdout):
        """Initialises the function logger
        Logs the function that called the logger instead of the log type

        Args:
            timestamps (bool, optional): Enable or disable the printing of timestamps. Defaults to False.
            stdout (any, optional): The output stream to write to. Defaults to sys.stdout.
        """

        self.timestamps = timestamps
        self.stdout = stdout

    def log(self, function: str, msg: str, functionTextColor: AnsiColorCodes = AnsiColorCodes.Reset):
        """Log a message from a function

        Args:
            function (str): The function name that called the log function
            msg (str): The message to log
            functionTextColor (AnsiColorCodes, optional): The color of the text saying the function name. Defaults to AnsiColorCodes.Reset.
        """

        timestamp = ""
        if self.timestamps:
            timestamp = f"{AnsiColorCodes.Gray}{datetime.datetime.now().time()}{AnsiColorCodes.Reset} "

        print(f"{timestamp}[{functionTextColor}{function}{AnsiColorCodes.Reset}] {msg}", file=self.stdout)

class Logger:
    def __init__(self, logging_type: LoggingTypes, timestamps: bool = False, stdout = sys.stdout):
        """Initialises the logger

        Args:
            logging_type (LoggingTypes): How to log messages (Prefix: [*] MSG, Plain: MSG)
            timestamps (bool, optional): Enable or disable the printing of timestamps. Defaults to False.
            stdout (any, optional): The output stream to write to. Defaults to sys.stdout.
        """

        self.logging_type = logging_type
        self.timestamps = timestamps
        self.stdout = stdout

    def info(self, msg: str):
        prefixes = ""

        if self.timestamps:
            prefixes += f"{AnsiColorCodes.Reset}{datetime.datetime.now().time()}{AnsiColorCodes.Reset} "
        if self.logging_type == LoggingTypes.Prefix:
            prefixes += f"{AnsiColorCodes.Reset}[{AnsiColorCodes.Green}+{AnsiColorCodes.Reset}] "

        prefixes += f"{AnsiColorCodes.Green}INFO      {AnsiColorCodes.Reset} "

        print(f"{prefixes}{msg}", file=self.stdout)

    def notice(self, msg: str):
        prefixes = ""

        if self.timestamps:
            prefixes += f"{AnsiColorCodes.Reset}{datetime.datetime.now().time()}{AnsiColorCodes.Reset} "
        if self.logging_type == LoggingTypes.Prefix:
            prefixes += f"{AnsiColorCodes.Reset}[{AnsiColorCodes.Blue}*{AnsiColorCodes.Reset}] "

        prefixes += f"{AnsiColorCodes.Blue}NOTICE    {AnsiColorCodes.Reset} "

        print(f"{prefixes}{msg}", file=self.stdout)

    def warning(self, msg: str):
        prefixes = ""

        if self.timestamps:
            prefixes += f"{AnsiColorCodes.Reset}{datetime.datetime.now().time()}{AnsiColorCodes.Reset} "
        if self.logging_type == LoggingTypes.Prefix:
            prefixes += f"{AnsiColorCodes.Reset}[{AnsiColorCodes.Yellow}-{AnsiColorCodes.Reset}] "

        prefixes += f"{AnsiColorCodes.Yellow}WARNING   {AnsiColorCodes.Reset} "

        print(f"{prefixes}{msg}", file=self.stdout)

    def alert(self, msg: str):
        prefixes = ""

        if self.timestamps:
            prefixes += f"{AnsiColorCodes.Reset}{datetime.datetime.now().time()}{AnsiColorCodes.Reset} "
        if self.logging_type == LoggingTypes.Prefix:
            prefixes += f"{AnsiColorCodes.Reset}[{AnsiColorCodes.Magenta}-{AnsiColorCodes.Reset}] "

        prefixes += f"{AnsiColorCodes.Magenta}ALERT     {AnsiColorCodes.Reset} "

        print(f"{prefixes}{msg}", file=self.stdout)

    def error(self, msg: str):
        prefixes = ""

        if self.timestamps:
            prefixes += f"{AnsiColorCodes.Reset}{datetime.datetime.now().time()}{AnsiColorCodes.Reset} "
        if self.logging_type == LoggingTypes.Prefix:
            prefixes += f"{AnsiColorCodes.Reset}[{AnsiColorCodes.Red}!{AnsiColorCodes.Reset}] "

        prefixes += f"{AnsiColorCodes.Red}ERROR     {AnsiColorCodes.Reset} "

        print(f"{prefixes}{msg}", file=self.stdout)

    def critical(self, msg: str):
        prefixes = ""

        if self.timestamps:
            prefixes += f"{AnsiColorCodes.Reset}{datetime.datetime.now().time()}{AnsiColorCodes.Reset} "
        if self.logging_type == LoggingTypes.Prefix:
            prefixes += f"{AnsiColorCodes.Reset}[{AnsiColorCodes.Red}!{AnsiColorCodes.Reset}] "

        prefixes += f"{AnsiColorCodes.Red}CRITICAL  {AnsiColorCodes.Reset} "

        print(f"{prefixes}{msg}", file=self.stdout)
