import customtkinter as ctk

def criar_janela():
    # Criar a janela principal
    janela = ctk.CTk()
    janela.title("Informações do Carro")

    # Definir o tamanho da janela
    janela.geometry("400x300")

    # Função para ler as informações do carro de um arquivo TXT
    def ler_info_carro():
        try:
            with open('teste.txt', 'r') as arquivo:
                info_carro = [ arquivo.readlines()]
        except FileNotFoundError:
            info_carro = ["Arquivo não encontrado"]
        return info_carro

    # Função para criar e mostrar as informações do carro
    def mostrar_informacoes_carro(frame):
        # Obter as informações do carro
        info_carro = ler_info_carro()

        # Limpar o frame antes de adicionar as informações
        for widget in frame.winfo_children():
            widget.destroy()

        # Exibir as informações do carro no frame
        for i, linha in enumerate(info_carro):
            label = ctk.CTkLabel(frame, text=linha)
            label.grid(row=i, column=0, sticky="w")

    # Criar o frame para as informações do carro
    frame_carro = ctk.CTkFrame(janela)
    frame_carro.pack(pady=20)

    # Mostrar as informações do carro inicialmente
    mostrar_informacoes_carro(frame_carro)

    # Função para mostrar o próximo carro
    def proximo_carro():
        mostrar_informacoes_carro(frame_carro)

    # Botão para mostrar o próximo carro
    botao_proximo = ctk.CTkButton(janela, text="Próximo", command=proximo_carro)
    botao_proximo.pack(side="right", padx=10)

    # Função para mostrar o carro anterior
    def carro_anterior():
        mostrar_informacoes_carro(frame_carro)

    # Botão para mostrar o carro anterior
    botao_anterior = ctk.CTkButton(janela, text="Anterior", command=carro_anterior)
    botao_anterior.pack(side="left", padx=10)

    # Exibir a janela
    janela.mainloop()

# Criar e exibir a janela
criar_janela()
