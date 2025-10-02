from flask import Flask
import os


app=Flask(__name__)
@app.route('/')
def olar():
    pasta=os.path.join(os.path.expanduser('~'),'Desktop/pasta')
    if not os.path.exists(pasta):
        return"<p>pasta não encontrada</p>"
    txt=[f for f in os.listdir(pasta) if f.endswith('.txt')]
    if not txt:
        return "<p>nehum arquivo encontrado</p>"
    for x in txt:
        completo=os.path.join(pasta,x)
        with open(completo,'r') as file:
            ler=file.read()
            lendo=ler[:300]
        return f"<p>arquivos.txt encontrado<script>document.write('<br>'.repeat(5))</script>{lendo}"
    
  

app.run(debug=True)


    
