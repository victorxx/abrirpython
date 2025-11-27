from playwright.sync_api    import sync_playwright
import time




with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://agenciabrasil.ebc.com.br/')
    page.wait_for_load_state('load')
    buscar=page.locator('div')
    palavra='stf'.lower()
    for x in range(buscar.count()):
        rodando=buscar.nth(x)
        filtro=rodando.inner_text().lower()
        if palavra in filtro:
            print('ok temos sim')
            clicar=rodando.locator('a').nth(3).click()
            time.sleep(10)
    input('pressione')
    browser.close()
   
