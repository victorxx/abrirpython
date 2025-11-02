import requests
import time
import os
from playwright.sync_api import sync_playwright


def buscar():
    """Busca a URL da primeira imagem no Pinterest."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://br.pinterest.com/rosy_marques/imagens-japonesas/')
        page.wait_for_load_state('load')
        page.wait_for_selector('img', timeout=10000)  # garante que imagem carregou
        url = page.locator('img').nth(0).get_attribute('src')
        browser.close()
        return url


def baixar():
    """Baixa a imagem e salva no Desktop."""
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    arquivo = 'dado.png'
    caminho = os.path.join(desktop, arquivo)
    
    url = buscar()
    if not url:
        print("⚠️ Nenhuma imagem encontrada.")
        return None
    
    resposta = requests.get(url)
    if resposta.status_code == 200:
        with open(caminho, 'wb') as file:
            file.write(resposta.content)
        print(f"✅ Imagem baixada: {caminho}")
        return caminho
    else:
        print("❌ Erro ao baixar a imagem:", resposta.status_code)
        return None


def upload():
    """Preenche o textbox e envia a imagem para o input."""
    caminho = baixar()
    if not caminho:
        print("⚠️ Não foi possível baixar a imagem.")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
        page.wait_for_load_state('load')
        
        # Preenche o textbox (se existir)
        try:
            page.get_by_role('textbox').nth(0).fill('ok')
        except:
            print("⚠️ Textbox não encontrado. Verifique o role ou use outro seletor.")
        
        # Seta o arquivo
        try:
            
            page.set_input_files('input[type="file"]', caminho)
        except:
            print("⚠️ Input de arquivo não encontrado.")

        time.sleep(5)  # tempo para conferência
        browser.close()
        print('✅ Upload e preenchimento concluído.')


upload()
