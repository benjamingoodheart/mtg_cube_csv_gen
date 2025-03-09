import requests
from utils.exceptions import LookupSetError, SetCodeLengthError

class CLIUtil:
    """
    Helper utility for CLI validations
    """
    def __init__(self):
        self.set_code = ''

    def validate_num_args(self, args: str)->bool:
        return len(args) == 2

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
