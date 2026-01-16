from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html',timeout=50000)
    buscar=page.locator("text=roberto")
    quantidade=buscar.count()

    print(f"Quantidade de elementos encontrados {quantidade}")
    print('finalizado')
    browser.close()
  <!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <style>
            .card{
                width:100%;
                height: 550px;
                margin:20px;
                gap:20px;
                display: grid;
                transform: translate(33%,50%);
            }
            .card div{
                width:200px;
                height: 220px;
                border-radius: 12px;
                background-color: peru;
                color:purple;
                box-shadow: 10px 10px 10px purple;
            }
        </style>
    </head>
    <body>
        
        <div class="card">
            <div>victor</div>
            <script>
                for(let $i=0;$i<500;$i++){
                    document.write('<br>');
                }
            </script>
            <div>Carlos</div>
            <script>
                for(let $i=0;$i<100;$i++){
                    document.write('<br>');
                }
            </script>
            <div>tiago</div>
            <script>
                for(let i=0;i<1000;i++){
                    document.write('<br>');
                }
            </script>
            <div>roberto</div>
        </div>
    </body>
</html>
