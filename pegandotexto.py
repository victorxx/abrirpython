from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.mercadolivre.com.br/")
    page.wait_for_load_state("load")

    # Pega o texto do 4º botão na página
    buscar = page.get_by_role("button").nth(3).inner_text()
    print(buscar)

    time.sleep(3)
    browser.close()
