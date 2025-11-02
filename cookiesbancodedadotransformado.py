from playwright.sync_api import sync_playwright
import time
import json
import mysql.connector

with sync_playwright() as p:
    # Abre o navegador
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.youtube.com/')
    page.wait_for_load_state('load')

    # Pega os cookies
    cookies = page.context.cookies()
    cookies_json = json.dumps(cookies)  # Converte para JSON

    # Conexão com o banco
    conexao = mysql.connector.connect(
        host='localhost',
        user='vitor',
        password='12345',
        database='novo'
    )

    if conexao.is_connected():
        cursor = conexao.cursor()
        
        # Chama a procedure passando os cookies em JSON
        cursor.callproc('co', (cookies_json,))
        
        conexao.commit()
        cursor.close()
        conexao.close()
        print('Cookies salvos com sucesso!')

    # Fecha o navegador
    browser.close()
