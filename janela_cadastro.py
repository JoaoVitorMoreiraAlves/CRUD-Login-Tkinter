from tkinter import *
import mysql.connector

def janela_cadastro():
    janela_cadastro = Tk()
    janela_cadastro.geometry("600x450")
    janela_cadastro.resizable(width=False, height=False)
    janela_cadastro.title("Cadastro")

    #Função

    def cadastra():
        #Função para conferir se as senhas estão certas e todos os campos preenchidos
        email = e_email.get()
        senha = e_senha.get()
        senha2 = e_senha2.get()

        if senha != senha2:
            l_resultado["text"] = "As Senhas são Diferentes"
            e_senha.delete(0, END)
            e_senha2.delete(0, END)
        else:
            if senha == "" or email == "":
                l_resultado["text"] = "Preencha todos os campos!!"
                e_senha.delete(0, END)
                e_senha2.delete(0, END)
            else:
                if confere(email):
                    l_resultado["text"] = "Parabéns Você se CADASTROU"
                    insere(email, senha)
                    e_senha.delete(0, END)
                    e_senha2.delete(0, END)
                    e_email.delete(0, END)
                elif not confere(email):
                    l_resultado["text"] = "Esse Email já existe!!!"
            
    def insere(email,senha):
        #Função para inserir o novo cadastro no banco de dados
        con = mysql.connector.connect(
        host='localhost', 
        user='root', 
        password='07022003j123',
        database='usuarios'
        )
        cursor = con.cursor()
        cursor.execute(f"INSERT INTO tbl_usuarios(email,senha) VALUES('{email}', '{senha}')")
        con.commit()
        cursor.close()
        con.close()

    def confere(email):
        #Função que vai testar se o email informado não possui nenhum outro ja cadastrado e retorna False caso tenha algum outro email
        #E Verdadeiro se não existir outro email ja cadastrado
        con = mysql.connector.connect(
        host='localhost', 
        user='root', 
        password='07022003j123',
        database='usuarios'
        )

        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS usuarios.tbl_usuarios (email VARCHAR(50) NOT NULL PRIMARY KEY, senha VARCHAR(50) NOT NULL);")
        cursor.execute("SELECT email FROM tbl_usuarios")
        meuresultado = cursor.fetchall()

        aux = str(email)

        for i in range(0, len(meuresultado)):
            if aux == meuresultado[i][0]:
                return False
        return True


    #Frame e Label de Cima
    frame_cima = Frame(janela_cadastro,width=600, height=100, bg="#FFFFFF")
    frame_cima.grid(row=0, column=0)


    l_cima = Label(frame_cima, text="Realizar Cadastro de Usuário", font="Arial 16 bold", bg="#FFFFFF")
    l_cima.place(x=160, y=55)




    # Frame baixo
    frame_baixo = Frame(janela_cadastro, width=600, height=350, bg="#FFFFFF")
    frame_baixo.grid(row=1, column=0)



    #Label e Entry do email

    l_email = Label(frame_baixo, text="E-Mail:", font="Arial 12 bold", bg="#FFFFFF")
    l_email.place(x=100, y=80)

    e_email = Entry(frame_baixo, width=30, relief=SOLID)
    e_email.place(x=290, y=82)


    #Label e Entry da Senha

    l_senha = Label(frame_baixo, text="Senha:", font="Arial 12 bold", bg="#FFFFFF",)
    l_senha.place(x=98, y=120)

    e_senha = Entry(frame_baixo, width=30, relief=SOLID,  textvariable='',show="*")
    e_senha.place(x=290, y=122)


    #Label e Entry da Senha de Confirmação

    l_senha2 = Label(frame_baixo, text="Confirmação da Senha:", font="Arial 12 bold", bg="#FFFFFF")
    l_senha2.place(x=98, y=165)

    e_senha2 = Entry(frame_baixo, width=30, relief=SOLID,  textvariable='',show="*")
    e_senha2.place(x=290, y=168)


    l_resultado = Label(frame_baixo, text=" ", bg="#FFFFFF", fg="RED", font="Arial 14 bold")
    l_resultado.place(x=170, y=220)



    #Botão Para Realizar Cadastramento
    b_cadastramento = Button(frame_baixo, text="Realizar Cadastro", width=50, height=2,
                    bg="#363636", fg="#FFFFFF", command=cadastra)
    b_cadastramento.place(x=110, y=250)

    b_sair = Button(frame_baixo, text="Sair", width=10, height=2,
                    bg="#363636", fg="#FFFFFF", command=janela_cadastro.destroy)
    b_sair.place(x=230, y=300)


    janela_cadastro.mainloop()

if __name__ == "__main__":
    janela_cadastro()