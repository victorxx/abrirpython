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

<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="widt=device-width,initial-scale=1.0">
        <style>
            table{
                width:990px;
                border-radius: 12px;
                padding:20px;
                text-align: center;
                margin:auto 50px;
                border-collapse: collapse;
                position: absolute;
                left: 10%;
                bottom:40%;
            }
            th,td{
                width:50%;
                padding:20px;
                height: 25px;
            }
            @media(max-width:550px){
                table{
                    width:90%;
                    padding:20px;
                    left: 0;
                }
            }
        </style>
    </head>
    <body>
<table border="10" id="janela">
   <thead>
    <tr>
        <th>nome</th><th>sobrenome</th>
    </tr>
   </thead>
   <tbody>
    <tr>
        <td>victor</td><td>saib</td>
    </tr>
    <tr>
        <td>victor</td><td>luis</td>
    </tr>
    <tr>
        <td>ricardo</td><td>antonio</td>
    </tr>
   </tbody>
</table>
    </body>
</html>
