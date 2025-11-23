from playwright.sync_api import sync_playwright
import time



with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')
    x=page.locator('.card')
    for y in x.all():
        if "Vendo" in y.inner_text():
            print('temos sim')
            y.get_by_role('button').click()
            print('clicado')
            time.sleep(10)

    browser.close()
from playwright.sync_api import sync_playwright
import time



with sync_playwright () as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')
    card=page.locator('.card',has_text='Vendo bicicleta')
    card.get_by_role('button').click()
    time.sleep(10)
    browser.close()


<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Dashboard de Classificados</title>
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
        background: #f2f2f2;
    }

    h1 {
        text-align: center;
    }

    .card {
        background: white;
        border-radius: 6px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 0 5px rgba(0,0,0,0.2);
    }

    .title {
        font-size: 20px;
        font-weight: bold;
    }

    .btn-responder {
        margin-top: 10px;
        background: #2196f3;
        color: white;
        border: none;
        padding: 8px 12px;
        border-radius: 4px;
        cursor: pointer;
    }

    .btn-responder a {
        color: white;
        text-decoration: none;
        font-weight: bold;
    }

    .btn-responder:hover {
        background: #0b7dda;
    }

    .respostas {
        margin-top: 10px;
        padding-left: 10px;
        border-left: 3px solid #2196f3;
    }

    .resposta-item {
        background: #e8f3ff;
        margin: 5px 0;
        padding: 5px 8px;
        border-radius: 4px;
    }
</style>
</head>
<body>

<h1>Classificados - Respostas</h1>

<div id="lista"></div>

<script>
// Dados fake para testes + links externos
const anuncios = [
    { id: 1, titulo: "Vendo bicicleta", descricao: "Bicicleta aro 29, ótima condição.", respostas: [], link: "https://example.com/bicicleta" },
    { id: 2, titulo: "Preciso de freela em JavaScript", descricao: "Projeto pequeno, pagamento rápido.", respostas: [], link: "https://example.com/freela" },
    { id: 3, titulo: "Procuro apartamento para alugar", descricao: "2 quartos, próximo ao centro.", respostas: [], link: "https://example.com/apartamento" }
];

function render() {
    const container = document.getElementById("lista");
    container.innerHTML = "";

    anuncios.forEach(anuncio => {
        const card = document.createElement("div");
        card.className = "card";
        card.setAttribute("data-id", anuncio.id);

        card.innerHTML = `
            <div class="title">${anuncio.titulo}</div>
            <div>${anuncio.descricao}</div>

            <button class="btn-responder" data-responder="${anuncio.id}">
                <a href="${anuncio.link}" target="_blank">Abrir página</a>
            </button>

            <div class="respostas" id="respostas-${anuncio.id}">
                ${anuncio.respostas.map(r => `<div class="resposta-item">${r}</div>`).join("")}
            </div>
        `;

        container.appendChild(card);
    });
}

// Clique no botão (mas NÃO no link) → ainda abre o prompt
document.addEventListener("click", function(e) {
    const button = e.target.closest("[data-responder]");

    // se clicou somente no botão (fora do <a>), abre o prompt
    if (button && e.target.tagName !== "A") {
        const id = button.getAttribute("data-responder");
        const resposta = prompt("Digite sua resposta para o anúncio " + id + ":");

        if (resposta) {
            const anuncio = anuncios.find(a => a.id == id);
            anuncio.respostas.push(resposta);
            render();
        }

        e.preventDefault();
    }
});

render();
</script>

</body>
</html>

