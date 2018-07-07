import pandas as pd
import requests
from bs4 import BeautifulSoup

# creates blank list for use later when creating the data frame
records = []

# sets an item finds its value, recurses for every item
item = 0
while item <= 21853:
    item = str(item)

    # this url will be used to find the item name by using its ID
    r_name = requests.get("https://www.runelocus.com/item-details/?item_id="+item)
    nameSoup = BeautifulSoup(r_name.text, 'html.parser')
    nameResults = nameSoup.find_all('h2')
    # modifies nameList results to only show the name
    nameList = nameResults[0].text
    name = nameList[19:(len(nameList)-1)]

    # in the url below the item name doesnt matter, just the ID, this url can only provide the price
    r_price = requests.get("http://services.runescape.com/m=itemdb_oldschool/Zulrah's_scales/viewitem?obj="+item)
    priceSoup = BeautifulSoup(r_price.text, 'html.parser')

    # checks for a specific statement to see if an item can even have a price value
    checkForItem = priceSoup.find_all('h3')
    if checkForItem[0].text != "Sorry, there was a problem with your request.":

        # locates the span title containing the price and strips the span + assigns to variable
        priceResults = priceSoup.find_all('span')
        price = priceResults[4].text

    else:
        price = "NULL"

    if price != "NULL":
        date = pd.datetime.now().date()
        date = str(date) # conversion to string needed to avoid list containing 'datetime.date(xxxx, x, x)' for date value
        records.append((date, name, price.strip()))

    item = int(item)
    item += 1

# create data frame with all items from records list
df = pd.DataFrame(records, columns=['date', 'item', 'price'])
# since price data is formatted as xxxK or xxxM when over 99,999 or 99,999,999 excel replace formatting should be utilized
df.to_csv('GEData.csv', index=False, encoding='utf-8')
print('done')
