import random
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#Função para ler o arquivo txt em forma de dicionário
#Depois ele armazena essas informações na variável carros
def ler_arquivo_carros(caminho_arquivo):
    carros = []
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            categoria, nome, velocidade, potencia, aceleracao = linha.strip().split(',')
            carro = {
                'categoria': categoria,
                'nome': nome,
                'velocidade': int(velocidade),
                'potencia': int(potencia),
                'aceleracao': int(aceleracao)
            }
            carros.append(carro)
    return carros

#Função para filtrar carros port mais de uma categoria: Ex: 'iniciais', 'Ultra_Raro'    
def filtrar_carros_por_categorias(carros, categorias_desejadas):
    carros_filtrados = [carro for carro in carros if carro['categoria'] in categorias_desejadas]
    return carros_filtrados

#Função para sortear somente um carro inicial, essa função poderia ser utilizada para sortear um carro para
#a primeira vez que o jogador entrar dentro do jogo.
def sorteio_carro_inicial(carros):
    categoria_desejada = ['Iniciais']  # Definindo as categorias desejadas
    carro_inicial = filtrar_carros_por_categorias(carros, categoria_desejada)
    if not carro_inicial:
        return None
    carro_sorteado_inicial = random.choice(carro_inicial)
    return carro_sorteado_inicial

#Essa função irá sortear um carro que estiver entre a categoria de iniciais e ultra raro. Essa função é adequada para o sorteio apenas no mapa da cidade
def sorteio_carro_cidade(carros):
    categorias_desejadas = ['Iniciais', 'Ultra-Raro']  # Definindo as categorias desejadas
    carros_cidade = filtrar_carros_por_categorias(carros, categorias_desejadas)
    if not carros_cidade:
        return None
    carro_sorteado_cidade = random.choice(carros_cidade)
    return carro_sorteado_cidade

#Essa função sorteia um carro dentro da categoria dos medianos, semi-profissionais e ultra raro. Função para o mapa do campo
def sorteio_carro_campo(carros):
    categorias_desejadas = ['Medianos', 'Semi-profissional', 'Ultra-Raro']  # Definindo as categorias desejadas
    carros_campo = filtrar_carros_por_categorias(carros, categorias_desejadas)
    if not carros_campo:
        return None
    carro_sorteado_campo = random.choice(carros_campo)
    return carro_sorteado_campo

#Essa função sorteia um carro que estiver dentro da categoria profissional e ultra raro. Função para o mapa do deserto
def sorteio_carro_deserto(carros):
    categorias_desejadas = ['Profissional', 'Ultra-Raro']  # Definindo as categorias desejadas
    carros_deserto = filtrar_carros_por_categorias(carros, categorias_desejadas)
    if not carros_deserto:
        return None
    carro_sorteado_deserto = random.choice(carros_deserto)
    return carro_sorteado_deserto

#Essa função pega os atributos dos carros e realiza o cálculo da Média Ponderada. Vel vale 5, pot vale 3 e acel vale 2
def mediaPonderada(velocidade, potencia, aceleracao):
    mediaP=((velocidade*5)+(potencia*3)+(aceleracao*2)) / 10
    return mediaP

#Essa função pega o carro 1 = carro_selecionado e carro2 = carro_competidor para compará-los e retornar o carro com maior média
def comparar_carros(carro1, carro2):
    media1 = mediaPonderada(carro1['velocidade'], carro1['potencia'], carro1['aceleracao'])
    media2 = mediaPonderada(carro2['velocidade'], carro2['potencia'], carro2['aceleracao'])

    if media1 > media2:
        return carro1
    elif media1 < media2:
        return carro2
    else:
        return None

#Essa função não tem nada feito, mas a ideia é pegar o dinheiro do jogador para fazer atualizações, como caso ele perca uma corrida ou ganhe
def dinheiro_jogador():
    saldo_jogador = 0
    return saldo_jogador

#Essa função não tem nada, mas a ideia é ter a lógica de quando o jogador perde a corrida e perde o seu carro selecionado
def perda_carro(carro_jogador):
    pass

#Essa função não tem nada, mas a ideia é fazer a lógica de quando o jogador ganha a corrida e recebe o carro_competidor em sua garagem
def ganhar_carro(carro_adversario):
    pass

#Essa função é para executar as funções de lógica e cálculo do mapa de cidade
def execucao_cidade():
  #Essa parte começa lendo o arquivo de carros.txt
  caminho_arquivo = 'carros.txt'
  carros = ler_arquivo_carros(caminho_arquivo)
  
  #Essa parte armazenaria o carro_selecionado pelo usuário dentro da garagem, mas por enquanto está sorteando
  carro_selecionado = sorteio_carro_campo(carros)
  #Essa parte está certa e ele armazena o carro_competidor sorteado dentro do mapa cidade
  carro_competidor = sorteio_carro_cidade(carros)
  
  #Essa parte armazenaria a quanntidade de dinheiro atual do jogador para fazer possíveis alterações
  dinheiro_atual = dinheiro_jogador()
  
  #Isso apareceria como texto dentro da interface_cidade
  print(f"O carro {carro_selecionado['nome']} foi sorteado com a velocidade {carro_selecionado['velocidade']}, potencia {carro_selecionado['potencia']} e aceleração {carro_selecionado['aceleracao']}")
  print(f"O carro {carro_competidor['nome']} foi sorteado com a velocidade {carro_competidor['velocidade']}, potencia {carro_competidor['potencia']} e aceleração {carro_competidor['aceleracao']}")
  print("Você deseja competir com o adversário?")
  
  #Esse laço de repetição seria para fazer a verificação se o jogador iria aceitar a corrida ou não
  while True:
    #Essa seria substituído por um botão de sim para continuar e não para sair
    escolha = int(input("Aperte sim[1] para continuar e não[0] para encerrar!"))
    if escolha == 1:
      #Essa parte seria sobre a lógica do pagamento da inscrição, mas que não foi feita
      dinheiro_atual -=500
      if carro_selecionado and carro_competidor:
          vencedor = comparar_carros(carro_selecionado, carro_competidor)
          
          #Aceitando a corrida e ganhando, ele ganharia o carro do adversário mais o dinheiro da inscrição dele de volta e a do adversário
          if vencedor == carro_selecionado:
              print("Parabéns, você venceu a corrida e ganhou o dinheiro da inscrição do adversário junto com o carro dele")
              #Essa parte seria a devolução do dinheiro da inscrição e o ganho do dinheiro de inscrição do adversário, mas que não foi feita
              dinheiro_atual+=1000
              #Essa seria a lógica do jogador ganhar o carro do adversário e adicioná-lo em sua garag
              ganhar_carro(carro_competidor)
              break
            
          #Se perdesse, o jogador perderia seu carro e o dinheiro que ele gastou na inscrição
          elif vencedor == carro_competidor:
              print("Que pena, infelizmente você perdeu a corrida e o dinheiro da inscrição junto com seu carro")
              #Essa seria a lógica do usuário perder o carro_selecionado para caso ele perdesse a corrida.
              #Caso o usuário esteja utilizando o seu carro_inicial, ele não perderia o carro
              perda_carro(carro_selecionado)
              break
          else:
              print("Houve um empate entre os veículos")
      else:
          print("Não há carros suficientes na categoria 'Iniciais' para realizar a comparação.")
          break
    else:
        break

#Essa função é para executar as funções lógicas e cálculo do mapa do campo
def execucao_campo():
  #Essa parte começa lendo o arquivo de carros.txt
  caminho_arquivo = 'carros.txt'
  carros = ler_arquivo_carros(caminho_arquivo)
  
  #Essa parte armazenaria o carro_selecionado pelo usuário dentro da garagem, mas por enquanto está sorteando
  carro_selecionado = sorteio_carro_campo(carros)
  #Essa parte está certa e ele armazena o carro_competidor sorteado dentro do mapa cidade
  carro_competidor = sorteio_carro_campo(carros)
  
  #Essa parte armazenaria a quanntidade de dinheiro atual do jogador para fazer possíveis alterações
  dinheiro_atual = dinheiro_jogador()

  #Isso apareceria como texto dentro da interface_campo
  print(f"O carro {carro_selecionado['nome']} do jogador foi selecionado com a velocidade {carro_selecionado['velocidade']}, potencia {carro_selecionado['potencia']} e aceleração {carro_selecionado['aceleracao']}")
  print(f"O carro {carro_competidor['nome']} foi sorteado para competir com a velocidade {carro_competidor['velocidade']}, potencia {carro_competidor['potencia']} e aceleração {carro_competidor['aceleracao']}")
  print("Você deseja competir com o adversário?")

  #Esse laço de repetição seria para fazer a verificação se o jogador iria aceitar a corrida ou não
  while True:
      escolha = int(input("Aperte sim[1] para continuar e não[0] para encerrar!"))
      if escolha == 1:
        #Essa parte seria sobre a lógica do pagamento da inscrição, mas que não foi feita
        dinheiro_atual-=1000
        if carro_selecionado and carro_competidor:
            vencedor = comparar_carros(carro_selecionado, carro_competidor)
            
            #Aceitando a corrida e ganhando, ele ganharia o carro do adversário mais o dinheiro da inscrição dele de volta e a do adversário
            if vencedor == carro_selecionado:
                print("Parabéns, você venceu a corrida e ganhou o dinheiro da inscrição do adversário junto com o carro dele")
                #Essa parte seria a devolução do dinheiro da inscrição e o ganho do dinheiro de inscrição do adversário, mas que não foi feita
                dinheiro_atual+=2000
                #Essa seria a lógica do jogador ganhar o carro do adversário e adicioná-lo em sua garagem
                ganhar_carro(carro_competidor)
                break
              
            #Se perdesse, o jogador perderia seu carro e o dinheiro que ele gastou na inscrição
            elif vencedor == carro_competidor:
                print("Que pena, infelizmente você perdeu a corrida e o dinheiro da inscrição junto com seu carro")
                #Essa seria a lógica do usuário perder o carro_selecionado para caso ele perdesse a corrida.
                #Caso o usuário esteja utilizando o seu carro_inicial, ele não perderia o carro
                perda_carro(carro_selecionado)
                break
            else:
                print("Houve um empate entre os veículos")
        else:
            print("Não há carros suficientes na categoria 'Iniciais' para realizar a comparação.")
            break
      else:
          break

#Essa função é para executar as funções lógicas e cálculo do mapa do deserto
def execucao_deserto():
  caminho_arquivo = 'carros.txt'
  carros = ler_arquivo_carros(caminho_arquivo)

  #Essa parte armazenaria a quanntidade de dinheiro atual do jogador para fazer possíveis alterações
  dinheiro_atual = dinheiro_jogador()

  #Essa parte armazenaria o carro_selecionado pelo usuário dentro da garagem, mas por enquanto está sorteando
  carro_selecionado = sorteio_carro_campo(carros)
  #Essa parte está certa e ele armazena o carro_competidor sorteado dentro do mapa cidade
  carro_competidor = sorteio_carro_deserto(carros)

  #Isso apareceria como texto dentro da interface_deserto
  print(f"O carro {carro_selecionado['nome']} foi sorteado com a velocidade {carro_selecionado['velocidade']}, potencia {carro_selecionado['potencia']} e aceleração {carro_selecionado['aceleracao']}")
  print(f"O carro {carro_competidor['nome']} foi sorteado com a velocidade {carro_competidor['velocidade']}, potencia {carro_competidor['potencia']} e aceleração {carro_competidor['aceleracao']}")
  print("Você deseja competir com o adversário?")

  #Esse laço de repetição seria para fazer a verificação se o jogador iria aceitar a corrida ou não
  while True:
      escolha = int(input("Aperte sim[1] para continuar e não[0] para encerrar!"))
      if escolha == 1:
          #Essa parte seria sobre a lógica do pagamento da inscrição, mas que não foi feita
          dinheiro_atual-=2000
          
          #Essa parte só acontece se houver os dois carros
          if carro_selecionado and carro_competidor:
              vencedor = comparar_carros(carro_selecionado, carro_competidor)
              
              #Aceitando a corrida e ganhando, ele ganharia o carro do adversário mais o dinheiro da inscrição dele de volta e a do adversário
              if vencedor == carro_selecionado:
                  print("Parabéns, você venceu a corrida e ganhou o dinheiro da inscrição do adversário junto com o carro dele")
                  #Essa parte seria a devolução do dinheiro da inscrição e o ganho do dinheiro de inscrição do adversário, mas que não foi feita
                  dinheiro_atual +=4000
                  #Essa seria a lógica do jogador ganhar o carro do adversário e adicioná-lo em sua garagem
                  ganhar_carro(carro_competidor)
                  break
                
              #Se perdesse, o jogador perderia seu carro e o dinheiro que ele gastou na inscrição
              elif vencedor == carro_competidor:
                  print("Que pena, infelizmente você perdeu a corrida e o dinheiro da inscrição junto com seu carro")
                  #Essa seria a lógica do usuário perder o carro_selecionado para caso ele perdesse a corrida.
                  #Caso o usuário esteja utilizando o seu carro_inicial, ele não perderia o carro
                  perda_carro(carro_selecionado)
                  break
              else:
                  print("Houve um empate entre os veículos")
          else:
              print("Não há carros suficientes na categoria 'Iniciais' para realizar a comparação.")
              break
      else:
          print('saindo ...')
          break

#Essa função serve para exibir com uma caixa de mensagem na interface quem ganhou a corrida
def exibir_resultado_comparacao(vencedor, janela):
    if vencedor:
        messagebox.showinfo("Resultado", f"O carro vencedor é: {vencedor['nome']}")
    else:
        messagebox.showinfo("Resultado", "Houve um empate entre os veículos.")
    janela.destroy()

#Essa função faz a mescla de algumas funções anteriores como o sorteio dos carros e agora printa esas informações 
def executar_sorteio_categoria(funcao_sorteio, titulo):
    caminho_arquivo = 'carros.txt'
    carros = ler_arquivo_carros(caminho_arquivo)
  
    #Essa parte recebe o parâmetro sorteio que será posteriormente utilizado nas interfaces
    carro_selecionado = funcao_sorteio(carros)
    carro_competidor = funcao_sorteio(carros)
    
    #Se há um carro_selecionado e um carro_competidor, ele executa esse código
    if carro_selecionado and carro_competidor:
        janela_resultado = tk.Toplevel()
        janela_resultado.title(titulo)
        
        #Essa parte é a mais complicada, pois ele printa as imagens utilizando como endereço o nome que tiver no carro.txt
        #O problema disso é que o nome das imagens devem estar salvas extamente da mesma forma do que no carro.txt, o que eu já fiz e devo ter mandado para vocês
        #Eu acredito que essa é a forma mais simples de se utilizar as imagens, mas pode ser mudado
        imagem_selecionado = Image.open(f"img/iniciais/{carro_selecionado['nome']}.png")
        imagem_competidor = Image.open(f"img/iniciais/{carro_competidor['nome']}.png")

        #Isso define qual será os tamanhos das imagens
        imagem_selecionado = imagem_selecionado.resize((150, 100))
        imagem_competidor = imagem_competidor.resize((150, 100))

        #Essa parte printa as imagens
        foto_selecionado = ImageTk.PhotoImage(imagem_selecionado)
        foto_competidor = ImageTk.PhotoImage(imagem_competidor)

        label_selecionado = ctk.CTkLabel(janela_resultado, image=foto_selecionado)
        label_selecionado.image = foto_selecionado
        label_selecionado.pack(padx=20, pady=10)

        label_competidor = ctk.CTkLabel(janela_resultado, image=foto_competidor)
        label_competidor.image = foto_competidor
        label_competidor.pack(padx=20, pady=10)

        texto = f"O carro {carro_selecionado['nome']} foi sorteado com a velocidade {carro_selecionado['velocidade']}, potencia {carro_selecionado['potencia']} e aceleração {carro_selecionado['aceleracao']}.\n"
        texto += f"O carro {carro_competidor['nome']} foi sorteado com a velocidade {carro_competidor['velocidade']}, potencia {carro_competidor['potencia']} e aceleração {carro_competidor['aceleracao']}.\n"
        texto += "Você deseja competir com o adversário?"
        label_resultado = ctk.CTkLabel(janela_resultado, text=texto, wraplength=300)
        label_resultado.pack(padx=20, pady=20)
        
        #Botão para continuar e realizar os cálculos e lógica
        botao_sim = ctk.CTkButton(janela_resultado, text="Sim", command=lambda: comparar_e_exibir(carro_selecionado, carro_competidor, janela_resultado))
        botao_sim.pack(side="left", padx=20, pady=20)
        
        #Botão para sair
        botao_nao = ctk.CTkButton(janela_resultado, text="Não", command=janela_resultado.destroy)
        botao_nao.pack(side="right", padx=20, pady=20)
        
    #Se não há algum dos carros, ele printa essa caixa de mensagem na interface
    else:
        messagebox.showerror("Erro", "Não há carros suficientes na categoria selecionada para realizar a comparação.")

#Essa parte compara para ver quem é o vencedor e printa na interface isso
def comparar_e_exibir(carro_selecionado, carro_competidor, janela):
    vencedor = comparar_carros(carro_selecionado, carro_competidor)
    exibir_resultado_comparacao(vencedor, janela)

#Essa parte printa a interface da cidade
def interface_cidade():
    interface = ctk.CTk()
    interface.title("Interface corrida")

    botao_cidade = ctk.CTkButton(interface, text="Sorteio Cidade", command=lambda: executar_sorteio_categoria(sorteio_carro_cidade, "Sorteio Carros Cidade"))
    botao_cidade.pack(pady=10)

    interface.mainloop()

#Essa parte printa a interface do campo
def interface_campo():
    interface = ctk.CTk()
    interface.title("Interface corrida")

    botao_campo = ctk.CTkButton(interface, text="Sorteio Campo", command=lambda: executar_sorteio_categoria(sorteio_carro_campo, "Sorteio Carros Campo"))
    botao_campo.pack(pady=10)

    interface.mainloop()

#Essa parte printa a interface do deserto
def interface_deserto():
    interface = ctk.CTk()
    interface.title("Interface corrida")

    botao_deserto = ctk.CTkButton(interface, text="Sorteio Deserto", command=lambda: executar_sorteio_categoria(sorteio_carro_deserto, "Sorteio Carros Deserto"))
    botao_deserto.pack(pady=10)

    interface.mainloop()
    
#Programa principal que será excluído, mas coloquei apenas para testar
interface_deserto()
