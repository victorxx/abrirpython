conteudo=[]


print('entrada o conteúdo digite fim para finalizar...')
while True:
    linha=input()
    if linha.lower()=='fim':
        break
    conteudo.append(linha)

for p in conteudo:
    print(p.strip())
