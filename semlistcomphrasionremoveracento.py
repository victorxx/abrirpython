import unicodedata


texto='olá'

texto_normalizado=unicodedata.normalize('NFD',texto)
resultado=''
for c in texto_normalizado:
    if unicodedata.category(c) !='Mn':
        resultado+=c
print(resultado)
