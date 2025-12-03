import os

# Pergunta ao usuário se quer adicionar um link
pergunta = input('QUER ADICIONAR UM LINK ? S OU N: ').lower()
link = ''  # inicializa link vazio

if pergunta == 's':
    link = input('Insira seu link aqui: ')
    texto_link=input('digite aqui texto do link')

titulo = input('Digite o titulo do video: ')
video_url = input('Cole a URL embed do video (ex: https://www.youtube.com/embed/XXXX): ')

# HTML do h2 só será incluído se link não for vazio
h2_html = f'<h2><a href="{link}">{texto_link}</a></h2>' if link else ''

html = f'''
<!DOCTYPE html>
<html lang="pt-br">
<head>
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

        .propaganda2 {{
            width: 90%;
            max-width: 600px;
            height: 300px;
            margin-top: 20px;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.15);
        }}

        .propaganda2 iframe {{
            width: 100%;
            height: 100%;
            border: none;
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

        @media(max-width: 550px) {{
            #video iframe {{
                height: 230px;
            }}
        }}

        .propaganda {{
            margin-top: 40px;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            padding-bottom: 40px;
        }}

        .propaganda button {{
            background-color: red;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 12px 18px;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.2s;
        }}

        .propaganda button:hover {{
            background-color: #cc0000;
            transform: scale(1.05);
        }}
    </style>

    <script>
        function go(url) {{
            window.location.href = url;
        }}
    </script>
</head>
<body>

    <h1>{titulo}</h1>
    {h2_html}

    <div class="propaganda2">
        <iframe src="https://produto-63y.pages.dev/oportunidade" scrolling="no" frameborder="0"></iframe>
    </div>
    

    <div id="video">
        <iframe 
            src="{video_url}"
            title="YouTube video player"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen>
        </iframe>
         <div class="propaganda">
        <button onclick="go('https://produto-63y.pages.dev/facebookgrupo')">
        GRUPO DE FACEBOOK</button>
        
        <button onclick="go('https://www.instagram.com/geocredibnkvitoria/')">CRÉDITO PESSOAL</button>

        <button onclick="go('https://br.pinterest.com/internet6g/')">CONFIRA ESSA OPORTUNIDADE</button>

        <button onclick="go('https://produto-63y.pages.dev/guarapari')">APARTAMENTO EM GUARAPARI TEMPORADA PRAIA DO MORRO</button>
        
        </div>
        
    </div>

    <div class="propaganda">

        <button onclick="go('https://www.airbnb.com.br/r/saibvictore?s=6&t=061n0g')">
            QUERO COMEÇAR NO AIRBNB
        </button>

        <button onclick="go('https://produto-63y.pages.dev/vps')">
            VPS RÁPIDO E SEGURO PARA PROJETOS
        </button>

        <button onclick="go('https://sites.google.com/view/recomendao-do-dia/oportunidade?authuser=1')">
            CONFIRA ESSA OPORTUNIDADE
        </button>

        <button onclick="go('https://vendaschamada.blogspot.com/')">
            OPA! TEM OFERTA AQUI
        </button>

        <button onclick="go('https://recomendadodia23.blogspot.com/')">
        OPAAAAAAA VAMOS CONFERIR ESSAS OFERTAS?
        </button>

    </div>

</body>
</html>
'''

desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
nome_arquivo = 'pagina.html'
juntar = os.path.join(desktop, nome_arquivo)

with open(juntar, 'w', encoding='utf-8') as file:
    file.write(html)

print('ok página criada com sucesso...')
