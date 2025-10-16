import time
import random
from playwright.sync_api import sync_playwright
import json
import os

def desktop():
    desktop=os.path.join(os.path.expanduser('~'),'Desktop')
    nome='arquivo.json'
    completo=os.path.join(desktop,nome)
    return completo

def buscar():
    try:
        with sync_playwright() as p:
            completo=desktop()
            browser=p.chromium.launch(headless=False)
            page=browser.new_page()
            page.goto('https://www.youtube.com/')
            page.wait_for_load_state('load')
            cookies=page.context.cookies()
            with open(completo,'w') as arquivo:
                json.dump(cookies,arquivo)
            print('arquivo escrito com sucesso')
            browser.close()
    except:
        print('ok deu algo errado...')

buscar()
