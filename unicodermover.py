import unicodedata
stringvelha='olá'
stringnova=''.join(c for c in unicodedata.normalize('NFD',stringvelha) if not unicodedata.combining(c))
print(stringnova)
