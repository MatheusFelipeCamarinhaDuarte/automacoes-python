from tkinter import messagebox

class Banco_de_dados():
    """Classe de banco de dados e suas operações"""
    from typing import Callable, Optional, Tuple, List

    def __init__(self):
        self.cursor = None
        self.conexao = None
        self.usuario = ''
        self.senha = ''
        self.banco = ''

    def iniciar(self,usuario:str,senha:str,banco:str) -> None:
        """Método para inciar o banco de dados a partir de usuáriom senha e nome do banoc de dados

        Args:
            janela_principal (Janela): Janela principal da aplicação
            usuario (str): Nome do usuário passado por meio de input
            senha (str): senha do usuário passado por meio de input
            banco (str): Nome do banco passado por meio de input

        Returns:
            conecao: retorna uma conexão com o banco de dados especificado.
        """
        import psycopg2
        self.usuario = usuario
        self.senha = senha
        self.banco = banco
        try:
            conn1 = psycopg2.connect(
                host="localhost",
                user=usuario,
                password=senha,
                database=banco
            )
            cur1 = conn1.cursor()
            self.cursor = cur1 
            self.conexao = conn1
            messagebox.showinfo("Sucesso", "Conexão estabelecida com sucesso")
        except:
            self.cursor = None 
            self.conexao = None
            self.usuario = ''
            self.senha = ''
            self.banco = ''
            messagebox.showerror("Erro", "Os dados passados de usuário, senha ou banco estão incorretos.")

    def finalizar(self) -> None:
        """Método para o fechamento correto do banco de dados."""
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def id(self,substituir):
        id = 1
        if substituir:
            self.cursor.execute("DELETE FROM produto")
        else:
            self.cursor.execute("SELECT * FROM produto")
            result1 = self.fetchall()
            maior_numero = 0
            for i in result1:
                numero = int(i[0])
                if numero >= maior_numero:
                    maior_numero = numero
            id = maior_numero + 1
        return id

    def cadastrar_produtos(self,matriz:list,janela_principal,substituir:bool=False):
        """Método para cadastrar produtos a partir de uma matriz igual a todos. O formato desta matriz é:
            formato ideal:
            - 0 - codigo de barras (str - número)
            - 1 - descricao do produto (str)
            - 2 - grupo (grid)
            - 3 - subgrupo (grid)
            - 4 - preço de venda (double)
            - 5 - preço de compra (double)
            - 6 - unidade de medida de compra (abreviação)
            - 7 - unidade de medida de venda (abreviação)
            - 8 - fator de conversao (int)
            - 9 - codigo ncm (xxxx.xx.xx)
            - 10 - tributacao (int)
            - 11 - cst_pis (int)
            - 12 - cst_cofins (int)
            - 13 - cst_pis_entrada (int)
            - 14 - cst_cofins_entrada (int)
        Args:
            matriz (list): _description_
            janela_principal (_type_): _description_
            substituir (bool, optional): _description_. Defaults to False.
        """
        import tkinter as tk
        cursor = self.cursor
        conexao = self.conexao
        if conexao:
            id = self.id(substituir)        
            
            # Inserção dos grupos e subgrupos, junto com a troca de seus nomes por grid
            matriz = self.troca_de_grupo(matriz)
            
            lista_erros = []
            contador_produtos_totais = 0
            cursor.execute("SELECT * FROM tributacao WHERE tributacao = 0;")
            result = cursor.fetchall()
            for produto in matriz:
                contador_produtos_totais += 1
                
                codigo_barra,nome,grupo,subgrupo,preco_venda,custo_medio,unid_venda,unid_compra,fator_conversao,codigo_ncm,cst_pis,cst_cofins,cst_pis_entrada,cst_cofins_entrada = produto[0],produto[1],produto[2],produto[3],produto[4],produto[5],produto[6],produto[7],produto[8],produto[9],produto[11],produto[12],produto[13],produto[14]
                
                # Define os atributos a serem passados para o banco
                # codigo_barra = produto[0] # codigo barra
                # nome = produto[1] # descricao do produto
                # grupo = produto[2] # grupo
                # subgrupo = produto[3] # subgrupos
                # preco_venda = produto[4] # preço da venda
                # custo_medio = produto[5] # preco de compra
                # unid_venda = produto[6] # unidade de medida de venda
                # unid_compra = produto[7] # Unidade de medida de compra
                # fator_conversao = produto[8] # fator de conversao
                # codigo_ncm = produto[9] # NCM
                try:
                    tributacao = produto[10]
                    if tributacao == '':
                        tributacao = result[0][0]
                except:
                    tributacao = result[0][0]
                
                importar, errado, custo_medio, motivo_erro = self.verificacao_erro_produto(unid_venda,unid_compra,codigo_barra,nome,preco_venda,custo_medio)
                if importar:
                    try:
                        cursor.execute("INSERT INTO produto(codigo, codigo_barra, nome, grupo, subgrupo, preco_unit, preco_custo, unid_med, unid_med_entrada, qtde_unid_entrada, codigo_ncm, tributacao, cst_pis, cst_cofins, cst_pis_entrada, cst_cofins_entrada) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (id, codigo_barra, nome, grupo, subgrupo, preco_venda, custo_medio, unid_venda, unid_compra, fator_conversao, codigo_ncm, tributacao, cst_pis, cst_cofins, cst_pis_entrada, cst_cofins_entrada))
                        # print(id, custo_medio)
                        id += 1
                    except Exception as e:
                        motivo_erro.append(e)
                        errado = True
                        importar = False
                        break
                if errado:
                    if importar:
                        print('FDP '+nome)
                        importado = 'Importado com restrição'
                    else:
                        importado = 'Não importado'
                    # print(f"Produto {nome} ERRADO!")
                    lista_erros.append([nome,codigo_barra,preco_venda,custo_medio,importado,motivo_erro])            
            conexao.commit()
                        
            # COMEÇO = Componetizar
            if lista_erros != []:
                from app.componentes.arquivo.relatorios import relatorio_erros_produto, baixar_arquivo_relatorio
                mensagem = tk.Toplevel()
                xa = (mensagem.winfo_screenwidth() // 2) - (300 // 2)
                ya = (mensagem.winfo_screenheight() // 2) - (300 // 2)
                mensagem.geometry(f"{200}x{200}+{xa}+{ya}")            
                label = tk.Label(mensagem, text=f'Produtos totais: {contador_produtos_totais}')
                label.pack()
                cursor.execute("SELECT * FROM produto;")
                result1 = cursor.fetchall()
                label1 = tk.Label(mensagem, text=f'Produtos adicionados: {len(result1)}')
                label1.pack()
                label3 = tk.Label(mensagem, text=f'Produtos não adicionados: {contador_produtos_totais - len(result1)}')
                label3.pack()
                label2 = tk.Label(mensagem, text=f'Produtos com erros: {len(lista_erros)}')
                label2.pack()
                nome_arquivo = relatorio_erros_produto(lista_erros)
                cursor.execute('SELECT nome FROM empresa WHERE codigo = 1')
                resultado = cursor.fetchall()
                nome_cliente = resultado[0][0]
                botao = tk.Button(mensagem, text='Baixar', command=lambda: baixar_arquivo_relatorio(nome_arquivo, mensagem, janela_principal,janela_principal,nome_cliente))
                botao.pack()
                # app/temp/relatorios/relatorio_erro_produto.csv
            # FIM = Componetizar
            else:
                from app.telas.tela_2_escolha_tipo import escolha_tipo
                label2 = tk.Label(mensagem, text="Todos os produtos foram adicionados com sucesso!!")
                resposta = messagebox.askyesno('Teste',"Todos os dados foram inseridos com sucesso!\nDeseja voltar ao menu?")
                if resposta:
                    escolha_tipo(janela_principal)
                else:
                    pass
                label2.pack()
                # print("Todos os produtos foram adicionados com sucesso!!")
            self.finalizar()

    def troca_de_grupo(self, matriz:list[list]) -> list[list]:
        """Método para trocar o grupo pelo grid equivalente

        Args:
            matriz (list[list]): matriz antes

        Returns:
            list[list]: matriz depois da mudança
        """
        grupo_dict = {}
        for linha in matriz:
            grupo = linha[2]
            subgrupo = linha[3]
            if grupo in grupo_dict:
                grupo_dict[grupo].add(subgrupo)
            else:
                grupo_dict[grupo] = {subgrupo}
        for item in grupo_dict:
            grupo_dict[item] = list(grupo_dict[item])
        
        grupo_com_grid, subgrupo_com_grid = self.cadastrar_grupos_produtos(grupo_dict)
        
        for linha in matriz:
            linha[2] = grupo_com_grid[linha[2]]
            linha[3] = subgrupo_com_grid[linha[3]]
        return matriz

    def cadastrar_grupos_produtos(self,dicionario:dict) -> Tuple[dict,dict]:
        """Este métodos, de acordo com um dicionário onde os grupos são
        a chave e os subgrupos são os valores, faz a inserção dos grupos
        e sub grupos e devolve um grid

        Args:
            dicionario (dict): Dicionário pronto com grupos e subgrupos

        Returns:
            Tuple[dict,dict]: Envia 2 dicionário (um de grupo e outro de subgrupo). 
            cada dicionário tem o nome como chave e o grid como valor
        """
        self.cursor.execute(f"DELETE FROM grupo_produto")
        self.cursor.execute(f"DELETE FROM subgrupo_produto")
        id = 1
        id_sub = 1
        grupo_com_grid = {} 
        subgrupo_com_grid = {}
        for grupo, subgrupos in dicionario.items():
            self.cursor.execute("INSERT INTO grupo_produto (codigo,nome,flag) VALUES (%s,%s,%s);", (id,grupo,'A'))
            self.cursor.execute("SELECT * FROM grupo_produto WHERE codigo = %s;", (id,))
            result1 = self.cursor.fetchall()
            grid_grupo = result1[0][3]
            grupo_com_grid[grupo] = grid_grupo
            for subgrupo in subgrupos:
                self.cursor.execute("INSERT INTO subgrupo_produto (codigo,nome,grupo,flag) VALUES (%s,%s,%s,%s);", (id_sub,subgrupo,grid_grupo,'A'))
                self.cursor.execute("SELECT * FROM subgrupo_produto WHERE codigo = %s;",(id_sub,))
                result1 = self.cursor.fetchall()
                grid_subgrupo = result1[0][4]
                subgrupo_com_grid[subgrupo] = grid_subgrupo
                id_sub += 1
            id += 1
        
        self.cursor.execute("SELECT grid FROM deposito WHERE codigo = 100;")
        resultado = self.cursor.fetchall()
        try:
            grid_depoisto = resultado[0][0]
        except:
            self.cursor.execute("INSERT INTO deposito (codigo,nome,empresa,flag) VALUES (%s,%s,%s,%s);", ('100','DEPOSITO LOJA',1,'A'))
            self.cursor.execute("SELECT grid FROM deposito WHERE codigo = 100;")
            resultado = self.cursor.fetchall()
            grid_depoisto = resultado[0][0]
        # self.cursor.execute("DELETE FROM deposito_grupo_produto WHERE codigo = 100;")
        self.cursor.execute("DELETE FROM deposito_grupo_produto WHERE deposito = (%s);", (grid_depoisto,))
        for nome_grupo,grid_dos_grupos in grupo_com_grid.items():
            self.cursor.execute("INSERT INTO deposito_grupo_produto (deposito,grupo) VALUES (%s,%s);", (grid_depoisto,grid_dos_grupos))
        self.conexao.commit()
        return grupo_com_grid, subgrupo_com_grid

    def verificacao_erro_produto(self,unid_venda:str,unid_compra:str,codigo_barra:str,nome:str,preco_venda:str,custo_medio:str) -> Tuple[bool,bool,str,list]:
        """Método de verificacao de erros antes das importações.

        Args:
            unid_venda (str): unidade de venda
            unid_compra (str): unidade de compra
            codigo_barra (str): código de barras em string
            nome (str): nome do produto 
            preco_venda (str): o Preço de venda em string

        Returns:
            Tuple[bool,bool,str,list]: retorna o relatório se tem erro, se deve
            importar, como ficou o custo_medio e a lista de motivos de erro (se houver)
        """
        from app.classes.correcoes import Correcao
        correcao = Correcao
        motivo_erro = []
        errado = False
        importar = True
        if len(codigo_barra) < 5:
            motivo_erro.append('codigo de barras inválido')
            errado = True
            importar = True
        if custo_medio =='' or custo_medio == '0' or custo_medio == '0.0' or custo_medio == '0.00' or custo_medio == None:
            custo_medio = '0.10'
            motivo_erro.append('Falta preço custo - Adicionado o padrão (0.10)')
            errado = True
            importar = True
        if correcao.identificar_kit(unid_venda):
            motivo_erro.append('Kit não importado, favor, verificar cadastro.')
            errado = True
            importar = False
        if correcao.identificar_kit(unid_compra):
            motivo_erro.append('Kit não importado, favor, verificar cadastro.')
            errado = True
            importar = False
        if codigo_barra == '':
            motivo_erro.append('Falta de codigo de barras')
            errado = True
            importar = False
        if nome == '' :
            motivo_erro.append('Falta de nome')
            errado = True
            importar = False
        if preco_venda == '' :
            motivo_erro.append('Falta de preço de venda')
            errado = True
            importar = False
        
        return importar, errado, custo_medio, motivo_erro
        
        
        
        
        
        
        
        
        
        
        