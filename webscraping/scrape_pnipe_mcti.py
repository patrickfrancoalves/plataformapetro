from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import numpy as np 

mainlist = []
infile = open('listalab.txt','r')
for line in infile:
    mainlist.append(line.strip().split(','))

infile.close()


lista = []
for item  in mainlist:
    lista.append(item[0][12:])




webdriver = webdriver.Chrome()
webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

for item in lista:
    #url = 'https://pnipe.mcti.gov.br/laboratory/' + item
    url = 'https://pnipe.mcti.gov.br/laboratory/' + str(item)
    
    print(url)
    webdriver.get(url)
    time.sleep(3)    

    
    soup = BeautifulSoup(webdriver.page_source,'html.parser')
    time.sleep(2)
    contacts = soup.find_all('div', attrs={'class':'sc-pYBma ewstdt'})

    dados = []
    for contact in contacts:
        dados.append(contact.text)
    time.sleep(2)
    try:
        data = {'num_mcti': [item],
                'sobre'   : [dados[0]], 
                'endereco': [dados[1]], 
                'cidade'  : [dados[2]],
                'cep'     : [dados[4]],
                'nome'    : [dados[5]],
                'tel'     : [dados[6]],
                'email'   : [dados[7]],
                'site'    : [dados[8]]
                }
        df = pd.DataFrame(data)
        print(df)
        df.to_csv('df{0}.csv'.format(item), encoding="utf-8-sig")
    except:
        pass