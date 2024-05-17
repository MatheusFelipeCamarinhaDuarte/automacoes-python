import psycopg2
from funcoes.funcoes_limpar_dados import limpar_nome

#Inicia o banco de dados
def iniciar_banco(intencao):
        while True:
            banco = input(f"Digite o nome do banco que deseja {intencao} os dados: ")
            try:
                conn1 = psycopg2.connect(
                    host="localhost",
                    user="postgres",
                    password="postgres",
                    database=banco
                )
                cur1 = conn1.cursor()
                break
            except:
                 print("A conexão com o banco de dados falhou, confira e digite novamente")
        return conn1, cur1

# Cadastra os produtos:
def cadastrar_no_banco(cursor,tabela,listagem,lista_keys_grupo,lista_grupos):
        lista_erros = []
        cursor.execute('DELETE FROM produto')
        id = 1
        contador_verificado = 0
        for produto in tabela:
            contador_verificado += 1
            codigo_barra = produto[2]
            nome = produto[3]
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
        if lista_erros != []:
            print('Produtos com problema:')
            for item in lista_erros:
                print(f'Linha: {item[0]}\nNome: {item[1]} - Codigo de barras: {item[2]} - preço: {item[3]}')
        else:
             print("Todos os produtos foram adicionados com sucesso!!")
# Finaliza o banco com commit
def finalizar_banco(conexao, cursor):
    conexao.commit()
    cursor.close()
    conexao.close()