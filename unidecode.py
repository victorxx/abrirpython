import unicodedata





texto='árvore'
texto=unicodedata.normalize('NFKD',texto)
texto=''.join(c for c in texto if not unicodedata.combining(c))
print(texto)
