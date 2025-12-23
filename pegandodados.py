from playwright.sync_api import sync_playwright
import time

with sync_playwright()  as  p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')

    dados=[]

    conteudos=page.query_selector_all('.conteudo')


    for conteudo in conteudos:
        titulo=conteudo.query_selector('h2').inner_text()


        usuarios=conteudo.query_selector_all('.usuario li')


        lista=[u.inner_text() for u in usuarios]

        dados.append({
            'conteudo':titulo,
            'usuario':lista
        })
    browser.close()
    print(dados)
    print('ta tudo certo...')

<!DOCTYPE html>
<html lang="pt-br">
    <head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<style>

</style>
    </head>
<body>
<div class="conteudo">
    <h2>primeiro conteudo</h2>
    <div class="usuario">
        <li>victor</li>
        <li>gustavo</li>
        <li>marcio</li>
    </div>
    <button disabled>curtido</button>
</div>
<div class="conteudo">
    <h2>segundo conteudo</h2>
    <div class="usuario">
        <li>rodrigo</li>
        <li>gustavo</li>
        <li>marcio</li>
    </div>
    <button disabled>curtido</button>
</div>
</body>
</html>


