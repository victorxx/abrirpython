from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    indo=page.locator('.ir')
    indo.scroll_into_view_if_needed()
    print('ok')
    print('ok já foi')
    browser.close()


<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <style>
            body{
                background-color: black;
            }
            .ir{
                width:100%;
                height: 250px;
                padding:20px;
                border-radius: 12px;
                background-color: red;
                font-size: 50px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <script>
        document.write('<br>'.repeat(100));
        </script>
        <div class="ir">
            ok
        </div>
    </body>
</html>
