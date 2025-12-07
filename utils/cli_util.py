import requests
from utils.exceptions import LookupSetError, SetCodeLengthError
from utils.flags import Flags

class CLIUtil:
    """
    Helper utility for CLI validations
    """
    def __init__(self):
        self.set_code = ''
        self.f = Flags()
        self.options = []

    def count_args(self, args:list)-> int:
        return len(args)

    def has_flags(self, args:list)->bool:
        flag_list = self.f.get_flags()
        for arg in args:
            if arg in flag_list:
                return True
        return False
        
    def validate_num_args(self, args: str)->bool:
        return len(args) >= 2

    def validate_set_code(self, set_code: str)-> bool:
        try:
            if (len(set_code) == 3) is False:
                raise SetCodeLengthError
            return True
        except SetCodeLengthError as e:
            print(e)

        try:
            url = f'https://api.scryfall.com/sets/{set_code}'
            headers = {'user-agent': 'bg-dev-cube-gen-app'}
            r = requests.get(url, headers=headers)
            if r.status_code != 200:
                raise LookupSetError
        except LookupSetError as e:
            print(e)
        return True

    def _set_set_code(self, set_code):
        self.validate_set_code(set_code)
        self.set_code = set_code
        
    def get_options(self)->list:
        return self.options
        
    def set_options(self, options:list)-> None:
        for option in options:
            if option == '-r':
                self.options.append('-r')
            if option == '-cq':
                self.options.append('-cq')
                self.options.append(options[options.index('-cq')+1])
            if option == '-e':
                e_index = options.index('-e')
                for i, option in enumerate(options):
                    if option in ('-r', '-cq'):
                        break
                    #only append the number once
                    if option not in self.options and i >= e_index:
                        self.options.append(option)