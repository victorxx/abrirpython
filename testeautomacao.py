<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Simulação Airbnb</title>
<style>
body {
    font-family: Arial, sans-serif;
    background: #f0f2f5;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.imovel {
    border: 1px solid #ccc;
    border-radius: 8px;
    background: white;
    padding: 10px 15px;
    margin-bottom: 15px;
    width: 400px;
    position: relative;
}

.imovel h3 {
    margin: 0 0 5px 0;
}

.imovel p {
    margin: 5px 0;
}

.imovel a {
    position: absolute;
    right: 15px;
    top: 15px;
    text-decoration: none;
    color: #1877f2;
    font-weight: bold;
    cursor: pointer;
}

/* Div de notificação */
#notificacao {
    position: fixed;
    top: 20px;
    right: 20px;
    background: #1877f2;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    display: none; /* começa escondido */
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
}
</style>
</head>
<body>

<h2>Simulação Airbnb</h2>

<div class="imovel">
    <h3>Apartamento no Centro</h3>
    <p>Preço: R$ 120,00 por noite</p>
    <a href="#" onclick="mostrarNotificacao('Apartamento no Centro')">Ver detalhes</a>
</div>

<div class="imovel">
    <h3>Casa na Praia</h3>
    <p>Preço: R$ 350,00 por noite</p>
    <a href="#" onclick="mostrarNotificacao('Casa na Praia')">Ver detalhes</a>
</div>

<div class="imovel">
    <h3>Loft Moderno</h3>
    <p>Preço: R$ 200,00 por noite</p>
    <a href="#" onclick="mostrarNotificacao('Loft Moderno')">Ver detalhes</a>
</div>

<div class="imovel">
    <h3>Chalé nas Montanhas</h3>
    <p>Preço: R$ 300,00 por noite</p>
    <a href="#" onclick="mostrarNotificacao('Chalé nas Montanhas')">Ver detalhes</a>
</div>

<!-- Notificação na tela -->
<div id="notificacao"></div>

<script>
// Função para mostrar notificação
function mostrarNotificacao(nomeImovel) {
    const notif = document.getElementById('notificacao');
    notif.textContent = `Você clicou no imóvel: ${nomeImovel}`;
    notif.style.display = 'block';

    // Esconde a notificação após 2 segundos
    setTimeout(() => {
        notif.style.display = 'none';
    }, 2000);
}
</script>

</body>

from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')


    imoveis=page.locator('div')
    total=imoveis.count()


    for i in range(total):
        imovel=imoveis.nth(i)
        texto=imovel.inner_text().lower()

        if "Montanhas".lower() in texto:
            print(f'encontrado')
            link=imovel.locator("a")
            if link.count()>0:
                print('encontrado')
                link.nth(0).click()
            break
    input('pressione algo para fechar')
    browser.close()

</html>
