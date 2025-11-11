from flask import Flask, render_template_string, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <style>
            body {
                align-items: center;
                background-color: black;
                display: flex;
                justify-content: center;
                color: white;
                height: 100vh;
            }
            #pasta {
                display: grid;
                grid-template-columns: auto;
                gap: 20px 30px;
                align-items: center;
                text-align: center;
            }
            #pasta input[type='radio'] {
                accent-color: red;
                width: 150px;
                height: 100px;
                padding: 20px;
                cursor: pointer;
            }
            #pasta label {
                font-size: 30px;
                cursor: pointer;
            }
            #pasta button {
                width: 150px;
                height: 60px;
                border-radius: 12px;
                background-color: red;
                color: white;
                font-size: 20px;
                border: none;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div id="pasta">
            <form id="escolha" method="post" action="/enviado">
                <label for="coca">COCA COLA</label>
                <input type="radio" id="coca" name="opcao" value="coca">
                
                <label for="fanta">FANTA UVA</label>
                <input type="radio" id="fanta" name="opcao" value="fanta">

                <button id="enviar" type="submit">Enviar</button>
            </form>
        </div>
    </body>
    </html>
    ''')

@app.route('/enviado', methods=['POST'])
def enviado():
    # Captura o valor enviado pelo form
    dado = request.form.get('opcao')  # ← nome correto do input

    if not dado:
        return "Nenhuma opção foi selecionada!"
    conexao=mysql.connector.connect(
        host='localhost',
        user='vitor',
        password='12345',
        database='novo'
    )
    if conexao.is_connected():
        cursor=conexao.cursor()
        cursor.execute(f"update refrigerante set opcao='{dado}' where id=1;")
        conexao.commit()
        cursor.close()
        conexao.close()
    return '<script>window.location.href="/"</script>'


if __name__ == '__main__':
    app.run(debug=True)
