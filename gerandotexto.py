conteudo=[

]
print('Digite a sua frase escreva fim para o programa finalizar...')
while True:
    linha=input()
    if linha.lower()=='fim':
        break
    conteudo.append(linha)
    for x in conteudo:
        print(x+'opaaa')

    


print('finalizado....')
