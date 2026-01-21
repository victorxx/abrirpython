from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()


    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    
    locator=page.get_by_text('loja')
    quantidade=locator.count()
    print(f'A quantidade encontrada é->{quantidade}')
    browser.close()
