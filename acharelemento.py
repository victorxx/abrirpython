from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.espiritosanto-es.com.br/')
    page.wait_for_load_state('load')

    div_elemento=page.query_selector('#propaganda')


    if div_elemento:
        print('elemento encontrado')
    else:
        print('elemento não econtrado...')
    browser.close()
