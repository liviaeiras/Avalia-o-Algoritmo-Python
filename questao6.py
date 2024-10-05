import random

# Gera uma lista de 20 números aleatórios entre 1 e 50
numeros = [random.randint(1, 50) for _ in range(20)]

# Conta quantos números são ímpares
impares = [num for num in numeros if num % 2 != 0]

# Imprime os resultados
print("Números gerados:", numeros)
print("Quantidade de números ímpares:", len(impares))
