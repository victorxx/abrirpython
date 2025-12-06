from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Abrir o arquivo HTML local
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html', wait_until='load')
    
    # Selecionar o país
    page.select_option('#pais', 'brasil')
    print('Brasil selecionado')
    
    # Marcar o checkbox/radio
    page.check('text=quero')
    print('Input selecionado')

    
    # Esperar um pouco para ver o resultado
    time.sleep(3)
    
    browser.close()
<!DOCTYPE html>
<html lang="pt-br">
    <head>

    </head>
    <body>
        <form id="meu">
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome">

            <label for="pais">Pais:</label>
            <select id="pais" name="pais">
                <option value="">selecione</option>
                <option value="brasil">brasil</option>
                <option value="portugal">portugal</option>
            </select>
            <label>
                <input type="checkbox" name="new">quero
            </label>
        </form>
    </body>
</html>
