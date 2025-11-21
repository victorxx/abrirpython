import mysql.connector
from playwright.sync_api import sync_playwright
import time
import json
import os

with sync_playwright() as p:
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    arquivo = 'imprimti.png'
    juntar = os.path.join(desktop, arquivo)

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Caminho local do seu arquivo
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')

    # Aguarda o carregamento completo
    page.wait_for_load_state('networkidle')

    # Screenshot da página
    page.screenshot(path=juntar, full_page=True)

    browser.close()
