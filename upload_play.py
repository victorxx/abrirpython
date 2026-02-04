from playwright.sync_api import sync_playwright
import time

arquivo=r"C:\Users\vitor\Downloads\avg_antivirus_free_setup.exe"

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()


    page.goto('http://localhost/teste/index.php')
    page.wait_for_selector("input[type='file']")
    page.click("button[type='submit']")
    print('Upload concluido com sucesso')
    input('Pressione enter pra fechar')
    browser.close()

<?php
if(isset($_FILES['arquivo']))
    {
        $nome=$_FILES['arquivo']['name'];
        $tmp=$_FILES['arquivo']['tmp_name'];
        

        $enviar=__DIR__."/".$nome;
        if(move_uploaded_file($tmp,$enviar))
            {
                echo "<script>alert('ok está enviado')</script>";
            }else{
                echo "<script>alert('não foi possivel')</script>";
            }
        
    }
?>


<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <style>
      body{
        margin:0;
        justify-content: center;
        height: 100vh;
        align-items: center;
        display: flex;
        justify-content: center;
        background-color: black;
      }
      form{
        gap:30px;
        width:660px;
        line-height: 140px;
        font-size: 44px;
        padding:20px;
        background-color: lime;
        border-radius: 12px;
        flex-direction: column;
        align-items: center;
        display: flex;
      }
      input[type="file"]
      {
        width:100%;
        padding:30px;
        font-size: 55px;
        background-color: aqua;
        cursor: pointer;
        border-radius: 12px;
        height: 440px;
        max-width: 660px;
      }button{
        color:red;
        width:100%;
        cursor: pointer;
        max-width: 660px;
        height: 330px;
        border-radius: 12px;
        font-size: 55px;
      }
      button:hover{
        background-color: lime;
        transform:scale(1.03);
      }
    </style>
  </head>
  <body>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="arquivo">
      <button type="submit">GRAVAR</button>
    </form>

  </body>
</html>
