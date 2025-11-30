import unicodedata


texto='primeiro texto mãe'
limpo=unicodedata.normalize('NFD',texto)
limpinho=''.join(c for c in limpo if unicodedata.category(c)!='Mn')
print(limpinho)
print('limpo')
