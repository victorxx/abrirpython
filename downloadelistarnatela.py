from flask import Flask
import requests
import os


app=Flask(__name__)
@app.route('/')
def iniciar():
    urljapa='https://i.pinimg.com/280x280_RS/ea/07/72/ea0772f3ce896b4ac5aa71e3c50f4654.jpg'
    desktop=os.path.join(os.path.expanduser('~'),'Desktop')

    imagem='japinha.png'

    caminho_imagem=os.path.join(desktop,imagem)

    puxar=requests.get(urljapa)

    if puxar.status_code==200:
        with open(caminho_imagem,'wb') as file:
            file.write(puxar.content)
            print('imagem salva com sucesso')
    return f'<p>imagem salva no desktop  <br>{caminho_imagem}</p>'

app.run(debug=True)
