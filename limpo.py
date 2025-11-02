
import os
desktop=os.path.join(os.path.expanduser('~'),'Desktop')
completo=[f for f in os.listdir(desktop)if f.endswith('.txt')]
for x in completo:
    mudar=x.replace('.txt','')
    juntar=os.path.join(desktop,mudar)
    print(juntar)
