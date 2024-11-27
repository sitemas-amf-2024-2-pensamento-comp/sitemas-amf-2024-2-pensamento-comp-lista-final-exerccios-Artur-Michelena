def calcular_media(num1, num2):
    """Calcula a média de dois números."""
    return (num1 + num2) / 2

def main():
    print("Bem-vindo ao programa de cálculo de média!")
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = calcular_media(numero1, numero2)
        print(f"A média entre {numero1} e {numero2} é: {resultado:.2f}")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()