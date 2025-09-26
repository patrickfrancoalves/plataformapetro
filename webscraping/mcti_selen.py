from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import pandas as pd
import numpy as np 


url = 'https://pnipe.mcti.gov.br/search?term=&type=LAB'

webdriver = webdriver.Chrome()
webdriver.get(url)
webdriver.forward()


time.sleep(31)

webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
soup = BeautifulSoup(webdriver.page_source,'html.parser')

contacts = soup.find_all('a', attrs={'class':'MuiButtonBase-root MuiButton-root MuiButton-text jss40'})

for contact in contacts:
    print(contact['href'])

    # - Href Link -
#href = soup.get('href')
#print(href) 

#7009-7020