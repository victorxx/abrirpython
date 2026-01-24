from playwright.sync_api import sync_playwright
import os

# Definir caminho do arquivo na área de trabalho
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
arquivo = "clicado.txt"
juntar = os.path.join(desktop, arquivo)

# Inicializar a lista de dados com os valores do arquivo
dados = []
if os.path.exists(juntar):
    # Se o arquivo existir, abre e lê as linhas, removendo quebras de linha extras
    with open(juntar, 'r', encoding='utf-8') as file:
        dados = [linha.strip() for linha in file]

# Usando o Playwright para automatizar o navegador
with sync_playwright() as p:
    # Lançar o navegador Chromium (não headless para ver o que está acontecendo)
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        # Acessar a página local HTML
        page.goto('file:///C:/Users/vitor/Desktop/pagina.html')
        # Esperar a página carregar completamente
        page.wait_for_load_state('load')

        # Localizar todos os elementos dentro do .container div
        selecionar = page.locator('.container div')
        # Contar quantos elementos foram encontrados
        contagem = selecionar.count()

        # Iterar sobre todos os elementos encontrados
        for i in range(contagem):
            # Extrair o texto do elemento e remover espaços em branco
            texto = selecionar.nth(i).text_content().strip()
            
            # Verificar se o texto já foi registrado
            if texto in dados:
                continue  # Se já foi salvo, passa para o próximo

            # Se o texto não estiver nos dados, salvar no arquivo
            with open(juntar, 'a', encoding='utf-8') as file:
                file.write(texto + '\n')  # Escrever o texto no arquivo

            # Exibir mensagem indicando que o novo texto foi salvo
            print(f'Novo texto salvo com sucesso: {texto}')
            break  # Após salvar o primeiro novo texto, interromper o loop

    except Exception as e:
        # Caso ocorra algum erro, exibir uma mensagem
        print(f'Deu algo errado: {e}')

    finally:
        # Independentemente de ter erro ou não, o navegador será fechado
        print('Finalizando o navegador...')
        browser.close()


<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <style>
            body{
                background-color: black;
                height: 100vh;
                justify-content: center;
                align-items: center;
                display: flex;
            }
            .container{
                display: grid;
                grid-template-columns: repeat(3,1fr);
                background-color: red;
                line-height: 150px;
                text-align: center;
                gap:20px;
                
            }
            .container div{
                width:220px;
                height: 150px;
                font-size: 33px;
                background-color: orangered;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div>1</div>
            <div>2</div>
            <div>3</div>
        </div>
    </body>
</html>
