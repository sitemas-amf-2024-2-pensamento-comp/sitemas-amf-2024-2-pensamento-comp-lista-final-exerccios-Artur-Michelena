"""
Continue:
- Pula a iteração atual do loop e passa para a próxima.
- Deve ser usado quando você deseja ignorar uma condição específica e continuar iterando.

Break:
- Interrompe o loop atual imediatamente, parando sua execução.
- Deve ser usado quando uma condição específica for atingida e o loop precisar ser encerrado.
"""

def demonstrar_continue_e_break():
    """Demonstra o uso dos comandos continue e break em um loop."""
    print("Iterando de 1 a 10, pulando o número 3 e parando no número 5:")
    for numero in range(1, 11):
        if numero == 3:
            print(f"Pulei o número {numero} (continue).")
            continue  # Pula esta iteração e vai para a próxima
        if numero == 5:
            print(f"Quebrei o loop no número {numero} (break).")
            break  # Encerra o loop completamente
        print(f"Número atual: {numero}")

# Executa a função
demonstrar_continue_e_break()