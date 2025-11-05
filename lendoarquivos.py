from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def inicio():
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    
    # Garante que a pasta existe
    if not os.path.exists(desktop):
        return 'A pasta Desktop não foi encontrada.'
    
    # Lista apenas arquivos .txt (ignora maiúsculas)
    arquivos = [f for f in os.listdir(desktop) if f.lower().endswith('.txt')]

    if not arquivos:
        return 'Não temos nada aqui.'

    # Cria links para cada arquivo
    links = ''
    for x in arquivos:
        nome = x.replace('.txt', '')
        links += f'<a href="/pagina/{nome}">{nome}</a><br><br>\n'

    return links


@app.route('/pagina/<ok>')
def pagina(ok):
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    caminho = os.path.join(desktop, f'{ok}.txt')

    if not os.path.exists(caminho):
        return 'Arquivo não encontrado.'

    with open(caminho, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    # Mostra apenas os primeiros 300 caracteres
    restringi = conteudo[:300]
    return f'<pre>{restringi}</pre>'


if __name__ == '__main__':
    app.run(debug=True)
