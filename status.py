from flask import Flask ,render_template,render_template_string, request,redirect
import time 
import mysql.connector

app=Flask(__name__)
@app.route('/')
def inicio():
    return """
    
    <!DOCTYPE html>
<html lang="pt-br">
    <head>
        <style>
            body{
                background-color: black;
                color:white;
                display: flex;
                height: 100vh;
                align-items: center;
            }
            form{
                text-align: center;
                width:90%;
                max-width: 600px;
            }
            select{
                width:100%;
                margin-top:20px;
                height:300px;
                text-align:center;
                font-size:50px;
            }
            button{
                border-radius: 12px;
                padding:10px;
                width:100%;
                max-width: 200px;
                font-size: 20px;
            }
        @media(max-width:550px){
            select{
                font-size: 20px;
            }
        }
        button{
            font-size: 20px;
        }
        </style>
    </head>
    <body>
            <form method="POST" action="/pagina">
            <select name="estado">
                <option value="ativado">ativar</option>
                <option value="desativado">desativado</option>
            </select>
            <button type="submit">enviar</button>
        </form>
    </body>
</html>


    """
@app.route('/pagina',methods=['POST'])
def paginas():
    puxar=request.form['estado']
    conexao=mysql.connector.connect(
        host='localhost',
        user='vitor',
        password='12345',
        database='novo'
    )
    if conexao.is_connected():
        cursor=conexao.cursor()
        cursor.execute("INSERT INTO SERVICO(servico_status)VALUES(%s)",(puxar,))
        return """""
        <script>
         window.location.href = "/";
        </script>
        """


create table if not exists servico(
id int primary key auto_increment,
servico_status varchar(300)
);

set sql_safe_updates=0;

select * from servico;
       
app.run(debug=True)

