def tira_repetidos(lista):
    meu_set = set()
    for item in lista:
        meu_set.add(item)
    minha_lista = list(meu_set)
    minha_lista.sort()
    return minha_lista