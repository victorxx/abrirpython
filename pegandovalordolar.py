from playwright.sync_api import sync_playwright
import time
import os
desktop=os.path.join(os.path.expanduser('~'),'Desktop')
anotacao='ok.txt'
abrir=os.path.join(desktop,anotacao)
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.melhorcambio.com/ouro-hoje')
    page.wait_for_load_state('load')
    valor=page.get_by_role('textbox').nth(0).input_value()
    print(valor)
    print('ok o valor...')
    browser.close()
