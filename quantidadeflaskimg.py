import os
from flask import Flask
from playwright.sync_api import sync_playwright


app=Flask(__name__)
@app.route('/')
def iniciar():
   with sync_playwright() as p:
      browser=p.chromium.launch(headless=True)
      page=browser.new_page()
      page.goto('https://br.pinterest.com/uniter1265/garotas-japonesas/')
      page.wait_for_load_state('load')
      img=page.locator('img')
      contagem=img.count()
      return str(contagem)
   
app.run(debug=True)
 
