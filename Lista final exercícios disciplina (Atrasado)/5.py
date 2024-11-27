"""
Afirmativas sobre o programa:

1. O programa diferencia as idades por categorias (menor de idade, maior de idade, idoso). **Verdadeiro**
   - Utiliza `if`, `elif` e `else` para classificar a idade.

2. O programa impede entradas inválidas de idade. **Verdadeiro**
   - Exibe mensagens de erro e reinicia o processo para entradas negativas ou não numéricas.

3. O programa impede entradas de gênero inválidas. **Verdadeiro**
   - Apenas aceita 'M' ou 'F' como entradas válidas, exigindo correção em caso de erro.

4. Qualquer combinação válida de idade e gênero faz o programa funcionar corretamente. **Verdadeiro**
   - Aceita e processa todas as combinações de entradas válidas.

5. O programa apresenta erro ao receber uma entrada não numérica para a idade. **Falso**
   - O código usa `try-except` para tratar erros, exibindo mensagens e reiniciando o processo de entrada.
"""

def verificar_idade_e_genero():
    while True:
        try:
            # Entrada e validação da idade
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("Erro: A idade não pode ser negativa. Tente novamente.")
                continue

            # Entrada e validação do gênero
            sexo = input("Digite seu gênero (M/F): ").strip().upper()
            if sexo not in ["M", "F"]:
                print("Erro: Gênero inválido. Digite 'M' para Masculino ou 'F' para Feminino.")
                continue

            # Se as entradas forem válidas, encerra o loop
            break
        except ValueError:
            print("Erro: Por favor, insira um número válido para a idade.")

    # Classificação da idade
    if idade < 18:
        categoria = "Menor de idade."
    elif idade < 60:
        categoria = "Maior de idade."
    else:
        categoria = "Idoso."

    # Identificação do gênero
    genero = "Masculino" if sexo == "M" else "Feminino."

    # Exibindo os resultados
    print("\nResultados:")
    print(categoria)
    print(f"Gênero Registrado: {genero}")

# Executar a função principal
verificar_idade_e_genero()