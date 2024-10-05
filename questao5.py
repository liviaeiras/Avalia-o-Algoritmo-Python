# Recebe a frase do usuário
frase = input("Digite uma frase: ").replace(" ", "").lower()

# Conta a frequência de cada letra
frequencia = {}
for letra in frase:
    frequencia[letra] = frequencia.get(letra, 0) + 1

# Imprime o resultado
for letra, contagem in frequencia.items():
    print(f"A letra '{letra}' aparece {contagem} vezes.")
