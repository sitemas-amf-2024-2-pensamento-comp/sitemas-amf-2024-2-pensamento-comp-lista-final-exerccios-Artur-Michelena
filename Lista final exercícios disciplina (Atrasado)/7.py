def encontrar_maior_numero():
    lista_numeros = []
    print("Digite 3 números inteiros:")
    
    for i in range(3):
        while True:
            try:
                num = int(input(f"Digite o número {i + 1}: "))
                lista_numeros.append(num)
                break
            except ValueError:
                print("Erro: É obrigatório digitar um número inteiro.")
    
    maior = max(lista_numeros)
    print(f"\nO maior número é: {maior}")

encontrar_maior_numero()