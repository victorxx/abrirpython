import os
from playwright.sync_api import sync_playwright

desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
arquivo = "contadorclick.txt"
juntar = os.path.join(desktop, arquivo)

# Verifica se já existe 'clicado 1'
termo = False
linhas = []

if os.path.exists(juntar):
    with open(juntar, 'r') as file:
        linhas = file.readlines()

for linha in linhas:
    if 'clicado 1' in linha:
        print('existe sim')
        termo = True

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')

    click = page.locator('.card div')
    quantidade = click.count()
    clicado = 0

    for x in range(quantidade):
        texto = click.nth(x).text_content().strip()

        # Se já clicou '1', clicar próximo
        if termo and texto == '2':  
            click.nth(x).click()
            clicado += 1
            if clicado == 1:
                with open(juntar, 'a') as file:
                    file.write(f'clicado {texto}\n')
            break
        # Se não clicou '1' ainda, clicar no 1
        elif not termo and texto == '1':
            click.nth(x).click()
            clicado += 1
            if clicado == 1:
                with open(juntar, 'a') as file:
                    file.write(f'clicado {texto}\n')
            break

    print('ok')
    browser.close()
