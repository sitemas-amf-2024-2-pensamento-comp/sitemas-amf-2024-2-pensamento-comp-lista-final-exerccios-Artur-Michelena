def mostrar_impares():
    impares = [i for i in range(1, 101) if i % 2 != 0]
    print("Números ímpares:", ", ".join(map(str, impares)))

mostrar_impares()

"""
Método Indutivo: A partir da análise de casos específicos, podemos identificar
padrões ou regras gerais que podem ser aplicadas a uma tarefa.
"""
