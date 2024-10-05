# Solicita a entrada do usuário
entrada = input("Digite uma lista de números separados por espaços: ")

# Converte a entrada em uma lista de números inteiros
numeros = [float(num) for num in entrada.split()]

# Calcula a média, o maior e o menor número
media = sum(numeros) / len(numeros) if numeros else 0
maior = max(numeros) if numeros else None
menor = min(numeros) if numeros else None

# Imprime os resultados
print("Média:", media)
print("Maior número:", maior)
print("Menor número:", menor)
