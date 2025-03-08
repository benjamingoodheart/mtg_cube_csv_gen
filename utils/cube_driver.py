import requests


class CubeDriver:
    def __init__(self, set_code)  -> None:
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
    
    def add_cards(self) -> None:
        for o in self.search_obj["data"]:
            self.cards.append({o["name"], o["collector_number"]})
    
    def set_url(self, new_url):
        print(new_url)
        self.set_uri = new_url
    
    def set_next_page_obj(self):
        self.r_2 = requests.get(self.set_uri, headers=self.headers)
        self.search_obj = self.r_2.json()
        print(self.r_2.json())

    def get_json_data(self):
        return self.block_obj["data"]
    
    
        

    