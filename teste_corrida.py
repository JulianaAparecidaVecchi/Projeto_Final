import random

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

def filtrar_carros_por_categoria(carros, categoria_desejada):
    carros_filtrados = [carro for carro in carros if carro['categoria'] == categoria_desejada]
    return carros_filtrados
    
def filtrar_carros_por_categorias(carros, categorias_desejadas):
    carros_filtrados = [carro for carro in carros if carro['categoria'] in categorias_desejadas]
    return carros_filtrados

def sorteio_carro_cidade(carros):
    categorias_desejadas = ['Iniciais', 'Ultra-raro']  # Definindo as categorias desejadas
    carros_cidade = filtrar_carros_por_categorias(carros, categorias_desejadas)
    if not carros_cidade:
        return None
    carro_sorteado_cidade = random.choice(carros_cidade)
    return carro_sorteado_cidade

def sorteio_carro_campo(carros):
    categorias_desejadas = ['Medianos', 'Semi-profissional', 'Ultra-Raro']  # Definindo as categorias desejadas
    carros_campo = filtrar_carros_por_categorias(carros, categorias_desejadas)
    if not carros_campo:
        return None
    carro_sorteado_campo = random.choice(carros_campo)
    return carro_sorteado_campo

def sorteio_carro_deserto(carros):
    categorias_desejadas = ['Profissional', 'Ultra-raro']  # Definindo as categorias desejadas
    carros_deserto = filtrar_carros_por_categorias(carros, categorias_desejadas)
    if not carros_deserto:
        return None
    carro_sorteado_deserto = random.choice(carros_deserto)
    return carro_sorteado_deserto

def mediaPonderada(velocidade, potencia, aceleracao):
    mediaP=((velocidade*5)+(potencia*3)+(aceleracao*2)) / 10
    return mediaP

def comparar_carros(carro1, carro2):
    media1 = mediaPonderada(carro1['velocidade'], carro1['potencia'], carro1['aceleracao'])
    media2 = mediaPonderada(carro2['velocidade'], carro2['potencia'], carro2['aceleracao'])

    if media1 > media2:
        return carro1
    elif media1 < media2:
        return carro2
    else:
        return None

def execucao_cidade():
    caminho_arquivo = 'carros.txt'
    carros = ler_arquivo_carros(caminho_arquivo)
    carro1 = sorteio_carro_cidade(carros)
    carro2 = sorteio_carro_cidade(carros)


    print(f"O carro {carro1['nome']} foi sorteado com a velocidade {carro1['velocidade']}, potencia {carro1['potencia']} e aceleração {carro1['aceleracao']}")
    print(f"O carro {carro2['nome']} foi sorteado com a velocidade {carro2['velocidade']}, potencia {carro2['potencia']} e aceleração {carro2['aceleracao']}")
    print("Você deseja competir com o adversário?")

    while True:
        escolha = int(input("Aperte sim[1] para continuar e não[0] para encerrar!"))
        if escolha == 1:
            if carro1 and carro2:
                vencedor = comparar_carros(carro1, carro2)
                if vencedor == carro1:
                    print("Parabéns, você venceu a corrida e ganhou o dinheiro da inscrição do adversário junto com o carro dele")
                    break
                elif vencedor == carro2:
                    print("Que pena, infelizmente você perdeu a corrida e o dinheiro da inscrição junto com seu carro")
                    break
                else:
                    print("Houve um empate entre os veículos")
            else:
                print("Não há carros suficientes na categoria 'Iniciais' para realizar a comparação.")
                break
        else:
            break

def execucao_campo():
    caminho_arquivo = 'carros.txt'
    carros = ler_arquivo_carros(caminho_arquivo)
    carro1 = sorteio_carro_campo(carros)
    carro2 = sorteio_carro_campo(carros)


    print(f"O carro {carro1['nome']} foi sorteado com a velocidade {carro1['velocidade']}, potencia {carro1['potencia']} e aceleração {carro1['aceleracao']}")
    print(f"O carro {carro2['nome']} foi sorteado com a velocidade {carro2['velocidade']}, potencia {carro2['potencia']} e aceleração {carro2['aceleracao']}")
    print("Você deseja competir com o adversário?")

    while True:
        escolha = int(input("Aperte sim[1] para continuar e não[0] para encerrar!"))
        if escolha == 1:
            if carro1 and carro2:
                vencedor = comparar_carros(carro1, carro2)
                if vencedor == carro1:
                    print("Parabéns, você venceu a corrida e ganhou o dinheiro da inscrição do adversário junto com o carro dele")
                    break
                elif vencedor == carro2:
                    print("Que pena, infelizmente você perdeu a corrida e o dinheiro da inscrição junto com seu carro")
                    break
                else:
                    print("Houve um empate entre os veículos")
            else:
                print("Não há carros suficientes na categoria 'Iniciais' para realizar a comparação.")
                break
        else:
            break

def execucao_deserto():
    caminho_arquivo = 'carros.txt'
    carros = ler_arquivo_carros(caminho_arquivo)
    carro1 = sorteio_carro_deserto(carros)
    carro2 = sorteio_carro_deserto(carros)


    print(f"O carro {carro1['nome']} foi sorteado com a velocidade {carro1['velocidade']}, potencia {carro1['potencia']} e aceleração {carro1['aceleracao']}")
    print(f"O carro {carro2['nome']} foi sorteado com a velocidade {carro2['velocidade']}, potencia {carro2['potencia']} e aceleração {carro2['aceleracao']}")
    print("Você deseja competir com o adversário?")

    while True:
        escolha = int(input("Aperte sim[1] para continuar e não[0] para encerrar!"))
        if escolha == 1:
            if carro1 and carro2:
                vencedor = comparar_carros(carro1, carro2)
                if vencedor == carro1:
                    print("Parabéns, você venceu a corrida e ganhou o dinheiro da inscrição do adversário junto com o carro dele")
                    break
                elif vencedor == carro2:
                    print("Que pena, infelizmente você perdeu a corrida e o dinheiro da inscrição junto com seu carro")
                    break
                else:
                    print("Houve um empate entre os veículos")
            else:
                print("Não há carros suficientes na categoria 'Iniciais' para realizar a comparação.")
                break
        else:
            break