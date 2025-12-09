from bs4 import BeautifulSoup
import os
desktop=os.path.join(os.path.expanduser('~'),'Desktop')
arquivo='pagina.html'
juntar=os.path.join(desktop,arquivo)

with open(juntar,'r') as file:
    html=file.read()
soup=BeautifulSoup(html,'html.parser')

img=soup.find_all('img')
quantidade=len(img)
print(quantidade)
