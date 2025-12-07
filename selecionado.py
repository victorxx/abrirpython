from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    time.sleep(1)
    page.locator('select').select_option(label='brasil')
    print('escolhido o texto visivel...') 
    time.sleep(20)
    browser.close()
<!DOCTYPE html>
<html lang="pt-br">
    <head>
    </head>
    <body>
    <select id="pais" name="pais">
    <option value="">selecione</option>
    <option value="brasil">brasil</option>
    <option value="rio">rio</option>
    </select>
    </body>
</html>
