import unittest
import csv
from utils import cube_driver, cli_util, exceptions

class TestDriver(unittest.TestCase):
    def test_driver(self):
        c = cube_driver.CubeDriver('ons')
        assert c.url == "https://api.scryfall.com/sets/ons"

    def test_bad_url(self):
        c = cube_driver.CubeDriver('3ed')
        self.assertFalse(c.url == "https://api.scryfall.com/sets/ons")

    def test_get_json(self):
        c = cube_driver.CubeDriver('ons')
        self.assertIsNotNone(len(c.get_json()))

    def test_get_json_data(self):
        c = cube_driver.CubeDriver('ons')
        self.assertGreater(len(c.get_json_data()), 0)

class TestsDriverTwo(unittest.TestCase):
    def setUp(self):
        self.c = cube_driver.CubeDriver('ons')

    def test_driver(self):
        self.c.add_cards()
        while self.c.has_more() is True:
            self.c.set_url(self.c.search_obj["next_page"])
            self.c.set_next_page_obj()
            self.c.add_cards()

        self.assertEqual(len(self.c.cards) - 1, self.c.get_total_cards())

    def test_calc_qty(self):
        assert self.c.calc_desired_qty("common") == 4
        assert self.c.calc_desired_qty("uncommon") == 3
        assert self.c.calc_desired_qty("rare") == 1
        assert self.c.calc_desired_qty("mythic") == 1
        assert self.c.calc_desired_qty("promo") == 0

    def test_csv_write(self):
        self.c.add_all_cards()
        self.c.write_csv()
        
        with open('./out/ons_cards.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            limit = 5
            cnt = 0
            for row in reader:
                cnt +=1
                if cnt <= limit:
                    print(row)
                else:
                    pass


    
class TestCustomExceptions(unittest.TestCase):
    def test_too_few_exceptions(self):
        e = exceptions.TooFewArgumentsError()
        self.assertRaises(e.__class__)

    def test_set_length_error(self):
        e = exceptions.SetCodeLengthError()
        self.assertRaises(e.__class__)

    def test_set_lookup_error(self):
        e = exceptions.LookupSetError()
        self.assertRaises(e.__class__)

class TestCLIUtil(unittest.TestCase):
    def test_good_set(self):
        cli = cli_util.CLIUtil()
        self.assertIs(cli.validate_set_code("ONS"), True)

    def test_bad_set(self):
        cli = cli_util.CLIUtil()
        cli
        self.assertRaises(Exception)

        cli._set_set_code('a')
        self.assertRaises(Exception)

        cli._set_set_code("123")
        self.assertRaises(Exception)

    def test_good_arguments(self):
        cli = cli_util.CLIUtil()
        ans = cli.validate_num_args(["app.py", "ons"])
        self.assertIs(ans, True)

    def test_bad_arguments(self):
        cli = cli_util.CLIUtil()
        self.assertFalse( cli.validate_num_args(["app.py"]))
        self.assertFalse( cli.validate_num_args(["app.py", "ons", "lgn", "scg"]))

if __name__ == "__main__":
    unittest.main()
