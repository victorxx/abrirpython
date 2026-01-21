
textos=[
    "Bem-vindo à loja virtual",
    "Confira nossas promoções",
    "Visite a loja física mais próxima",
    "Produtos disponíveis online",
    "loja de roupas e acessórios"
]

quantidade=sum(1 for t in textos if 'loja' in t)

print(f'o número de vezes que apareceu o item')
print(quantidade)
