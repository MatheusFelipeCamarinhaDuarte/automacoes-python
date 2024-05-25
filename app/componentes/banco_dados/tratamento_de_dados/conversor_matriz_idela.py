from app.componentes.banco_dados.execucoes_banco import inserir_grupos_as
from app.componentes.banco_dados.tratamento_de_dados.corrigir_atributos_produtos import corrigir_nome_acentos
'''
formato ideal:
0 - codigo de barras
1 - descricao do produto
2 - grupo
3 - subgrupo
4 - preço de venda
5 - preço de compra 
6 - unidade de medida de compra
7 - unidade de medida de venda
8 - fator de conversao
9 - codigo ncm
'''


def conversor_seller_produto(matriz,cursor):
        estrutura_marcadorlogicas = []
        for linha in matriz:
            estrutura_marcadorlogicas.append(linha[8]) # grupos
        grupos_dict = {}
        
        
        for estrutura in estrutura_marcadorlogicas:
            # print(estrutura)

            lista = estrutura.split('/')
            grupo = corrigir_nome_acentos(lista[0])
            subgrupo = corrigir_nome_acentos(lista[1])

            if grupo in grupos_dict:
                grupos_dict[grupo].add(subgrupo)
            else:
                grupos_dict[grupo] = {subgrupo}
        for grupo in grupos_dict:
            grupos_dict[grupo] = list(grupos_dict[grupo])
        
        grupo_com_grid, subgrupo_com_grid = inserir_grupos_as(grupos_dict,cursor)
        
        
        nova_matriz = []
        # Converter matriz para o formato padrao
        for linha in matriz:
            linha_da_nova_matriz = []
            
            codigo_barra = linha[0]
            linha_da_nova_matriz.append(codigo_barra) # codigo barra

            nome = linha[1]
            linha_da_nova_matriz.append(nome) # descricao do produto         

            estrutura = linha[8]
            lista = estrutura.split('/')
            grupo = corrigir_nome_acentos(lista[0])
            subgrupo = corrigir_nome_acentos(lista[1])
            if grupo in grupo_com_grid:
                linha_da_nova_matriz.append(grupo_com_grid[grupo]) # grupo
            else:
                linha_da_nova_matriz.append('') # grupo
            if subgrupo in subgrupo_com_grid:
                linha_da_nova_matriz.append(subgrupo_com_grid[subgrupo]) # subgrupo
            else:
                linha_da_nova_matriz.append('') # grupo

            preco_venda = linha[3]
            linha_da_nova_matriz.append(preco_venda) # preço da venda

            custo_medio = linha[5]
            linha_da_nova_matriz.append(custo_medio) # preco de compra

            unid_venda = linha[4]
            linha_da_nova_matriz.append(unid_venda) # unidade de medida de venda

            unid_compra = linha[6]
            linha_da_nova_matriz.append(unid_compra) # Unidade de medida de compra

            fator_conversao = linha[9]
            linha_da_nova_matriz.append(fator_conversao) # fator de conversao

            codigo_ncm = linha[2]
            linha_da_nova_matriz.append(codigo_ncm) # NCM
            nova_matriz.append(linha_da_nova_matriz)
            
            # nova_matriz.append(codigo_reduzido = linha[7]) # por enquanto sem uso
            # nova_matriz.append(cest = linha[10]) # por enquanto sem uso
            # nova_matriz.append(cod_speed = linha[11]) # por enquanto sem uso
        
        # Retorna nova a matriz
        return nova_matriz