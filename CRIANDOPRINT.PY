from playwright.sync_api import sync_playwright
import time
import os
desktop=os.path.join(os.path.expanduser('~'),'Desktop')
arquivo='img.png'
juntar=os.path.join(desktop,arquivo)
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://cqcs.com.br/noticia/bradesco-seguros-aposta-em-diversificacao-e-identifica-estabilizacao-no-mercado-de-seguro-auto/')
    page.wait_for_load_state('load')
    buscar=page.screenshot(path=juntar,full_page=False)
    browser.close()
    print('ok já foi')
