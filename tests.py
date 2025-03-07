import unittest
from utils import cube_driver



class TestDriver(unittest.TestCase):
    def test_driver(self):
        c = cube_driver.CubeDriver('ons')
        assert c.url == "https://api.scryfall.com/cards/search?q=ons"

    def test_bad_url(self):
        c = cube_driver.CubeDriver('3ed')
        self.assertFalse(c.url == "https://api.scryfall.com/cards/search?q=ons")

if __name__ == "__main__":
    unittest.main()