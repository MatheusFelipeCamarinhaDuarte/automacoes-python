from app.assets.conexao_banco import iniciar_banco
def cadastrar_no_banco(usuario,senha,banco,matriz,substituir:bool=False):
    conexao, cursor = iniciar_banco(usuario,senha,banco)
    if not conexao:
        # TESTANDO SE ESTÃO COM DADOS INCORRETOS
        print("INCORRETOS")
        pass
    else:
        print("CORRETOS")
        id = 1
        if substituir:
            cursor.execute("DELETE FROM produtos")
        else:
            cursor.execute("SELECT * FROM produto")
            result1 = cursor.fetchall()
            maior_numero = 0
            for i in result1:
                numero = int(i[0])
                if numero >= maior_numero:
                    maior_numero = numero
            id = maior_numero+1
        lista_erros = []
        contador_produtos_totais = 0
        for produto in matriz:
            contador_produtos_totais += 1
            # Define os atributos a serem passados para o banco
            codigo_barras = produto[0]
            nome = produto[1]
            ncm = produto[2]
            preco_venda = produto[3]
            unid_venda = produto[4]
            custo_medio = produto[5]
            unid_compra = produto[6]
            codigo_reduzido = produto[7]
            estrutura_mercadologica = produto[8]
            fator_conversao = produto[9]
            cest = produto[10]
            cod_speed = produto[11]
            
            # Verifica se o produto tem um destes campos como nulo, e adiciona eles a lista de erro.
            if codigo_barras == '' or nome == '' or preco_venda == '' or custo_medio:
                lista_erros.append([nome,codigo_barras,preco_venda,custo_medio])
                print(f"Produto {nome} ERRADO!")
                continue
            try:
                cursor.execute("INSERT INTO produto(codigo,codigo_barra,nome,grupo,preco_unit, preco_prazo, unid_med, tributacao,codigo_ncm,cst_pis,cst_cofins,cst_pis_entrada,cst_cofins_entrada) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (id, codigo_barra, nome, grupo, preco_unitario, preco_prazo, unidade_de_medida, tributacao, codigo_ncm, cst_pis, cst_cofins, cst_pis_entrada, cst_cofins_entrada))
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

                # A corrigir
                nome = limpar_nome(nome)
                

                preco_unitario = produto[10]

                preco_prazo = produto[11]

                unidade_de_medida = produto[12]
                tributacao = '090'
                cst_pis,cst_cofins,cst_pis_entrada,cst_cofins_entrada = 99,99,99,99


                for i in range(len(listagem)):
                    if produto[5] in listagem[lista_keys_grupo[i]]:
                        grupo = lista_grupos[lista_keys_grupo[i]]
                        print(f'Produto {id} OK!')
                        break