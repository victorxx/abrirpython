from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    conteudo=page.locator('#texto')
    quantidade=conteudo.all_text_contents()
    termo='loja'
    achou=0
    for x in quantidade:
        if termo in x:
            achou+=1
    print(f'achamos o termo achou ->{achou}')


    browser.close()
