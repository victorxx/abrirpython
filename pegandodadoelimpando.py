from playwright.sync_api import sync_playwright
import unicodedata
def remover(conteudo):
    nf=unicodedata.normalize('NFD',conteudo)
    return''.join([c for c in nf if not unicodedata.combining(c)])

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    primeiro=page.locator('article').nth(0).inner_text()
    indo=remover(primeiro)
    print(indo)
    browser.close()
