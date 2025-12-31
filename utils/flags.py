class Flags:
    """Helper utilities for flags
    """
    def __init__(self)-> None:
        self.flags = [
            '-r', # Rarity <no args>
            '-cq', # Custom Quantity <single arg>
            '-e', # excluding <arbitrary num of arguments>
        ]
    
    def flag_is_valid(self, flag:str)-> bool:
        if flag.lower() in self.flags:
            return True
        return False
    
    def get_flags(self)->list:
        return self.flags

    def is_integer(self, flag:any)->bool:
        if flag is int:
            return True
        return False