import customtkinter as ctk

cor_5 = '#d9c6c6'

# Função para mostrar o carro atual e atualizar a lista
def mostrar_linha(frame, linha):
    # Limpar o frame antes de adicionar a linha
    for widget in frame.winfo_children():
        widget.destroy()

    # Exibir a linha no frame
    label = ctk.CTkLabel(frame, text=linha)
    label.grid(row=5,column=1)
# Função para a janela da garagem
def janela_garagem():
    garagem_janela = ctk.CTk()

    with open('teste.txt', 'r') as arquivo:
        conteudo = arquivo.readlines()
    
    # Frame para exibir a linha do arquivo
    frame_linha = ctk.CTkFrame(garagem_janela)
    frame_linha.grid(row=1,column=2)
#
    # Índice da linha atual
    indice_linha_atual = 0

    # Mostrar a primeira linha do arquivo
    mostrar_linha(frame_linha, conteudo[indice_linha_atual])

    def proxima_linha():
        nonlocal indice_linha_atual
        if indice_linha_atual < len(conteudo) - 1:
            indice_linha_atual += 1
            mostrar_linha(frame_linha, conteudo[indice_linha_atual])

    def linha_anterior():
        nonlocal indice_linha_atual
        if indice_linha_atual > 0:
            indice_linha_atual -= 1
            mostrar_linha(frame_linha, conteudo[indice_linha_atual])

    botao_proximo = ctk.CTkButton(garagem_janela, text='PRÓXIMO', width=100, height=50, command=proxima_linha)
    botao_proximo.grid(row=1,column=3)

    botao_anterior = ctk.CTkButton(garagem_janela, text='ANTERIOR', width=100, height=50, command=linha_anterior)
    botao_anterior.grid(row=1,column=1)

    garagem_janela.mainloop()

# Chamada da função para abrir a janela da garagem
janela_garagem()
