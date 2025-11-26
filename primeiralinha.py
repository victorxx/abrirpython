
import os


dados='titulo do meu texto \n texto'
ok=os.path.join(os.path.expanduser('~'),'Desktop','pasta')

os.makedirs(ok,exist_ok=True)

arquivo='meu.txt'

juntar=os.path.join(ok,arquivo)


with open(juntar,'w') as file:
    file.write(dados)


print(f'ok salvo com sucesso...')

with open(juntar,'r') as file:
    primeira_linha=file.readline().strip()
print('primeira linha\n',primeira_linha)
