import psycopg2
import tkinter as tk
from tkinter import messagebox
from app.componentes.banco_dados.tratamento_de_dados.conversor_matriz_idela import conversor_seller_produto
try:
    from app.componentes.banco_dados.conexao_banco import iniciar_banco,finalizar_banco
    from app.componentes.banco_dados.execucoes_banco import definir_id_com_exclusao
    from app.componentes.banco_dados.tratamento_de_dados.corrigir_atributos_produtos import corrigir_nome_acentos,corrigir_unidade
    from app.componentes.arquivo.relatorios import relatorio_erros_produto, baixar_arquivo_relatorio
except:
    from conexao_banco import iniciar_banco,finalizar_banco
    from app.componentes.banco_dados.execucoes_banco import definir_id_com_exclusao

def cadastrar_no_banco(usuario,senha,banco,matriz,janela_principal,tela_atual,substituir:bool=False,origem:str = 'seller',):
    conexao, cursor = iniciar_banco(usuario,senha,banco)
    if conexao:
        print("CORRETOS")
        id = definir_id_com_exclusao(substituir, cursor)
        
        
        match origem:
            case 'seller':
                matriz = conversor_seller_produto(matriz,cursor)
        conexao.commit()
        
        
        
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
            nome = corrigir_nome_acentos(produto[1]) # descricao do produto
            grupo = produto[2] # grupo
            subgrupo = produto[3] # subgrupos
            preco_venda = produto[4] # preço da venda
            custo_medio = produto[5] # preco de compra
            unid_venda = corrigir_unidade(produto[6]) # unidade de medida de venda
            unid_compra = corrigir_unidade(produto[7]) # Unidade de medida de compra
            fator_conversao = produto[8] # fator de conversao
            codigo_ncm = produto[9] # NCM
            cursor.execute("SELECT * FROM tributacao WHERE tributacao = 0;")
            result = cursor.fetchall()
            
            # codigo_reduzido = produto[7] # por enquanto sem uso
            # cest = produto[10] # por enquanto sem uso
            # cod_speed = produto[11] # por enquanto sem uso

            # campos com dados genéricos fixos
            
            tributacao = result[0][0]
            cst_pis,cst_cofins,cst_pis_entrada,cst_cofins_entrada = 99,99,99,99
            
            # Verifica se o produto tem um destes campos como nulo, e adiciona eles a lista de erro.
            
            motivo_erro = ''
            # print('não consigo converter este codigo de barras para inteiro')
            # lista_erros.append([nome,codigo_barra,preco_venda,motivo_erro])
            if codigo_barra == '':
                motivo_erro = 'Falta de codigo de barras'
                lista_erros.append([nome,codigo_barra,preco_venda,motivo_erro])
                print(f"Produto {nome} ERRADO!")
                continue
            if len(codigo_barra) < 5:
                motivo_erro = 'codigo de barras inválido'
                lista_erros.append([nome,codigo_barra,preco_venda,motivo_erro])
                print(f"Produto {nome} ERRADO!")
                continue
            if nome == '' :
                motivo_erro = 'Falta de nome'
                lista_erros.append([nome,codigo_barra,preco_venda,motivo_erro])
                print(f"Produto {nome} ERRADO!")
                continue
            if preco_venda == '' :
                motivo_erro = 'Falta de preço de venda'
                print(produto)
                lista_erros.append([nome,codigo_barra,preco_venda,motivo_erro])
                print(f"Produto {nome} ERRADO!")
                continue
            if custo_medio =='':
                custo_medio = '0.0'
                # motivo_erro = 'Falta de Custo médio'
                # lista_erros.append([nome,codigo_barra,preco_venda,motivo_erro])
                # print(f"Produto {nome} ERRADO!")
                # continue
            try:
                cursor.execute("INSERT INTO produto(codigo, codigo_barra, nome, grupo, subgrupo, preco_unit, preco_custo, unid_med, unid_med_entrada, tributacao, codigo_ncm, cst_pis, cst_cofins, cst_pis_entrada, cst_cofins_entrada) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (id, codigo_barra, nome, grupo,subgrupo, preco_venda, custo_medio, unid_venda, unid_compra, tributacao, codigo_ncm, cst_pis, cst_cofins, cst_pis_entrada, cst_cofins_entrada))
                id += 1
            except Exception as e:
                lista_erros.append([nome,codigo_barra,preco_venda, e])
                print(produto)
        conexao.commit()
        # print(f'Produtos totais: {contador_produtos_totais}')
        
        # print(f'Produtos adicionados: {len(result1)}')
        
        if lista_erros != []:
            mensagem = tk.Toplevel()
            xa = (mensagem.winfo_screenwidth() // 2) - (200 // 2)
            ya = (mensagem.winfo_screenheight() // 2) - (200 // 2)
            mensagem.geometry(f"{200}x{200}+{xa}+{ya}")            
            label = tk.Label(mensagem, text=f'Produtos totais: {contador_produtos_totais}')
            label.pack()
            cursor.execute("SELECT * FROM produto;")
            result1 = cursor.fetchall()
            label1 = tk.Label(mensagem, text=f'Produtos adicionados: {len(result1)}')
            label1.pack()
            label2 = tk.Label(mensagem, text=f'Produtos com problema: {contador_produtos_totais - len(result1)}')
            label2.pack()
            # print('Produtos com problema: {}')
            # for item in lista_erros:
                # print(f'Nome: {item[0]}\nMotivo: {item[3]}')
            nome_arquivo = relatorio_erros_produto(lista_erros)
            botao = tk.Button(mensagem, text='Baixar', command=lambda: baixar_arquivo_relatorio(nome_arquivo, mensagem, janela_principal,tela_atual))
            botao.pack()
            # app/temp/relatorios/relatorio_erro_produto.csv
        else:
            from app.telas.escolha_tipo import escolha_tipo
            label2 = tk.Label(mensagem, text="Todos os produtos foram adicionados com sucesso!!")
            resposta = messagebox.askyesno('Teste',"Todos os dados foram inseridos com sucesso!\nDeseja voltar ao menu?")
            if resposta:
                escolha_tipo(janela_principal)
                tela_atual.withdraw()
            else:
                pass
            label2.pack()
            # print("Todos os produtos foram adicionados com sucesso!!")
        
        
        
        
        
        
        finalizar_banco(conexao, cursor)



# relatorio_erros_produto()
# cadastrar_no_banco("postgres", "postgres","banco_teste","")