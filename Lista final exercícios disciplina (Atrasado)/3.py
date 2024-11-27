# <, significa menor que.
def verificar_menor():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num1 < num2:
        print(f"{num1} é menor que {num2}.")
    elif num2 < num1:
        print(f"{num2} é menor que {num1}.")
    else:
        print("Os números são iguais.")

# >, significa maior que.
def verificar_maior():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num1 > num2:
        print(f"{num1} é maior que {num2}.")
    elif num2 > num1:
        print(f"{num2} é maior que {num1}.")
    else:
        print("Os números são iguais.")

# =, significa recebe.
def mostrar_dados():
    nome, idade, peso, altura = "Pedro", 18, 64.5, 1.65
    print(f"Nome: {nome}, Idade: {idade}, Peso: {peso}, Altura: {altura}")

# >=, significa maior ou igual; <=, significa menor ou igual.
def verificar_idade():
    idade = int(input("Digite uma idade: "))
    if idade >= 18:
        print(f"Maior de idade, idade = {idade}")
    elif idade > 0:
        print(f"Menor de idade, idade = {idade}")
    else:
        print("Erro no cadastro. Idade inválida.")

# ==, significa igual; !=, significa diferente.
def comparar_nomes():
    nome1 = input("Digite o primeiro nome: ")
    nome2 = input("Digite o segundo nome: ")
    if nome1 == nome2:
        print(f"Ambas as pessoas têm o mesmo nome: {nome1}")
    else:
        print(f"O primeiro nome é {nome1}. O segundo nome é {nome2}.")

# and, significa 'e'.
def encontrar_maior_numero():
    numeros = [int(input(f"Digite o número {i + 1}: ")) for i in range(3)]
    maior = max(numeros)
    print(f"O maior número é: {maior}")

# not, significa não.
def verificar_membro():
    membros = {"JORGE", "CARLOS", "ROBERTA", "CLARA", "JOSÉ"}
    pessoa = input("Digite um nome: ").upper()
    if pessoa in membros:
        print(f"{pessoa} é membro do clube.")
    else:
        print(f"{pessoa} não é membro do clube.")

# or, significa 'ou'.
def verificar_entrada(idade, tem_permissao, esta_acompanhado):
    if idade >= 18 or tem_permissao or esta_acompanhado:
        print("A pessoa pode entrar na festa.")
    else:
        print("A pessoa não pode entrar na festa.")

def main():
    print("\nVerificando menor que:")
    verificar_menor()

    print("\nVerificando maior que:")
    verificar_maior()

    print("\nExibindo dados:")
    mostrar_dados()

    print("\nVerificando idade:")
    verificar_idade()

    print("\nComparando nomes:")
    comparar_nomes()

    print("\nEncontrando o maior número:")
    encontrar_maior_numero()

    print("\nVerificando membro do clube:")
    verificar_membro()

    print("\nVerificando entrada na festa:")
    verificar_entrada(idade=20, tem_permissao=False, esta_acompanhado=False)

main()