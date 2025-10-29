from playwright.sync_api import sync_playwright
import time



with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.youtube.com/watch?v=mvBlcE3knhI')
    page.wait_for_load_state('load')
    texto=page.get_by_role('button',name='Seja membro')
    contagem=texto.count()
    print(contagem)
    browser.close()
