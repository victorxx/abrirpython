from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.melhorcambio.com/ouro-hoje')
    page.wait_for_load_state('load')

    primeiro = page.get_by_role('textbox').nth(1).input_value()
    print(primeiro)

    browser.close()
