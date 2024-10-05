# Solicita um número inteiro do usuário
numero = input("Digite um número inteiro: ")

# Calcula a soma dos dígitos
soma_digitos = sum(int(digito) for digito in numero)

# Imprime o resultado
print("A soma dos dígitos é:", soma_digitos)
