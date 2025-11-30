from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')

    # Preencher os campos usando os labels
    page.get_by_label("INICIO:").fill("primeiro")
    page.get_by_label("SEGUNDO:").fill("segundo")
    page.get_by_label("TERCEIRO:").fill("terceiro")

    time.sleep(3)  # só para visualizar o preenchimento
    browser.close()
    print('Finalizando...')


<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <style>
            /* Seu CSS permanece exatamente como estava */
        </style>
    </head>
    <body>
        <div id="inicio">
            <div>
                <label for="inicio1">INICIO:</label>
                <input id="inicio1" type="text">
            </div>
            <div>
                <label for="segundo2">SEGUNDO:</label>
                <input id="segundo2" type="text">
            </div>
            <div>
                <label for="terceiro3">TERCEIRO:</label>
                <input id="terceiro3" type="text">
            </div>
        </div>
    </body>
</html>
