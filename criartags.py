from playwright.sync_api import sync_playwright 
import time


with sync_playwright() as p:
    try:
                browser=p.chromium.launch(headless=False)
                page=browser.new_page()
                page.goto('https://www.espiritosanto-es.com.br/?slug=1764349832_odigos-e-heats-para-he-ims-3')
                page.wait_for_load_state('load')
                pesquisar=page.locator('article')
                for x in range(pesquisar.count()):
                    quantidade2=pesquisar.nth(x)
                    conteudo=quantidade2.inner_text().lower()
                    picotar=conteudo.split()
                    print(picotar)
                for y in picotar:
                       resposta='#'+y
                       print(resposta)
                browser.close()
    except:
           print('ko deu algo errado')
        
