# Solicita a entrada do usuário
numeros = list(map(int, input("Digite uma lista de números separados por espaços: ").split()))

# Filtra os múltiplos de 3 ou 5
multiplos = [num for num in numeros if num % 3 == 0 or num % 5 == 0]

# Imprime a nova lista
print("Números que são múltiplos de 3 ou 5:", multiplos)
