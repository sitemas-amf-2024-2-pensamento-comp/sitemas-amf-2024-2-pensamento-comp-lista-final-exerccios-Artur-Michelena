def encontrar_maior_numero():
    numeros = []
    print("Por favor, insira 3 números inteiros:")

    for i in range(1, 4):
        while True:
            try:
                numero = int(input(f"Digite o número {i}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Erro: É obrigatório digitar um número inteiro válido.")
    
    maior = max(numeros)
    print(f"\nO maior número digitado foi: {maior}")

# Chamada da função
encontrar_maior_numero()