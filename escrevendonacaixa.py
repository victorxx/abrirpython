<!DOCTYPE html>
<html lang="pt-br">
    <head>

    </head>
    <body>
        <form id="meu">
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome">
            
        </form>
    </body>
</html>
from playwright.sync_api import sync_playwright
import time
import os





with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    page.fill('input[name="nome"]','victor goes duarte saib')
    time.sleep(30)
    browser.close()
