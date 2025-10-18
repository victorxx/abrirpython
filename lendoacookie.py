from playwright.sync_api import sync_playwright
import os
import json
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        contexto=browser.new_context()
        desktop=os.path.join(os.path.expanduser('~'),'Desktop')
        arquivo='novo.json'
        juntar=os.path.join(desktop,arquivo)
        with open(juntar,'r') as file:
            lendo=json.load(file)
        contexto.add_cookies(lendo)
        print('lido....')
        page=contexto.new_page()
        page.goto('https://www.youtube.com/')
        page.wait_for_load_state('load')
        browser.close()
except:
    print('ok deu algo errado...')
