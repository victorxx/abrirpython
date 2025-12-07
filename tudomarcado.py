from playwright.sync_api import sync_playwright 
import time

with sync_playwright () as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    time.sleep(2)
    page.get_by_label('Premium').check()
    page.get_by_label('Noite').check()
    page.get_by_label('Nao').check()
    print('ok tudo marcado...')
    time.sleep(2)

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Exemplo Radio Avançado</title>
</head>
<body>
    <h1>Formulário Radio Avançado</h1>
    <form id="formRadioAvancado">
        <!-- Grupo 1: Plano -->
        <fieldset>
            <legend>Escolha seu plano:</legend>
            <label><input type="radio" name="plano" value="basico"> Basico</label>
            <label><input type="radio" name="plano" value="intermediario"> Intermediario</label>
            <label><input type="radio" name="plano" value="premium"> Premium</label>
        </fieldset>
        <br>

        <!-- Grupo 2: Horário -->
        <fieldset>
            <legend>Escolha seu horario de atendimento:</legend>
            <label><input type="radio" name="horario" value="manha"> Manha</label>
            <label><input type="radio" name="horario" value="tarde"> Tarde</label>
            <label><input type="radio" name="horario" value="noite"> Noite</label>
        </fieldset>
        <br>

        <!-- Grupo 3: Notificações -->
        <fieldset>
            <legend>Deseja receber notificações?</legend>
            <label><input type="radio" name="notificacao" value="sim"> Sim</label>
            <label><input type="radio" name="notificacao" value="nao"> Nao</label>
        </fieldset>
        <br>

        <button type="submit">Enviar</button>
    </form>

    <p id="resultado"></p>

    <script>
        const form = document.getElementById('formRadioAvancado');
        form.addEventListener('submit', function(e){
            e.preventDefault();
            const plano = form.plano.value;
            const horario = form.horario.value;
            const notificacao = form.notificacao.value;
            document.getElementById('resultado').innerText =
                `Plano: ${plano}, Horario: ${horario}, Notificacao: ${notificacao}`;
        });
    </script>
</body>
</html>
