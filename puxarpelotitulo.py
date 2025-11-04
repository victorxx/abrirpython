from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.youtube.com/')
    page.wait_for_load_state('load')
    titulo=page.get_by_title()
    print(titulo)
    print('ok titulo do site')
    browser.close()
