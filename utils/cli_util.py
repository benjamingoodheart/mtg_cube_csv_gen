import requests
import sys

class CLIUtil:
    def __init__(self):
        pass

    def validate_num_args(self, args):
        try:
            len(args) == 2
        except Exception:
            if len(args) < 2:
                print("\nError! You didn't pass any arguments! Pass a set code like ONS. ie: `python3 app.py ONS`")
                return False
            if len(args) > 2:
                print("\nError! Agh! You passed too many arguments. Only pass one after app.py ie. `python3 app.py ONS")
                return False
        return True
  
    def validate_set_code(self, set_code)-> bool:
        try:
            len(set_code) == 3
        except Exception:
            print("Error! set code must be exactly 3 characters")
            return False
            
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
        
        