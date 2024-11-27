import random

def jogo_adivinhacao():
    """Inicia um jogo de adivinhação onde o usuário tenta adivinhar um número entre 1 e 100."""
    sorteio = random.randint(1, 100)
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar um número de 1 a 100.")

    while True:
        try:
            # Entrada do número do usuário
            num_sorte = int(input("Digite seu número da sorte: "))

            # Validação do intervalo
            if num_sorte < 1 or num_sorte > 100:
                print("Erro: Insira um número entre 1 e 100.")
                continue

            # Comparação com o número sorteado
            if num_sorte < sorteio:
                print("Errado. O número é maior!")
            elif num_sorte > sorteio:
                print("Errado. O número é menor!")
            else:
                print(f"Parabéns! Você acertou o número: {sorteio}")
                break
        except ValueError:
            print("Erro: Insira um número inteiro válido.")

# Inicia o jogo
if __name__ == "__main__":
    jogo_adivinhacao()