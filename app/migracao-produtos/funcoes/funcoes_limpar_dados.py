def limpar_nome(nome):
    if 'Ç' in nome:
        nome = nome.replace('Ç', 'C')
    if 'Ã' in nome:
        nome = nome.replace('Ã', 'A')
    if 'Õ' in nome:
        nome = nome.replace('Õ', 'O')
    nome = nome.replace(',','')
    return nome