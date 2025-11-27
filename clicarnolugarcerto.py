from playwright.sync_api import sync_playwright
import time



with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    nomes='Franquia! ⚔️✨'.lower()
    page.goto('https://www.espiritosanto-es.com.br/')
    page.wait_for_load_state('load')
    buscar=page.locator('article')
    quantidade=buscar.count()
    
    for x in range(quantidade):
        conteudo=buscar.nth(x)
        texto=conteudo.inner_text().lower()
        if nomes in texto.lower():
            link=conteudo.locator('a')
            if link.count()>0:
                link.nth(0).click()
                break
           
                
    input('presione algo para fechar') 
    browser.close()
