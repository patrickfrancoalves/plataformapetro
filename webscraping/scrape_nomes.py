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
    time.sleep(2)    

    
    soup = BeautifulSoup(webdriver.page_source,'html.parser')
    time.sleep(2)
    nomes = soup.find_all('div', attrs={'class':'MuiBox-root jss58'})
    datas = soup.find_all('p', attrs={'class':'MuiTypography-root MuiTypography-body1 MuiTypography-colorTextPrimary MuiTypography-noWrap'})
    univs = soup.find_all('p', attrs={'class':'MuiTypography-root MuiTypography-body1 MuiTypography-colorTextPrimary'})

    lista_nomes = []
    
    for nome in nomes:
        lista_nomes.append(nome.get_text())


    lista_datas = []
    for data in datas:
        print(data.get_text())
        lista_datas.append(data.get_text())


    lista_univs = []
    for univ in univs:
        print(univ.get_text())
        lista_univs.append(univ.get_text())

    try:
        
        df = pd.DataFrame({'nome': lista_nomes, 'data_criacao': lista_datas, 'universidade': lista_univs})
        df['lab'] = item
        df.to_csv('nomes{0}.csv'.format(item), encoding="utf-8-sig")
    except:
        pass

    