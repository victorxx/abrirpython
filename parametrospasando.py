from flask import Flask

app=Flask(__name__)
@app.route('/')
@app.route('/<ok>')
def inicio(ok=None):
    if ok:
        return 'o dado foi passado agora podemos continuar'
    return 'não teve o dados não podemos continuar'
app.run(debug=True)
