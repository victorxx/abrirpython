def calcular(faturamento,custo):
    return faturamento-custo

faturamento=int(input('Qual seria o faturamento?'))
custo=int(input('Qual seria o custo?'))
lucro=calcular(faturamento,custo)
print('o lucro é ',custo)
