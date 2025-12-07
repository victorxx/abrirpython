from playwright.sync_api import sync_playwright

def ir(page):
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')

def verificar(page):
    ok = page.locator('input[name="plano"][value="basico"]')
    if not ok.is_checked():
        print('OK, não está ativo ainda.')
    return ok

def marcar(ok):
    ok.check()
    print('OK marcado!')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Navegar para a página
    ir(page)

    page.wait_for_load_state('load')

    # Verificar o radio
    okok = verificar(page)

    # Marcar o radio
    marcar(okok)

    print('Tudo feito!')
    browser.close()

<!DOCTYPE html>
<html lang="pt-br">
    <head>

    </head>
    <body>
        <label>
         <input type="radio" name="plano" value="basico">BASICO
        </label>
        <label>
            <input type="radio" name="plano" value="premium"> PREMIUM
        </label>
    </body>
</html>

