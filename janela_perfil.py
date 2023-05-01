from tkinter import *
import excluir_conta
import atualiza_perfil



def janela_perfil():
    janela_perfil = Tk()
    janela_perfil.geometry("600x450")
    janela_perfil.resizable(width=False, height=False)
    janela_perfil.title("Perfil")



    #Divindo os Frames
    frame_cima = Frame(janela_perfil, width=600, height=100, bg="#FFFFFF")
    frame_cima.grid(row=0, column=0)


    frame_baixo = Frame(janela_perfil, width=600, height=350, bg="#FFFFFF")
    frame_baixo.grid(row=1, column=0)

    #Label do Frame de Cima
    l_cima = Label(frame_cima, text="Bem Vindo ao Seu Perfil\n Você Deseja:", font="Arial 16 bold", bg="#FFFFFF")
    l_cima.place(x=180, y=25)

    #Botão de Deslogar
    b_deslogar = Button(frame_baixo, text="Deslogar", font="Arial 16 bold", bg="#363636",fg="#FFFFFF", command=janela_perfil.destroy)
    b_deslogar.place(x=240, y=20)
    
    #Botão de Atualizar
    b_atualizar = Button(frame_baixo, text="Atualizar senha", font="Arial 16 bold", bg="#363636",fg="#FFFFFF", command=atualiza_perfil.atualiza_perfil)
    b_atualizar.place(x=210, y=130)

    #Botão de Exclusão
    b_excluir = Button(frame_baixo, text="Excluir Conta", font="Arial 16 bold", bg="#363636",fg="#FFFFFF", command=excluir_conta.janela_excluir_conta)
    b_excluir.place(x=220, y=240)


    janela_perfil.mainloop()

if __name__ == "__main__":
    janela_perfil()