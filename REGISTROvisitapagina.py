create table if not exists visitado(
id int auto_increment primary key,
visitado date,
url text
);
ALTER TABLE VISITADO modify VISITADO DATETIME;
SELECT * FROM VISITADO;
SELECT HOUR(VISITADO),MINUTE(VISITADO)FROM VISITADO;

import mysql.connector
from playwright.sync_api import sync_playwright
import time
from flask import Flask
app=Flask(__name__)
@app.route('/')
def inicio():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://www.youtube.com/')
        page.wait_for_load_state('load')
        titulo=page.url
        print('pegamos o dado')
        browser.close()
        print('finalizado com sucesso....')
        conexao=mysql.connector.connect(
            host='localhost',
            user='vitor',
            password='12345',
            database='novo'
        )
        if conexao.is_connected():
            cursor=conexao.cursor()
            cursor.execute(
                "INSERT INTO VISITADO (visitado, URL) VALUES (NOW(), %s)",
                (titulo,)
            )
            conexao.commit()
            cursor.close()
            conexao.close()
            print('finalizado com sucesso....')
            return 'ok dado gravado com sucessoo......'
        
app.run(debug=True)
