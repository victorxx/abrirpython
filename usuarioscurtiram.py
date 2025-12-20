from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=True)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    usuarios=page.query_selector_all('span.curtiu')
    curtiram=''
    for x in usuarios:
        ok=x.inner_text()
        curtiram+=ok+' '
    print(curtiram)
    print('podemos finalizar aqui')
    browser.close()

<!DOCTYPE html>
<html lang="pt-br">
    <head>
<style>
.post{
border:1px solid #ccc;
width:300px;
}
.usuario span{
    display: inline-block;
    margin-right: 10px;
    color:white;
    border-radius: 12px;
}
.curtiu{
    background-color: green;
}
.naocurtiu{
    background-color: red;
}
</style>
    </head>
<body>
<div class="post">
    <div class="usuario">
        <strong>o mar é vermelho sim</strong>
        <span class="curtiu">joao</span>
        <span class="curtiu">maia</span>
        <span class="curtiu">cerejo</span>
        <span class="curtiu">alemao</span>
    </div>
    <div class="usuario">
        <strong>o mar 2</strong>
        <span class="curtiu">gloria</span>
    </div>
</div>
</body>
</html>
