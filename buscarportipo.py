from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')
    texto=page.get_by_role("button", name="comprar")
    contagem=texto.count()
    print(contagem)
    browser.close()
    


