import psycopg2
from tkinter import messagebox
from app.componentes.banco_dados.tratamento_de_dados.conversor_matriz_idela import conversor_seller_produto

try:
    from app.componentes.banco_dados.conexao_banco import iniciar_banco
    from app.componentes.banco_dados.execucoes_banco import definir_id_com_exclusao, relatorio_erros
except:
    from conexao_banco import iniciar_banco
    from app.componentes.banco_dados.execucoes_banco import definir_id_com_exclusao, relatorio_erros

def cadastrar_no_banco(usuario,senha,banco,matriz,substituir:bool=False,origem:str = 'seller'):
    conexao, cursor = iniciar_banco(usuario,senha,banco)
    if conexao:
        print("CORRETOS")
        id = definir_id_com_exclusao(substituir, cursor)
        
        
        match origem:
            case 'seller':
                matriz = conversor_seller_produto(matriz,cursor)
        
        
        
        
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
        lista_erros = []
        contador_produtos_totais = 0
        for produto in matriz:
            contador_produtos_totais += 1
            # Define os atributos a serem passados para o banco
            codigo_barra = produto[0] # codigo barra
            nome = produto[1] # descricao do produto
            grupo = produto[2] # grupo
            subgrupo = produto[3] # subgrupos
            preco_venda = produto[4] # preço da venda
            custo_medio = produto[5] # preco de compra
            unid_venda = produto[6] # unidade de medida de venda
            unid_compra = produto[7] # Unidade de medida de compra
            fator_conversao = produto[8] # fator de conversao
            codigo_ncm = produto[9] # NCM
            
            
            # codigo_reduzido = produto[7] # por enquanto sem uso
            # cest = produto[10] # por enquanto sem uso
            # cod_speed = produto[11] # por enquanto sem uso

            # campos com dados genéricos fixos
            tributacao = '090'
            cst_pis,cst_cofins,cst_pis_entrada,cst_cofins_entrada = 99,99,99,99
            
            # Verifica se o produto tem um destes campos como nulo, e adiciona eles a lista de erro.
            

            print('não consigo converter este codigo de barras para inteiro')
            lista_erros.append([nome,codigo_barra,preco_venda,motivo_erro])
            if codigo_barra == '' or nome == '' or preco_venda == '' or custo_medio:
                motivo_erro = 'Falta de dados'
                lista_erros.append([nome,codigo_barra,preco_venda,motivo_erro])
                print(f"Produto {nome} ERRADO!")
                continue
            try:
                cursor.execute("INSERT INTO produto(codigo, codigo_barra, nome, grupo, subgrupo, preco_unit, preco_custo, unid_med, unid_med_entrada, tributacao, codigo_ncm, cst_pis, cst_cofins, cst_pis_entrada, cst_cofins_entrada) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (id, codigo_barra, nome, grupo,subgrupo, preco_venda, custo_medio, unid_venda, unid_compra, tributacao, codigo_ncm, cst_pis, cst_cofins, cst_pis_entrada, cst_cofins_entrada))
                id += 1
            except Exception as e:
                lista_erros.append(nome)
                print(e)

        print(f'Produtos totais: {contador_produtos_totais}')    
        cursor.execute("SELECT * FROM produto;")
        result1 = cursor.fetchall()
        print(f'Produtos adicionados: {len(result1)}')
        if lista_erros != []:
            print('Produtos com problema:')
            for item in lista_erros:
                print(f'Linha: {item[0]}\nNome: {item[1]} - Codigo de barras: {item[2]} - preço: {item[3]}')
        else:
            print("Todos os produtos foram adicionados com sucesso!!")



# relatorio_erros()
# cadastrar_no_banco("postgres", "postgres","banco_teste","")