from flask import Flask

app=Flask(__name__)

@app.route('/')
def inicio():
    return '<a href="pagina/1">acessar</a>'

@app.route('/pagina/<ok>')
def rota(ok):
    if ok=='1':
        return 'ok você está página 1'


app.run(debug=True)
