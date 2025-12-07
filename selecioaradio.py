from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    page.get_by_role('radio',name="Basico").check()
    page.get_by_role('radio',name='tarde').check()
    print('escolhido....')
    time.sleep(20)
    browser.close()

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Exemplo Radio Buttons</title>
</head>
<body>
    <h1>Formulário Radio Buttons Complexo</h1>
    <form id="formRadio">
        <label>Escolha seu plano:</label><br>
        <label>
            <input type="radio" name="plano" value="basico"> Basico
        </label><br>
        <label>
            <input type="radio" name="plano" value="intermediario"> Intermediario
        </label><br>
        <label>
            <input type="radio" name="plano" value="premium"> Premium
        </label><br><br>

        <label>Escolha seu horario de atendimento:</label><br>
        <label>
            <input type="radio" name="horario" value="manha"> Manha
        </label><br>
        <label>
            <input type="radio" name="horario" value="tarde"> Tarde
        </label><br>
        <label>
            <input type="radio" name="horario" value="noite"> Noite
        </label><br><br>

        <button type="submit">Enviar</button>
    </form>

    <p id="resultado"></p>

    <script>
        const form = document.getElementById('formRadio');
        form.addEventListener('submit', function(e){
            e.preventDefault();
            const plano = form.plano.value;
            const horario = form.horario.value;
            document.getElementById('resultado').innerText =
                `Plano escolhido: ${plano}, Horario escolhido: ${horario}`;
        });
    </script>
</body>
</html>
