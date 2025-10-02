from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def ola():
    # Caminho para a pasta na área de trabalho
    pasta = os.path.join(os.path.expanduser('~'), 'Desktop/pasta')

    # Verifica se a pasta existe
    if not os.path.exists(pasta):
        return "<p>Pasta não encontrada.</p>"

    # Filtra apenas arquivos .txt
    txt_arquivos = [f for f in os.listdir(pasta) if f.endswith('.txt')]

    # Se não houver arquivos .txt
    if not txt_arquivos:
        return "<p>Nenhum arquivo .txt encontrado.</p>"

    # Cria caminhos completos
    caminhos_completos = [os.path.join(pasta, f) for f in txt_arquivos]

    # Monta o HTML
    lista_html = "<br>".join(caminhos_completos)

    return f"<p>Arquivos .txt encontrados:<br>{lista_html}</p>"

if __name__ == "__main__":
    app.run(debug=True)
