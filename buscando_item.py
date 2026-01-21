from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()

    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')


    locator=page.locator('.conteudo')
    quantidade=0
    for i in range(locator.count()):
        if 'loja' in locator.nth(i).inner_text():
            quantidade+=1
    print(f'A quantidade de termos são {quantidade}')
    browser.close()
