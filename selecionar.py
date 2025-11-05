from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Abra o arquivo local
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')
    time.sleep(1)

    # Selecionar o primeiro input pelo name
    quantidade=page.locator('input[type="radio"][name="genero"]').nth(0).click()
    print(quantidade)
    

    time.sleep(2)
    input('Pressione algo para sair...')
    browser.close()
