from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    button=page.locator('button')
    color=button.evaluate('ok=>window.getComputedStyle(ok).backgroundColor')
    print(color)
    print('ok está tudo certo')
    browser.close()

<!DOCTYPE html>
<html lang="pt-br">
    <head>
<style>
        button{
            width:550px;
            border-radius: 12px;
            text-align: center;
            position: absolute;
            left: 10%;
            top:100px;
            background-color: red;
            color:white;
            border-radius: 12px;
        }
        @media(max-width:550px){
            button{
                left: 0;
                width:250px;
            }
        }
        button:disabled{
            background-color: black;
        }
</style>
</head>
<body>
    
<button disabled>DESATIVADO</button>
</body>
</html>
