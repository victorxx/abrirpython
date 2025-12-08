from playwright.sync_api import sync_playwright
import time
import os
dekstop=os.path.join(os.path.expanduser('~'),'Desktop')
anotacao='ok.txt'
juntar=os.path.join(dekstop,anotacao)
if os.path.exists(juntar):
    print('ok temos sim')
else:
    print('ok não tem')
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.melhorcambio.com/ouro-hoje')
    page.wait_for_load_state('load')
    valor=page.get_by_role('textbox').nth(0).input_value()
    
    print(f'valor ok {valor}')
    with open(juntar,'a',encoding='utf-8') as file:
        file.write(valor+'\n')
    print('escrito....')
    browser.close()
