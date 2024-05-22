
def cadastrar_no_banco(cursor,matriz):
        lista_erros = []
        id = 1
        contador_verificado = 0

        for produto in matriz:
            contador_verificado += 1

            #Corretos
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
    


            # A corrigir
            nome = limpar_nome(nome)
            

            preco_unitario = produto[10]

            preco_prazo = produto[11]

            unidade_de_medida = produto[12]
            codigo_ncm = produto[16]

            if codigo_ncm == '':
                codigo_ncm = "2935.90.29"

            tributacao = '090'
            cst_pis,cst_cofins,cst_pis_entrada,cst_cofins_entrada = 99,99,99,99
            if codigo_barra == '' or nome == '' or preco_unitario == '':
                lista_erros.append([contador_verificado,nome,codigo_barra,preco_unitario])
                print(f"Produto {id} ERRADO!")
                continue

            for i in range(len(listagem)):
                if produto[5] in listagem[lista_keys_grupo[i]]:
                    grupo = lista_grupos[lista_keys_grupo[i]]
                    cursor.execute("INSERT INTO produto(codigo,codigo_barra,nome,grupo,preco_unit, preco_prazo, unid_med, tributacao,codigo_ncm,cst_pis,cst_cofins,cst_pis_entrada,cst_cofins_entrada) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (id, codigo_barra, nome, grupo, preco_unitario, preco_prazo, unidade_de_medida, tributacao, codigo_ncm, cst_pis, cst_cofins, cst_pis_entrada, cst_cofins_entrada))
                    print(f'Produto {id} OK!')
                    id += 1
                    break

        print(f'Produtos totais: {contador_verificado}')    
        cursor.execute("SELECT * FROM produto;")
        result1 = cursor.fetchall()
        print(f'Produtos adicionados: {len(result1)}')

        # verifica se tem produtos errados, e se não tiver, exibe que está tudo ok!
        if lista_erros != []:
            print('Produtos com problema:')
            for item in lista_erros:
                print(f'Linha: {item[0]}\nNome: {item[1]} - Codigo de barras: {item[2]} - preço: {item[3]}')
        else:
            print("Todos os produtos foram adicionados com sucesso!!")

def deletar_banco_anterior(cursor):
    cursor.execute('DELETE FROM produto')
