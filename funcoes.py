# listados = [752,752,752,752,752,752,752,753,753,753,753,753,753,753,753,753,753,753,753,753,753,753,753,753,753,753,753,753,753,753,753,753,753,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,754,755,755,755,755,755,755,755,755,755,755,755,756,756,756,756,756,756,756,756,756,756,756,756,756,756,756,756,756,756,756,756,756,757,757,757,757,757,757,757,757,757,757,757,758,758,758,758,758,759,759,759,759,759,759,759,759,759,759,759,759,760,760,760,760,760,760,760,760,760,760,760,760,760,760,761,761,761,761,761,761,761,761,761,761,761,761,761,761,761,761,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,763,764,764,764,767,767,767,767,768,768,768,768,768,768,768,768,768,768,770,770,770,770,770,770,770,770,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,771,773]

def tira_repetidos(lista):
    meu_set = set()
    for item in lista:
        meu_set.add(item)
    minha_lista = list(meu_set)
    minha_lista.sort()
    return minha_lista

def delimitador_manual(lista,tabela):
    lista_codigos = {}
    for chave in lista:
        trechos = int(input(f"Quantos trechos repetidos de {chave} há? (Digite 0 para pular)"))
        if trechos != 0 and trechos != None:
            codigos = []
            for i in range(trechos):
                linha_inicial = int(input(f"em qual linha começa {chave} {i+1}?"))
                linha_final = int(input(f"em qual linha termina {chave} {i+1}?"))
                codigos_provisorio = tira_repetidos(tabela[linha_inicial-2:linha_final-1, 5])
                codigos.extend(codigos_provisorio)
            lista_codigos[chave] = codigos
        else:
            lista_codigos[chave] = []
    return lista_codigos

def delimitador_automatico(lista,tabela):
    print('Insira no seguinte formato, subistituindo início pela\nlinha em que inicia e fim pela que termina, quantas\nvezes for necessário. e separando por ";". insira tudo na mesma linha.')
    for item in lista:
        print(f'{item} | INICIO - FIM, INICIO - FIM;')
    # resposta = input("Digite:")
    resposta = 'bazar_e_utilidades | 2664 - 2719, 2825 - 2924;'+'bebidas_alcoolicas | 2 - 270;bebidas_nao_alcoolicas | 271 - 566, 1792 - 1893;biscoitos_snacks_aperitivos | 567 - 947;bomboniere | 948 - 1202, 1203 - 1460;congelados_sorvetes_gelo | 2079 - 2227;food_service | 1461 - 1553, 1630 - 1668;mercearia | 1894 - 1926, 2228 - 2663, 2720 - 2824;padaria | 1669 - 1791, 1554 - 1629;tabacaria | 1927 - 2079;'
    if resposta[-1] == ';':
        resposta = resposta[:-1]
    lista_codigos_auto = {}
    lista_resposta = resposta.split(';')
    for grupo in lista_resposta:
        divisao_nome_numeros = grupo.split('|')
        nome_grupo = divisao_nome_numeros[0].strip()
        numeros = divisao_nome_numeros[1].strip()
        trechos = numeros.split(', ')
        codigos = []
        for trecho in trechos:
            inicio_fim = trecho.split(' - ')
            inicio = inicio_fim[0] 
            fim = inicio_fim[1]
            codigos_provisorio = tira_repetidos(tabela[int(inicio)-2:int(fim)-1, 5])
            codigos.extend(codigos_provisorio)
        lista_codigos_auto[nome_grupo] = codigos
    return lista_codigos_auto

# nova_lista = tira_repetidos(listados)

# print(nova_lista)

