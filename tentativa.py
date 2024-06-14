# Abre o arquivo de texto para leitura
with open('carros.txt', 'r') as arquivo:
    # Lê todas as linhas do arquivo e as armazena em uma lista
    linhas = arquivo.readlines()

# Remove espaços em branco e quebras de linha de cada linha lida
linhas = []

# Exibe as linhas lidas
print(linhas)

    
    