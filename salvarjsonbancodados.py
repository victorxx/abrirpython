import mysql.connector
import json
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.youtube.com/')
    page.wait_for_load_state('load')
    cookies=page.context.cookies()
    cookie_j=json.dumps(cookies)

    conexao=mysql.connector.connect(
        host='localhost',
        user='vitor',
        password='12345',
        database='novo'
        
    )
    if conexao.is_connected():
        cursor=conexao.cursor()

        cursor.callproc('co',(cookie_j,))
        conexao.commit()
        conexao.close()
        print('cookies salvos com sucesso...')


create table if not exists cookie(
id int primary key auto_increment,
cookies json
);
set sqL_safe_updates=0;
delimiter //
create procedure co(
in p json
)
begin
insert into cookie(cookies)values(p);
end//
select * from cookie;
