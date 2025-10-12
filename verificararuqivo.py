from flask import Flask
import os



app=Flask(__name__)
@app.route('/')
def iniciar():
    desktop=os.path.join(os.path.expanduser('~'),'Desktop','pasta')
    arquivos=[f for f in os.listdir(desktop)if f.endswith('.txt')]
    if not arquivos:
        return 'não temos arquivos'
    else:
        return 'temos arquivo sim'
    

app.run(debug=True)
