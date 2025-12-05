import os


from bs4 import BeautifulSoup 
desktop=os.path.join(os.path.expanduser('~'),'Desktop')
arquivo='pagina.html'
juntar=os.path.join(desktop,arquivo)

if os.path.exists(juntar):
    print('finalizado....')
    with open(juntar,'r') as file:
        lendo=file.read()
    soup=BeautifulSoup(lendo,'html.parser')
    links=soup.find_all('a')
    primeiro=links[0]['href']='https://www.youtube.com/watch?v=2uBrqwj70TQ&t=28s'
    with open(juntar,'w') as file:
        file.write(str(soup))
    print('escrito...')
    print('finalizado...')
