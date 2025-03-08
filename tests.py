import unittest
from utils import cube_driver



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
        print(c.get_json())
        
class TestsDriverTwo(unittest.TestCase):
    def setUp(self):
        self.c = cube_driver.CubeDriver('ons')
    
    def test_driver(self):
        self.c.add_cards()
        
    
        print(self.c.search_obj["has_more"])
        while self.c.has_more() is True:
            self.c.set_url(self.c.search_obj["next_page"])
            self.c.set_next_page_obj()
            self.c.add_cards()
            print(self.c.cards)

        
        self.assertGreater(len(self.c.cards), self.c.get_total_cards())
        
if __name__ == "__main__":
    unittest.main()