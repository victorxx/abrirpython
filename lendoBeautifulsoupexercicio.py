import os
from bs4 import BeautifulSoup


desktop=os.path.join(os.path.expanduser('~'),'Desktop')
arquivo='pagina.html'
caminho=os.path.join(desktop,arquivo)


with open(caminho,'r',encoding='utf-8') as file:
    html=file.read()

soup=BeautifulSoup(html,'html.parser')

todos=soup.find_all('td')

conteudo=''

quantidade=0

for td in todos:
    conteudo+=td.get_text(strip=True)+' '
    quantidade+=1
    if quantidade==2:
        conteudo+='\n'
        quantidade=0
arquivo='ok.txt'
juntei=os.path.join(desktop,arquivo)
with open(juntei,'a+') as file:
    file.write(conteudo)
print('ok está tudo ok')
