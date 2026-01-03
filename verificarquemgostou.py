<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<style>
    body{
        font-family: Arial, Helvetica, sans-serif;
    }
    .comentario{
        width:550px;
        background-color: orangered;
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
        justify-content:space-around;
        align-items: center;
    }
    button{
        padding:15px 20px;
        font-size: 30px;
        color:white;
        cursor: pointer;
        border-radius: 12px;
    }
</style>
</head>
<body>
    <div class="comentario">
        <div class="usuario">
            Ricardo,Romarcio,Tadeu
        </div>
        <div class="produto">
            <span>remedio</span>
            <button>gostei</button>
        </div>
    </div>
</body>

from playwright.sync_api import sync_playwright
import time




with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html',timeout=50000)
    page.wait_for_load_state()
    comentarios=page.locator('.comentario')
    total=comentarios.count()
    for x in range(total):
        comentario=comentarios.nth(x)

        usuario=comentario.locator('.usuario').text_content().strip()
        produto=comentario.locator('.produto span').text_content().strip()
        botao=comentario.locator("button").text_content().strip()

        print(usuario,produto,botao)
        browser.close()
        print('ok')
</html>
