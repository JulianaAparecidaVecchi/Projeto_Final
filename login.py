import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import menu_principal
import json

cor_botao = "#EA2828"
cor_botao_hover = '#FC3441'
dados_arquivo = 'dados_jogadores.json'

def salvar_dados(jogador, filename=dados_arquivo):
    try:
        with open(filename, 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []

    # Verifica se o jogador já existe
    for i, j in enumerate(dados):
        if j['nome'] == jogador['nome']:
            dados[i] = jogador
            break
    else:
        dados.append(jogador)

    with open(filename, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def carregar_dados(filename=dados_arquivo):
    try:
        with open(filename, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def janela_login():
    global frame_login, login, input_nome, input_senha
    login = ctk.CTk()
    login.title('Login Satoshi Garage')

    img = tk.PhotoImage(file='./img/logosf.png')
    label_img = tk.Label(master=login, image=img)
    label_img.image = img
    label_img.grid(column=1, row=1, padx=20, pady=20)

    frame_login = ctk.CTkFrame(master=login, width=400 , height=400)
    frame_login.grid(column=2, row=1, padx=20, pady=20)

    label_title = ctk.CTkLabel(master=frame_login, text='LOGIN SATOSHI GARAGE', font=("Arial", 30, "bold"))
    label_title.grid(column=1, row=1, padx=20, pady=20)
    
    input_nome = ctk.CTkEntry(master=frame_login, placeholder_text='Nome de usuário', width=300, height=50, font=("Arial", 25))
    input_nome.grid(column=1, row=2, padx=20, pady=20)

    input_senha = ctk.CTkEntry(master=frame_login, placeholder_text='Senha', width=300, font=("Arial", 15), show="*")
    input_senha.grid(column=1, row=3, padx=20, pady=20)

    botao_logar = ctk.CTkButton(master=frame_login, text='LOGIN', width=300, fg_color=cor_botao, hover_color=cor_botao_hover, command=login_usuario)
    botao_logar.grid(column=1, row=4, padx=20, pady=20)

    label_cadastro = ctk.CTkLabel(master=frame_login, text='Caso não tenha cadastro:', font=('Arial', 15))
    label_cadastro.grid(column=1, row=5)
    botao_cadastro = ctk.CTkButton(master=frame_login, text='CADASTRAR-SE', font=('Arial', 15), width=300, fg_color=cor_botao, hover_color=cor_botao_hover, command=login_cadastrar)
    botao_cadastro.grid(column=1, row=6, padx=20, pady=20)

    login.mainloop()

def login_usuario():
    nome = input_nome.get()
    senha = input_senha.get()
    dados = carregar_dados()

    for jogador in dados:
        if jogador.get("nome") == nome and jogador.get("senha") == senha:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso")
            login.destroy()  # Fecha a janela de login
            menu_principal.janela_jogo_inicio()  # Abre a janela do jogo principal
            return
    messagebox.showerror("Erro", "Nome do usuário ou senha incorretos.")


def login_cadastrar():
    global input_nome_cadastro, input_senha_cadastro, frame_cadastro

    frame_login.grid_forget()
    
    frame_cadastro = ctk.CTkFrame(master=login, width=400 , height=400)
    frame_cadastro.grid(column=2, row=1, padx=20, pady=20)
    
    label_cadastro = ctk.CTkLabel(master=frame_cadastro, text='CADASTRAR-SE AQUI', font=("Arial", 15, "bold"))
    label_cadastro.grid(column=1, row=1, padx=20, pady=20)

    label_obg1 = ctk.CTkLabel(master=frame_cadastro, text='*Campo obrigatório', font=("Arial", 10, "bold"), text_color=cor_botao_hover)
    label_obg1.grid(column=1, row=2)
    input_nome_cadastro = ctk.CTkEntry(master=frame_cadastro, placeholder_text='Nome de usuário', width=300, font=("Arial", 15))
    input_nome_cadastro.grid(column=1, row=3, padx=20)

    label_obg2 = ctk.CTkLabel(master=frame_cadastro, text='*Campo obrigatório', font=("Arial", 10, "bold"), text_color=cor_botao_hover)
    label_obg2.grid(column=1, row=4)
    input_senha_cadastro = ctk.CTkEntry(master=frame_cadastro, placeholder_text='Senha', width=300, font=("Arial", 15), show="*")
    input_senha_cadastro.grid(column=1, row=5, padx=20)

    botao_cadastrar = ctk.CTkButton(master=frame_cadastro, text='CADASTRAR-SE', font=('Arial', 15), width=300, fg_color=cor_botao, hover_color=cor_botao_hover, command=realizar_cadastro)
    botao_cadastrar.grid(column=1, row=6, padx=20, pady=40)
    
    botao_voltar = ctk.CTkButton(master=frame_cadastro, text='VOLTAR', font=('Arial', 15), width=150, fg_color=cor_botao, hover_color=cor_botao_hover, command=voltar_login)
    botao_voltar.grid(column=1, row=7, pady=10)

def realizar_cadastro():
    nome = input_nome_cadastro.get()
    senha = input_senha_cadastro.get()

    if not nome or not senha:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos")
        return
    
    dados = carregar_dados()

    # Verifica se o nome de usuário já existe
    for jogador in dados:
        if jogador['nome'] == nome:
            messagebox.showerror("erro", "Usuário escrito já existe")
            return

    novo_jogador = {
        "nome": nome,
        "senha": senha,
        "carros_na_garagem": [],
        "dinheiro_no_banco": 0,
    }

    salvar_dados(novo_jogador)
    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso")
    voltar_login()

def voltar_login():
    frame_cadastro.grid_forget()
    frame_login.grid(column=2, row=1, padx=20, pady=20)

janela_login()
