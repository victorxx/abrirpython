from playwright.sync_api import sync_playwright
import time
import os


with sync_playwright() as p:
    browsr=p.chromium.launch(headless=False)
    page=browsr.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')
    ir=page.locator("label:text('Masculino')").click()
    input('iniciar')
    browsr.close()
