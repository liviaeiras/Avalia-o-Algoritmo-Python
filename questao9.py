# Solicita a entrada do usuário
entrada = input("Digite uma lista de palavras separadas por espaços: ")

# Converte a entrada em uma lista de palavras
palavras = entrada.split()

# Conta quantas palavras têm mais de 5 letras
contagem = sum(1 for palavra in palavras if len(palavra) > 5)

# Imprime o resultado
print("Número de palavras com mais de 5 letras:", contagem)
