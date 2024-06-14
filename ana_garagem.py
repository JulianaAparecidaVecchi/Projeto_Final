import customtkinter as ctk
import menu_principal

cor_5 = '#d9c6c6'
carros = [
    ['Iniciais', 'Volkswagen Gol', 180, 80, 12, './img/iniciais/volkswagengol.png'],
    ['Iniciais', 'Chevrolet Celta', 170, 78, 13, './img/iniciais/chevroletcelta.png'],
    ['Iniciais', 'Chevrolet Corsa', 175, 82, 11, './img/iniciais/chevroletcorsa.png'],
    ['Iniciais', 'Fiat Palio', 165, 76, 14, './img/iniciais/fiatpalio.png']
]

# Função para mostrar o carro atual e atualizar a lista
def atualizar_carro(frame, lista, indice):
    # Limpar o frame antes de adicionar a linha
    for widget in frame.winfo_children():
        widget.destroy()

    # Exibir a linha no frame
    if 0 <= indice < len(lista):
        cartao_carro = menu_principal.card_carro(frame, lista[indice])
        cartao_carro.grid(row=0, column=0)

# Função para a janela da garagem
def janela_garagem():
    garagem_janela = ctk.CTk()
    garagem_janela.title("Garagem")

    # Frame para o conteúdo do carro
    frame_conteudo = ctk.CTkFrame(garagem_janela)
    frame_conteudo.grid(row=0, column=0, columnspan=3)

    # Índice da linha atual
    indice_linha_atual = 0

    # Mostrar a primeira linha do arquivo
    atualizar_carro(frame_conteudo, carros, indice_linha_atual)

    def proxima_linha():
        nonlocal indice_linha_atual
        if indice_linha_atual < len(carros) - 1:
            indice_linha_atual += 1
            atualizar_carro(frame_conteudo, carros, indice_linha_atual)

    def linha_anterior():
        nonlocal indice_linha_atual
        if indice_linha_atual > 0:
            indice_linha_atual -= 1
            atualizar_carro(frame_conteudo, carros, indice_linha_atual)

    # Frame para os botões
    frame_botoes = ctk.CTkFrame(garagem_janela)
    frame_botoes.grid(row=1, column=0, columnspan=3)

    botao_proximo = ctk.CTkButton(frame_botoes, text='PRÓXIMO', width=100, height=50, command=proxima_linha)
    botao_proximo.grid(row=0, column=2)

    botao_anterior = ctk.CTkButton(frame_botoes, text='ANTERIOR', width=100, height=50, command=linha_anterior)
    botao_anterior.grid(row=0, column=0)

    garagem_janela.mainloop()

# Chamada da função para abrir a janela da garagem
janela_garagem()
