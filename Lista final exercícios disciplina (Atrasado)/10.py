def calcular_renda():
    """Solicita os dados financeiros e calcula a renda líquida."""
    try:
        renda = float(input("Digite a sua renda mensal (em R$): "))
        despesas = float(input("Digite suas despesas mensais (em R$): "))
        pontuacao_credito = int(input("Digite sua pontuação de crédito: "))
        parcela_mensal = float(input("Digite o valor da parcela mensal do empréstimo (em R$): "))
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")
        return calcular_renda()  # Reinicia o processo de entrada em caso de erro

    renda_liquida = renda - despesas
    print(f"Sua renda líquida é: R$ {renda_liquida:.2f}")
    return renda_liquida, pontuacao_credito, parcela_mensal

def verificar_elegibilidade(renda_liquida, pontuacao_credito):
    """Verifica se o cliente é elegível para o empréstimo."""
    return pontuacao_credito >= 650 and renda_liquida >= 2000

def verificar_parcela(renda_liquida, parcela_mensal):
    """Verifica se a parcela mensal está dentro do limite permitido."""
    limite_parcela = 0.3 * renda_liquida
    return parcela_mensal <= limite_parcela, limite_parcela

def solicitar_emprestimo():
    """Gerencia o fluxo de verificação para a solicitação de empréstimo."""
    renda_liquida, pontuacao_credito, parcela_mensal = calcular_renda()
    
    # Verificação de elegibilidade
    if verificar_elegibilidade(renda_liquida, pontuacao_credito):
        print("Você é elegível para o empréstimo.")
    else:
        print("Desculpe, você não atende aos critérios para o empréstimo.")
        return

    # Verificação do valor da parcela
    parcela_aceitavel, limite_parcela = verificar_parcela(renda_liquida, parcela_mensal)
    if parcela_aceitavel:
        print(f"A parcela mensal de R$ {parcela_mensal:.2f} está dentro do limite de R$ {limite_parcela:.2f}.")
        print("Parabéns, seu empréstimo pode ser aprovado!")
    else:
        print(f"A parcela mensal de R$ {parcela_mensal:.2f} excede o limite permitido de R$ {limite_parcela:.2f}.")
        print("Infelizmente, o empréstimo não pode ser aprovado.")

# Iniciar o processo de empréstimo
solicitar_emprestimo()