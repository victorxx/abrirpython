from flask import Flask,request,render_template_string,render_template
import os
import time


app=Flask(__name__)
@app.route('/')
def inicio():
    return """
<!DOCTYPE html>
<html lang="pt-br">
    <head>
    </head>
    <body>
        <form action="/upload" method="post" enctype="multipart/form-data">
            arquivo:<input type="file" name="arquivo">
            <br>
            <br>
            <br>
            <button type="submit">enviar</button>
        </form>
    </body>
</html>
"""
@app.route('/upload',methods=['post'])
def upload():
    caminho=os.path.join(os.path.expanduser('~'),'Desktop')
    arquivo=request.files['arquivo']
    if arquivo.filename=="":
        return "vazio"
    juntar=os.path.join(caminho,arquivo.filename)
    arquivo.save(juntar)
    return 'salvo com sucesso'
   
app.run(debug=True)

   
