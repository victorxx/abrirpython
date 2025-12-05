from playwright.sync_api import sync_playwright
import time



okk='jogo'.lower()
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.espiritosanto-es.com.br/')
    page.wait_for_load_state('load')
    procurar=page.locator('article')
    for x in range(procurar.count()):
        ok=procurar.nth(x)
        nomes=ok.inner_text().lower()
        if okk in nomes:
            print('ok temos sim')
            link=ok.locator('a').click()
            print('clicando no link')
            time.sleep(10)
            page.go_back()
            print('indo para próxima...')
    browser.close()

    
