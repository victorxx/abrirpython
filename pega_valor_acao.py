from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://investidor10.com.br/acoes/bbas3/')
    page.wait_for_load_state('load')

    buscar=page.locator("text=R$").first
    if buscar.count()>0:
        print('achamos o item')
        imprimir=buscar.inner_text()
        print(imprimir)
    browser.close()
    print('finalizando o programa')
