from flask import Flask,redirect,render_template,render_template_string,request
import time
import os
import mysql.connector
app=Flask(__name__)
@app.route('/')
def inicio():
    conexao=mysql.connector.connect(
       host='localhost',
       user='vitor',
       database='novo',
       password='12345'
    )
    if conexao.is_connected():
        cursor=conexao.cursor()
        cursor.execute("select titulo from dado")
        resultado=''
        for x in cursor.fetchall():
            resultado+=f'<a href="post/{x[0]}">{x[0]}</a>'
        conexao.close()
        cursor.close()
        return resultado
    
@app.route('/post/')
def nao_passado_nada():
    return 'não foi passado nenhum valor'

@app.route('/post/<ok>',methods=['GET'])
def postagem(ok):

    
    conexao=mysql.connector.connect(
        host='localhost',
        user='vitor',
        password='12345',
        database='novo'
    )
    if conexao.is_connected():
       cursor=conexao.cursor()
       cursor.execute("select texto from dado where titulo=%s",(ok,))
       completo=''
       unico=cursor.fetchone()
       if unico:
           completo=unico[0]
           return completo
       else:
        return 'não temos nada aqui'
           
        

       
    
app.run(debug=True)
