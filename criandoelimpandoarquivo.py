from playwright.sync_api import sync_playwright
import os
desktop=os.path.join(os.path.expanduser('~'),'Desktop')
arquivo='ok.txt'
juntar=os.path.join(desktop,arquivo)

if not os.path.exists(juntar):
    print('arquivo não existe criando')
    open(juntar,'w').close()
else:
    open(juntar,'w').close()
    print('limpando arquivo...')
