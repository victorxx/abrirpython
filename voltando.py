from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.youtube.com/')
    page.wait_for_load_state('load')
    print('carregado...')
    time.sleep(10)
    buscar_link=page.locator('a').nth(0).click()
    time.sleep(5)
    page.go_back()
    print('voltando')
    browser.close()
