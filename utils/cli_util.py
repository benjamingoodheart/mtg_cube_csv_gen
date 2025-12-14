import requests
import sys
import re
from utils.exceptions import LookupSetError, SetCodeLengthError, NoCustomQuantityError
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
        
    def validate_num_args(self, args: list)->bool:
        return len(args) >= 2

    def validate_args(self, args:list)->bool:
        if args[2] not in ['-r', '-cq', '-e']:
            return False
        if args in ['-r', '-cq']:
            return False
        if args[2] == '-cq':
            if args[3] is None:
                return False
            if args[3]:
                reg = re.findall(r"\d", args[3])
                if len(reg) == 0:
                    return False
        if args[2] == '-r':
            if len(args) >= 4:
                if args[3] is not None:
                    return False
        if args[2] == '-e':
            if len(args) < 4:
                return False
            if args[3] == '-cq' or args[3] == '-r':
                return False
            if len(args) >=4:
                reg = re.findall(r"\d", args[3])
                if len(reg) == 0:
                    return False                
        return True

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
        try:
            for option in options:
                if option == '-r':
                    self.options.append('-r')
                if option == '-cq':
                    self.options.append('-cq')
                    if options[-1]=='-cq' or options[options.index('-cq')+1]== '-e':
                        raise NoCustomQuantityError
                    self.options.append(options[options.index('-cq')+1])
                if option == '-e':
                    e_index = options.index('-e')
                    for i, option in enumerate(options):
                        if option in ('-r', '-cq'):
                            break
                        #only append the number once
                        if option not in self.options and i >= e_index:
                            self.options.append(option)
        except NoCustomQuantityError as e:
            print(e)
            sys.exit()