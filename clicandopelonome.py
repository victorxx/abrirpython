from playwright.sync_api import sync_playwright
import time
import json

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')
    buscar=page.locator('a').all()
    for x in buscar:
        
        if 'não tem vez' in x.inner_text():
            print('ok temos sim')
            x.click()
    time.sleep(20)
    browser.close()
    
    
