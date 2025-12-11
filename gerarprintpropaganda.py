import os

titulo = input('Entrada do título: ')
conteudo = input('Entrada do conteúdo: ')

# Dividindo o conteúdo em parágrafos
paragrafos = [f'<p>{p.strip()}</p>' for p in conteudo.split('\n') if p.strip()]
html_paragrafos = '\n'.join(paragrafos)

modelo = f'''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo}</title>
<style>
body {{
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}}

header {{
    background-color: #004080;
    color: white;
    padding: 20px;
    text-align: center;
}}

.container {{
    display: flex;
    flex-direction: row;
    max-width: 1200px;
    margin: 20px auto;
    gap: 20px;
}}

.content {{
    flex: 3;
    background: white;
    padding: 20px;
    border-radius: 8px;
}}

.ad {{
    flex: 1;
    background-color: #ffcc00;
    padding: 20px;
    text-align: center;
    border-radius: 8px;
    font-weight: bold;
    font-size: 18px;
}}

h1 {{
    color: #004080;
}}

p {{
    margin-bottom: 15px;
}}

@media (max-width: 768px) {{
    .container {{
        flex-direction: column;
    }}

    .ad {{
        margin-top: 20px;
    }}
}}
</style>
</head>
<body>

<header>
    <h1>{titulo}</h1>
</header>

<div class="container">
    <div class="content">
        {html_paragrafos}
    </div>

    <!-- Bloco de anúncio com scale 1.4 -->
    <div class="ad" style="transform: scale(1.4);">
       🚗 Proteja seu carro agora!<br>
       Seguro Auto rápido, confiável e sob medida para você. Ligue já: (027) 99949-7001 e garanta tranquilidade no trânsito.
    </div>
</div>

</body>
</html>
'''

# Salvar arquivo na área de trabalho
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
arquivo = os.path.join(desktop, 'pagina.html')

with open(arquivo, 'w', encoding='utf-8') as f:
    f.write(modelo)

print('Gerado com sucesso na área de trabalho!')
