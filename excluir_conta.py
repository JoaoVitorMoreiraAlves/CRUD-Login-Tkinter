from tkinter import *
import mysql.connector
import janela_perfil

email_importado = []
def delete():
    #Função para deletar um usuário
    con = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='07022003j123',
    database='usuarios'
    )
    cursor = con.cursor()
    cursor.execute(f"DELETE FROM tbl_usuarios WHERE email = '{email_importado}' ")
    con.commit()
    cursor.close()
    con.close()


def janela_excluir_conta():
    janela_excluir_conta = Tk()
    janela_excluir_conta.geometry("600x450")
    janela_excluir_conta.resizable(width=False, height=False)
    janela_excluir_conta.title("Excluir Conta")

    #Divindo os Frames
    frame_cima = Frame(janela_excluir_conta, width=600, height=100, bg="#FFFFFF")
    frame_cima.grid(row=0, column=0)


    frame_baixo = Frame(janela_excluir_conta, width=600, height=350, bg="#FFFFFF")
    frame_baixo.grid(row=1, column=0)

    #Label do Frame de Cima
    l_cima = Label(frame_cima, text="Deseja mesmo Excluir a sua conta?", font="Arial 16 bold", bg="#FFFFFF")
    l_cima.place(x=130, y=25)

    #Botão de Sair
    b_login = Button(frame_baixo, text="Sim", width=50, height=2, command=lambda: [delete(),janela_excluir_conta.destroy()],
                        bg="#363636", fg="#FFFFFF")
    b_login.place(x=110, y=200)

    #Botões de login e cadastramento
    b_login = Button(frame_baixo, text="Não", width=50, height=2, command=janela_excluir_conta.destroy,
                        bg="#363636", fg="#FFFFFF")
    b_login.place(x=110, y=250)

    janela_excluir_conta.mainloop()

if __name__ == "__main__":
    janela_excluir_conta()