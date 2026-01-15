from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')

    cards = page.locator('.card')
    total_cards = cards.count()

    print(f'Total de cards encontrados: {total_cards}')

    for i in range(total_cards):
        pergunta = cards.nth(i).locator('.pergunta').inner_text().strip().lower()

        if pergunta == "faz entrega?":
            cliente = cards.nth(i).locator('.cliente').inner_text().split('\n')[0]
            print(f'Cliente: {cliente} | Pergunta: {pergunta}')

    browser.close()

    <!DOCTYPE html>
<html lang="pt-br">
    <head>
<meta charset="utf-8">
<style>
        body{
            margin:0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: black;
        }
        .card{
            width:550px;
            border-radius: 12px;
            background-color: orangered;
            transition: ease 0.2s;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 10x 10x 10px purple;
        }
        .card:hover{
            transform: scale(2.0);
        }
        @media(max-width:90em){
            .card:hover{
                scale: 70%;
            }
        }
        .cliente{
            width:250px;
            padding:20px;
            background-color: orchid;
            border-radius: 12px;
            color:#fff;
            text-align: center;
        }
        .pergunta{
            color:yellow;
            font-size:18px;
            box-shadow:2px 2px 8px purple;
            padding:8px;
            border-radius:8px;
            background:rgba(0,0,0,0.2);
        }
        .produto{
            width:250px;
            background-color: plum;
            border-radius: 12px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }
</style>
    </head>
    <body>
        <div class="card">
            <div class="cliente">
                Ricardo
                <div class="pergunta">
                    faz entrega?
                </div>
            </div>
            <div class="produto">
                xbox one
            </div>
        </div>
         <div class="card">
            <div class="cliente">
                Ricardo
                <div class="pergunta">
                    parcela?
                </div>
            </div>
            <div class="produto">
                xbox one
            </div>
        </div>
    </body>
</html>
