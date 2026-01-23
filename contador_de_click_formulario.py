<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <head>
            <style>
                  body{
                    height: 100vh;
                    background-color: black;
                  }
                .card{
                    width:90%;
                    height: auto;
                    display: grid;
                    transform: translate(10%,50%);
                    gap:20px;
                    grid-template-columns: repeat(3,1fr);
                }
                .card div{
                    width:250px;
                    height: 120px;
                    font-size: 33px;
                    background-color: orangered;
                    border-radius: 12px;
                    cursor:pointer;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <div>1</div>
                <div>2</div>
                <div>3</div>
            </div>
        </body>
</html>
from playwright.sync_api import sync_playwright
import os

# Caminho do arquivo no desktop
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
arquivo = "contadorclick.txt"
juntar = os.path.join(desktop, arquivo)

# Verifica se já existe "clicado 1"
termo = False
if os.path.exists(juntar):
    with open(juntar, 'r') as file:
        if 'clicado 1' in file.read():
            termo = True
            print('existe sim')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')

    click = page.locator('.card div')

    for x in range(click.count()):
        texto = click.nth(x).text_content()

        if (termo and texto != "1") or (not termo and texto == "1"):
            click.nth(x).click()
            with open(juntar, 'a') as file:
                file.write(f'clicado{texto}\n')
            break  # clica apenas uma vez

    browser.close()
    print('finalizado')
