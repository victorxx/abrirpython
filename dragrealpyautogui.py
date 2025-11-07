import pyautogui
import time
try:
        # nome da imagem que você quer localizar
        imagem = r'C:\Users\vitor\Desktop\SETOR.png'
        print('inicio do programa....')

        time.sleep(4)  # tempo pra você abrir a tela

        # procura a imagem na tela (usa OpenCV pra "confidence")
        local = pyautogui.locateOnScreen(imagem, confidence=0.8)

        if local:
              pyautogui.moveTo(local)
              time.sleep(3)
              pyautogui.dragRel(200,0)
              print('movido até o local')
   

 
        else:
            print("Imagem não encontrada.")

except pyautogui.ImageNotFoundException:
     print('ok deu algo errado')
