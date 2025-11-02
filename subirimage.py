import time
from playwright.sync_api import sync_playwright
import time
import os


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('file:///C:/Users/vitor/Desktop/Imagens_Baixadas/index.html')
    page.wait_for_load_state('load')
    primeiro=page.get_by_role('textbox').nth(0).fill('escrito ok')
    page.set_input_files('input[type="file"]', r'C:\Users\vitor\Desktop\pngtree-abstract-cloudy-background-beautiful-natural-streaks-of-sky-and-clouds-red-image_15684333.jpg')
    
    time.sleep(20)
    browser.close()
