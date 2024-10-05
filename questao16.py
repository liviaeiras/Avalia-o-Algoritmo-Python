# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Inicializa o fatorial
fatorial = 1

# Calcula o fatorial
for i in range(2, numero + 1):
    fatorial *= i

# Imprime o resultado
print(fatorial)
