from grupos_autosystem import pegar_grupos

lista_codigos_string = ['bebidas_nao_alcoolicas','bebidas_alcoolicas','bazar_e_utilidades','biscoitos_snacks_aperitivos', 'bomboniere', 'congelados_sorvetes_gelo', 'food_service', 'mercearia', 'padaria', 'tabacaria']

teste = pegar_grupos()
teste2 = teste.keys()

print(lista_codigos_string)
print(teste2)

if lista_codigos_string == teste2:
    print("ok")
else:
    print("As listas não são iguais.")
