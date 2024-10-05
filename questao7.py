# Solicita a entrada do usuário
entrada = input("Digite uma lista de números separados por espaços: ")

# Converte a entrada em uma lista de números inteiros
numeros = [int(num) for num in entrada.split()]

# Ordena a lista usando Bubble Sort
n = len(numeros)
for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] > numeros[j + 1]:
            # Troca os elementos se estiverem na ordem errada
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# Imprime a lista ordenada
print("Lista em ordem crescente:", numeros)

