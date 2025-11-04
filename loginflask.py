import mysql.connector
from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return """
    <form method="POST" action="/pagina">
        Nome: <input type="text" name="nome"><br>
        Senha: <input type="password" name="senha"><br>
        <button type="submit">Enviar</button>
    </form>
    """

@app.route('/pagina', methods=['POST'])
def pagina():
    nome = request.form['nome']
    senha = request.form['senha']

    # Conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='localhost',
        database='novo',
        user='vitor',
        password='12345'
    )

    cursor = conexao.cursor()
    # Usando placeholders para evitar SQL Injection
    cursor.execute("SELECT NOME FROM LOGIN WHERE NOME=%s AND senha=%s", (nome, senha))
    unico = cursor.fetchone()

    cursor.close()
    conexao.close()

    if unico:
        return f"Usuário encontrado: {unico[0]}"
    else:
        return "Usuário ou senha incorretos"

app.run(debug=True)
