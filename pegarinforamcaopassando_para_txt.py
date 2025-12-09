from playwright.sync_api import sync_playwright 
import time
import os
dado=os.path.join(os.path.expanduser('~'),'Desktop')
arquivo='ok.txt'
juntar=os.path.join(dado,arquivo)
if os.path.exists(juntar):
    print('ok o arquivo existe... ')
else:
    print('ok o arquivo não existe')
    with open(juntar,'r') as file:
        file.read()
    print('ok arquivo criado...')


with  sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    time.sleep(1)
    th=page.locator('th')
    for x in range(th.count()):
        dado=th.nth(x).inner_text()
        with open(juntar,'a+') as file:
            file.write(dado+' ')
    with open(juntar,'a+') as file:
        file.write('\n')
    print('ok')
    browser.close()
