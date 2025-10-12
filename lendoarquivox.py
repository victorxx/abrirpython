from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def listar():
    # Caminho da área de trabalho do usuário
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')

    # Lista os arquivos .txt na área de trabalho
    arquivos = [f for f in os.listdir(desktop) if f.endswith('.txt')]

    if not arquivos:
        return 'Não temos arquivo .txt'

    # Pega o caminho completo do primeiro arquivo encontrado
    caminho_arquivo = os.path.join(desktop, arquivos[0])

    # Abre e lê o conteúdo do arquivo
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        lendo = file.read()
        return lendo[:300]  # Retorna os primeiros 300 caracteres

if __name__ == '__main__':
    app.run(debug=True)
