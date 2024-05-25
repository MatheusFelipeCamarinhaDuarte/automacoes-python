def corrigir_unidade(unidade):
    match unidade:
        case 'AMPERE':
            return 'A'
        case 'AMPERE/HORA':
            return 'AH'
        case 'CENTIMETRO':
            return 'CM'
        case 'CAIXA':
            return 'CX'
        case 'GRAMA':
            return 'G'
        case 'GALAO':
            return 'GL'
        case 'HORA':
            return 'H'
        case 'HERTZ':
            return 'HZ'
        case 'QUILOGRAMA':
            return 'KG'
        case 'KILOGRAMA':
            return 'KG'
        case 'QUILOHERTZ':
            return 'KHZ'
        case 'QUILOVOLT':
            return 'KV'
        case 'QUILOWATT':
            return 'KW'
        case 'LITRO':
            return 'L'
        case 'MILILITRO':
            return 'L'
        case 'METRO':
            return 'M'
        case 'METRO QUADRADO':
            return 'M2'
        case 'METRO CUBICO':
            return 'M3'
        case 'MILIGRAMA':
            return 'MG'
        case 'MEGAHERTZ':
            return 'MHZ'
        case 'MINUTO':
            return 'MIN'
        case 'MILIMETRO':
            return 'MM'
        case 'MEGAWATT':
            return 'MW'
        case 'PEÇA':
            return 'PC'
        case 'PACOTE':
            return 'PCT'
        case 'CONJUNTO':
            return 'PCT'
        case 'PACK':
            return 'PCT'
        case 'FARDO':
            return 'PCT'
        case 'SEGUNDO':
            return 'S'
        case 'TONELADA':
            return 'T'
        case 'UNIDADE':
            return 'UN'
        case 'FATIA':
            return 'UN'
        case 'GARRAFA':
            return 'UN'
        case 'BANDEJA':
            return 'UN'
        case 'VOLT':
            return 'V'
        case 'WATT':
            return 'W'
        case _:
            return 'UN'
def corrigir_kit(unidade):
    if unidade == 'KIT':
        codigo_barra = 'KIT'
        return False 
def corrigir12():
    pass
def corrigir123():
    pass
def corrigir1234():
    pass
def corrigir12345():
    pass
def corrigir123456():
    pass
def corrigir1234567():
    pass
def corrigir12345678():
    pass
def corrigir123456789():
    pass
def corrigir1234567891():
    pass