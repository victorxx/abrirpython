create table if not exists usuario(
id int primary key auto_increment,
nome varchar(100)
);
create table if not exists img(
id int primary key auto_increment,
caminho text,
id_img int,
foreign key(id_img) references usuario(id)
);
insert into usuario(nome)values('victor');
select * from usuario left join img on usuario.id=img.id_img;


from flask import Flask, request
import os
import mysql.connector

app = Flask(__name__)

@app.route('/')
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <body>
        <form method="post" enctype="multipart/form-data" action="/aceito">
            <input type="file" name="meu" required>
            <br><br><br>
            <button type="submit">Enviar</button>
        </form>
    </body>
    </html>
    """

@app.route('/aceito', methods=['POST'])
def pagina():
    # Caminho onde será salvo o arquivo
    caminho_pasta = os.path.join(os.path.expanduser('~'), 'Desktop', 'pasta')
    os.makedirs(caminho_pasta, exist_ok=True)

    arquivo = request.files['meu']
    if arquivo.filename == "":
        return "vazio"

    # Caminho completo
    juntar = os.path.join(caminho_pasta, arquivo.filename)
    arquivo.save(juntar)  # <-- salva o arquivo
    caminho_absoluto = os.path.abspath(juntar)

    # Conexão com o MySQL
    conexao = mysql.connector.connect(
        host='localhost',
        database='novo',
        user='vitor',
        password='12345'
    )

    if conexao.is_connected():
        cursor = conexao.cursor()
        # Exemplo: inserir novo registro
        cursor.execute("INSERT INTO  img (caminho,id_img) VALUES (%s,%s)", (caminho_absoluto,1,))
        print('ok foi')
        conexao.commit()
        cursor.close()
        conexao.close()

    return f"Arquivo salvo em: {caminho_absoluto}"

if __name__ == '__main__':
    app.run(debug=True)
