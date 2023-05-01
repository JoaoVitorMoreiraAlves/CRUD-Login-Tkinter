from tkinter import *
from janela_cadastro import *
import janela_perfil
import mysql.connector
import excluir_conta
import atualiza_perfil

def main():

    janela_login = Tk()
    janela_login.geometry("600x450")
    janela_login.resizable(width=False, height=False)
    janela_login.title("Login")
    janela_login.configure(bg="#FFFFFF")



    #Parte de Cima do Login 

    frame_cima = Frame(janela_login,width=600, height=100, bg="#FFFFFF")
    frame_cima.grid(row=0, column=0)


    l_cima = Label(frame_cima, text="Entre com o Login", font="Arial 16 bold", bg="#FFFFFF")
    l_cima.place(x=210, y=55)



    #Parte de Baixo

    frame_baixo = Frame(janela_login, width=600, height=350, bg="#FFFFFF")
    frame_baixo.grid(row=1, column=0)


    #Label e Entry do email

    l_email = Label(frame_baixo, text="E-Mail:", font="Arial 12 bold", bg="#FFFFFF")
    l_email.place(x=100, y=80)

    global e_email 
    e_email = Entry(frame_baixo, width=30, relief=SOLID)
    e_email.place(x=180, y=82)




    #Label e Entry da Senha

    l_senha = Label(frame_baixo, text="Senha:", font="Arial 12 bold", bg="#FFFFFF")
    l_senha.place(x=98, y=120)

    global e_senha
    e_senha = Entry(frame_baixo,width=30, relief=SOLID, textvariable='',show="*")
    e_senha.place(x=180, y=122)


    #Label do resultado
    global l_resultado
    l_resultado = Label(frame_baixo, text="Por Favor Informe Senha e Email", bg="#FFFFFF", fg="RED", font="Arial 14 bold")
    l_resultado.place(x=110, y=160)


    #Botão de Sair
    b_sair = Button(frame_baixo, text="Sair", width=50, height=2, command=janela_login.destroy,
                            bg="#363636", fg="#FFFFFF")
    b_sair.place(x=110, y=200)

    #Botões de login e cadastramento
    b_login = Button(frame_baixo, text="Login", width=50, height=2, command=login,
                            bg="#363636", fg="#FFFFFF")
    b_login.place(x=110, y=250)



    b_cadastra = Button(frame_baixo, text="Cadastrar", width=50, height=2, command=janela_cadastro,
                            bg="#363636", fg="#FFFFFF")
    b_cadastra.place(x=110, y=300)


    janela_login.mainloop()



#lógica do Login
def login():
    email = e_email.get()
    senha = e_senha.get()

    meubd = mysql.connector.connect(
        host='localhost', 
        user='root', 
        password='07022003j123',
        database='usuarios'
    )
    cursor = meubd.cursor()
    #Caso a tabela não exista criar ela
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios.tbl_usuarios (email VARCHAR(50) NOT NULL PRIMARY KEY, senha VARCHAR(50) NOT NULL);")
    #Coletar os emails e senhas que estão na lista
    cursor.execute("SELECT * FROM tbl_usuarios")
    meuresultado = cursor.fetchall()
    tentativa = (email, senha)

    if tentativa in meuresultado: #Caso o email e senha informado esteja no banco de dados ele inicia a tela de perfil
        excluir_conta.email_importado= e_email.get()
        atualiza_perfil.email_senha_importado = (e_email.get(), e_senha.get())
        e_senha.delete(0, END)
        e_email.delete(0, END)
        janela_perfil.janela_perfil()
    else:
        if email == "" and senha == "":
            l_resultado["text"] = "Por Favor Informe Email e Senha para Login"
        else:
            l_resultado["text"] = "Login/Senha Errado insira novamente"
            e_senha.delete(0, END)
            e_email.delete(0, END)
    cursor.close()
    meubd.close()

if __name__ == '__main__':
    main()