from playwright.sync_api import sync_playwright
import time
import os



with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')
    time.sleep(2)
    primeiro=page.get_by_role('checkbox').nth(0).check()
    time.sleep(90)
    browser.close()
