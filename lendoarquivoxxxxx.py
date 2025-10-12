from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def iniciar():
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop', 'pasta')
    arquivos = [f for f in os.listdir(desktop) if f.endswith('.txt')]

    if not arquivos:
        return 'não temos arquivos'

    conteudo = []

    for x in range(min(5,len(arquivos))):
        completo=os.path.join(desktop,arquivos[x])
        with open(completo,'r',encoding='utf-8') as file:
            lendo=file.read()
            restringir=lendo[:300]
            texto=''.join(restringir)
            conteudo.append(texto)
    resultado='<br>'.join(conteudo)
    return resultado

app.run(debug=True)
    
