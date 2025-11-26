import os


texto='meu texto \n  texto primeiro'

pasta=os.path.join(os.path.expanduser('~'),'Desktop','pasta')

nome='meu.txt'

juntar=os.path.join(pasta,nome)

with open(juntar,'w') as file:
    file.write(texto)
print(f'texto inserido com sucesso...')
with open(juntar,'r') as file:
    primeira_linha=file.readline()
print(primeira_linha)
