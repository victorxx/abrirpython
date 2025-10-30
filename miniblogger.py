from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def inicio():
    conexao = mysql.connector.connect(
        host='localhost',
        user='vitor',
        password='12345',
        database='novo'
    )

    if conexao.is_connected():
        cursor = conexao.cursor()
        cursor.execute('SELECT titulo FROM post LIMIT 1;')
        resultado = cursor.fetchone()  # pega só um registro

        cursor.close()
        conexao.close()

        if resultado:
            return f'<a href="/pagina/{resultado[0]}">acessar</a>'
        else:
            return 'Nenhum post encontrado.'

    return 'Erro ao conectar ao banco de dados.'


@app.route('/pagina/<ok>')
def rota(ok):
    conexao = mysql.connector.connect(
        host='localhost',
        database='novo',
        user='vitor',
        password='12345'
    )

    if conexao.is_connected():
        cursor = conexao.cursor()

        # >>> Aqui mantemos o estilo original com f-string, mas corrigido:
        cursor.execute(f"SELECT texto FROM post WHERE titulo = '{ok}' LIMIT 1;")

        unico = cursor.fetchone()
        cursor.close()
        conexao.close()

        if unico:
            return f'<br> {unico[0]}'
        else:
            return f'Página {ok} não encontrada.'

    return 'Erro ao conectar ao banco de dados.'


if __name__ == '__main__':
    app.run(debug=True)
