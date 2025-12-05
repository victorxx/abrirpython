from bs4 import BeautifulSoup
import os


desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
arquivo = 'pagina.html'
caminho = os.path.join(desktop, arquivo)

with open(caminho, 'r', encoding='utf-8') as file:
    conteudo = file.read()

soup=BeautifulSoup(conteudo,'html.parser')


links=soup.find_all('a')
links[0].string='Google.com'
links[0]['href']='https://www.google.com'
links[1].string='youtube.com'

links[1]['href']='https:www.youtube.com'

with open(caminho,'w') as file:
    file.write(str(soup))
print('finalizado com sucesso...')


<!DOCTYPE html>

<html lang="pt-br">
<head>
<style>
body{
    background-color: black;
}
    li{
        background-color: red;
        width: 100px;
        border-radius: 12px;
        height: 250px;
        display: grid;
        grid-template-columns: auto auto;
    }
     </style>
</head>
<body>
<li>
<a href="https://www.google.com">Google.com</a>
</li>
<li>
<a href="https:www.youtube.com">youtube.com</a>
</li>
</body>
</html>
