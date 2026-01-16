from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html',timeout=5000)
    page.wait_for_load_state('load')
    for x in range(10):
        page.mouse.wheel(0,1000)
        time.sleep(1)
        print('rolando a pagina')
    browser.close()
    print('finalizando o programa')
    
