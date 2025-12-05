from bs4 import BeautifulSoup
import os


desktop=os.path.join(os.path.expanduser('~'),'Desktop')
arquivo='pagina.html'
caminho=os.path.join(desktop,arquivo)
with open(caminho,'r',encoding='utf-8') as file:
    conteudo=file.read()

soup=BeautifulSoup(conteudo,'html.parser')
botao=soup.find_all('button')
print(f'total de botao'+str(len(botao)))


if len(botao)>2:
    print('temos sim mais de dois itens na página')
    botao[2].string='rica games é o melhor do mundo'
with open(caminho,'w',encoding='utf-8') as file:
    file.write(soup.prettify())
print('editado o arquivo...')



<!DOCTYPE html>
<html lang="pt-br">
 <head>
  <title>
   BOLA quase INFARTA de *TANTO RIR*
  </title>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <style>
   body {
            background-color: #000;
            color: #fff;
            margin: 0;
            padding: 0;
            font-family: Arial, Helvetica, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        h1 {
            margin-top: 20px;
            font-size: 2rem;
        }

        h2 a {
            color: yellow;
            text-decoration: none;
        }

        h2 a:hover {
            text-decoration: underline;
        }

        .propaganda2 {
            width: 90%;
            max-width: 600px;
            height: 300px;
            margin-top: 20px;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.15);
        }

        .propaganda2 iframe {
            width: 100%;
            height: 100%;
            border: none;
        }

        #video {
            width: 90%;
            max-width: 600px;
            margin-top: 40px;
        }

        #video iframe {
            width: 100%;
            height: 320px;
            border-radius: 12px;
            border: none;
        }

        @media(max-width: 550px) {
            #video iframe {
                height: 230px;
            }
        }

        .propaganda {
            margin-top: 40px;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            padding-bottom: 40px;
        }

        .propaganda button {
            background-color: red;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 12px 18px;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.2s;
        }

        .propaganda button:hover {
            background-color: #cc0000;
            transform: scale(1.05);
        }
  </style>
  <script>
   function go(url) {
            window.location.href = url;
        }
  </script>
 </head>
 <body>
  <h1>
   BOLA quase INFARTA de *TANTO RIR*
  </h1>
  <h2>
   <a href="https://br.pinterest.com/internet6g/">
    CONFIRA ISSO AQUI !
   </a>
  </h2>
  <div class="propaganda2">
   <iframe frameborder="0" scrolling="no" src="https://produto-63y.pages.dev/oportunidade">
   </iframe>
  </div>
  <div class="propaganda">
   <button onlick="go('https://fbs.partners?ibl=837120&amp;ibp=33393839')">
    💹 Comece no Mercado Forex Hoje! 💹
   </button>
   <button onclick="go('https://br.pinterest.com/pin/546835579793959220')">
    🚘 Proteja seu carro hoje mesmo! 🚘
   </button>
  </div>
  <div class="propaganda">
   <button onclick="go('https://www.airbnb.com.br/r/saibvictore?s=6&amp;t=061n0g')">
    rica games é o melhor do mundo
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
  <div id="video">
   <iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" src="https://www.youtube.com/embed/oRAhCn4NinY?si=dFg98KdVRl-VYzDR" title="YouTube video player">
   </iframe>
   <div class="propaganda">
    <button onclick="go('https://produto-63y.pages.dev/facebookgrupo')">
     GRUPO DE FACEBOOK
    </button>
    <button onclick="go('https://produto-63y.pages.dev/pixelart')">
     🎨 Curso de Pixel Art – Comece Hoje! 🎨
    </button>
    <button onclick="go('https://www.instagram.com/geocredibnkvitoria/')">
     CRÉDITO PESSOAL
    </button>
    <button onclick="go('https://br.pinterest.com/internet6g/')">
     CONFIRA ESSA OPORTUNIDADE
    </button>
    <button onclick="go('https://produto-63y.pages.dev/guarapari')">
     APARTAMENTO EM GUARAPARI TEMPORADA PRAIA DO MORRO
    </button>
   </div>
  </div>
 </body>
</html>
