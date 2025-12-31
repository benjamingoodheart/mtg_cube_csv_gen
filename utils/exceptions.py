class TooFewArgumentsError(Exception):
    def __init__(self)->None:
        self.msg = """
        Error! You didn't pass enough arguments. 
        You'll need a set code. Try `python3 app.py ONS`"""
        super().__init__(self.msg)

    def __str__(self)->str:
        return f'{self.msg}'
        
class SetCodeLengthError(Exception):
    def __init__(self)->None:
        self.msg = "Error! Set Code Must Be Exaclty 3 Characters ie SCG "
        super().__init__()

    def __str__(self)->str:
        return f'{self.msg}'

class LookupSetError(Exception):
    def __init__(self)->None:
        self.msg = "Error! Could not locate set on scryfall"
        super().__init__()

    def __str__(self)->str:
        return f'{self.msg}'

class ConflictingFlagsError(Exception):
    def __init__(self)->None:
        self.msg = "Error! You cannot use -r and -cq in the same command. Please only use one of those flags"
        super().__init__()
    
    def __str__(self)->str:
        return f'{self.msg}'
    
class NoCustomQuantityError(Exception):
    def __init__(self)->None:
        self.msg = "Error! You did not pass a quantity after the -cq flag. Try something like `python3 app.py LGN -cq 4`"
        super().__init__()
    
    def __str__(self)->str:
        return f'{self.msg}'