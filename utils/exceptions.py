class TooFewArgumentsError(Exception):
    def __init__(self):
        self.msg = """
        Error! You didn't pass enough arguments. 
        You'll need a set code. Try `python3 app.py ONS`"""
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.msg}'

class TooManyArgumentsError(Exception):
    def __init__(self, args):
        self.msg = """
        Error! Agh! You passed too many arguments. 
        Only pass one after app.py ie. `python3 app.py ONS"""
        self.args = args
        super().__init__(self.args)

    def __str__(self):
        return f'{self.args} -> {self.msg}'

class SetCodeLengthError(Exception):
    def __init__(self,):
        self.msg = "Error! Set Code Must Be Exaclty 3 Characters ie SCG "
        super().__init__()

    def __str__(self):
        return f'{self.msg}'

class LookupSetError(Exception):
    def __init__(self):
        self.msg = "Error! Could not locate set on scryfall"
        super().__init__()

    def __str__(self):
        return f'{self.msg}'
