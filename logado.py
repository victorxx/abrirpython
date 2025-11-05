from flask import Flask,redirect,render_template,render_template_string,request
import time
import os


app=Flask(__name__)
@app.route('/')
def inicio():
    return """"
    
 <!DOCTYPE html>
<html lang="pt-br">
    <head>
        <style>
            body{
                background-color: black;
                padding:20px;
            }
            form{
                width:100%;
                text-align: center;
                padding:20px;
                color:white;
                height: 20px;
            }
            form input{
                height: 120px;
            }
            form button{
                width:100px;
                height: 100px;
                border-radius: 12px;
            }
            @media(max-width:550px){
                form button{
                    width:50px;
                    height: 50px;
                }
            }
        </style>
    </head>
    <body>
    <div id='mostrar'>
        <form method="post" action="/pagina">
            <input id="nome" name="nome">
            <input id="senha" name="senha">
            <button type="submit">ok vai</button>
        </form>
        </div>
               <script>
let cookies=document.cookie.split(';');
for(let i=0;i<cookies.length;i++){
    let cookie=cookies[i].trim();
    if(cookie.startsWith('meu=vi')){
        document.getElementById('mostrar').style.display='none';
        alert('ja estamos logado');
    }
}
       </script>
    </body>
</html>   
    """
@app.route('/pagina',methods=['POST'])
def pagina():
    nome=request.form['nome']
    senha=request.form['senha']
    if nome=='victor' and senha =='123':
        return """
        ESTAMOS LOGADO
 <script>
        let data=new Date() ;
        data.setTime(data.getTime()+24*60*60*10000);
        let expires='expires='+data.toUTCString()   ;
        document.cookie='meu=vi;' +expires+';path=/' ;
           
        </script>
"""
app.run(debug=True)
