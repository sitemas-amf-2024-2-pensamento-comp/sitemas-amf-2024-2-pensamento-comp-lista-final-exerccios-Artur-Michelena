"""
Em Python, estruturas condicionais permitem ao programa tomar decisões
com base em condições específicas.

if: Avalia uma condição e executa um bloco de código se a condição for verdadeira.
  Ex: if num >= 18

elif: Significa "else if" e permite verificar outra condição se a anterior for falsa.
  Ex:  elif num < 18 and num > 0

else: Executa um bloco de código se todas as condições anteriores forem falsas.
  Ex:   else:
          print("Erro na numeração. Tente novamente.")
"""

def coletar_dados():
    """Coleta idade e gênero do usuário com validação de entrada."""
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("Erro: A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Erro: Por favor, insira um número válido.")
    
    while True:
        sexo = input("Digite seu gênero (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            break
        else:
            print('Erro: Entrada inválida. Digite "M" para Masculino ou "F" para Feminino.')
    
    return idade, sexo

def analisar_dados(idade, sexo):
    """Analisa e exibe a categoria de idade e gênero."""
    if idade < 18:
        categoria = "Menor de idade"
    elif idade < 60:
        categoria = "Maior de idade"
    else:
        categoria = "Idoso"
    
    genero = "Masculino" if sexo == "M" else "Feminino"
    
    print(f"\nRegistro completo:")
    print(f"Idade: {idade} ({categoria})")
    print(f"Gênero: {genero} ({sexo})")

def main():
    idade, sexo = coletar_dados()
    analisar_dados(idade, sexo)

if __name__ == "__main__":
    main()