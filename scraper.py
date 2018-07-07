import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# create the progress bar function for use later during scraping
def progbar(curr, total, full_progbar):
    frac = curr/total
    filled_progbar = round(frac*full_progbar)
    print('\r', '#'*filled_progbar + '-'*(full_progbar-filled_progbar), '[{:>7.2%}]'.format(frac), end='')

# checks to see if we can even access the page
page = ''
while page == '':
    try:
        page = requests.get("http://services.runescape.com/m=itemdb_oldschool/viewitem?obj=13190")
        break
    except:
        print("Connection refused by server..")
        print("Retrying in 5 seconds..")
        time.sleep(5)
        continue

# creates blank list for use later when creating the data frame
records = []

# sets an item finds its value, recurses for every item
item = 0
while item <= 21853:
    item = str(item)

    # finds price by entering the ID into the URL and scraping from the corresponding page
    r_price = requests.get("http://services.runescape.com/m=itemdb_oldschool/viewitem?obj="+item)
    priceSoup = BeautifulSoup(r_price.text, 'html.parser')

    # checks for a specific statement to see if an item can even have a price value
    checkForItem = priceSoup.find_all('h3')
    if checkForItem[0].text != "Sorry, there was a problem with your request.":

        # this url will be used to find the item name by using its ID
        r_name = requests.get("https://www.runelocus.com/item-details/?item_id="+item)
        nameSoup = BeautifulSoup(r_name.text, 'html.parser')
        nameResults = nameSoup.find_all('h2')
        # modifies nameList results to only show the name
        nameList = nameResults[0].text
        name = nameList[19:(len(nameList)-1)]

        # locates the span title containing the price and strips the span + assigns to variable
        priceResults = priceSoup.find_all('span')
        price = priceResults[4].text

    else:
        price = "NULL"

    if price != "NULL":
        # limits to 10k http requests before sleeping for 1 hour (sleep time may need to be altered depending on Jagex max request permissions
        if int(item)/10000 != 1 or int(item)/10000 != 2 or int(item)/10000 != 3:
            date = pd.datetime.now().date()
            date = str(date) # conversion to string needed to avoid list containing 'datetime.date(xxxx, x, x)' for date value
            records.append((date, name, price.strip())) # appends to record for use in creating pd data frame
            #converts item to an int for progress bar then back into a str
            item = int(item)
            progbar(item, 21853, 20)
            item = str(item)

        else:
            sleep(3600)

    item = int(item)
    item += 1

# create data frame with all items from records list
df = pd.DataFrame(records, columns=['date', 'item', 'price'])
# since price data is formatted as xxxK or xxxM when over 99,999 or 99,999,999 excel replace formatting should be utilized
df.to_csv('GEData.csv', index=False, encoding='utf-8')
print('CSV Updated')
