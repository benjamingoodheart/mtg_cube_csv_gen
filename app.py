from utils import cube_driver, cli_util
from utils.exceptions import TooFewArgumentsError, TooManyArgumentsError
import sys

cli = cli_util.CLIUtil()

try: 
    too_short_error = Exception("Error! You didn't pass enough arguments. You'll need a set code. Try `python3 app.py ONS`")
    too_many_error = Exception("Error! Agh! You passed too many arguments. Only pass one after app.py ie. `python3 app.py ONS")
    args = sys.argv
    set_code = ''
    if cli.validate_num_args(args) is True:
        set_code = args[1]
    else:
        if len(args) < 2:
            raise TooFewArgumentsError
        if len(args) > 2:
            raise TooManyArgumentsError(args)
except TooFewArgumentsError as e:
    print(e)
except TooManyArgumentsError as e:
    print(e)

if cli.validate_set_code(set_code) is True:
    driver = cube_driver.CubeDriver(set_code)
    driver.add_all_cards()
    driver.write_csv()
    print("complete!")