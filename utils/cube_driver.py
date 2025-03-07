class CubeDriver:
    def __init__(self, set_code):
        self.set_code = set_code
        self.url = f'https://api.scryfall.com/cards/search?q={set_code}'
        self.headers = {'user-agent': 'bg-dev-cube-gen-app'}

    