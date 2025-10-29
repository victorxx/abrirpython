from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.mercadolivre.com.br/console-sony-playstation-5-edico-slim-disk-1tb-branco-controle-sem-fio-dualsense-ps5-branco/p/MLB52897777?pdp_filters=item_id%3AMLB4133992197#polycard_client=offers&wid=MLB4133992197&sid=offers&deal_print_id=f2061088-f57f-4e51-ac77-6ef872a2bf4d&tracking_id=34a347de-dcec-4d3c-a64d-1a010808ed9c&position=1')
    page.wait_for_load_state('load')
    selecao=page.get_by_text('SELECIONAR')
    contagem=selecao.count()
    print(contagem)
    browser.close()

