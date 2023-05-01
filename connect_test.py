#Aprendendo a inserir no banco de dados

import mysql.connector
from main import pega_email

con = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='07022003j123',
    database='usuario'
)

cursor = con.cursor()
a = "joaova1@gmail.com"
b = "123"

def exclui():
    return pega_email('nada')

def insere(email,senha,a):
    con = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='07022003j123',
    database='usuario'
    )

    cursor = con.cursor()
    cursor.execute(f"DELETE FROM tbl_usuarios WHERE email = '{a}' ")

    cursor.execute(f"INSERT INTO tbl_usuarios(email,senha) VALUES('{email}', '{senha}')")
    con.commit()
    cursor.close()
    con.close()

#insere(a,b, 'joao@gmail.com')

a = exclui()

print(a)
con.commit()

cursor.execute("SELECT * FROM tbl_usuarios")

meuresultado = cursor.fetchall()

print(meuresultado)

cursor.close()
con.close()