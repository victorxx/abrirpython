from flask import Flask


app=Flask(__name__)

@app.route('/')
def rodar():
    return '''<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <style>
            #vermelho{
                background-color:red;
                width:550px;
                display: flex;
                flex-direction: row;
                flex-wrap: wrap;
                height:250px;
                cursor:pointer;
            }
        </style>
    </head>
    <body>
        <div id="vermelho" onclick="ok()">
 
        </div>
        <script>
                let vermelho=document.getElementById('vermelho');
                let posicao=parseInt(getComputedStyle(vermelho).width);
            
            function ok(){
                posicao-=10;
                vermelho.style.width=posicao+'px';

            }
        </script>

    </body>
</html>'''

app.run(debug=True)
