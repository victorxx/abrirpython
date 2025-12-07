from playwright.sync_api import sync_playwright
import time



with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    page.locator('input[name="noticias"]').check()
    time.sleep(10)
    page.locator('input[name="noticias"]').uncheck()
    print('desativando...')
    browser.close()


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Formulário Completo de Teste</title>
</head>
<body>
    <h1>Formulário Completo de Teste</h1>
    <form id="formCompleto">
        <!-- Input de texto -->
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome"><br><br>

        <!-- Input de email -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>

        <!-- Select (Dropdown) -->
        <label for="assunto">Assunto:</label>
        <select id="assunto" name="assunto">
            <option value="">--Selecione--</option>
            <option value="suporte">Suporte</option>
            <option value="vendas">Vendas</option>
            <option value="outros">Outros</option>
        </select><br><br>

        <!-- Radio buttons -->
        <label>Genero:</label>
        <label><input type="radio" name="genero" value="Masculino"> Masculino</label>
        <label><input type="radio" name="genero" value="Feminino"> Feminino</label>
        <label><input type="radio" name="genero" value="Outro"> Outro</label><br><br>

        <!-- Checkboxes -->
        <label><input type="checkbox" name="noticias"> Receber noticias</label><br>
        <label><input type="checkbox" name="promocoes"> Receber promocoes</label><br><br>

        <!-- Textarea -->
        <label for="mensagem">Mensagem:</label><br>
        <textarea id="mensagem" name="mensagem" rows="4" cols="50"></textarea><br><br>

        <!-- Botão de envio -->
        <button type="submit">Enviar</button>
    </form>

    <h2>Resultado do Formulario:</h2>
    <p id="resultado"></p>

    <script>
        const form = document.getElementById('formCompleto');
        form.addEventListener('submit', function(e){
            e.preventDefault(); // evita reload da pagina

            // Captura dos valores
            const nome = form.nome.value;
            const email = form.email.value;
            const assunto = form.assunto.value;
            const genero = form.genero.value;
            const noticias = form.noticias.checked ? "Sim" : "Nao";
            const promocoes = form.promocoes.checked ? "Sim" : "Nao";
            const mensagem = form.mensagem.value;

            // Exibe no paragrafo resultado
            document.getElementById('resultado').innerText =
                `Nome: ${nome}, Email: ${email}, Assunto: ${assunto}, Genero: ${genero}, Noticias: ${noticias}, Promocoes: ${promocoes}, Mensagem: ${mensagem}`;
        });
    </script>
</body>
</html>
