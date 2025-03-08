from utils import cube_driver

c = cube_driver.CubeDriver('ons')
for o in c.search_obj:
    print(o)
c.set_url(c.search_obj["next_page"])
c.set_next_page_obj()


'''has_more = obj["has_more"]
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

'''