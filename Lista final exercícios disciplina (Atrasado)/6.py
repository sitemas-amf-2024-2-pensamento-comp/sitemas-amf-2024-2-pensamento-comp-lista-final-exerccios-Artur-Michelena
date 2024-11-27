# Gerando todas as combinações possíveis de A, B e C
valores = [(A, B, C) for A in [0, 1] for B in [0, 1] for C in [0, 1]]

# Cabeçalho da tabela
print(f"{'A':^3} {'B':^3} {'C':^3} {'A || (B && C)':^15} {'!A && B && C':^15} {'!(A && B && !C)':^15}")

# Iteração para calcular e exibir os resultados das expressões lógicas
for A, B, C in valores:
    exp1 = A or (B and C)  # A || (B && C)
    exp2 = not A and B and C  # !A && B && C
    exp3 = not (A and B and not C)  # !(A && B && !C)
    print(f"{A:^3} {B:^3} {C:^3} {str(bool(exp1)):^15} {str(bool(exp2)):^15} {str(bool(exp3)):^15}")
