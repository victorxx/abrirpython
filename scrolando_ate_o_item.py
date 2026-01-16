from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    item=page.get_by_text('roberto')
    item.scroll_into_view_if_needed()
    print(f'ok já achamos o termo {item.inner_text()}')
    input('pressione enter para fechar')
    browser.close()
  <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            height: 100%;
            margin: 0;
            padding: 0;
        }

        .card {
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .card div {
            width: 200px;
            height: 220px;
            margin: 1000px 0; /* cria espaço entre os elementos para precisar rolar */
            border-radius: 12px;
            background-color: peru;
            color: purple;
            box-shadow: 10px 10px 10px purple;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <div class="card">
        <div role="listitem">victor</div>
        <div role="listitem">Carlos</div>
        <div role="listitem">tiago</div>
        <div role="listitem">roberto</div>
    </div>
</body>
</html>

