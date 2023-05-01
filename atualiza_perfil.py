from tkinter import *
import mysql.connector
email_senha_importado = tuple()

def mandando():
    #Função para enviar a nova senha do usuário
    con = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='07022003j123',
    database='usuarios'
    )
    cursor = con.cursor()
    email = email_senha_importado[0]
    senha = str(e_senha_nova.get())
    cursor.execute(f"UPDATE tbl_usuarios SET senha = {senha} WHERE email = {email};")
    con.commit()
    cursor.close()
    con.close()

def atualiza():
    #Função para conferir se a nova senha está correta e se a senha anterior foi digitada corretamente
    if e_senha_nova.get() != e_senha_nova2.get():
            l_resultado["text"] = "As Senhas são Diferentes"
            e_senha_nova.delete(0, END)
            e_senha_nova2.delete(0, END)
    else:
        if e_senha_nova.get() == "" or e_senha_antiga.get() == "":
            l_resultado["text"] = "Preencha todos os preenchidos"
            e_senha_nova.delete(0, END)
            e_senha_nova2.delete(0, END)
        elif e_senha_antiga.get() != email_senha_importado[1]:
            l_resultado["text"] = "Senha Atual está errada!"
            e_senha_nova.delete(0, END)
            e_senha_nova2.delete(0, END)
        else:
            mandando()
            l_resultado["text"] = "Senha Alterada com sucesso"


def atualiza_perfil():
    janela_perfil = Tk()
    janela_perfil.geometry("600x450")
    janela_perfil.resizable(width=False, height=False)
    janela_perfil.title("Atualizar Conta")


    

    #Divindo frames
    frame_cima = Frame(janela_perfil,width=600, height=100, bg="#FFFFFF")
    frame_cima.grid(row=0, column=0)

    frame_baixo = Frame(janela_perfil, width=600, height=350, bg="#FFFFFF")
    frame_baixo.grid(row=1, column=0)

    #Labels
    l_titulo = Label(frame_cima, text="Atualizando Senha", font="Arial 16 bold", bg="#FFFFFF")
    l_titulo.place(x=200, y=70)

    #label + entry senha antiga
    global e_senha_antiga
    l_senha_antiga = Label(frame_baixo, text="Senha Antiga:", font="Arial 12 bold",
                           bg="#FFFFFF")
    l_senha_antiga.place(x=50, y=50)

    e_senha_antiga = Entry(frame_baixo, width=30, relief=SOLID)
    e_senha_antiga.place(x=300,y=55)


    #label + entry senha nova
    global e_senha_nova
    l_senha_nova = Label(frame_baixo, text="Senha Nova:", font="Arial 12 bold",
                           bg="#FFFFFF")
    l_senha_nova.place(x=50, y=90)

    e_senha_nova = Entry(frame_baixo, width=30, relief=SOLID, textvariable="", show="*")
    e_senha_nova.place(x=300,y=95)


    #label + entry senha nova confirmação
    global e_senha_nova2
    l_senha_nova2 = Label(frame_baixo, text="Confirmação da Senha Nova:", font="Arial 12 bold",
                           bg="#FFFFFF")
    l_senha_nova2.place(x=50, y=130)

    e_senha_nova2 = Entry(frame_baixo, width=30, relief=SOLID, textvariable="", show="*")
    e_senha_nova2.place(x=300,y=135)


    #Label
    global l_resultado
    l_resultado = Label(frame_baixo, textvariable="", bg="#FFFFFF", font="Arial 16 bold", fg="RED")
    l_resultado.place(x=170, y=190)


    #Botão de Sair
    b_sair = Button(frame_baixo, text="Atualizar", width=50, height=2, command=atualiza,
                            bg="#363636", fg="#FFFFFF")
    b_sair.place(x=110, y=230)


    #Botões de login e cadastramento
    b_login = Button(frame_baixo, text="Sair", width=50, height=2, command=janela_perfil.destroy,
                            bg="#363636", fg="#FFFFFF")
    b_login.place(x=110, y=280)



    janela_perfil.mainloop()