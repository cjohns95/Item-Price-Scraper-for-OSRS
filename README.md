# Item Price Data scraper for Old School Runescape

This script scrapes the official OSRS GE data and organizes it by date, item name, and price. It inserts all of this data into a CSV file of your choice. I created it so that you can collect useful data enabling you to analyse the market or specific items and make profit investing in them.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3 (pandas, requests, BeautifulSoup)
  
CSV Editor (I used excel)

### Installing

Just place the python script and the CSV file in the same folder and you're good to go.

### Deployment

This script will run through all of the items currently in the game (as of 07/07/2018 that is 21853) and will theoretically take about  21.21 hours give or take a few conseridering server connection speed, etc. If you want it to take less time you can alter the script to only run through a certain range of item ids by changing the 0 on line 9 and the 21853 on line 10 to whichever range you would prefer. The data is output with the current day so that you may run it every day and have the opportunity to then perform analysis on the data by date.

## Authors

* **Clifton Johnson** - [cjohns95](https://github.com/cjohns95)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* I did not create the progress bar function, I found it on [StackOverflow](https://stackoverflow.com/questions).
