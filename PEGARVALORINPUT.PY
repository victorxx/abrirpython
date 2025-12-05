from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    valor=page.locator('input').input_value()
    print('valor do input'+valor)
    browser.close()
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <style>
            input{
                width:100%;

                border-radius: 12px;
                height: 250px;
            }
            body{
                background-color: black;
            }
        </style>
    </head>
    <body>
        <input placeholder="VALOR" value="victor saib">
    </body>
</html>
