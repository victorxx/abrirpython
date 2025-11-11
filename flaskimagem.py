from flask import Flask,redirect,render_template,request
import os
import time
import random
import mysql.connector
app=Flask(__name__)
@app.route('/')
def inicio():
    conexao=mysql.connector.connect(
        host='localhost',
        user='vitor',
        password='12345',
        database='novo'
    )
    if conexao.is_connected():
        cursor=conexao.cursor()
        cursor.execute(f"select caminho from img where id=1;")
        unico=cursor.fetchone()

    return f'''''
    
    <!DOCTYPE html>
<html lang="pt-br">
    <head>
        <style>
            body{{
                background-color: black;
            }}
            #img{{
                display: grid;
                grid-template-columns: auto;
                padding:20px;
                text-align: center;
                color:white;
            }}
            #img img{{
                position: absolute;
                left: 20%;
                bottom:20%;
            }}
        </style>
    </head>
    <body>
        <div id="img">
         <img src="{unico[0]}" >
        </div>
    </body>
</html>
    
    
    '''
app.run(debug=True)
