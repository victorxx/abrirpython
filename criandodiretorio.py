import os



desktop=os.path.join(os.path.expanduser('~'),'Desktop','pasta','ok')

if os.path.exists(desktop):
    print('ok o caminho ele existe...')
else:
    print('ok o caminho não existe vamos criar agora')
    os.makedirs(desktop)
    print('criado com sucesso...')
