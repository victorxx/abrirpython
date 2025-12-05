import os


arquivo='pagina.html'
desktop=os.path.join(os.path.expanduser('~'),'Desktop')
juntar=os.path.join(desktop,arquivo)
if not os.path.exists(juntar):
    print('não existe')
else:
    print('existe sim')
