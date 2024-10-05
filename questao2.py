numeros = []

while True:
    entrada = input("Digite um número ou 'parar' para encerrar: ")
    
    if entrada.lower() == "parar":
        break
    
    try:
        numeros.append(float(entrada))
    except ValueError:
        print("Entrada inválida! Por favor, insira um número válido.")

print("Números digitados:", numeros)
print("Soma dos números:", sum(numeros))

