import sys
from utils import cube_driver, cli_util
from utils.exceptions import TooFewArgumentsError, TooManyArgumentsError

cli = cli_util.CLIUtil()

try:
    args = sys.argv
    SET_CODE = ''
    
    if cli.validate_num_args(args) is True:
        SET_CODE = args[1]
        if cli.has_flags(args) is True:
            cli.set_options(args)
    else:
        if len(args) < 2:
            raise TooFewArgumentsError
except TooFewArgumentsError as e:
    print(e)
except TooManyArgumentsError as e:
    print(e)

if cli.validate_set_code(SET_CODE) is True:
    driver = cube_driver.CubeDriver(SET_CODE)
    print(f'gathering cards in set: {driver.set_code}')
    driver.add_all_cards()
    print(f'writing to ./out/{driver.set_code}_cards.csv')
    if len(cli.get_options())==0:
        driver.write_csv()
    if len(cli.get_options())>=1:
        flags=cli.get_options()
        driver.write_csv(*flags)
    print("complete!")
