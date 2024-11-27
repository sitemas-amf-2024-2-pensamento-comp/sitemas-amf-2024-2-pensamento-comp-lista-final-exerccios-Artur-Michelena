# int: valores inteiros. Ex: 0, 1, 2, 3, etc.
def somar_numeros():
    total = 0
    for _ in range(5):
        numero = int(input("Digite um número inteiro: "))
        total += numero
    print(f"A soma dos números é: {total}")

# float: valores com ponto flutuante, números com casas decimais. Ex: 1.0, 0.4, 5.5, etc.
def calcular_imc():
    altura = float(input("Informe sua altura (em metros): "))
    peso = float(input("Informe seu peso (em kg): "))
    imc = peso / (altura ** 2) 
    print(f"Seu IMC é: {imc:.2f}")

# string: cadeia de caracteres ou texto. Ex: 'Olá', 'Python', '000-000-00', etc.
def exibir_saudacao():
    nome = input("Digite seu nome: ")
    print(f"Seja bem-vindo, {nome}!")

# booleano: funciona em um sistema de True ou False
def verificar_maioridade():
    idade = int(input("Digite sua idade: "))
    maior = idade >= 18
    if maior:
        print(f"Você é maior de idade. Idade: {idade}")
    else:
        print(f"Você é menor de idade. Idade: {idade}")

# Função principal para executar os exemplos
def main():
    print("\nExemplo com variável do tipo int:")
    somar_numeros()

    print("\nExemplo com variável do tipo float:")
    calcular_imc()

    print("\nExemplo com variável do tipo string:")
    exibir_saudacao()

    print("\nExemplo com variável do tipo booleano:")
    verificar_maioridade()

main()