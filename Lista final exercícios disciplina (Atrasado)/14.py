def lista_duplicada():
    """Retorna uma lista com elementos duplicados."""
    return [10, 20, 30, 40, 50, 20, 10, 40]

def remover_duplicados(lista):
    """Remove os elementos duplicados de uma lista mantendo a ordem original."""
    lista_unica = []
    for elemento in lista:
        if elemento not in lista_unica:
            lista_unica.append(elemento)
    return lista_unica

def main():
    """Executa o processo de remoção de duplicados em uma lista."""
    lista = lista_duplicada()
    print(f"Lista Original: {lista}")
    lista_unica = remover_duplicados(lista)
    print(f"Lista sem duplicados: {lista_unica}")

if __name__ == "__main__":
    main()