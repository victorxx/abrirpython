from playwright.sync_api  import sync_playwright
import time


with sync_playwright() as p:
    browse=p.chromium.launch(headless=False)
    page=browse.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    buscar=page.locator('.conteudo')
    textos=buscar.all_text_contents()
    quantidade=0
    termo='loja'
    for x in textos:
        if termo in x:
            quantidade+=1
    print(f'número de itens encontrados {quantidade}')
    browse.close()
