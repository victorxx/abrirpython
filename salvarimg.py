import requests
import os
salvar= os.path.join(os.path.expanduser('~'), 'Desktop')
nome_arquivo="arquivo.png"
caminho_completo=os.path.join(salvar,nome_arquivo)

img='suaimg'

resposta=requests.get(img)
if resposta.status_code==200:
    with open(caminho_completo,"wb") as file:
        file.write(resposta.content)
        print('salva com sucesso')
else:
    print('Falha ao baixar')
