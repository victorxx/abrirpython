from playwright.sync_api import sync_playwright
import time
import requests
import random
import os


def inicio():
    try:
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True)
            page=browser.new_page()
            print('puxando o caminho da imagem....')
            page.goto('https://br.pinterest.com/uniter1265/garotas-japonesas/')
            escolher=page.locator('img').nth(0).get_attribute('src')
            print(escolher)
            
            browser.close()
            return escolher
    except:
        print('ok deu algo errado...')
def baixar():
    baixar=inicio()
    if baixar !=None:
        print(baixar)
        print('não esta vazio podemos continuar')
        desktop=os.path.join(os.path.expanduser('~'),'Desktop')
        nome='japa.png'
        juntar=os.path.join(desktop,nome)
        buscar=requests.get(baixar)
        if buscar.status_code==200:
            print('ok deu bom')
            with open(juntar,'wb') as file:
                file.write(buscar.content)
                print('gravado...')
        return juntar

def upload():
    verificar=baixar()
    if verificar!=None:
        print('podemos continuar')
        try:
            with sync_playwright() as p:
                browser=p.chromium.launch(headless=False)
                page=browser.new_page()
                page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
                page.wait_for_load_state('load')
                time.sleep(2)
                primeiro=page.get_by_role('textbox').nth(0).fill('ok')
                time.sleep(2)
                page.set_input_files('input[type="file"]',f"{verificar}")
                time.sleep(10)
                print('finalizando com sucesso...')
                browser.close()
        except:
            print('ok deu algo errado...')
upload()



<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <style>
        body {
            background-color: black;
            display: flex;
            justify-content: center;  /* centraliza horizontalmente */
            align-items: center;      /* centraliza verticalmente */
            height: 100vh;            /* altura total da janela */
            margin: 0;
        }

        form {
            background-color: #222;
            padding: 40px;
            border-radius: 15px;
            text-align: center;
        }

        form input {
            display: block;
            margin: 10px auto;
            padding: 10px;
            border-radius: 8px;
            border: none;
            font-size: 14px;
        }

        form button {
            border-radius: 10px;
            padding: 12px 25px;
            color: black;
            background-color: orange;
            font-size: 15px;
            border: none;
            cursor: pointer;
        }

        form button:hover {
            background-color: #ffb84d;
        }
    </style>
</head>
<body>
    <form id="form">
        <input name="vitor" type="text" placeholder="Digite algo">
        <input name="arquivo" type="file">
        <button id="entrar" type="submit">Enviar</button>
    </form>
</body>
</html>


        
