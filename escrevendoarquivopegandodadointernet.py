import os
from playwright.sync_api import sync_playwright
desktop=os.path.join(os.path.expanduser('~'),'Desktop')
arquivo='ok.txt'
juntar=os.path.join(desktop,arquivo)

if os.path.exists(juntar):
    print('ok está tudo certo')
else:
    with open(juntar,'w') as file:
        file.write()
    print('ok está tudo ok')


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    contador=0
    td=page.locator('td')
    for x in range(td.count()):
        dado=td.nth(x).inner_text()
        with open(juntar,'a+') as file:
            file.write(dado+' ')
        contador+=1
        if contador==2:
            with open(juntar,'a+') as file:
                file.write('\n')

    print('dados salvos com sucesso...')
    browser.close()
    
            





