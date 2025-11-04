from flask import Flask,request,render_template

app=Flask(__name__)


@app.route('/')
def enviar():
    return """""
    <form method="POST" action="/pagina">
    nome:<input type="text" name="nome" required>
    curso:<input type="text" name="curso" required>
    <button type="submit">enviar</button>
    </form>
    """
@app.route('/pagina', methods=['GET','POST'])
def inicio():
    mensagem=""
    if request.method=='POST':
        nome=request.form['nome']
        curso=request.form['curso']
        mensagem=f'Aluno{nome} do curso{curso}'
        return mensagem
    
app.run(debug=True)
