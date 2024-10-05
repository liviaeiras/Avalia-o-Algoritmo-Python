# Função para gerar a sequência de Fibonacci até o enésimo termo
def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]  # Retorna apenas os n primeiros termos

# Recebe o valor de n do usuário
n = int(input("Digite o valor de n: "))

# Imprime a sequência de Fibonacci
if n <= 0:
    print("Por favor, insira um número positivo.")
else:
    print(f"Sequência de Fibonacci até o {n}º termo:", fibonacci(n))
