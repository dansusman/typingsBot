'''

Created by Daniel Susman (dansusman)
Date: 01/21/2021

This module contains a bot that automates the solving of a typing test on
https://www.typings.gg. It is strictly for demonstration purposes and is not to be used
for an illegal or unethical activity.

Uses the well-known BeautifulSoup and Selenium libraries to web-scrape for
the words to replicate and input into the "input bar" on the website. Program will 
ask for the user to input a desired delay between key strokes, which will directly affect the 
bot's typing speed. Delay and WPM are inversely correlated.

'''
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver

delay = float(input("Delay: "))

# Use selenium to grab information from typings.gg
os.makedirs("webdriver", exist_ok=True)

DRIVER_PATH = '/usr/local/bin/chromedriver'
URL = 'https://typings.gg/'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)

for run_count in range(2):
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    words_to_type = soup.find_all('div', {'id': 'typing-area'})

    for tag in words_to_type:
        words_to_type = tag.find_all("span")

    # find_all returns html tags, convert to just words
    for i in range(len(words_to_type)):
        words_to_type[i] = words_to_type[i].text

    # clean up words to avoid spaces, carriage returns, etc.
    text = [x for x in words_to_type if x.strip()]

    for x in text:
        if x == "undefined":
            text.remove(x)

    # make all text into a string that can be inputted
    ''.join(text)

    if run_count > 0:
        input("Press enter to start bot...")

    first_elem = driver.find_element_by_id("input-field")
    first_elem.click()

    # for i in range(len(text)):
    #     time.sleep(delay)
    if text[0] == 'undefined ':
        continue
    for i in range(len(text)):
        first_elem.send_keys(text[i])
        time.sleep(delay)

# show results for 5 seconds, then close the web driver
time.sleep(5)
driver.close()
