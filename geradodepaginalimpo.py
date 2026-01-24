import os

# Pergunta ao usuário se quer adicionar um link
pergunta = input('QUER ADICIONAR UM LINK ? S OU N:\n ').lower()

link = ''
texto_link = ''

if pergunta == 's':
    link = input('Insira seu link aqui: \n')
    texto_link = input('Digite aqui texto do link \n')

titulo = input('Digite o titulo do video:\n ')
video_url = input('Cole a URL embed do video (ex: https://www.youtube.com/embed/XXXX): ')

# HTML do h2 só será incluído se link não for vazio
h2_html = f'<h2><a href="{link}">{texto_link}</a></h2>' if link else ''

html = f'''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta property="og:image" content="https://raw.githubusercontent.com/victorxx/tump/refs/heads/main/agradavel_post.jpg">
    <title>{titulo}</title>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {{
            background-color: #000;
            color: #fff;
            margin: 0;
            padding: 0;
            font-family: Arial, Helvetica, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        h1 {{
            margin-top: 20px;
            font-size: 2rem;
        }}

        h2 a {{
            color: yellow;
            text-decoration: none;
        }}

        h2 a:hover {{
            text-decoration: underline;
        }}

        #video {{
            width: 90%;
            max-width: 600px;
            margin-top: 40px;
        }}

        #video iframe {{
            width: 100%;
            height: 320px;
            border-radius: 12px;
            border: none;
        }}

        @media (max-width: 550px) {{
            #video iframe {{
                height: 230px;
            }}
        }}

        .propaganda {{
            margin-top: 40px;
            display: flex;
            justify-content: center;
            gap: 15px;
            padding-bottom: 40px;
        }}

        .propaganda a {{
            background-color: red;
            color: white;
            border-radius: 10px;
            padding: 12px 18px;
            font-size: 15px;
            font-weight: bold;
            text-decoration: none;
            transition: 0.2s;
        }}

        .propaganda a:hover {{
            background-color: #cc0000;
            transform: scale(1.05);
        }}
    </style>
</head>

<body>

    <h1>{titulo}</h1>
    {h2_html}

    <div class="propaganda">
        <a href="https://www.espiritosanto-es.com.br/saida/">
            OPA CONFIRA ESSA OPORTUNIDADE
        </a>
    </div>

    <div class="propaganda">
        <a href="https://www.espiritosanto-es.com.br/produtos/ios/">
            PRODUTOS IOS CONFIRA
        </a>
    </div>

    <div id="video">
        <iframe
            src="{video_url}"
            title="YouTube video player"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen>
        </iframe>
    </div>

</body>
</html>
'''

# Salva o arquivo na área de trabalho
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
nome_arquivo = 'pagina.html'
caminho = os.path.join(desktop, nome_arquivo)

with open(caminho, 'w', encoding='utf-8') as file:
    file.write(html)

print('✅ Página criada com sucesso na Área de Trabalho!')
