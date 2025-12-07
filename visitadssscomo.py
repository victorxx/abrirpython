from playwright.sync_api import sync_playwright
import time

def visitar(page,browser):
    page.goto('https://www.youtube.com/watch?v=Po-CYqju0-Q')
    page.wait_for_load_state('load')
    print('visitado')
    time.sleep(20)
    browser.close()

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    ir=visitar(page,browser)
   
    
