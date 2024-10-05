# Solicita um número inteiro positivo do usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero > 0:
    print(f"Tabela de multiplicação de {numero}:")
    for i in range(1, 11):  # Multiplica de 1 a 10
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Por favor, insira um número inteiro positivo.")
