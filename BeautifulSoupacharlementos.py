import os
from bs4 import BeautifulSoup
import time

desktop=os.path.join(os.path.expanduser('~'),'Desktop')
nome='pagina.html'
juntar=os.path.join(desktop,nome)
with open(juntar,'r') as file:
    lendo=file.read()

soup=BeautifulSoup(lendo,'html.parser')
soup.find_all('a')
quantidade=len(soup)
print(quantidade)
