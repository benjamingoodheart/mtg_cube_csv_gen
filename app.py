from utils import cube_driver, cli_util
import sys

cli = cli_util.CLIUtil()

args = sys.argv
cli.validate_num_args(args)
set_code = args[1]

cli.validate_set_code(set_code)

driver = cube_driver.CubeDriver(set_code)
driver.add_all_cards()
driver.write_csv()
print("complete!")