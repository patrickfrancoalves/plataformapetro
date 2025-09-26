#https://stackoverflow.com/questions/66515012/beautifulsoup-doesnt-take-the-full-html-code
#https://stackoverflow.com/questions/52687372/beautifulsoup-not-returning-complete-html-of-the-page

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import numpy as np 

#url = 'https://pokedex.org/'
url = 'https://pnipe.mcti.gov.br/laboratory/31198'

webdriver = webdriver.Chrome()
webdriver.get(url)
time.sleep(2)

webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
soup = BeautifulSoup(webdriver.page_source,'html.parser')


contacts = soup.find_all('ul', attrs={'class':'sc-pDbHj iBtvlG'})


dados = []

for contact in contacts:
    print('\n',contact)
    dados.append(contact)


#data = { 'sobre'   : [dados[0]], 
#         'endereco': [dados[1]], 
#         'cidade'  : [dados[2]],
#         'cep'     : [dados[4]],
#         'nome'    : [dados[5]],
#         'tel'     : [dados[6]],
#         'email'   : [dados[7]],
#         'site'    : [dados[8]]}
#df = pd.DataFrame(data)
#print(df)

#df.to_csv('df.csv', encoding="utf-8-sig")



 