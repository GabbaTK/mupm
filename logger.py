import datetime

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

class Logger:
    def __init__(self, logging_type: LoggingTypes, timestamps: bool = True, log_type: bool = False):
        """Initialises the logger

        Args:
            logging_type (LoggingTypes): How to log messages (Prefix: [*] MSG, Plain: MSG)
            timestamps (bool, optional): Enable or disable the printing of timestamps. Defaults to True.
            log_type (bool, optional): Whether to log just the message or include the type (INFO, WARNING, CRITICAL). Defaults to False.
        """

        self.logging_type = logging_type
        self.timestamps = timestamps
        self.log_type = log_type

    def info(self, msg: str):
        prefixes = ""

        if self.timestamps:
            now = datetime.datetime.now()
            prefixes += f"{AnsiColorCodes.Reset}{now.time()}{AnsiColorCodes.Reset} "
        if self.logging_type == LoggingTypes.Prefix:
            prefixes += f"{AnsiColorCodes.Reset}[{AnsiColorCodes.Green}+{AnsiColorCodes.Reset}] "
        if self.log_type:
            prefixes += f"{AnsiColorCodes.Green}INFO      {AnsiColorCodes.Reset} "

        print(f"{prefixes}{AnsiColorCodes.Green}{msg}{AnsiColorCodes.Reset}")

    def notice(self, msg: str):
        prefixes = ""

        if self.timestamps:
            now = datetime.datetime.now()
            prefixes += f"{AnsiColorCodes.Reset}{now.time()}{AnsiColorCodes.Reset} "
        if self.logging_type == LoggingTypes.Prefix:
            prefixes += f"{AnsiColorCodes.Reset}[{AnsiColorCodes.Blue}*{AnsiColorCodes.Reset}] "
        if self.log_type:
            prefixes += f"{AnsiColorCodes.Blue}NOTICE    {AnsiColorCodes.Reset} "

        print(f"{prefixes}{AnsiColorCodes.Blue}{msg}{AnsiColorCodes.Reset}")

    def warning(self, msg: str):
        prefixes = ""

        if self.timestamps:
            now = datetime.datetime.now()
            prefixes += f"{AnsiColorCodes.Reset}{now.time()}{AnsiColorCodes.Reset} "
        if self.logging_type == LoggingTypes.Prefix:
            prefixes += f"{AnsiColorCodes.Reset}[{AnsiColorCodes.Yellow}-{AnsiColorCodes.Reset}] "
        if self.log_type:
            prefixes += f"{AnsiColorCodes.Yellow}WARNING   {AnsiColorCodes.Reset} "

        print(f"{prefixes}{AnsiColorCodes.Yellow}{msg}{AnsiColorCodes.Reset}")

    def alert(self, msg: str):
        prefixes = ""

        if self.timestamps:
            now = datetime.datetime.now()
            prefixes += f"{AnsiColorCodes.Reset}{now.time()}{AnsiColorCodes.Reset} "
        if self.logging_type == LoggingTypes.Prefix:
            prefixes += f"{AnsiColorCodes.Reset}[{AnsiColorCodes.Magenta}-{AnsiColorCodes.Reset}] "
        if self.log_type:
            prefixes += f"{AnsiColorCodes.Magenta}ALERT     {AnsiColorCodes.Reset} "

        print(f"{prefixes}{AnsiColorCodes.Magenta}{msg}{AnsiColorCodes.Reset}")

    def error(self, msg: str):
        prefixes = ""

        if self.timestamps:
            now = datetime.datetime.now()
            prefixes += f"{AnsiColorCodes.Reset}{now.time()}{AnsiColorCodes.Reset} "
        if self.logging_type == LoggingTypes.Prefix:
            prefixes += f"{AnsiColorCodes.Reset}[{AnsiColorCodes.Red}!{AnsiColorCodes.Reset}] "
        if self.log_type:
            prefixes += f"{AnsiColorCodes.Red}ERROR     {AnsiColorCodes.Reset} "

        print(f"{prefixes}{AnsiColorCodes.Red}{msg}{AnsiColorCodes.Reset}")

    def critical(self, msg: str):
        prefixes = ""

        if self.timestamps:
            now = datetime.datetime.now()
            prefixes += f"{AnsiColorCodes.Reset}{now.time()}{AnsiColorCodes.Reset} "
        if self.logging_type == LoggingTypes.Prefix:
            prefixes += f"{AnsiColorCodes.Reset}[{AnsiColorCodes.Red}!{AnsiColorCodes.Reset}] "
        if self.log_type:
            prefixes += f"{AnsiColorCodes.Red}CRITICAL  {AnsiColorCodes.Reset} "

        print(f"{prefixes}{AnsiColorCodes.Red}{msg}{AnsiColorCodes.Reset}")
