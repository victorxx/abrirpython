from bs4 import BeautifulSoup
import time
import os


desktop=os.path.join(os.path.expanduser('~'),'Desktop')
arquivo='pagina.html'
juntar=os.path.join(desktop,arquivo)

with open(juntar,'r') as file:
    conteudo=file.read()
soup=BeautifulSoup(conteudo,'html.parser')

conteudo=soup.find_all('input')
conteudo[0]['value']='mudando o valor do input'
with open(juntar,'w') as file:
    file.write(str(soup))
print('ok ta tudo ok')
