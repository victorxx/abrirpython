from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto('https://www.espiritosanto-es.com.br/?slug=1761785834_errari-76-o-supercarro-que-so-existe-no-mundo-digital')
    page.wait_for_load_state('load')
    
    # Busca todos os iframes
    buscar = page.query_selector_all('iframe')
    
    # Conta quantos iframes foram encontrados
    contagem = len(buscar)
    print(contagem)
    
    browser.close()
