from playwright.sync_api import sync_playwright
import time



with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.youtube.com/watch?v=5Q4qcpDAdNk')
    page.wait_for_load_state('load')
    texto=page.get_by_text("Curso", exact=False)
    contagem=texto.count()
    print(contagem)
    browser.close()
