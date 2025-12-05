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
    primeiro=frutas[1].string='maca'
    
    print('finalizado...')
    with open(juntar,'w') as file:
        file.write(str(soup))
    print('atulizado o arquivo')
else:

    print('ok deu algo errado...')
