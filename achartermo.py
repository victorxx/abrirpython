from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    texto='5'.lower()
    page.goto('https://www.youtube.com/@CardioDF/videos',timeout=50000)
    page.wait_for_load_state('load')
    video=page.locator('#video-title-link')
    for x in range(video.count()):
        lista=video.nth(x)
        imprimir=lista.inner_text().lower()
        if texto in imprimir:
            print('temos o termo sim podemos fechar')
            break

    browser.close()
