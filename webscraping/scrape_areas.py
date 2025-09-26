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
    areas = soup.find_all('ul', attrs={'class':'sc-pDbHj iBtvlG'})
    codigos = soup.find_all('td', attrs={'class':'MuiTableCell-root MuiTableCell-body sc-fzoxnE GqMIW'})


    lista_area = []
    
    for area in areas:
        for area2 in area.find_all('li'):
            print("\n ",area2.get_text())
            lista_area.append(area2.get_text())

    
    
    try:
        data = {'areas': lista_area}
        df = pd.DataFrame(data)
        df['lab'] = item
        df.to_csv('area{0}.csv'.format(item), encoding="utf-8-sig")
    except:
        pass

    
    
    lista_codigo = []

    for codigo in codigos:
        print(codigo.get_text())
        lista_codigo.append(codigo.get_text())


    try:
        data = {'codigos': lista_codigo}
        df2 = pd.DataFrame(data)
        df2['lab'] = item
        df2.to_csv('cods{0}.csv'.format(item), encoding="utf-8-sig")
    except:
        pass


