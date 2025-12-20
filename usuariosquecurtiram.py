<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Posts</title>
</head>
<body>
    <div class="post">
        <div class="usuario">
            <strong>o mar é lindo</strong>
            <span class="curtiu">rogerio</span>
            <span class="curtiu">marcos</span>
            <span class="curtiu">olivia</span>
        </div>
        <div class="usuario">
            <strong>o mar é lindo 2</strong>
            <span class="curtiu">marcos oliveira</span>
            <span class="curtiu">gustavo</span>
            <span class="curtiu">edimar olinda</span>
        </div>
    </div>
</body>
</html>
from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=True)
    page=browser.new_page()

    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')

    page.wait_for_load_state('load')

    posts=page.query_selector_all('div.post>div.usuario')

    for i , post in enumerate(posts,start=1):
        titulo=post.query_selector('strong').inner_text()

        curtiu=post.query_selector_all('span.curtiu')
        usuarios=[span.inner_text() for span in curtiu]

        print(f'o nome do post é {titulo} o usuarios que curtiram{usuarios}')

