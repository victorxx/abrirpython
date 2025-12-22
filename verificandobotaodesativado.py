from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    


    #abrapagina
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')


    conteudo=page.query_selector('.conteudo')

    usuario_elemento=conteudo.query_selector('.pessoa')
    usuario=usuario_elemento.inner_text()

    button=conteudo.query_selector('button')
    desativado=button.is_disabled()
    if desativado==True:
        print('desativado')
    else:
        print('ativado')
    browser.close()

<!DOCTYPE html>
<html lang="pt-br">
    <head>

    </head>
    <body>
     <div class="conteudo">
    <strong>o mar é bonito</strong>
    <div class="pessoa">
        victor 
     </div>
    <button disabled>CURTIDO</button>
</div>
    </body>
</html>
