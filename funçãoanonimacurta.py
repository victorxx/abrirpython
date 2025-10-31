from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.mercadolivre.com.br/')

    # Seleciona o campo de busca e digita
    page.get_by_role('textbox').click()
    page.keyboard.type('xbox one')
    page.keyboard.press("Enter")
    time.sleep(10)  # espera carregar resultados

    # Pega o link do segundo produto que contém "Microsoft Xbox"
    buscar = page.get_by_text('Microsoft Xbox', exact=False).nth(1).evaluate('a=>a.close("a").href')

    # Vai para a página do produto
    page.goto(buscar)
    time.sleep(20)

    print("Busca concluída com sucesso!")
    browser.close()
