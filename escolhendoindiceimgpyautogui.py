import pyautogui
import time

print('começando')
time.sleep(3)

botao=r'C:\Users\vitor\Desktop\clique.png'

botoes=list(pyautogui.locateAllOnScreen(botao,confidence=0.9))
print(f'quantidade de botões achados {botoes}')
pyautogui.moveTo(botoes[1])
print('clicado')
