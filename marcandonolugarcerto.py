from playwright.sync_api import sync_playwright
import time

def marcar(page,browser):
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    page.locator('input[type="checkbox"][value="rio"]').check()
    print('marcado')
    time.sleep(20)
    
    browser.close()

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    ok=marcar(page,browser)
  
    
