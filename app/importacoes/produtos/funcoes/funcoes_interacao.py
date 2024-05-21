import pandas as pd
import os
from app.assets.conexao_banco import iniciar_banco
from funcoes.funcoes_separador import *

def escolha_importacao_dados():
    #AQUI
    # print('Por onde prefere importar os dados?')
    # print('1 - Via outro banco de dados postgres')
    # print('2 - Via CSV')
    # menu = int(input('Resposta:'))
    menu = 2
    match menu:
        case 1:
            conexao2, cursor2 = iniciar_banco("postgres","postgres","flora_loja")
            tabela = 'AQUI deve ter uma matriz equivalente a tabela abaixo'
            print("A ser implementado ainda")
            return
        case 2:
            diretorio_atual = os.path.dirname(__file__)
            diretorio_pai = os.path.dirname(diretorio_atual)
            caminho_arquivo = os.path.join(diretorio_pai, 'csv', 'produtos.csv')
            try:
                dados = pd.read_csv(caminho_arquivo, sep=';')
                dados = dados.fillna('')
                tabela = dados.values
            except FileNotFoundError:
                print(f"Erro: Arquivo {caminho_arquivo} não encontrado.")
    return tabela

def escolha_demilitador(lista_keys_grupo,tabela):
    #AQUI
    # print('Escolha:')
    # print('1 - Inserir manualmente')
    # print('2 - Inserir por bloco')
    # print('3 - Insera por .txt')
    # menu = int(input('Resposta:'))
    menu = 2
    match menu:
        case 1:
            listagem = delimitador_manual(lista_keys_grupo,tabela)
        case 2:
            listagem = delimitador_automatico(lista_keys_grupo,tabela)
        case 3:
            listagem = delimitador_txt(lista_keys_grupo,tabela)
    return listagem
    