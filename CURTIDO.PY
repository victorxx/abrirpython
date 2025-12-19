from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    buscar=page.query_selector_all('.curtiu')
    nomes=[u.inner_text() for u in buscar]
    transform_nomes=str(nomes)
    conteudo=page.query_selector('strong').inner_text()
    print('o conteúdo curtido por os usuários'+transform_nomes+'é esse aqui->'+conteudo)

    browser.close()


<!DOCTYPE html>
<meta charset="utf-8">
<title>treino</title>
<style>
    .post {
      border: 1px solid #ccc;
      padding: 15px;
      margin-bottom: 20px;
      border-radius: 5px;
      width: 300px;
    }
    .usuarios {
      margin-bottom: 10px;
    }
    .usuarios span {
      display: inline-block;
      margin-right: 5px;
      padding: 2px 6px;
      border-radius: 3px;
      color: white;
      font-size: 12px;
    }
    .curtiu { background: #4caf50; }
    .naocurtido { background: #f44336; }
</style>
<body>
<div class="post">
<div class="usuario">
    <strong>o movimento</strong>
    <br>
    <br>
    <span class="curtiu">joao</span>
    <div class="curtiu">maria</div>
    <div class="curtiu">cerena</div>
    <strong>curtiu</strong>
</div>
</div>
</body>
</html>
