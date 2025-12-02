from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://sites.google.com/view/omelhordainternet2/moedas-de-um-real-podem-valer-r-8-mil')
    page.wait_for_load_state('load')
    buscar=page.locator('.plFg0c a')

    for x in range(buscar.count()):
        links=buscar.nth(x)
        conteudo=links.get_attribute('href')
        print(conteudo)
    browser.close()
