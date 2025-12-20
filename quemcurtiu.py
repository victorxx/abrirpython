from playwright.sync_api import sync_playwright
import time

try:
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
        page.wait_for_load_state('load')

        posts=page.query_selector_all('div.post')

        for post in posts:
            titulo=post.query_selector('strong').inner_text()
            usuarios=post.query_selector_all('span')
            texto=[span.inner_text() for span in usuarios]
            print(f'esse seria o texto curtido por usuario{titulo} os usuarios seriam esses aqui->{texto}' )
    browser.close()
except:
    print('ok deu algo errado')

<!DOCTYPE html>
<html lang="pt-br">
<head>
<style>
    .post{
    width:440px;
    height: 250px;
    background-color: red;
    padding:20px;
    text-align: center;
    }
    span{
        width:330px;
        height: 250px;
        border-radius: 12px;
        background-color: yellow;
    }
</style>
</head>
<body>
<div class="post">
<strong>o mar sobre</strong>
<span>igor(curtiu)</span>
<span>jorge(curtiu)</span>
<span>igorjorge(curtiu)</span>
</div>
</body>
</html>
