from sys import argv

class RootNameNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)

class WrongArgumentType(Exception):
    def __init__(self, message):
        super().__init__(message)

class ArgumentOrder:
    Options = 0
    Positional = 1

class Option:
    def __init__(self, argument: str | list[str], code_name: str, arg_type, help: str, default = None):
        """
        Creates a new option for the program

        argument: The argument/aliases for search for (-v, --verbose...)
        code_name: The variable name to refrence in your code
        arg_type: What type is the argument (str, int), can be None to specify an argument without parameters
        help: When -h or --help is used, what should be displayed for this argument
        default: What is the default value if its not provided (leave blank to make this argument mandatory)
        """

        if type(argument) == str:
            self.argument = argument.lower()
        elif type(argument) == list:
            self.argument = []
            for sub_arg in argument:
                self.argument.append(sub_arg.lower())

        self.code_name = code_name
        self.arg_type = arg_type
        self.default = default
        self.help = help
        self.type = ArgumentOrder.Options
    
class Positional:
    def __init__(self, argument: str, code_name: str, position: int, arg_type, default = None):
        """
        Creates a new option for the program

        argument: The argument displayed in help (your_program.py [OPTIONS] POSITIONAL-ARGUMENT)
        code_name: The variable name to refrence in your code
        position: In what position will the argument be provided (python your_program.py POSITIONAL-ARGUMNET-POSITION-1, POSITIONAL-ARGUMENT-POSITION-2)
        arg_type: What type is the argument (str, int)
        default: What is the default value if its not provided (leave blank to make this argument mandatory)
        """

        self.code_name = code_name
        self.argument = argument.lower()
        self.position = position
        self.arg_type = arg_type
        self.default = default
        self.type = ArgumentOrder.Positional

class ArgumentHandler:
    def __init__(self, description: str):
        """
        Creates a handler for script arguments

        description: A description for the program that is displayed once the -h argument is used or invalid arguments are passed
        """

        self.description = description
        self.arguments = []

    def generateHelp(self, root_name):
        print(f"python {root_name}", end="")

        for arg in self.arguments:
            if arg.type == ArgumentOrder.Options:
                print(" [OPTIONS]", end="")
                break

        position_index = 1
        found = False
        while True:
            for arg in self.arguments:
                if arg.type == ArgumentOrder.Positional:
                    if arg.position == position_index:
                        found = True
                        print(f" {arg.argument.upper()}", end="")

            if not found:
                break

            found = False
            position_index += 1

        print("\n")

        print(self.description)

        print()

        print("ARGUMENTS")
        
        # Find the biggest argument
        biggest_len = 0
        for arg in self.arguments:
            if arg.type == ArgumentOrder.Options:
                # One alias
                if type(arg.argument) == str:
                    if len(arg.argument) > biggest_len:
                        biggest_len = len(arg.argument)

                # Multiple aliases
                if type(arg.argument) == list:
                    for alias in arg.argument:
                        if len(alias) > biggest_len:
                            biggest_len = len(alias)

        biggest_len += 2 # To add a little bit more spacing 

        for arg in self.arguments:
            if arg.type == ArgumentOrder.Options:
                # One alias
                if type(arg.argument) == str:
                    tab_distance = " " * (biggest_len - len(arg.argument))
                    
                    print(f"\t{arg.argument}    {tab_distance}{arg.help}")
                
                # Multiple aliases
                if type(arg.argument) == list:
                    for sub_arg in arg.argument:
                        tab_distance = " " * (biggest_len - len(sub_arg))

                        print(f"\t{sub_arg}    {tab_distance}{arg.help}")

        exit()

    def add(self, arg):
        """
        Adds an argument

        arg: The argument (Positional or Option)
        """

        self.arguments.append(arg)

    def parse(self, root_name: str):
        """
        Parses all the arguments provided

        root_name: The name of the main program running, if you only use it, it will be __file__
        """

        if "-h" in argv or "--help" in argv:
            self.generateHelp(root_name)

        try:
            ignore_index = argv.index(root_name)
        except ValueError:
            #raise RootNameNotFound("The provided root name was incorrent")
            ignore_index = 0
        
        args = argv[ignore_index + 1:]

        arguments = {}
        for arg in self.arguments:
            arguments[arg.code_name] = arg.default
        
        # Parse options
        found = False
        found_arg = ""
        for input_arg in args:
            if input_arg.startswith("-"):
                found = True

                # Check if its an argument without a parameter
                for arg in self.arguments:
                    if arg.type == ArgumentOrder.Options:
                        if (type(arg.argument) == str and arg.argument == input_arg) or (type(arg.argument) == list and input_arg in arg.argument):
                            found_arg = arg

                            if arg.arg_type == None:
                                found = False
                                arguments[arg.code_name] = True
            elif found == True:
                found = False

                try:
                    if arguments[found_arg.code_name] != found_arg.default:
                        if type(arguments[found_arg.code_name]) != list:
                            arguments[found_arg.code_name] = [arguments[found_arg.code_name]]
                            arguments[found_arg.code_name].append(found_arg.arg_type(input_arg))
                        else:
                            arguments[found_arg.code_name].append(found_arg.arg_type(input_arg))
                    else:
                        arguments[found_arg.code_name] = found_arg.arg_type(input_arg)
                except:
                    raise WrongArgumentType(f"Argument {input_arg} is type {type(input_arg)}, but is expected to be a type {found_arg.arg_type}")
                
        # Parse positional arguments
        wrong_type = False
        position_index = 1
        for input_arg in args:
            if input_arg.startswith("-"):
                # Check if its an argument without a parameter
                for arg in self.arguments:
                    if arg.type == ArgumentOrder.Options:
                        if (type(arg.argument) == str and arg.argument == input_arg) or (type(arg.argument) == list and input_arg in arg.argument):
                            if arg.arg_type != None:
                                wrong_type = True
                continue

            elif wrong_type:
                wrong_type = False
                continue

            for arg in self.arguments:
                if arg.type == ArgumentOrder.Positional:
                    if arg.position == position_index:
                        arguments[arg.code_name] = arg.arg_type(input_arg)

            position_index += 1

        # Verify that all arguments are present
        for arg in self.arguments:
            if arguments[arg.code_name] == None:
                if arg.default == None:
                    # Argument is missing
                    self.generateHelp(root_name)

        return arguments
