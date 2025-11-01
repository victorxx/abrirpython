from playwright.sync_api import sync_playwright
import time
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('urlsua')
        page.wait_for_load_state('load')
        time.sleep(1)
        buscar=page.get_by_role('textbox')
        buscar.click()
        buscar.fill('escrevendo...')
        time.sleep(5)
        buscar.fill('')
        print('fechado....')
        time.sleep(10)
        
        browser.close()

except:
    print('ok deu algo errado...')
