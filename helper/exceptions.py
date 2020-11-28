class ArgumentError(Exception):
    """ Exception raised for errors in the input arguments

    Attributes:
        argument -- input argument that raised the exception
        expected argument -- expected arguments
    """

    def __init__(self, argument):
        self.argument = f"Given Argument: {argument}"