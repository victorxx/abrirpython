from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    page.get_by_label('Nome:').fill('escrevendo')
    page.get_by_label('Mensagem:').fill('escrito')
    page.locator('input[type="checkbox"]').nth(1).click()
    print('finalizado...')
    page.locator('select').select_option(label='Suporte')
    page.locator('text="Enviar"').click()
    time.sleep(33)
    browser.close()


<h1>Formulário de Contato</h1>
<form id="contatoForm">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome"><br><br>

    <label for="mensagem">Mensagem:</label>
    <textarea id="mensagem" name="mensagem"></textarea><br><br>

    <label for="urgente">
        <input type="checkbox" id="urgente" name="urgente"> Mensagem urgente
    </label><br><br>

    <label for="urgente2">
        <input type="checkbox" id="urgente2" name="urgente2"> Mensagem urgente2
    </label><br><br>
    <label for="assunto">Assunto:</label>
    <select id="assunto" name="assunto">
        <option value="">--Selecione--</option>
        <option value="suporte">Suporte</option>
        <option value="vendas">Vendas</option>
        <option value="outros">Outros</option>
    </select><br><br>

    <button type="submit">Enviar</button>
</form>

<p id="resultadoContato"></p>

<script>
const formContato = document.getElementById('contatoForm');
formContato.addEventListener('submit', function(e){
    e.preventDefault();
    const nome = formContato.nome.value;
    const mensagem = formContato.mensagem.value;
    const urgente = formContato.urgente.checked ? "Sim" : "Não";
    const assunto = formContato.assunto.value;
    document.getElementById('resultadoContato').innerText =
        `Nome: ${nome}, Mensagem: ${mensagem}, Urgente: ${urgente}, Assunto: ${assunto}`;
});
</script>
