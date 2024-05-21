def pegar_grupos():
    resposta = input("Deseja pegar o valor padrão? (S/N) ")
    if resposta.upper() == "S":
        return {
        'bebidas_nao_alcoolicas':207246,
        'bebidas_alcoolicas':207255,
        'bazar_e_utilidades':207263,
        'biscoitos_snacks_aperitivos':207270,
        'bomboniere':207279,
        'congelados_sorvetes_gelo':207283,
        'food_service':207291,
        'mercearia':207299,
        'padaria':207303,
        'tabacaria':207314
        }
    else:
        bebidas_nao_alcoolicas = input('Defina a grid de bebidas_nao_alcoolicas: ')
        bebidas_alcoolicas = input('Defina a grid de bebidas_alcoolicas: ')
        bazar_e_utilidades = input('Defina a grid de bazar_e_utilidades: ')
        biscoitos_snacks_aperitivos = input('Defina a grid de biscoitos_snacks_aperitivos: ')
        bomboniere = input('Defina a grid de bomboniere: ')
        congelados_sorvetes_gelo = input('Defina a grid de congelados_sorvetes_gelo: ')
        food_service = input('Defina a grid de food_service: ')
        mercearia = input('Defina a grid de mercearia: ')
        padaria = input('Defina a grid de padaria: ')
        tabacaria = input('Defina a grid de tabacaria: ')
        return {
        'bebidas_nao_alcoolicas':bebidas_nao_alcoolicas,
        'bebidas_alcoolicas':bebidas_alcoolicas,
        'bazar_e_utilidades':bazar_e_utilidades,
        'biscoitos_snacks_aperitivos':biscoitos_snacks_aperitivos,
        'bomboniere':bomboniere,
        'congelados_sorvetes_gelo':congelados_sorvetes_gelo,
        'food_service':food_service,
        'mercearia':mercearia,
        'padaria':padaria,
        'tabacaria':tabacaria
        }