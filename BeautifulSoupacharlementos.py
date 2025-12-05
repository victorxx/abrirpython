from bs4 import BeautifulSoup
import os

# Caminho para a área de trabalho
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
nome_arquivo = 'pagina.html'
caminho = os.path.join(desktop, nome_arquivo)

# Abrindo o arquivo HTML
with open(caminho, 'r', encoding='utf-8') as file:
    conteudo = file.read()

# Criando o objeto BeautifulSoup
soup = BeautifulSoup(conteudo, 'html.parser')

# Encontrando todos os botões
botoes = soup.find_all('button')

# Contando os botões
quantidade = len(botoes)

print(f"Quantidade de botões encontrados: {quantidade}")
print('Finalizando...')
