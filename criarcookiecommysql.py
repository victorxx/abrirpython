create table if not exists cl
(
id int primary key auto_increment,
cookie text
);
insert into cl(cookie)values('rodrigo');
select * from cl;
delimiter //
create procedure ok
(
in entrada text
)
begin
insert into cl(cookie)values(entrada);
end//
call ok('rodrigo');
select * from cl;

import mysql.connector
from playwright.sync_api import sync_playwright

# Inicia o Playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Acessa o vídeo do YouTube
    page.goto('https://www.youtube.com/watch?v=AFVqjemLjT4')
    page.wait_for_load_state('load')
    
    # Captura e converte os cookies
    cookies = page.context.cookies()
    transforma = str(cookies)  # Opcional: pode usar json.dumps(cookies) para formato JSON

    # Conecta ao banco de dados MySQL
    conexao = mysql.connector.connect(
        host='localhost',
        user='vitor',
        password='12345',
        database='novo'
    )

    if conexao.is_connected():
        print('Conexão com banco estabelecida.')

        cursor = conexao.cursor()

        # Chama o procedimento armazenado chamado "OK" com um parâmetro
        try:
            cursor.callproc('OK', (transforma,))
            conexao.commit()  # importante se o procedimento faz inserções/alterações
            print('Procedimento armazenado executado com sucesso.')
        except mysql.connector.Error as err:
            print(f"Erro ao executar o procedimento: {err}")
        finally:
            cursor.close()
            conexao.close()

    browser.close()
    print('Finalizado.')
