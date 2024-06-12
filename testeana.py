def ler_arquivo_texto(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_txt:
            linhas = arquivo_txt.readlines()
        return linhas
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None

# Exemplo de uso:
linhas = ler_arquivo_texto('carros.txt')
if linhas:
    for linha in linhas:
        print(linha)

