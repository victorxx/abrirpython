from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    time.sleep(2)
    primeiro=page.locator('.grid')
    primeiro.scroll_into_view_if_needed()
    primeiro.click()
    time.sleep(40)
    browser.close()


<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <style>
            body{
                background-color: black;
            }
            .grid{
width:550px;
height: 330px;
text-align: center;
background-color: red;
border-radius: 12px;
padding:20px;
font-size: 200px;
            }
        </style>

    </head>
    <body>
        <div class="grid">
<a href="https://www.youtube.com/watch?v=pC1ge168Kls">ok</a>
        </div>
    </body>
</html>
