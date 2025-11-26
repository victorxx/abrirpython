import os

dados='titulo\n primeira linha\n segunda linha\n terceira linha'
desktop=os.path.join(os.path.expanduser('~'),'Desktop','pasta')
os.makedirs(desktop,exist_ok=True)
print('ok ta tudo certo.... a pasta ta ok')

arquivo='meu.txt'

juntar=os.path.join(desktop,arquivo)

with open(juntar,'w') as file:
    file.write(dados)
print(f'dado inserido com sucesso...')


with open(juntar,'r') as file:
    lendo=file.readlines()
    segunda_linha=lendo[3]
    print(segunda_linha)
