<!DOCTYPE html>
<html lang="pt-br">
   <head>
<meta charset="utf-8">
<title>comentarios</title>
<style>
    body{
        font-family: Arial, Helvetica, sans-serif;

    }
    .comentario{
        width:550px;
        background-color: orange;
        padding:20px;
        margin:20px auto;
        border-radius: 12px;
    }
    .usuario{
        font-size: 30px;
        margin-bottom:20px;

    }

    .produto{
        display: flex;
        justify-content: space-around;
        align-items: center;
    }
    button{
        padding:10px 20px;
        font-size: 30px;
        border-radius: 12px;
        color:white;
        cursor: pointer;
        border:none;
    }
</style>
   </head> 
   <body>
<div class="comentario">
    <div class="usuario">
        RICARDO,ROMARCIO,TADEU
    </div>
    <div class="produto">
        <span>Remedio</span>
        <button>NÃO GOSTEI</button>
    </div>
</div>
<div class="comentario">
    <div class="usuario">
        RICARDO
    </div>
    <div class="produto">
        <span>Remedio</span>
        <button>GOSTEI</button>
    </div>
</div>
   </body>
</html>
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('file:///C:/Users/vitor/Desktop/pagina.html', timeout=50000)
    page.wait_for_load_state('load')

    comentarios = page.locator('.comentario')
    total = comentarios.count()

    for x in range(total):
        comentario = comentarios.nth(x)

        usuario = comentario.locator('.usuario').inner_text().strip()
        produto = comentario.locator('.produto span').inner_text().strip()
        bott = comentario.locator('button').inner_text().strip()

        if bott == "NÃO GOSTEI":
            print('pessoas que não gostaram')
            print(usuario, produto, bott)
        if bott!="NÃO GOSTEI":
            print("pessoas que gostaram")
            print(usuario,produto,bott)

    browser.close()
