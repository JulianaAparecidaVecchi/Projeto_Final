import random
import tkinter as tk
import customtkinter as ctk
import menu_principal
from PIL import Image, ImageTk
import random

largura_desejada = 200
altura_desejada = 200

def redimensionar_imagem(endereço, largura, altura):
    # Carregar a imagem usando PIL
    img_pil = Image.open(endereço)
    # Redimensionar a imagem para as dimensões desejadas
    img_redimensionada = img_pil.resize((largura, altura))
    return img_redimensionada

def card_carro(janela, lista):
    card = ctk.CTkFrame(master=janela)
    imgr=menu_principal.converter_img(lista[5])
    img = ctk.CTkLabel(master=card, image=imgr, text='')
    img.grid(row=1, column=1)
    linha_nome = ctk.CTkLabel(master=card, text=lista[1])
    linha_nome.grid(row=2, column=1)
    linha_velocidade = ctk.CTkLabel(master=card, text=f'Velocidade: {lista[2]}')
    linha_velocidade.grid(row=3, column=1)
    linha_potencia = ctk.CTkLabel(master=card, text=f'Potência: {lista[3]}')
    linha_potencia.grid(row=4, column=1)
    linha_aceleracao = ctk.CTkLabel(master=card, text=f'Aceleração: {lista[4]}')
    linha_aceleracao.grid(row=5, column=1)
    card.grid(row=1, column=1)

def sortear_carro_inicial(arquivo, num1, num2):
    with open(arquivo, 'r') as arquivo:
        carros = arquivo.readlines()  
    numero_sorteado = random.randint(num1, num2)
    carro_sorteado = carros[numero_sorteado].strip().split(',')  # Convertendo a linha em uma lista
    return carro_sorteado

# Sorteando um carro inicial
carro_sorteado = sortear_carro_inicial('carros.txt', 0, 18)
print(carro_sorteado)

# Criando a janela e exibindo o carro sorteado
teste = ctk.CTk()
teste.title('JANELA TESTE')
card_carro(teste, carro_sorteado)
teste.mainloop()