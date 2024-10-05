# Solicita a entrada do usuário e define as vogais
entrada = input("Digite uma lista de caracteres separados por espaços: ").split()
vogais = "aeiouAEIOU"

# Contadores
contagem_vogais = sum(1 for char in entrada if char in vogais)
contagem_consoantes = sum(1 for char in entrada if char.isalpha() and char not in vogais)

# Imprime os resultados
print("Quantidade de vogais:", contagem_vogais)
print("Quantidade de consoantes:", contagem_consoantes)
