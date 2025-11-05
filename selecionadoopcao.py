from playwright.sync_api import sync_playwright
import time
import os


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')
    page.locator('select[name="pais"]').select_option("Portugal")
    page.wait_for_load_state('load')
    input('selecionado primeiro')
    browser.close()

