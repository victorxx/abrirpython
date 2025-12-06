from playwright.sync_api import sync_playwright
import time





with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    selecionar=page.check('input[value="emprego"]')
    selecionar2=page.check('input[value="casa"]')
    print('finalizado...')
    time.sleep(50)
    browser.close()

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Teste Checkbox</title>
</head>
<body>

<h2>Selecione suas opções:</h2>

<form id="form-opcoes">

    <label>
        <input type="checkbox" id="opc1" value="carro">
        Quero receber ofertas de carro
    </label>
    <br>

    <label>
        <input type="checkbox" id="opc2" value="casa">
        Quero receber ofertas de casa
    </label>
    <br>

    <label>
        <input type="checkbox" id="opc3" value="emprego">
        Quero receber ofertas de emprego
    </label>
    <br><br>

    <button type="submit" id="enviar">Enviar</button>

</form>

</body>
</html>

