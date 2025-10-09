from flask import Flask
import os

app=Flask(__name__)
@app.route('/')
def iniciar():
    numeros=[1,2,3,4,5,6]
    foi=[f for f in numeros]
    resultado=''
    
    for x in numeros:
        x=str(x)
        resultado+=x+'<br>'
    return resultado



    

 
app.run(debug=True)
