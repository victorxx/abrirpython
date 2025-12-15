from playwright.sync_api import sync_playwright
import os

# Função para pegar título do Wikipedia
def pegar_titulo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        url = 'https://pt.wikipedia.org/wiki/Mochi'
        page.goto(url)
        page.wait_for_load_state('load')
        titulo = page.locator('h1').inner_text()
        print('Conteúdo capturado com sucesso!')
        browser.close()
        return titulo

# Função para criar a página HTML
def criar_pagina_html():
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    arquivo = 'pagina.html'
    caminho = os.path.join(desktop, arquivo)

    titulo = pegar_titulo()

    # Cada palavra em um parágrafo
    paragrafo = ''
    for palavra in titulo.split():
        paragrafo += f'<p>{palavra}</p>\n'

    html = f'''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{titulo}</title>
        <style>
            body {{
                background-color: black;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                background-color: white;
                color: black;
                border-radius: 12px;
                padding: 20px;
                text-align: center;
                max-width: 600px;
                width: 80%;
                font-size: 50px;
            }}
            p {{
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {paragrafo}
        </div>
    </body>
    </html>
    '''

    with open(caminho, 'w', encoding='utf-8') as file:
        file.write(html)

    print(f'Página HTML criada: {caminho}')
    return caminho

# Função para gerar screenshot da página
def criar_screenshot():
    desktop=os.path.join(os.path.expanduser('~'),'Desktop')
    arquivo='ok.png'
    juntar=os.path.join(desktop,arquivo)
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
        page.wait_for_load_state('load')
        imagem=page.screenshot(path=juntar)
        print('ok já foi')
        browser.close()
   

# Executa
criar_screenshot()
