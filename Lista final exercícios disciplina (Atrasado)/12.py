"""
Pop:
- Utiliza o índice da lista para remover e retornar o elemento correspondente.
- Se o índice não for especificado, remove o último elemento.
- Útil quando você conhece a posição do elemento ou deseja remover o último item.

Remove:
- Remove o primeiro elemento da lista que corresponde ao valor fornecido.
- Gera um erro se o valor não estiver na lista.
- Ideal quando você quer remover um valor específico, sem se preocupar com o índice.
"""

def demonstrar_pop():
    """Demonstra o uso do método pop em uma lista."""
    lista = [10, 20, 30, 40, 50, 10]
    print("Exemplo com pop:")
    print(f"Lista Inicial: {lista}")
    elemento_removido = lista.pop(2)  # Remove o elemento no índice 2
    print(f"Lista após uso do pop: {lista}")
    print(f"Elemento removido (índice 2): {elemento_removido}")
    print("-" * 40)

def demonstrar_remove():
    """Demonstra o uso do método remove em uma lista."""
    lista = [10, 20, 30, 40, 50, 20]
    print("Exemplo com remove:")
    print(f"Lista Inicial: {lista}")
    lista.remove(20)  # Remove a primeira ocorrência do valor 20
    print(f"Lista após remover o valor 20: {lista}")
    print("-" * 40)

def main():
    """Função principal para executar os exemplos."""
    demonstrar_pop()
    demonstrar_remove()

if __name__ == "__main__":
    main()