import os
from playwright.sync_api import sync_playwright
caminho=os.path.join(os.path.expanduser('~'),'Desktop')
arquivo='imagem.png'
juntar=os.path.join(caminho,arquivo)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Abrir arquivo local
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    
    page.wait_for_load_state('load')
    
    # Capturar screenshot
    screenshot = page.screenshot(path=juntar)
    
    print("Screenshot salva como screenshot.png")

    browser.close()
