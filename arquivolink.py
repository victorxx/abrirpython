from flask import Flask 
import os

app = Flask(__name__)

@app.route('/')
def iniciar():
    ok = os.path.join(os.path.expanduser('~'), 'Desktop')
    foi = [f for f in os.listdir(ok) if f.endswith('.txt')]

    if not foi:
        return 'Nenhum arquivo .txt encontrado'

    completo = [os.path.join(ok, f) for f in foi]
    resultado = ''
    
    for x in completo:
        # Cria um link HTML com href para o caminho completo
        resultado += f'<a href="file://{x}">{x}</a><br>'
    
    return resultado

if __name__ == '__main__':
    app.run(debug=True)
