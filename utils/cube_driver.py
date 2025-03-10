"""
Cube Driver module
"""
import csv
import requests # type: ignore

class CubeDriver:
    """
    Main driver class for the cube csv gen application 
    """
    def __init__(self, set_code: str)  -> None:
        """
        Args:
            set_code (str): three character identification code for magic set
        """
        self.set_code = set_code
        self.url = f'https://api.scryfall.com/sets/{set_code}'
        self.headers = {'user-agent': 'bg-dev-cube-gen-app'}

        self.cards = []
        self.r = requests.get(self.url, headers=self.headers)
        self.block_obj = self.r.json()
        self.set_uri = self.block_obj["search_uri"]

        self.r_2 = requests.get(self.set_uri,headers=self.headers)
        self.search_obj = self.r_2.json()

    def get_json(self) -> dict[str, any]:
        return self.block_obj

    def get_total_cards(self) -> int:
        return self.block_obj["card_count"]

    def has_more(self) -> bool:
        return self.search_obj["has_more"]

    def normalize_colorless(self, card_colors:list)->list:
        """
        Normalizes empty card color list to be 'colorless'. 
        Otherwise, returns the passed in card color list.

        Args:
            card_colors (list): list of card colors

        Returns:
            list: card color(s)
        """
        if not card_colors:
            return ["C"]
        return card_colors

    def add_cards(self) -> None:
        """
        iterates over paginated search result and builds a list out of the object
        """
        for o in self.search_obj["data"]:
            self.cards.append({
                'card_name':o["name"], 
                'collector_num':o["collector_number"], 
                'colors': self.normalize_colorless(o["colors"]), 
                'rarity': o["rarity"]})

    def add_all_cards(self) -> None:
        """
        adds every card in a set
        """
        self.add_cards()
        while self.has_more() is True:
            self.set_url(self.search_obj["next_page"])
            self.set_next_page_obj()
            self.add_cards()
    def set_url(self, new_url:str) -> None:
        """
        Args:
            new_url (str): the new url to search
        """
        self.set_uri = new_url

    def set_next_page_obj(self) -> None:
        """
        moves to the next page
        """
        self.r_2 = requests.get(self.set_uri, headers=self.headers)
        self.search_obj = self.r_2.json()

    def get_json_data(self) -> dict:
        """

        Returns:
            dict: the content in the 'data' key of the searched object
        """
        return self.search_obj["data"]

    def calc_desired_qty(self, card_rarity: str) -> int:
        """
        determines desired quantity based on card rarity
        
        Args:
            card_rarity (str): < "common" | "uncommon" | "rare" | "mythic" >

        Returns:
            int: < 4 | 3 | 1 | 0 >
        """
        if card_rarity == 'common':
            return 4
        if card_rarity == 'uncommon':
            return 3
        if card_rarity == 'rare':
            return 1
        if card_rarity == 'mythic':
            return 1
        return 0

    def write_csv(self)-> None:
        """
        builds and outputs a .csv file
        """
        with open(f'./out/{self.set_code.lower()}_cards.csv', 'w', newline='') as csvfile:
            fieldnames = [
                'card_name', 
                'collector_num', 
                'colors', 'rarity', 
                'desired_qty', 
                'owned', 
                'qty_owned']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for card in self.cards:
                writer.writerow({
                    'card_name': card["card_name"],
                    'collector_num': card["collector_num"],
                    'colors' : card["colors"],
                    'rarity': card["rarity"],
                    'desired_qty' : self.calc_desired_qty(card["rarity"]),
                    'owned': 'N', #defaults to no
                    'qty_owned': 0,
                })
