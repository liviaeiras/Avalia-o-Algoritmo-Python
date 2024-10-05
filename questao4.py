# Lista de nomes
nomes = ["Ines", "Isa", "Luiz Miguel", "Isaque", "Neymar", "Cristiano", "Claudia"]

# Encontra o nome mais longo e o mais curto
nome_mais_longo = max(nomes, key=len)
nome_mais_curto = min(nomes, key=len)

# Imprime os resultados
print("Nome mais longo:", nome_mais_longo)
print("Nome mais curto:", nome_mais_curto)
