from playwright.sync_api import sync_playwright
import json
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Carregar cookies
    cookies_path = r'C:\Users\vitor\Desktop\facebooklogin\loginface.json'
    with open(cookies_path, 'r', encoding='utf-8') as file:
        cookies = json.load(file)
        page.context.add_cookies(cookies)

    # Abrir grupo
    page.goto('https://www.facebook.com/groups/202080559928269')
    page.wait_for_load_state('load')

    # Procurar divs com "ouro" e clicar no botão "Comentar"
    divs = page.locator('div')
    quantidade = divs.count()

    for x in range(quantidade):
        texto = divs.nth(x).inner_text()
        if 'ouro' in texto.lower():
            print('ok temos sim')
            botoes = divs.nth(x).get_by_role('button')
            quantidade_botoes = botoes.count()
            for y in range(quantidade_botoes):
                botao_texto=botoes.nth(y).inner_text()
                if 'Comentar' in botao_texto:
                    print('achamos o botão')
                    botoes.nth(y).wait_for(state='visible')
                    botoes.nth(y).click()
                    print('botão clicado')
                    time.sleep(3)
    input('quer fechar?')
    browser.close()
