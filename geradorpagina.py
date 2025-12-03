# ==============================
#  GERADOR DE PÁGINA HTML
#  Modelo automático igual ao que você usa
# ==============================

titulo = input("Digite o título do vídeo: ")
video_url = input("Cole a URL embed do vídeo (ex: https://www.youtube.com/embed/XXXX): ")

html = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{titulo}</title>

    <style>
        body {{
            background-color: black;
            margin: 0;
            padding: 0;
            color: white;
            font-family: Arial, sans-serif;

            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 25px;
        }}

        #video {{
            width: 90%;
            max-width: 600px;
            padding: 20px;
            background-color: red;
            border-radius: 12px;
            text-align: center;
        }}

        #video iframe {{
            width: 100%;
            height: 250px;
            border: none;
            border-radius: 12px;
        }}

        #propaganda {{
            width: 90%;
            max-width: 600px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}

        #propaganda iframe {{
            width: 100%;
            height: 200px;
            border: none;
            border-radius: 12px;
        }}

        #propaganda button {{
            background-color: red;
            color: white;
            padding: 20px;
            border-radius: 12px;
            border: none;
            font-size: 20px;
            cursor: pointer;
        }}

        @media(max-width: 550px){{
            #video iframe {{
                height: 180px;
            }}
        }}
    </style>
</head>

<body>

    <h1 style="color:white; text-align:center;">{titulo}</h1>

    <div id="propaganda">
        <iframe 
            loading="lazy"
            src="https://produto-63y.pages.dev/oportunidade"
            title="Anúncio Fixo Responsivo">
        </iframe>

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
    </div>

    <div id="video">
        <iframe 
            src="{video_url}"
            allowfullscreen>
        </iframe>
    </div>

    <script>
        function go(url){{
            window.location.href = url;
        }}
    </script>

</body>
</html>
"""

with open("pagina_pronta.html", "w", encoding="utf-8") as file:
    file.write(html)

print("\n🔥 Página criada com sucesso: pagina_pronta.html")


<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Video com Oportunidades</title>

    <style>
        body {
            background-color: black;
            margin: 0;
            padding: 0;
            color: white;
            font-family: Arial, sans-serif;

            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 25px;
        }

        /* Caixinha do vídeo */
        #video {
            width: 90%;
            max-width: 600px;
            padding: 20px;
            background-color: red;
            border-radius: 12px;
            text-align: center;
        }

        #video iframe {
            width: 100%;
            height: 250px;
            border: none;
            border-radius: 12px;
        }

        /* Bloco de propaganda */
        #propaganda {
            width: 90%;
            max-width: 600px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        #propaganda iframe {
            width: 100%;
            height: 200px;
            border: none;
            border-radius: 12px;
        }

        #propaganda button {
            background-color: red;
            color: white;
            padding: 20px;
            border-radius: 12px;
            border: none;
            font-size: 20px;
            cursor: pointer;
        }

        /* Responsividade */
        @media(max-width: 550px){
            #video iframe {
                height: 180px;
            }
        }
    </style>
</head>

<body>

    <!-- PROPAGANDA TOPO -->
    <div id="propaganda">
        <iframe 
            loading="lazy"
            src="https://produto-63y.pages.dev/oportunidade"
            title="Anúncio Fixo Responsivo">
        </iframe>

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
    </div>

    <!-- VÍDEO PRINCIPAL -->
    <div id="video">
        <iframe 
            src="https://www.youtube.com/embed/C6lS9w-XkFo?si=PpOT0m30R1mcAKhy"
            allowfullscreen>
        </iframe>
    </div>

    <script>
        function go(url){
            window.location.href = url;
        }
    </script>

</body>
</html>

