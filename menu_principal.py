import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

cor_0 = '#FC3441'
cor_1 = '#ea2828'
cor_2 = '#050505'
cor_3 = '#747474'
cor_4 = '#7c7c7c'
cor_5 = '#d9c6c6'

def janela_jogo_inicio():
    janela_jogo = ctk.CTk()
    janela_jogo.title('SATOSHI GARAGE')
    janela_jogo.minsize(300, 650)
    menu_frame(janela_jogo)
    geral_frame(janela_jogo)
    janela_jogo.mainloop()

def menu_frame(master):
    frame_menu = ctk.CTkFrame(master=master, fg_color=cor_1)
    frame_menu.grid(row=1, column=1, sticky="nsew")  # Adicionando sticky para expandir na vertical

    # Configurar a expansão dinâmica da linha que contém o frame do menu
    master.rowconfigure(1, weight=1)

    botao_menu(frame_menu, 1, 1, converter_img('./img/icones/garage.png'), garagem)
    botao_menu(frame_menu, 2, 1, converter_img('./img/icones/up.png'), upgrade)
    botao_menu(frame_menu, 3, 1, converter_img('./img/icones/sair.png'), lambda:fechar_jogo(master))

    # Configurar a expansão dinâmica dos elementos do frame_menu
    frame_menu.columnconfigure(0, weight=1)  # Botões se expandem na horizontal
    frame_menu.rowconfigure((0, 1, 2), weight=1)  # Botões se expandem na vertical

def converter_img(endereço):
    # Carregar a imagem usando PIL
    img_pil = Image.open(endereço)
    # Converter a imagem PIL para um formato suportado pelo PhotoImage
    img_botao = ImageTk.PhotoImage(img_pil)
    return img_botao

def botao_menu(master, row, column, img, acao):
    menu_botao = ctk.CTkButton(master=master, image=img, command=acao, fg_color=cor_1, hover_color=cor_0, text='', height=100)  # Ajustando a altura dos botões
    menu_botao.image = img
    menu_botao.grid(row=row, column=column, padx=40, pady=(40, 0), sticky="nsew")  # Aumentando pady para mover os botões para cima

def geral_frame(master):
    frame_geral = ctk.CTkFrame(master=master, fg_color=cor_5)
    frame_geral.grid(row=1, column=2)
    
    titulo_mapa = ctk.CTkLabel(master=frame_geral, text='MAPAS', font=('Arial', 15,'bold'))
    titulo_mapa.grid(row=1, column=2)
    
    dinheiro = ctk.CTkLabel(master=frame_geral, text='R$', font=('Arial', 15))
    dinheiro.grid(row=1, column=3)
    
    mapa_selecionado = tk.IntVar()
    
    mapa(frame_geral, 2, 1, converter_img('./img/icones/cidade.png'), mapa_selecionado, 1)
    mapa(frame_geral, 2, 2, converter_img('./img/icones/campo.png'), mapa_selecionado, 2)
    mapa(frame_geral, 2, 3, converter_img('./img/icones/deserto.png'), mapa_selecionado, 3)
    
    botao_jogar = ctk.CTkButton(master=frame_geral, text='JOGAR', width=100, height=50, font=('Arial', 15), fg_color=cor_2, hover_color=cor_3, text_color='#FFFFFF', command=lambda: iniciar_mapa(mapa_selecionado.get()))
    botao_jogar.grid(row=3, column=1, padx=20, pady=20)
    
    carro_selecionado = ctk.CTkLabel(master=frame_geral, text='CARRO SELECIONADO', font=('Arial', 15))
    carro_selecionado.grid(row=3, column=2, columnspan=2)

def mapa(master, row, column, img, variavel, valor):
    mapa_botao = ctk.CTkButton(master=master, image=img, fg_color=cor_5, hover_color=cor_0,text='', width=20, height=20, command=lambda: variavel.set(valor))
    mapa_botao.grid(row=row, column=column, padx=10,pady=20)


def iniciar_mapa(mapa):
    if mapa == 1:
        print('Mapa 1')
    elif mapa == 2:
        print('Mapa 2')
    elif mapa == 3:
        print('Mapa 3')
    else:
        print('Mapa selecionado inválido')



def garagem():
    print('Lógica da garagem')

def upgrade():
     print('Lógica do Upgrade')

def fechar_jogo(janela):
    janela.destroy()

def lógica_mapa():
    print('Deserto')     


