
texto='''''
O Conhecimento do nome das letras e a sua relação com o desenvolvimento da escrita: evidência de adultos iletrados
'''
transforma=texto.split('\n')

texto=''
for x in transforma:
    texto+=f'<p>{x.strip()}</p>'
print(texto)
