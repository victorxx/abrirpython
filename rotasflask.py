from flask import Flask
import time

app=Flask(__name__)
@app.route('/<rota>')
def inicio(rota):
    if rota=='1':
        return 'você digitou um'
    if rota=='2':
        return 'você digitou 2'
app.run(debug=True)
