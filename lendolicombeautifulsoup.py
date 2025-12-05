import os
from bs4 import BeautifulSoup



desktop=os.path.join(os.path.expanduser('~'),'Desktop')
arquivo='pagina.html'
juntar=os.path.join(desktop,arquivo)
if os.path.exists(juntar):
    print('ok podemos continuar')
    with open(juntar,'r') as file:
        lendo=file.read()
    soup=BeautifulSoup(lendo,'html.parser')
    frutas=soup.find_all('li')
    for x in frutas:
        print(x.text)
    print('finalizado...')
else:

    print('ok deu algo errado...')
