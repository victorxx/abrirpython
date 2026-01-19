from playwright.sync_api import sync_playwright
import time

termo="CARINA"

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://mercadodecavalos.com.br/30877/mangalarga')
    page.wait_for_load_state('load')

    tentativas=0
    max_tentativas=60
    encontrou=False

    while tentativas< max_tentativas:
        if termo in page.content():
            print('Achamos o termo')
            encontrou=False
            break
        page.mouse.wheel(0,1000)
        time.sleep(0.6)
        if not encontrou:
            print('esgotado')
    browser.close()
    print('finalizado')
