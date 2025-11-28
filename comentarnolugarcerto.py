
from playwright.sync_api import sync_playwright
import time
import os
import json
palavra='cupons '

with sync_playwright() as p:
    cookie_link=r'C:\Users\vitor\Desktop\facebooklogin\loginface.json'
    browser=p.chromium.launch(headless=False)
    with open(cookie_link,'r',encoding='utf-8') as file:
        lendo=json.load(file)
    page=browser.new_page()
    desativar_ativado=True
    page.context.add_cookies(lendo)
    page.goto('https://www.facebook.com/groups/342230823010664')
    page.wait_for_load_state('load')
    time.sleep(2)
    while desativar_ativado:
        page.mouse.wheel(0,100000)
        time.sleep(0.1)
        print('movimentando o mouse...')
        buscar=page.locator('div')
        for x in range(buscar.count()):
            dado=buscar.nth(x)
            dados=dado.inner_text().lower()
            if palavra in dados:
                print('achamos')
                desativar_ativado=False
                comentar=dado.locator('text=Comentar').nth(1)
                clicado=comentar.click()
                time.sleep(3)
                page.mouse.wheel(0,-10000)
                buscando=page.locator('div')
                for y in range(buscando.count()):
                    p=buscando.nth(y)
                    texto=p.inner_text().lower()
                    if 'cupons' in texto:
                        print('estamos no lugar certo')
                        caixa=page.get_by_role('textbox').fill('escrevendo....')
                        
                        
                        
                        break


                
            
          
                
                break
    input('pressione enter para parar')
    browser.close()

from playwright.sync_api import sync_playwright
import time
import os
import json
palavra='cupons '

with sync_playwright() as p:
    cookie_link=r'C:\Users\vitor\Desktop\facebooklogin\loginface.json'
    browser=p.chromium.launch(headless=False)
    with open(cookie_link,'r',encoding='utf-8') as file:
        lendo=json.load(file)
    page=browser.new_page()
    desativar_ativado=True
    page.context.add_cookies(lendo)
    page.goto('https://www.facebook.com/groups/342230823010664')
    page.wait_for_load_state('load')
    time.sleep(2)
    while desativar_ativado:
        page.mouse.wheel(0,100000)
        time.sleep(0.1)
        print('movimentando o mouse...')
        buscar=page.locator('div')
        for x in range(buscar.count()):
            dado=buscar.nth(x)
            dados=dado.inner_text().lower()
            if palavra in dados:
                print('achamos')
                desativar_ativado=False
                comentar=dado.locator('text=Comentar').nth(1)
                clicado=comentar.click()
                time.sleep(3)
                page.mouse.wheel(0,-10000)
                buscando=page.locator('div')
                for y in range(buscando.count()):
                    p=buscando.nth(y)
                    texto=p.inner_text().lower()
                    if 'cupons' in texto:
                        print('estamos no lugar certo')
                        caixa=page.get_by_role('textbox').click()
                        page.keyboard.type('escrevendo na caixa de texto...')
                        
                        
                        break


                
            
          
                
                break
    input('pressione enter para parar')
    browser.close()
