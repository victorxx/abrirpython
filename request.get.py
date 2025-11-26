from flask import Flask,redirect,render_template,request
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
    
@app.route('/post/<ok>')
def pagina(ok):
    conexao=mysql.connector.connect(
        host='localhost',
        user='vitor',
        password='12345',
        database='novo'
    )
    if conexao.is_connected():
        cursor=conexao.cursor()
        retorno=''
        cursor.execute("select texto from dado where titulo=%s",(ok,))
        resultado=cursor.fetchone()
        if resultado:
            retorno+=resultado[0]
        cursor.close()
        conexao.close()
        return retorno
            
        
    
app.run(debug=True)
