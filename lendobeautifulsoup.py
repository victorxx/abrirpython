<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Imoveis para Temporada</title>
</head>
<body>
    <h1>Imoveis Disponiveis</h1>
    
    <div class="imovel" id="imovel1">
        <h2>Apartamento na Praia</h2>
        <p>Local: Guarapari, ES</p>
        <p>Preco: R$ 250,00 por dia</p>
    </div>

    <div class="imovel" id="imovel2">
        <h2>Casa na Serra</h2>
        <p>Local: Domingos Martins, ES</p>
        <p>Preco: R$ 400,00 por dia</p>
    </div>

    <div class="imovel" id="imovel3">
        <h2>Flat no Centro</h2>
        <p>Local: Vitoria, ES</p>
        <p>Preco: R$ 180,00 por dia</p>
    </div>
</body>
</html>
from bs4 import BeautifulSoup
import os

desktop=os.path.join(os.path.expanduser('~'),'Desktop')
arquivo='pagina.html'
juntar=os.path.join(desktop,arquivo)
# Abre o arquivo HTML
with open(juntar, "r", encoding="utf-8") as f:
    html = f.read()

# Cria objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Pega título da página
titulo = soup.title.text
print("Titulo da página:", titulo)

# Pega todos os imóveis
imoveis = soup.find_all("div", class_="imovel")

for imovel in imoveis:
    nome = imovel.h2.text
    local = imovel.find_all("p")[0].text
    preco = imovel.find_all("p")[1].text
    print(f"{nome} | {local} | {preco}")
