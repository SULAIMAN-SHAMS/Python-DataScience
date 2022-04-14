# by SULAIMAN SHAMS

import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen



html=urlopen('https://en.wikipedia.org/wiki/Computer')



bs=BeautifulSoup(html.read(),'html.parser')


print(bs)



paragraphs=bs.find_all('p')
print(paragraphs)



namelist=bs.find_all('span',{'class':'mw-indicators'})
for name in namelist:
    print(name.get_text())




len(namelist)




len(namelist)



namelist=bs.find_all('div',{'class':'mw-body'})
for name in namelist:
    print(name.get_text())




for i in bs.select('p'):
    print(i.text)




import wikipedia as w
import pandas as pd







