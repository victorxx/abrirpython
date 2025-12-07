
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selecionar Checkboxes</title>
</head>
<body>
    <h2>Escolha suas cidades</h2>

    <label><input type="checkbox" class="cidade" value="Sao Paulo"> Sao Paulo</label><br>
    <label><input type="checkbox" class="cidade" value="Rio de Janeiro"> Rio de Janeiro</label><br>
    <label><input type="checkbox" class="cidade" value="Belo Horizonte"> Belo Horizonte</label><br>
    <label><input type="checkbox" class="cidade" value="Curitiba"> Curitiba</label><br>

    <br>
    <button onclick="selecionarTodos()">Selecionar Todos</button>
    <button onclick="desmarcarTodos()">Desmarcar Todos</button>

    <script>
        function selecionarTodos() {
            const checkboxes = document.querySelectorAll('.cidade');
            checkboxes.forEach(cb => cb.checked = true);
        }

        function desmarcarTodos() {
            const checkboxes = document.querySelectorAll('.cidade');
            checkboxes.forEach(cb => cb.checked = false);
        }
    </script>
</body>
</html>

from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')

    page.wait_for_load_state('load')

    page.check('input[type="checkbox"][value="rio"]')
    time.sleep(30)
    print('escolhido')
    browser.close()
