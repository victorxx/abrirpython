import pyautogui
import time

time.sleep(2)  # tempo pra preparar a tela
imagem=r'C:\Users\vitor\Desktop\compartilhar.png'
try:
    # tenta localizar a imagem
    imagem = pyautogui.locateOnScreen(f'{imagem}', confidence=0.8)

    if imagem:
        print("Imagem encontrada!")
        pyautogui.click(imagem)  # clica na posição encontrada
    else:
        print("Imagem não encontrada.")
        
except pyautogui.ImageNotFoundException:
    print("Imagem não encontrada (exceção capturada).")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
