from playwright.sync_api import sync_playwright
import os
import unicodedata
def remover(conteudo):
    nf=unicodedata.normalize('NFD',conteudo)
    return ''.join([c for c in nf if not unicodedata.combining(c)])

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
    page.wait_for_load_state('load')
    n=page.locator('p')
    for x in range(n.count()):
        ok=n.nth(x)
        texto=ok.inner_text()
    indo=remover(texto)
    print(indo)
    browser.close()

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Venda de Servidores VPS</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: #f4f6f9;
            color: #333;
        }

        header {
            background: #2b67f6;
            padding: 20px;
            text-align: center;
            color: white;
        }

        header h1 {
            margin: 0;
            font-size: 32px;
        }

        .container {
            width: 90%;
            max-width: 1100px;
            margin: auto;
            padding: 40px 0;
        }

        .section-title {
            text-align: center;
            font-size: 28px;
            margin-bottom: 30px;
        }

        .plans {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
        }

        .plan {
            background: white;
            width: 300px;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
            transition: 0.3s;
        }

        .plan:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }

        .plan h3 {
            margin: 0;
            font-size: 22px;
            color: #2b67f6;
        }

        .plan ul {
            list-style: none;
            padding: 0;
            margin: 20px 0;
            text-align: left;
        }

        .plan ul li {
            margin-bottom: 10px;
        }

        .price {
            font-size: 26px;
            margin: 15px 0;
            font-weight: bold;
            color: #111;
        }

        .btn {
            display: inline-block;
            background: #2b67f6;
            padding: 12px 20px;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-size: 16px;
            transition: 0.3s;
        }

        .btn:hover {
            background: #1f4ec7;
        }

        footer {
            text-align: center;
            background: #111;
            color: #fff;
            padding: 20px;
            margin-top: 40px;
        }

        .whatsapp-btn {
            position: fixed;
            right: 20px;
            bottom: 20px;
            background: #25d366;
            color: white;
            padding: 16px 18px;
            border-radius: 50%;
            font-size: 24px;
            text-decoration: none;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }
        #ok{
            scale:2.0;
        }
    </style>
</head>
<body>

<header>
    <h1>Servidores VPS Premium</h1>
    <p>Servidores potentes no Brasil com ótimo custo-benefício e suporte</p>
    <P id="ok">📌 (27) 99986-0405 – SMS, WhatsApp ou similar</P>
    <p>Alta Performance, Ativação Imediata e Suporte 24h</p>
</header>

<div class="container">
    <h2 class="section-title">Planos Disponíveis</h2>

    <div class="plans">
        
        <div class="plan">
            <h3>Plano Iniciante</h3>
            <ul>
                <li>1 vCPU</li>
                <li>2 GB RAM</li>
                <li>20 GB SSD</li>
                <li>1 Gbps</li>
            </ul>
            <div class="price">R$ CONSULTAR</div>
            <a class="btn" href="https://wa.me/5527999860405" target="_blank">Contratar</a>
        </div>

        <div class="plan">
            <h3>Plano Intermediário</h3>
            <ul>
                <li>2 vCPU</li>
                <li>4 GB RAM</li>
                <li>40 GB SSD</li>
                <li>1 Gbps</li>
            </ul>
            <div class="price">R$ CONSULTAR</div>
            <a class="btn" href="https://wa.me/5527999860405" target="_blank">Contratar</a>
        </div>

        <div class="plan">
            <h3>Plano Avançado</h3>
            <ul>
                <li>4 vCPU</li>
                <li>8 GB RAM</li>
                <li>80 GB SSD</li>
                <li>1 Gbps</li>
            </ul>
            <div class="price">R$ CONSULTAR</div>
            <a class="btn" href="https://wa.me/5527999860405" target="_blank">Contratar</a>
        </div>

    </div>
</div>

<footer>
    © 2025 Servidores VPS • Suporte via WhatsApp: (27) 99986-0405
</footer>

<a class="whatsapp-btn" href="https://wa.me/5527999860405" target="_blank">💬</a>

</body>
</html>
