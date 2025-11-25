from playwright.sync_api import sync_playwright
import time
import os
import json

filtro='Boa tarde!'

with sync_playwright() as p:
    caminho=r'C:\Users\vitor\Desktop\facebooklogin\loginface.json'
    with open(caminho,'r',encoding='utf-8') as file:
        lendo=json.load(file) 
    browser=p.chromium.launch(headless=False)

    page=browser.new_page()
    page.context.add_cookies(lendo)
    page.goto('https://www.facebook.com/groups/1118054336571444')
    page.wait_for_load_state('load')
    for x in range(3):
        buscar=page.locator('div')
        contagem=buscar.count()
    for y in range(contagem):
        busquei=buscar.nth(y).inner_text().lower()
        if filtro.lower() in busquei:
            print('achamos essa expressão')
            comentar=page.locator('text="Comentar"')
            quantidade=comentar.count()
            if quantidade>0:
                comentar.click()
                break
            
         
    input('pressione algo')
        
    
    browser.close()
    
