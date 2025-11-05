from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <body>
        <form method="post" enctype="multipart/form-data" action="/aceito">
            <input type="file" name="meu">
            <br><br><br><br><br>
            <button type="submit">Enviar</button>
        </form>
    </body>
    </html>
    """

@app.route('/aceito', methods=['POST'])
def pagina():
        
     arquivo=request.files['meu']

     if arquivo.filename=="":
         return 'está vazio'
     
  
    




if __name__ == "__main__":
    app.run(debug=True)
