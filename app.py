import requests
import json

url = 'https://api.scryfall.com/cards/search?q=ons'
headers = {'user-agent': 'bg-dev-cube-gen-app'}

r = requests.get(url, headers=headers)
obj = r.json()

print(obj["total_cards"])
has_more = obj["has_more"]
print(obj["next_page"])

total_cards = obj["total_cards"]
cards_printed = 0


for o in obj["data"]:
    cards_printed += 1
    print(o['name'])
    
if has_more == True:
    # repeat
    
    print("we'll repeat")
    print(f'we still have {total_cards - cards_printed}  cards to go')

