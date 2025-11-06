from playwright.sync_api import sync_playwright
import time
import os
import requests


def puxar():
    try:
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=False,args=['--window-position=-20000,0'])
        
            page=browser.new_page()
            
            page.goto('https://br.pinterest.com/uniter1265/garotas-japonesas/')
            page.wait_for_load_state('load')
            time.sleep(2)
            primeiro=page.locator('img').nth(0).get_attribute('src')
            print(primeiro)
            browser.close()
    except:
        print('ok deu algo errado...')

puxar()
