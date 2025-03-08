import requests
from utils.exceptions import LookupSetError, SetCodeLengthError

class CLIUtil:
    def __init__(self):
        pass

    def validate_num_args(self, args)->bool:
        return(len(args) == 2) 
           
    def validate_set_code(self, set_code)-> bool:
        try:
            if (len(set_code) == 3) is False:
                raise SetCodeLengthError
            else:
                return True  
        except SetCodeLengthError as e:
            print(e)
            
        try:
            url = f'https://api.scryfall.com/sets/{set_code}'
            headers = {'user-agent': 'bg-dev-cube-gen-app'}
            r = requests.get(url, headers=headers)
            if r.status_code != 200:
                raise Exception
        except Exception as e:
            print("\nError! Could not locate set on scryfall", e)
            return False
        
        return True

    def _set_set_code(self, set_code):
        self.validate_set_code(set_code)
        self.set_code = set_code
        
        