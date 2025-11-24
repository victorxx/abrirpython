from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')
    primeiro=page.get_by_role('textbox').nth(0).fill('escrevendo...')
    segundo=page.get_by_role('textbox').nth(1).fill('escrevendo2...')
    page.locator('label:text("Masculino ")').click()
    page.locator('label:text("Cidade:")').select_option(label="Rio de Janeiro")
    page.locator('label:text("Quero receber newsletter")').click()
    time.sleep(10)
    browser.close()


<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Formulário de Treino</title>
</head>
<body>
    <h1>Formulário de Treino</h1>

    <form id="formTreino">
        <!-- Campos de texto -->
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome"><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>

        <!-- Radio buttons -->
        <label>Gênero:</label>
        <input type="radio" id="masc" name="genero" value="masculino">
        <label for="masc">Masculino</label>
        <input type="radio" id="fem" name="genero" value="feminino">
        <label for="fem">Feminino</label><br><br>

        <!-- Select -->
        <label for="cidade">Cidade:</label>
        <select id="cidade" name="cidade">
            <option value="">Selecione</option>
            <option value="sp">São Paulo</option>
            <option value="rj">Rio de Janeiro</option>
            <option value="bh">Belo Horizonte</option>
        </select><br><br>

        <!-- Checkbox -->
        <label>
            <input type="checkbox" id="newsletter" name="newsletter">
            Quero receber newsletter
        </label><br><br>

        <!-- Botão enviar -->
        <button type="submit">Enviar</button>
    </form>

    <!-- Mensagem de confirmação -->
    <div id="mensagem"></div>

    <script>
        const form = document.getElementById('formTreino');
        const mensagem = document.getElementById('mensagem');

        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Evita recarregar a página
            mensagem.textContent = "Formulário enviado com sucesso!";
        });
    </script>
</body>
</html>
