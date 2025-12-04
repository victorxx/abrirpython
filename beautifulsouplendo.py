from bs4 import BeautifulSoup
import time
import os



desktop=os.path.join(os.path.expanduser('~'),'Desktop')
nome='pagina.html'
juntar=os.path.join(desktop,nome)

with open(juntar,'r') as file:
    lendo=file.read()
soup=BeautifulSoup(lendo,'html.parser')
quantidade=soup.find_all('a')
for x in quantidade:
    print(x.text)

