<!DOCTYPE html>
<html>
    <head>

    </head>
    <body>
        <div class="conteudo">
            <h2>primeiro conteudo</h2>
            <div class="usuario">
                <li>victor</li>
                <li>ricardo</li>
                <li>matheus</li>
            </div>
            <button disabled>curtido</button>
        </div>
        <div class="conteudo">
            <h2>segundo conteudo</h2>
            <div class="usuario">
                <li>olivia</li>
                <li>ricardo</li>
                <li>matheus</li>
            </div>
            <button disabled>curtido</button>
        </div>
    </body>

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')

    dados = []

    conteudos = page.query_selector_all('.conteudo')

    for conteudo in conteudos:
        titulo = conteudo.query_selector('h2').inner_text()

        usuarios = conteudo.query_selector_all('.usuario li')
        lista_usuarios = [u.inner_text() for u in usuarios]

        dados.append({
            'conteudo': titulo,
            'usuarios': lista_usuarios
        })

    browser.close()

    
    for x in dados:
        print(x)

</html>
