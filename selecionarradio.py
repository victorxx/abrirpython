from playwright.sync_api import sync_playwright
import os
import time

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')
    page.get_by_role('textbox').nth(0).fill('inserir')
    page.get_by_role('textbox').nth(1).fill('inserir 2')
    page.check('#masc')
    print('preenchido os dois + radio')
    input('quer fechar?')
    browser.close()
