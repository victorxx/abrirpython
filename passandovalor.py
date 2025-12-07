from playwright.sync_api import sync_playwright
import time
def indo(page,browser,dado):
    page.goto(dado)
    page.wait_for_load_state('load')
    print('carregado...')
    time.sleep(30)
    browser.close()
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    ir=indo(page,browser,'https://www.youtube.com/watch?v=BiTbPRjkhkQ')
    
