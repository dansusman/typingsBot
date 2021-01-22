# typingsBot

This project is a one-day build exploring web scraping in Python's BeautifulSoup and Selenium libraries.

The aim of the bot is not to disturb the credibility of typings.gg's typing test, but instead to 
learn common web scraping tools, which I can later use for more interesting projects. 

To use, simply run python3 typingsBot.py and enter your desired Delay. This will launch a ChromeDriver 
instance (Chrome browser, controlled by an automated test tool). Return to your terminal window 
and hit Enter when prompted. The program will begin spamming the correct words it has scraped from
the website, completing the typing test with perfect accuracy and superhuman speed. A delay of 0.1
is my recommendation, as it isn't overly fast nor overly slow. After displaying the final information
for five seconds, the driver instance will quit, closing the Chrome window and ending the script.

The purpose of this project is SOLELY for fun, so have fun!
