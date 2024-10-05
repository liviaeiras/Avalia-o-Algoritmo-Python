# Solicita a entrada do usuário
entrada = input("Digite uma lista de números separados por espaços: ")
numeros = list(set(int(num) for num in entrada.split()))  # Converte para int e remove duplicatas

# Ordena e obtém o segundo maior número
if len(numeros) < 2:
    print("A lista deve conter pelo menos dois números distintos.")
else:
    print("O segundo maior número é:", sorted(numeros)[-2])
