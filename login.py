import tkinter as tk
import customtkinter as ctk

def tela_login():
    cor_botao= "#ED2224"
    cor_botao_hover='#FC3441'
    # Criar janela de login
    login = ctk.CTk()
    login.title('Login Satoshi Garage')

    # Carregar imagem
    img = tk.PhotoImage(file='./img/logosf.png')

    # Exibir imagem
    label_img = tk.Label(master=login, image=img)
    label_img.image = img  # Manter uma referência à imagem para evitar que seja coletada pelo garbage collector
    label_img.grid(column=1,row=1,padx=20,pady=20)

    #Criando o frame(como se fosse uma div em HTML)
    frame_login = ctk.CTkFrame(master=login, width=400 , height=400)
    frame_login.grid(column=2,row=1,padx=20,pady=20)

    #Componentes do frame
    label_title = ctk.CTkLabel(master=frame_login, text='LOGIN SATOSHI GARAGE', font=("Arial", 15, "bold"))
    label_title.grid(column=1,row=1,padx=20,pady=20)
    #Login
    input1=ctk.CTkEntry(master=frame_login,placeholder_text='Nome de usuário',width=300,font=("Arial", 15))
    input1.grid(column=1,row=2,padx=20,pady=20)

    #senha
    input2=ctk.CTkEntry(master=frame_login,placeholder_text='Senha',width=300,font=("Arial", 15),show="*")
    input2.grid(column=1,row=3,padx=20,pady=20)

    #botao de logar
    botao_logar = ctk.CTkButton(master=frame_login, text='LOGIN', width=300,fg_color=cor_botao, hover_color=cor_botao_hover )
    botao_logar.grid(column=1,row=4,padx=20,pady=20)

    #parte de cadastro
    label_cadastro=ctk.CTkLabel(master=frame_login,text='Caso não tenha cadastro:',font=('Arial',15))
    label_cadastro.grid(column=1,row=5)
    botao_cadastro=ctk.CTkButton(master=frame_login,text='CADASTRAR',font=('Arial',15),width=300,fg_color=cor_botao, hover_color=cor_botao_hover ,command=login_cadastrar)
    botao_cadastro.grid(column=1,row=6,padx=20,pady=20)


    # Exibir janela
    login.mainloop()

def login_cadastrar():

tela_login()